import sys

from PyQt5 import QtWidgets

import Account_Manager
import Game_Manager
from ui import init
from db.table import Table
#from time import sleep

def main():
    gm = Game_Manager.Game_Manager()
    am = Account_Manager.Account_Manager(gm)


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    init_ui = init.Ui_MainWindow(am, gm)
    init_ui.setupUi(MainWindow)

    am.init_ui = init_ui
    am.init_window = MainWindow
    gm.init_ui = init_ui
    gm.init_window= MainWindow
    gm.init_game()
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":

    libpaths = QtWidgets.QApplication.libraryPaths()
    libpaths.append("C:\\Users\서강휘\AppData\Local\Programs\Python\Python37\Lib\site-packages\PyQt5\Qt\plugins")
    QtWidgets.QApplication.setLibraryPaths(libpaths)

    main()