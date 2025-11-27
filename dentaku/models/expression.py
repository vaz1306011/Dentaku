import logging

from dentaku.models import CharType

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Expression:
    def __init__(self) -> None:
        self.elements: list[str] = ["0"]

    def __str__(self) -> str:
        from dentaku.utils import display_operator

        return display_operator(self.elements)

    @property
    def is_last_number_zero(self) -> bool:
        if len(self.elements) == 1:
            return self.elements[0] == "0"
        return self.elements[-2] in (CharType.OPERATOR, CharType.PARENTHESIS)

    def add_number(self, number: str) -> None:
        if self.elements[-1] == ")":
            self.add_operator("*")
        elif self.is_last_number_zero:
            self.elements[-1] = number
            self.elements.pop()

        self.elements.append(number)

    def add_operator(self, operator: str) -> None:
        if self.elements[-1] in CharType.OPERATOR:
            self.elements[-1] = operator
        else:
            self.elements.append(operator)

    def add_parenthesis(self) -> None:
        self.elements.insert(-2, "(")
        self.elements.append(")")

    def backspace(self) -> None:
        self.elements.pop()
        if not self.elements:
            self.elements.append("0")

    def remove_parenthesis_and_minus(self) -> None:
        closing_count = 0
        for i in range(len(self.elements) - 1, -1, -1):
            if self.elements[i] == ")":
                if closing_count == 0:
                    del self.elements[i]
                closing_count += 1
            elif self.elements[i] == "(":
                closing_count -= 1
                if closing_count == 0:
                    del self.elements[i]

            if closing_count == 0:
                if self.elements[i] == "-":
                    del self.elements[i]
                break

    def caluculate(self) -> None:
        from dentaku.core.callculate import callculate
        from dentaku.utils.convert import normalize_operator

        expression_str = normalize_operator(self.elements)
        self.elements = list((callculate(expression_str)))

    def clear_entry(self) -> None:
        closing_count = 0
        for i in range(len(self.elements) - 1, -1, -1):
            if self.elements[i] == ")":
                closing_count += 1
            elif self.elements[i] == "(":
                closing_count -= 1

            if self.elements[i] in CharType.OPERATOR and closing_count == 0:
                break
            self.elements.pop()

    def clear(self) -> None:
        self.elements.clear()
        self.elements.append("0")

    def copy(self) -> "Expression":
        new_expr = Expression()
        new_expr.elements = self.elements.copy()
        return new_expr
