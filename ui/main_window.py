from PyQt5 import QtWidgets

class Main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def closeEvent(self, QCloseEvent):
        print("메인 윈도우가 닫혔다!")