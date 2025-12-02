from .button import Button


class BottomButton(Button):
    def __init__(
        self,
        text,
        color="#f6f6f6",
        bg_color="#4c4a4b",
        color_p="#f7f7f7",
        bg_color_p="#635f5f",
        parent=None,
    ):
        super().__init__(text, parent)
        self.set_colors(color, bg_color, color_p, bg_color_p)
