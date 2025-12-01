from enum import Enum


class CharType(Enum):
    DIGIT = "0123456789"
    OPERATOR = "+-*/"
    DECIMAL_POINT = "."
    PARENTHESIS = "()"

    def __contains__(self, item: str) -> bool:
        return item in self.value
