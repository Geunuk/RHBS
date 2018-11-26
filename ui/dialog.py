from PyQt5 import QtWidgets

class Dialog_Modified(QtWidgets.QDialog):
    def __init__(self, prev_dialog):
        super().__init__()
        self.__prev_dialog = prev_dialog

    def closeEvent(self, QCloseEvent):
        self.__prev_dialog.setEnabled(True)