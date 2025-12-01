from PySide6.QtWidgets import QPushButton


class TopButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)

        self.setFixedSize(48, 48)
        self.setStyleSheet(
            """
            QPushButton {
                border-radius: 24px;
                color: #f8f8f8;
                background-color: #767474;
                font-size: 20px;
            }
            QPushButton:pressed {
                color: #f9f9f9;
                background-color: #8b8989;
            }
            """
        )
