import datetime

from ui import dialog, manage_game, manage_game_add, error
from db import table
import Game

class Admin():
    def __init__(self, gm, init_ui, init_window):
        self.__game_manager = gm

        self.__init_ui = init_ui
        self.__init_window = init_window
        self.__game_manage_Dialog = None
        self.__game_manage_ui = None
        self.__manage_game_add_Dialog = None
        self.__manage_game_add_ui = None

    @property
    def game_manager(self):
        return self.__game_manager

    @game_manager.setter
    def game_manager(self, game_manager):
        self.__game_manager = game_manager

    def show_manage_game_box(self):
        print("경기 관리 박스 표시")
        self.__init_window.setEnabled(False)

        self.__game_manage_Dialog = dialog.Dialog_Modified(self.__init_window)
        self.__game_manage_ui = manage_game.Ui_Dialog(self, self.__init_ui)
        self.__game_manage_ui.game_manager = self.__game_manager
        self.__game_manage_ui.setupUi(self.__game_manage_Dialog)
        self.__game_manage_Dialog.show()

    def show_game_add_box(self):
        print("경기 추가 박스 표시")
        self.__game_manage_Dialog.setEnabled(False)

        self.__manage_game_add_Dialog = dialog.Dialog_Modified(self.__game_manage_Dialog)
        self.__manage_game_add_ui = manage_game_add.Ui_Dialog(self, self.__init_ui)
        self.__manage_game_add_ui.setupUi(self.__manage_game_add_Dialog)
        self.__manage_game_add_Dialog.show()

    def show_error_box(self, prev_dialog, msg):
        print("에러 박스 표시")
        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__error_Dialog = dialog.Dialog_Modified(prev_dialog)
        self.__error_ui = error.Ui_Dialog(self, prev_dialog)
        self.__error_ui.setupUi(self.__error_Dialog)
        self.__error_ui.error_label.setText(msg)
        self.__error_Dialog.show()

    def register_game(self, game_id, start_time, horse_name_list):
        print("경기 추가")

        today = datetime.date.today()
        start_time = datetime.datetime.strptime(start_time, "%p %I:%M")
        start_time = start_time.replace(year=today.year, month=today.month, day=today.day)

        valid_result = self.isvalid_register(game_id, start_time, horse_name_list)
        if valid_result == 0:
            self.__manage_game_add_Dialog.close()
            horse_table = table.Table("horse_info")
            horse_info_list = []
            for horse_name in horse_name_list:
                horse_info_list.append(horse_table.get_row((horse_name,)))
            new_game = Game.Game(game_id,False,[],horse_info_list,start_time,[],[1,1,1,1,1])
            self.__game_manager.game_list.append(new_game)
            self.__game_manage_ui.set_game_table()

        elif valid_result == 1:
            self.__manage_game_add_Dialog.setEnabled(False)
            self.show_error_box(self.__manage_game_add_Dialog, "빈 항목이 있습니다")

        elif valid_result == 2:
            self.__manage_game_add_Dialog.setEnabled(False)
            self.show_error_box(self.__manage_game_add_Dialog, "동일한 경기 이름이 존재합니다")

        elif valid_result == 3:
            self.__manage_game_add_Dialog.setEnabled(False)
            self.show_error_box(self.__manage_game_add_Dialog, "말이 중복됩니다")

        else:
            self.__manage_game_add_Dialog.setEnabled(False)
            self.show_error_box(self.__manage_game_add_Dialog, "경기 시간은 현재 시간보다 나중이어야 합니다")

    def delete_game(self, deleted_idx):
        print("경기 삭제")
        valid_result = self.isvalid_delete(self.__game_manager.game_list[deleted_idx])
        if(valid_result):
            self.__game_manager.game_list.pop(deleted_idx)
            self.__game_manage_ui.set_game_table()
        else:
            self.__game_manage_Dialog.setEnabled(False)
            self.show_error_box(self.__game_manage_Dialog, "종료되지 않은 경기 입니다.")

    def isvalid_register(self, game_id, start_time, horse_name_list):
        """
        :return: 0 => success
                  1 => empty input
                  2 => duplicate game_id
                  3 => duplicate horses
                  4 => duplicate ssn
        """
        game_id_list = []
        for game in self.__game_manager.game_list:
            game_id_list.append(game.id)

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

    def isvalid_delete(self,game):
        if(game.proceeding == True):
            return True
        else :
            return False