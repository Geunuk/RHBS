import datetime

from ui import dialog, manage_game, manage_game_add, error
from db import table
import Game

class Admin():
    def __init__(self, init_ui, init_window):
        self.__init_ui = init_ui
        self.__init_window = init_window
        self.__game_manage_Dialog = None
        self.__game_manage_ui = None
        self.__manage_game_add_Dialog = None
        self.__manage_game_add_ui = None
        self.__game_manager = None

    @property
    def game_manager(self):
        return self.__game_manager

    @game_manager.setter
    def game_manager(self, game_manager):
        self.__game_manager = game_manager

    def show_manage_game_box(self):
        print("show manage game box")
        self.__init_window.setEnabled(False)

        self.__game_manage_Dialog = dialog.Dialog_Modified(self.__init_window)
        self.__game_manage_ui = manage_game.Ui_Dialog(self, self.__init_ui)
        self.__game_manage_ui.game_manager = self.__game_manager
        self.__game_manage_ui.setupUi(self.__game_manage_Dialog)
        self.__game_manage_Dialog.show()

    def show_game_add_box(self):
        print("show game add box")
        self.__game_manage_Dialog.setEnabled(False)

        self.__manage_game_add_Dialog = dialog.Dialog_Modified(self.__game_manage_Dialog)
        self.__manage_game_add_ui = manage_game_add.Ui_Dialog(self, self.__init_ui)
        self.__manage_game_add_ui.setupUi(self.__manage_game_add_Dialog)
        self.__manage_game_add_Dialog.show()

    def show_error_box(self, prev_dialog, msg):
        print("show error box")
        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__error_Dialog = dialog.Dialog_Modified(prev_dialog)
        self.__error_ui = error.Ui_Dialog(self, prev_dialog)
        self.__error_ui.setupUi(self.__error_Dialog)
        self.__error_ui.error_label.setText(msg)
        self.__error_Dialog.show()

    def register_game(self, game_id, start_time, horse_name_list):
        print("register game")

        today = datetime.date.today()
        start_time = datetime.datetime.strptime(start_time, "%p %I:%M")
        start_time = start_time.replace(year=today.year, month=today.month, day=today.day)

        valid_result = self.isvalid_register(game_id, start_time, horse_name_list)
        if valid_result == 0:
            self.__manage_game_add_Dialog.close()
            horse_table = table.Table("horse_info")
            horse_info_list = []
            for horse_name in horse_name_list:
                print(horse_name)
                horse_info_list.append(horse_table.get_row((horse_name,)))
            new_game = Game.Game(game_id,False,[],horse_info_list,start_time,[],[1,1,1,1,1])
            self.__game_manager.game_list.append(new_game)
            self.__game_manage_ui.set_game_table()

        elif valid_result == 1:
            print("not valid register")
            self.__manage_game_add_Dialog.setEnabled(False)
            self.show_error_box(self.__manage_game_add_Dialog, "빈 항목이 있습니다")
        elif valid_result == 2:
            print("not valid register")
            self.__manage_game_add_Dialog.setEnabled(False)
            self.show_error_box(self.__manage_game_add_Dialog, "동일한 경기 이름이 존재합니다")
        elif valid_result == 3:
            print("not valid register")
            self.__manage_game_add_Dialog.setEnabled(False)
            self.show_error_box(self.__manage_game_add_Dialog, "말이 중복됩니다")
        else:
            print("not valid register")
            self.__manage_game_add_Dialog.setEnabled(False)
            self.show_error_box(self.__manage_game_add_Dialog, "경기 시간은 현재 시간보다 나중이어야 합니다")

    def delete_game(self, deleted_idx):
        print("delete game")

        self.__game_manager.game_list.pop(deleted_idx)
        self.__game_manage_ui.set_game_table()

    def isvalid_register(self, game_id, start_time, horse_name_list):
        """
        :return: 0 => success
                  1 => empty input
                  2 => duplicate game_id
                  3 => duplicate horses
                  4 => duplicate ssn
        """
        print("isvalid_register")

        game_table = table.Table("game_info")
        game_table.load_file()
        game_id_list = [x[0] for x in game_table.select_all_row(('game_id',))]

        if "" in [game_id, start_time]:
            return 1
        elif game_id in game_id_list:
            return 2
        elif len(horse_name_list) != len(set(horse_name_list)):
            return 3
        elif start_time.replace(second=0) <= datetime.datetime.now().replace(second=0):
            return 4
        else:
            return 0

    def isvalid_delete(self):
        return True