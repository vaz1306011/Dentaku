from .ui.dentaku_ui import DentakuUi


class DentakuApp:
    def __init__(self) -> None:
        self.__ui = DentakuUi()

    def start(self) -> None:
        self.__ui.start()
