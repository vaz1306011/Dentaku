from typing import Any, Generator

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QGridLayout, QVBoxLayout, QWidget

from .buttons import BottomButton, Button, RightButton, TopButton
from .scroll_label import ScrollLabel


class DentakuWidgets(QWidget):
    def setup_ui(self, bg_color: str = "#322e2e") -> None:
        # self.setWindowTitle("電卓")
        self.setFixedSize(230, 380)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(bg_color))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        Vstack = QVBoxLayout(self)
        Vstack.setAlignment(Qt.AlignmentFlag.AlignTop)
        Vstack.setContentsMargins(0, 0, 0, 0)
        Vstack.setSpacing(0)

        self.sub_label = ScrollLabel("", font_size=22, font_color="#a2a1a1")
        self.sub_label.setFixedHeight(50)
        self.sub_label.setLabelAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom
        )
        Vstack.addWidget(self.sub_label)

        self.main_label = ScrollLabel("0", font_size=30, font_color="#dfdfdf")
        self.main_label.setFixedHeight(50)
        Vstack.addWidget(self.main_label)

        self.button_back = TopButton("←", parent=self)
        self.button_ce = TopButton("CE", parent=self)
        self.button_c = TopButton("C", parent=self)

        self.button_plus_minus = BottomButton("+/-", parent=self)
        self.button_dot = BottomButton(".", parent=self)
        self.button_0 = BottomButton("0", parent=self)
        self.button_1 = BottomButton("1", parent=self)
        self.button_2 = BottomButton("2", parent=self)
        self.button_3 = BottomButton("3", parent=self)
        self.button_4 = BottomButton("4", parent=self)
        self.button_5 = BottomButton("5", parent=self)
        self.button_6 = BottomButton("6", parent=self)
        self.button_7 = BottomButton("7", parent=self)
        self.button_8 = BottomButton("8", parent=self)
        self.button_9 = BottomButton("9", parent=self)

        self.button_plus = RightButton("+", parent=self)
        self.button_minus = RightButton("-", parent=self)
        self.button_multiply = RightButton("×", parent=self)
        self.button_divide = RightButton("÷", parent=self)
        self.button_equal = RightButton("=", parent=self)

        layout = QGridLayout()
        layout.setContentsMargins(10, 0, 10, 0)
        layout.setSpacing(5)
        for i, button in enumerate(self.all_buttons()):
            row = 1 + i // 4
            col = i % 4
            layout.addWidget(button, row, col)

        Vstack.addLayout(layout)

    def all_buttons(self) -> Generator[Button, Any, None]:
        for widget in (
            self.button_back,
            self.button_ce,
            self.button_c,
            self.button_divide,
            self.button_7,
            self.button_8,
            self.button_9,
            self.button_multiply,
            self.button_4,
            self.button_5,
            self.button_6,
            self.button_minus,
            self.button_1,
            self.button_2,
            self.button_3,
            self.button_plus,
            self.button_plus_minus,
            self.button_0,
            self.button_dot,
            self.button_equal,
        ):
            yield widget

    def number_buttons(self) -> Generator[Button, Any, None]:
        for widget in (
            self.button_0,
            self.button_1,
            self.button_2,
            self.button_3,
            self.button_4,
            self.button_5,
            self.button_6,
            self.button_7,
            self.button_8,
            self.button_9,
        ):
            yield widget

    def operator_buttons(self) -> Generator[Button, Any, None]:
        for widget in (
            self.button_plus,
            self.button_minus,
            self.button_multiply,
            self.button_divide,
        ):
            yield widget


if __name__ == "__main__":
    app = QApplication([])
    window = DentakuWidgets()
    window.setup_ui()
    window.show()
    app.exec()
