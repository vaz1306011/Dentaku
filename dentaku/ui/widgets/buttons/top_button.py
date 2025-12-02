from .button import Button


class TopButton(Button):
    def __init__(
        self,
        text,
        color="#f8f8f8",
        bg_color="#767474",
        color_p="#f9f9f9",
        bg_color_p="#8b8989",
        parent=None,
    ):
        super().__init__(text, parent)
        self.set_colors(color, bg_color, color_p, bg_color_p)
