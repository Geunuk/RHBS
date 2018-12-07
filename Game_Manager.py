#import Member
#import Admin
import datetime
from ui import dialog, error, member_info as mem_info,game_status_show,betting_result
from db import table, game_info
import Game

class Game_Manager:
    def __init__(self):
        self.__game_list = []
        self.__horse_list = None
        self.__login_account = None
        self.__init_ui = None
        self.__init_window = None
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
    def login_account(self):
        return self.__login_account

    @login_account.setter
    def login_account(self, login_account):
        self.__login_account = login_account

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

    def show_game_status_box(self):
        print("경기진행상황확인")
        self.__init_window.setEnabled(False)
        self.__game_status_show_Dialog = dialog.Dialog_Modified(self.__init_window)
        self.__game_status_show_ui = game_status_show.Ui_Dialog(self, self.__init_ui, self.__init_window)
        self.__game_status_show_ui.setupUi(self.__game_status_show_Dialog)
        self.__game_status_show_Dialog.show()

    def show_betting_result_box(self):
        print("show_betting_result 호출")
        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__betting_result_Dialog = dialog.Dialog_Modified(self.__init_window)
        self.__betting_result_ui = betting_result.Ui_Dialog(self, self.__init_ui)
        self.__betting_result_ui.setupUi(self.__betting_result_Dialog)
        self.__betting_result_Dialog.show()

    def check_game_finish(self):
        print("check game finished")
        now = datetime.datetime.now().replace(second=0)
        for game in self.__game_list:
            if game.proceeding == False and game.start_time.replace(second=0) <= now:
                game.proceeding = True
                game.login_account = self.__login_account
                game.decide_result()
                game.calc_dividend()

    def init_game(self):
        print("게임 객체 생성하자")
        game_list = table.Table("game_info")
        betting_list = table.Table("betting_info")
        for game in game_list:
            bet_info = []
            for info in betting_list:
                if(info.game_id == game.game_id):
                    bet_info.append(info)
            game1 = Game.Game(game.game_id,game.proceeding,game.result,game.horses,game.start_time,bet_info,game.dividend_rate)
            #game1.calc_dividend_rate()
            self.__game_list.append(game1)

    def save_game_file(self):
        print("끝났으니 게임 세이브하자~")
        game_list = []
        for g in self.__game_list:
            game = game_info.Game_Info(g.id,g.start_time,g.result,g.horses,g.dividend_rate,g.proceeding)
            game_list.append(game)
        game_table = table.Table("game_info")
        game_table.clear()
        game_table.extend(game_list)
        game_table.save_file()