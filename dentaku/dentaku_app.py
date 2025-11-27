from dentaku.core.logic import Logic

from .ui.dentaku_ui import DentakuUi


class DentakuApp:
    def __init__(self) -> None:
        self.logic = Logic()
        self.ui = DentakuUi(self.logic)

    def start(self) -> None:
        self.ui.start()
