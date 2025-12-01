from functools import partial

from PySide6 import QtWidgets

from dentaku.core.logic import Logic
from dentaku.utils import normalize_operator

from .widgets.dentaku_widgets import DentakuWidgets


class DentakuUi(DentakuWidgets):
    def __init__(self, logic: Logic):
        super().__init__()
        self.setup_ui()
        self.__wire()

        self.logic = logic

    @staticmethod
    def __refresh_ui():
        from functools import wraps

        def decorator(func):
            @wraps(func)
            def wrapper(self: "DentakuUi", *args, **kwargs):
                result = func(self, *args, **kwargs)
                self.main_label.setText(str(self.logic))
                self.sub_label.setText(
                    str(self.logic.sub_expression)
                    if str(self.logic.sub_expression) != "0"
                    else ""
                )
                return result

            return wrapper

        return decorator

    def start(self) -> None:
        self.show()
        self.raise_()
        self.activateWindow()

    @__refresh_ui()
    def on_number_clicked(self, num):
        self.logic.press_number(num)

    @__refresh_ui()
    def on_pluse_minus_clicked(self):
        self.logic.press_plus_minus()

    @__refresh_ui()
    def on_dot_clicked(self):
        self.logic.press_number(".")

    @__refresh_ui()
    def on_operator_clicked(self, operator):
        self.logic.press_operator(operator)

    @__refresh_ui()
    def on_equal_clicked(self):
        self.logic.press_equals()

    @__refresh_ui()
    def on_back_clicked(self):
        self.logic.press_back()

    @__refresh_ui()
    def on_clear_entry_clicked(self):
        self.logic.press_clear_entry()

    @__refresh_ui()
    def on_clear_clicked(self):
        self.logic.press_clear()

    def __wire(self):
        for btn in self.number_buttons():
            btn.clicked.connect(partial(self.on_number_clicked, btn.text()))

        self.button_plus_minus.clicked.connect(self.on_pluse_minus_clicked)

        for btn in self.operator_buttons():
            operator = normalize_operator(btn.text())
            btn.clicked.connect(partial(self.on_operator_clicked, operator))
        self.button_dot.clicked.connect(self.on_dot_clicked)

        self.button_equal.clicked.connect(self.on_equal_clicked)

        self.button_back.clicked.connect(self.on_back_clicked)
        self.button_ce.clicked.connect(self.on_clear_entry_clicked)
        self.button_c.clicked.connect(self.on_clear_clicked)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    logic = Logic()
    window = DentakuUi(logic)
    window.show()
    app.exec()
