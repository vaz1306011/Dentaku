from PySide6 import QtWidgets

from .dentaku_widgets import DentakuWidgets


class DentakuUi(DentakuWidgets):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def start(self) -> None:
        self.show()
        self.raise_()
        self.activateWindow()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = DentakuUi()
    window.show()
    app.exec()
