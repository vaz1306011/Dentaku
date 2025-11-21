from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class DentakuWidgets(QWidget):
    def setup_ui(self):
        self.setWindowTitle("電卓")
        self.resize(280, 400)

        Vstack = QVBoxLayout(self)

        self.label = QLabel(str(0), self)
        Vstack.addWidget(self.label)

        self.button_back = QPushButton("←", self)
        self.button_ce = QPushButton("CE", self)
        self.button_c = QPushButton("C", self)

        self.button_plus_minus = QPushButton("+/-", self)
        self.button_dot = QPushButton(".", self)
        self.button_0 = QPushButton("0", self)
        self.button_1 = QPushButton("1", self)
        self.button_2 = QPushButton("2", self)
        self.button_3 = QPushButton("3", self)
        self.button_4 = QPushButton("4", self)
        self.button_5 = QPushButton("5", self)
        self.button_6 = QPushButton("6", self)
        self.button_7 = QPushButton("7", self)
        self.button_8 = QPushButton("8", self)
        self.button_9 = QPushButton("9", self)

        self.button_plus = QPushButton("+", self)
        self.button_minus = QPushButton("-", self)
        self.button_multiply = QPushButton("×", self)
        self.button_divide = QPushButton("÷", self)
        self.button_equal = QPushButton("=", self)

        layout = QGridLayout()
        for i, button in enumerate(self.button_widgets()):
            row = 1 + i // 4
            col = i % 4
            # button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            layout.addWidget(button, row, col)

        Vstack.addLayout(layout)

    def button_widgets(self):
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


if __name__ == "__main__":
    app = QApplication([])
    window = DentakuWidgets()
    window.setup_ui()
    window.show()
    app.exec()
