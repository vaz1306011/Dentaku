import logging

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
    def press_number(self, num: str):
        if self.status == ButtonType.EQUALS:
            self.expression.clear()
            self.sub_expression.clear()
        self.expression.add_number(num)

    @set_pre(ButtonType.NUMBER)
    def press_plus_minus(self):
        self.expression.convert_minus()

    @set_pre(ButtonType.OPERATOR)
    def press_operator(self, operator: str):
        if self.status == ButtonType.EQUALS:
            self.sub_expression.clear()
        self.expression.add_operator(operator)

    def press_equals(self):
        temp = self.expression.copy()
        try:
            self.expression.caluculate()
            self.sub_expression = temp
            self.status = ButtonType.EQUALS
        except ValueError:
            pass

    @set_pre(ButtonType.NONE)
    def press_back(self):
        if self.status == ButtonType.EQUALS:
            self.sub_expression.clear()
        self.expression.backspace()

    @set_pre(ButtonType.CLEAR_ENTRY)
    def press_clear_entry(self):
        self.expression.clear_entry()

    @set_pre(ButtonType.CLEAR)
    def press_clear(self):
        self.expression.clear()
        self.sub_expression.clear()
