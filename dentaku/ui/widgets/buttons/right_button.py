from .button import Button


class RightButton(Button):
    def __init__(
        self,
        text,
        color="#fffaf1",
        bg_color="#ff8c00",
        color_p="#fffbf2",
        bg_color_p="#ffa100",
        parent=None,
    ):
        super().__init__(text, parent)
        self.set_colors(color, bg_color, color_p, bg_color_p)
