from enum import Enum, auto


class ButtonType(Enum):
    NONE = auto()
    NUMBER = auto()
    OPERATOR = auto()
    PARENTHESIS = auto()
    EQUALS = auto()
    CLEAR = auto()
    CLEAR_ENTRY = auto()
