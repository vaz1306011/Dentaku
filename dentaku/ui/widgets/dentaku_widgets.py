from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from .buttons import BottomButton, RightButton, TopButton


class DentakuWidgets(QWidget):
    def setup_ui(self):
        self.setWindowTitle("電卓")
        self.setFixedSize(230, 380)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#2b2727"))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        Vstack = QVBoxLayout(self)
        Vstack.setContentsMargins(10, 10, 10, 10)
        Vstack.setSpacing(0)

        self.sub_label = QLabel("", self)
        self.sub_label.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        Vstack.addWidget(self.sub_label)

        self.main_label = QLabel(str(0), self)
        self.main_label.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        self.main_label.setTextFormat(Qt.TextFormat.RichText)
        self.main_label.setStyleSheet("font-size: 32px;")
        Vstack.addWidget(self.main_label)

        self.button_back = TopButton("←", self)
        self.button_ce = TopButton("CE", self)
        self.button_c = TopButton("C", self)

        self.button_plus_minus = BottomButton("+/-", self)
        self.button_dot = BottomButton(".", self)
        self.button_0 = BottomButton("0", self)
        self.button_1 = BottomButton("1", self)
        self.button_2 = BottomButton("2", self)
        self.button_3 = BottomButton("3", self)
        self.button_4 = BottomButton("4", self)
        self.button_5 = BottomButton("5", self)
        self.button_6 = BottomButton("6", self)
        self.button_7 = BottomButton("7", self)
        self.button_8 = BottomButton("8", self)
        self.button_9 = BottomButton("9", self)

        self.button_plus = RightButton("+", self)
        self.button_minus = RightButton("-", self)
        self.button_multiply = RightButton("×", self)
        self.button_divide = RightButton("÷", self)
        self.button_equal = RightButton("=", self)

        layout = QGridLayout()
        layout.setSpacing(5)
        for i, button in enumerate(self.all_buttons()):
            row = 1 + i // 4
            col = i % 4
            layout.addWidget(button, row, col)

        Vstack.addLayout(layout)

    def all_buttons(self):
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

    def number_buttons(self):
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

    def operator_buttons(self):
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
