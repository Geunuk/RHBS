import sys

from PyQt5 import QtWidgets

import Account_Manager
import Game_Manager
from ui import init,main_window
from db.table import Table


def main():
    gm = Game_Manager.Game_Manager()
    am = Account_Manager.Account_Manager(gm)


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = main_window.Main_window()
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
    main()