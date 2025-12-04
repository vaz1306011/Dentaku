class Char:
    GRAY_COLOR: str = "#858383"

    def __init__(self, char: str) -> None:
        self.raw: str = char
        self.is_gray: bool = False

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Char):
            return self.raw == other.raw
        elif isinstance(other, str):
            return self.raw == other
        return False

    @property
    def display(self) -> str:
        def replace_ops(text: str):
            text = text.replace("/", "÷")
            text = text.replace("*", "×")
            return text

        char = replace_ops(self.raw)
        if self.is_gray:
            return f"<span style='color: {self.GRAY_COLOR}'>{char}</span>"
        return char

    @classmethod
    def zero(cls) -> "Char":
        return cls("0")

    def set_gray(self, status: bool) -> None:
        self.is_gray = status
