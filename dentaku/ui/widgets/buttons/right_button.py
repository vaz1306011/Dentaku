from PySide6.QtWidgets import QPushButton


class RightButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)

        self.setFixedSize(48, 48)
        self.setStyleSheet(
            """
            QPushButton {
                border-radius: 24px;
                color: #fffaf1;
                background-color: #ff8c00;
                font-size: 30px;
            }
            QPushButton:pressed {
                color: #fffbf2;
                background-color: #ffa100;
            }
            """
        )
