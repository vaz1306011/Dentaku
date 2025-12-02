from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QFrame, QLabel, QScrollArea, QSizePolicy


class ScrollLabel(QScrollArea):
    def __init__(
        self,
        text: str,
        font_size: float = 10,
        font_color: str = "#FFFFFF",
    ) -> None:
        super().__init__()
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.anim = QPropertyAnimation(self.horizontalScrollBar(), b"value")
        self.anim.setDuration(150)
        self.anim.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.label = QLabel(text, self)
        self.__init_label(font_size, font_color)

        self.setWidget(self.label)

    def setText(self, text: str) -> None:
        self.label.setText(text)

    def setLabelAlignment(self, arg__1: Qt.AlignmentFlag) -> None:
        self.label.setAlignment(arg__1)

    def wheelEvent(self, event) -> None:
        delta = event.angleDelta().y()

        bar = self.horizontalScrollBar()
        start = bar.value()
        end = start - delta

        end = max(bar.minimum(), min(bar.maximum(), end))

        self.anim.stop()

        self.anim.setStartValue(start)
        self.anim.setEndValue(end)
        self.anim.start()

        event.accept()

    def __init_label(self, font_size, font_color):
        self.label.setContentsMargins(0, 0, 10, 0)
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        self.label.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        self.label.setTextFormat(Qt.TextFormat.RichText)

        font = self.label.font()
        font.setPointSizeF(font_size)
        self.label.setFont(font)

        palette = self.label.palette()
        palette.setColor(QPalette.ColorRole.WindowText, QColor(font_color))
        self.label.setPalette(palette)
