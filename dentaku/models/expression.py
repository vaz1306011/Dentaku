import logging
import re

from dentaku.models import CharType

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Expression:
    def __init__(self) -> None:
        self.elements: list[str] = ["0"]
        self.cursor_offset: int = 0

    def __str__(self) -> str:
        from dentaku.utils import display_operator

        return display_operator(self.elements)

    @property
    def normalized_elements(self) -> str:
        s = re.sub(r"<span.*?>", "", "".join(self.elements))
        s = re.sub(r"</span>", "", s)

        return s

    @property
    def curreny_index(self) -> int:
        return len(self.elements) - 1 - self.cursor_offset

    @property
    def current_char(self) -> str:
        return self.elements[-1 - self.cursor_offset]

    @current_char.setter
    def current_char(self, value: str) -> None:
        self.elements[-1 - self.cursor_offset] = value

    def add_on_cursor(self, value: str) -> None:
        self.elements.insert(len(self.elements) - self.cursor_offset, value)

    def move_cursor_left(self) -> None:
        if self.cursor_offset < len(self.elements) - 1:
            self.cursor_offset += 1

    def move_cursor_right(self) -> None:
        if self.cursor_offset > 0:
            self.cursor_offset -= 1

    @property
    def is_last_number_zero(self) -> bool:
        if len(self.elements) == 1:
            return self.elements[0] == "0"
        return self.elements[-2] in (CharType.OPERATOR, CharType.PARENTHESIS)

    def add_number(self, number: str) -> None:
        if self.current_char == ")":
            self.add_operator("*")
            self.set_gray(len(self.elements) - 1)
        elif self.is_last_number_zero:
            self.current_char = number
            self.elements.pop()

        self.add_on_cursor(number)
        # logger.debug(f"{self.elements=}")

    def add_operator(self, operator: str) -> None:
        if self.current_char in CharType.OPERATOR:
            self.current_char = operator
        else:
            self.add_on_cursor(operator)

    def backspace(self) -> None:
        if self.current_char == ")":
            self.set_gray(self.curreny_index)
            self.move_cursor_left()
        else:
            self.elements.pop()
            if not self.elements:
                self.elements.append("0")

    def convert_minus(self) -> None:
        if self.current_char == ")":
            del self.elements[self.curreny_index]
            for i in range(self.curreny_index - 1, -1, -1):
                if self.elements[i] == "(":
                    if self.elements[i + 1] == "-":
                        del self.elements[i + 1]
                    del self.elements[i]
                    break
            return
        if self.current_char not in CharType.DIGIT:
            print("qwe")
            return
        for i in range(len(self.elements) - 1, -1, -1):
            if self.elements[i] in CharType.OPERATOR:
                if self.elements[i] == "-":
                    self.elements[i] = "+"
                else:
                    self.elements.insert(i + 1, "-")
                    self.elements.insert(i + 1, "(")
                    self.add_on_cursor(")")
                break
        else:
            self.elements.insert(0, "-")
            self.elements.insert(0, "(")
            self.add_on_cursor(")")

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

        expression_str = normalize_operator(self.normalized_elements)
        self.elements = list((callculate(expression_str)))
        self.cursor_offset = 0

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
        if not self.elements:
            self.elements.append("0")

    def clear(self) -> None:
        self.elements.clear()
        self.elements.append("0")

    def copy(self) -> "Expression":
        new_expr = Expression()
        new_expr.elements = self.elements.copy()
        return new_expr

    def set_gray(self, index: int) -> None:
        self.remove_gray(index)
        self.elements[index] = (
            f"<span style='color: #858383'>{self.elements[index]}</span>"
        )

    def remove_gray(self, index: int) -> None:
        self.elements[index] = re.sub(r"<span.*?>", "", self.elements[index])
        self.elements[index] = re.sub(r"</span>", "", self.elements[index])
