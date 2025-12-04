import logging
import re
from typing import Optional

from .entities import Char
from .enums import CharType

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Expression:
    def __init__(self) -> None:
        self.elements: list[Char] = [Char("0")]
        self.cursor_offset: int = 0

    def __str__(self) -> str:
        return "".join(e.display for e in self.elements)

    @property
    def normalized_elements(self) -> str:
        return "".join(e.raw for e in self.elements)

    @property
    def current_index(self) -> int:
        return len(self.elements) - 1 - self.cursor_offset

    @current_index.setter
    def current_index(self, value: int) -> None:
        element_length = len(self.elements)
        value = max(0, min(element_length - 1, value))
        self.cursor_offset = element_length - 1 - value

    @property
    def current_char(self) -> str:
        return self.elements[-1 - self.cursor_offset].raw

    @current_char.setter
    def current_char(self, value: str) -> None:
        self.elements[-1 - self.cursor_offset] = Char(value)

    def get_left_char(self, offset: int) -> str:
        new_offset = self.cursor_offset + offset
        if new_offset >= len(self.elements):
            return ""
        return self.elements[-1 - new_offset].raw

    def get_right_char(self, offset: int) -> str:
        new_offset = self.cursor_offset - offset
        if new_offset < 0:
            return ""
        return self.elements[-1 - new_offset].raw

    def add_on_cursor(self, value: str) -> None:
        self.elements.insert(self.current_index + 1, Char(value))

    def add_on_index(self, index: int, value: str) -> None:
        self.elements.insert(index, Char(value))

    def remove_on_cursor(self) -> None:
        del self.elements[self.current_index]

    def add_number(self, number: str) -> None:
        if self.current_char == ")":
            self.add_operator("*")
            self.set_gray(True)
        elif self.__is_last_number_zero():
            self.remove_on_cursor()

        self.add_on_cursor(number)

    def add_dot(self) -> None:
        current_char = self.current_char
        if current_char == ".":
            return

        if current_char not in CharType.DIGIT:
            self.add_number("0")

        self.add_on_cursor(".")

    def add_operator(self, operator: str) -> None:
        if self.current_char in CharType.OPERATOR:
            self.current_char = operator
        else:
            self.add_on_cursor(operator)

    def add_parenthesis(self, parenthesis: str) -> None:
        current_char = self.current_char
        if parenthesis == "(":
            if current_char in CharType.DIGIT or current_char == ")":
                self.add_on_cursor("*")
                self.set_gray(True)
            self.add_on_cursor("(")
            self.add_on_cursor(")")
            self.set_gray(True)
            self.cursor_offset += 1

        elif parenthesis == ")":
            if current_char == "(":
                return
            if self.get_right_char(1) == ")":
                self.current_index += 1
                self.set_gray(status=False)

    def backspace(self) -> None:
        if self.current_char == ")":
            self.set_gray(True)
            self.current_index -= 1
            return

        if self.current_char == "(":
            self.current_index += 1
            self.remove_on_cursor()

        self.remove_on_cursor()
        if not self.elements:
            self.elements.append(Char.zero())

    def toggle_sign(self) -> None:
        if self.current_char == ")":
            self.__remove_negative_format()
            return
        if self.current_char not in CharType.DIGIT:
            return
        self.__apply_negative_format()

    def caluculate(self) -> None:
        from dentaku.core.callculate import calculate
        from dentaku.utils.convert import normalize_operator

        normalize_expression = normalize_operator(self.normalized_elements)
        ans = calculate(normalize_expression)
        self.elements = [Char(c) for c in ans]
        self.cursor_offset = 0

    def clear_entry(self) -> None:
        closing_count = 0
        for i in self.__reverse_range_from_cursor():
            if self.elements[i] == ")":
                closing_count += 1
            elif self.elements[i] == "(":
                closing_count -= 1

            if self.elements[i].raw in CharType.OPERATOR and closing_count == 0:
                break
            self.remove_on_cursor()
        if not self.elements:
            self.elements.append(Char.zero())

    def clear(self) -> None:
        self.elements.clear()
        self.elements.append(Char.zero())
        self.cursor_offset = 0

    def copy(self) -> "Expression":
        new_expr = Expression()
        new_expr.elements = self.elements.copy()
        return new_expr

    def set_gray(self, status) -> None:
        self.elements[self.current_index].set_gray(status)

    def __is_last_number_zero(self) -> bool:
        if len(self.elements) == 1:
            return self.elements[0] == "0"
        left_char = self.get_left_char(1)
        return self.current_char == "0" and (
            left_char in CharType.OPERATOR or left_char in CharType.PARENTHESIS
        )

    def __reverse_range_from_cursor(self) -> range:
        return range(self.current_index, -1, -1)

    def __apply_negative_format(self) -> None:
        for i in self.__reverse_range_from_cursor():
            if self.elements[i].raw in CharType.OPERATOR:
                if self.elements[i] == "-":
                    self.elements[i] = Char("+")
                else:
                    self.add_on_index(i + 1, "-")
                    self.add_on_index(i + 1, "(")
                    self.add_on_cursor(")")
                break
        else:
            self.add_on_index(0, "-")
            self.add_on_index(0, "(")
            self.add_on_cursor(")")

    def __remove_negative_format(self) -> None:
        del self.elements[self.current_index]
        for i in self.__reverse_range_from_cursor():
            if self.elements[i] == "(":
                if self.elements[i + 1] == "-":
                    del self.elements[i + 1]
                del self.elements[i]
                break
