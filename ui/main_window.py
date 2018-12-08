from PyQt5 import QtWidgets

class Main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.__game_manager = None

    @property
    def game_manager(self):
        return self.__game_manager

    @game_manager.setter
    def game_manager(self, game_manager):
        self.__game_manager = game_manager

    def closeEvent(self, QCloseEvent):
        self.__game_manager.save_game_file()