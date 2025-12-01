from PySide6.QtWidgets import QPushButton


class BottomButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)

        self.setFixedSize(48, 48)
        self.setStyleSheet(
            """
            QPushButton {
                border-radius: 24px;
                color: #f6f6f6;
                background-color: #4c4a4b;
                font-size: 20px;
            }
            QPushButton:pressed {
                background-color: #635f5f;
                color: #f7f7f7;
            }
            """
        )
