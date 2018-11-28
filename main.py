import sys

from PyQt5 import QtWidgets

import Account_Manager
import Game_Manager
from ui import init
from db.table import Table



def main():
    am = Account_Manager.Account_Manager()
    gm = Game_Manager.Game_Manager()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    init_ui = init.Ui_MainWindow(am, gm)
    init_ui.setupUi(MainWindow)

    am.init_ui = init_ui
    am.init_window = MainWindow

    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()