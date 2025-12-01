import logging
import re

from dentaku.models import CharType

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)


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
    def current_index(self) -> int:
        return len(self.elements) - 1 - self.cursor_offset

    @property
    def current_char(self) -> str:
        return self.elements[-1 - self.cursor_offset]

    @current_char.setter
    def current_char(self, value: str) -> None:
        self.elements[-1 - self.cursor_offset] = value

    def left_char(self, offset: int) -> str:
        if self.cursor_offset + offset >= len(self.elements):
            return ""
        return self.elements[-1 - self.cursor_offset - offset]

    def add_on_cursor(self, value: str) -> None:
        self.elements.insert(len(self.elements) - self.cursor_offset, value)

    def remove_on_cursor(self) -> None:
        del self.elements[len(self.elements) - 1 - self.cursor_offset]

    def move_cursor_left(self) -> None:
        if self.cursor_offset < len(self.elements) - 1:
            self.cursor_offset += 1

    def move_cursor_right(self) -> None:
        if self.cursor_offset > 0:
            self.cursor_offset -= 1

    @property
    def is_last_number_zero(self) -> bool:
        logger.debug(f"elements: {self.elements}")
        if len(self.elements) == 1:
            return self.elements[0] == "0"
        left_char = self.left_char(1)
        return self.current_char == "0" and (
            left_char in CharType.OPERATOR or left_char in CharType.PARENTHESIS
        )

    def add_number(self, number: str) -> None:
        if self.current_char in CharType.OPERATOR and number == ".":
            self.add_on_cursor("0")
        if self.current_char == ")":
            self.add_operator("*")
            self.set_gray(len(self.elements) - 1)
        elif self.is_last_number_zero:
            self.remove_on_cursor()

        self.add_on_cursor(number)

    def add_operator(self, operator: str) -> None:
        if self.current_char in CharType.OPERATOR:
            self.current_char = operator
        else:
            self.add_on_cursor(operator)

    def backspace(self) -> None:
        if self.current_char == ")":
            self.set_gray(self.current_index)
            self.move_cursor_left()
            return

        if self.current_char == "(":
            self.move_cursor_right()
            self.remove_on_cursor()

        self.remove_on_cursor()
        if not self.elements:
            self.elements.append("0")

    def toggle_sign(self) -> None:
        if self.current_char == ")":
            self.__remove_negative_format()
            return
        if self.current_char not in CharType.DIGIT:
            return
        self.__apply_negative_format()

    def caluculate(self) -> None:
        from dentaku.core.callculate import callculate
        from dentaku.utils.convert import normalize_operator

        expression_str = normalize_operator(self.normalized_elements)
        self.elements = [callculate(expression_str)]
        self.cursor_offset = 0

    def clear_entry(self) -> None:
        closing_count = 0
        for i in self.__reverse_range_from_cursor():
            if self.elements[i] == ")":
                closing_count += 1
            elif self.elements[i] == "(":
                closing_count -= 1

            if self.elements[i] in CharType.OPERATOR and closing_count == 0:
                break
            self.remove_on_cursor()
        if not self.elements:
            self.elements.append("0")

    def clear(self) -> None:
        self.elements.clear()
        self.elements.append("0")
        self.cursor_offset = 0

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

    def __reverse_range_from_cursor(self) -> range:
        return range(self.current_index, -1, -1)

    def __apply_negative_format(self) -> None:
        for i in self.__reverse_range_from_cursor():
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

    def __remove_negative_format(self) -> None:
        del self.elements[self.current_index]
        for i in self.__reverse_range_from_cursor():
            if self.elements[i] == "(":
                if self.elements[i + 1] == "-":
                    del self.elements[i + 1]
                del self.elements[i]
                break
