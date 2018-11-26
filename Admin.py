from ui import dialog

class Admin():
    def __init__(self):
        self.__game_manage_Dialog = None
        self.__game_manage_ui = None

    def show_game(self):
        print("show game box")
        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__game_manage_Dialog = dialog.Dialog_Modified(self.__init_window)
        #self.__game_manage_ui = manage_game.Ui_Dialog(self, self.__init_ui)
        self.__game_manage_ui.setupUi(self.__game_manage_Dialog)
        self.__game_manage_Dialog.show()

    def register_game(self):
        ...

    def delete_game(self):
        ...

    def show_game(self):
        ...

    def valid_register(self):
        ...