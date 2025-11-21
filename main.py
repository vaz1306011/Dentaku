"""
/* -------------------------------------------------------------------------- */
/* ファイル名：0G02019_dentaku */
/* 作 成 日：2025/11/17 */
/* 作 成 者：0G02019 謝 名飛 */
/* -------------------------------------------------------------------------- */
"""

from PySide6 import QtWidgets

from dentaku import DentakuApp

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    dentaku_app = DentakuApp()
    dentaku_app.start()

    app.exec()
