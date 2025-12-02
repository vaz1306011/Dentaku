import logging
from sys import setprofile

from dentaku.models import ButtonType, Expression

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Logic:
    def __init__(self) -> None:
        self.expression: Expression = Expression()
        self.sub_expression: Expression = Expression()
        self.status: ButtonType = ButtonType.NONE

    def __str__(self) -> str:
        return self.expression.__str__()

    @staticmethod
    def set_pre(name: ButtonType):
        from functools import wraps

        def decorator(func):
            @wraps(func)
            def wrapper(self: "Logic", *args, **kwargs):
                result = func(self, *args, **kwargs)
                self.status = name
                return result

            return wrapper

        return decorator

    @set_pre(ButtonType.NUMBER)
    def add_number(self, num: str):
        if self.status == ButtonType.EQUALS:
            self.expression.clear()
            self.sub_expression.clear()
        self.expression.add_number(num)

    @set_pre(ButtonType.NUMBER)
    def toggle_sign(self):
        self.expression.toggle_sign()

    @set_pre(ButtonType.OPERATOR)
    def add_operator(self, operator: str):
        if self.status == ButtonType.EQUALS:
            self.sub_expression.clear()
        self.expression.add_operator(operator)

    @set_pre(ButtonType.PARENTHESIS)
    def add_parenthesis(self, parenthesis: str):
        self.expression.add_parenthesis(parenthesis)

    def evaluate(self):
        temp = self.expression.copy()
        try:
            self.expression.caluculate()
            self.sub_expression = temp
            self.status = ButtonType.EQUALS
        except (SyntaxError, ValueError):
            pass

    @set_pre(ButtonType.NONE)
    def backspace(self):
        if self.status == ButtonType.EQUALS:
            self.sub_expression.clear()
        self.expression.backspace()

    @set_pre(ButtonType.CLEAR_ENTRY)
    def clear_entry(self):
        self.expression.clear_entry()

    @set_pre(ButtonType.CLEAR)
    def clear(self):
        self.expression.clear()
        self.sub_expression.clear()
