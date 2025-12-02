from PySide6.QtWidgets import QPushButton


class Button(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)

        self.setFixedSize(49, 49)
        self.setStyleSheet(
            """
            QPushButton {
                border-radius: 24px;
                font-size: 20px;
            }
            """
        )

    def set_colors(
        self,
        color: str,
        bg_color: str,
        color_p: str,
        bg_color_p: str,
    ) -> None:
        style_sheet = self.styleSheet()
        self.setStyleSheet(
            style_sheet
            + f"""
            QPushButton {{
                color: {color};
                background-color: {bg_color};
            }}
            QPushButton:pressed {{
                color: {color_p};
                background-color: {bg_color_p};
            }}
            """
        )
