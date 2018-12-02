#import Member
#import Admin
from ui import dialog, error, member_info as mem_info,game_status_show,betting_result
#from db import member_info, table
class Game_Manager:
    def __init__(self):
        self.__game_list = None
        self.__horse_list = None
        self.__init_ui = None
        self.__init_window = None
        '''self.__signup_Dialog = None
        self.__signup_ui = None
        self.__login_Dialog = None
        self.__login_ui = None'''

        self.__betting_result_Dialog = None
        self.__betting_result_ui = None
        self.__game_status_show_Dialog = None
        self.__game_status_show_ui = None
        self.__error_Dialog = None
        self.__error_ui = None

    @property
    def init_ui(self):
        return self.__init_ui

    @init_ui.setter
    def init_ui(self, init_ui):
        self.__init_ui = init_ui

    @property
    def init_window(self):
        return self.__init_window

    @init_window.setter
    def init_window(self, init_window):
        self.__init_window = init_window

    @property
    def game_list(self):
        return self.__game_list

    @game_list.setter
    def game_list(self, game_list):
        self.__game_list = game_list

    @property
    def horse_list(self):
        return self.__horse_list

    @horse_list.setter
    def horse_list(self, horse_list):
        self.__horse_list = horse_list

    def check_game_finish(self):
        ...

    def init_game(self):
        ...

    def show_game_status(self):
        ...

    def show_betting_result(self):
        print("show_betting_result 호출")
        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__betting_result_Dialog = dialog.Dialog_Modified(self.__init_window)
        self.__betting_result_ui = betting_result.Ui_Dialog(self, self.__init_ui)
        self.__betting_result_ui.setupUi(self.__betting_result_Dialog)
        self.__betting_result_Dialog.show()

    def read_game_file(self):
        ...

    def save_game_file(self):
        ...

    def read_betting_file(self):
        ...

    def save_betting_file(self):
        ...

    def read_horse_file(self):
        ...