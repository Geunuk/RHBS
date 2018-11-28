import Member
import Admin
from ui import dialog, signup, login, error, member_info as mem_info
from db import member_info, table

class Account_Manager():
    def __init__(self):
        self.__login_account = None

        self.__init_ui = None
        self.__init_window = None
        self.__signup_Dialog = None
        self.__signup_ui = None
        self.__login_Dialog = None
        self.__login_ui = None
        self.__member_info_Dialog = None
        self.__member_info_ui = None
        self.__error_Dialog = None
        self.__error_ui = None

    @property
    def login_account(self):
        return self.__login_account

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

    def show_signup_box(self):
        print("show signup box")
        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__signup_Dialog = dialog.Dialog_Modified(self.__init_window)
        self.__signup_ui = signup.Ui_Dialog(self, self.__init_ui)
        self.__signup_ui.setupUi(self.__signup_Dialog)
        self.__signup_Dialog.show()

    def show_login_box(self):
        print("show login box")
        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__login_Dialog = dialog.Dialog_Modified(self.__init_window)
        self.__login_ui = login.Ui_Dialog(self, self.__init_ui)
        self.__login_ui.setupUi(self.__login_Dialog)
        self.__login_Dialog.show()

    def show_member_info_box(self):
        print("show member info box")
        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__member_info_Dialog = dialog.Dialog_Modified(self.__init_window)
        self.__member_info_ui = mem_info.Ui_Dialog(self, self.__init_ui)
        self.__member_info_ui.setupUi(self.__member_info_Dialog)
        self.__member_info_Dialog.show()

    def show_error_box(self, prev_dialog, msg):
        print("show error box")
        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__error_Dialog = dialog.Dialog_Modified(prev_dialog)
        self.__error_ui = error.Ui_Dialog(self, prev_dialog)
        self.__error_ui.setupUi(self.__error_Dialog)
        self.__error_ui.error_label.setText(msg)
        self.__error_Dialog.show()

    def signup(self, input_member_info):
        print("sign up")

        valid_result = self.isvalid_signup(input_member_info)
        if valid_result == 0:
            print("valid signup")
            self.__signup_Dialog.close()
            member_table = table.Table("member_info")
            member = member_info.Member_Info(input_member_info[0], input_member_info[1]
                                             ,input_member_info[3], input_member_info[4]
                                             ,input_member_info[5], input_member_info[6]
                                             ,input_member_info[7])

            member_table.append(member)
            member_table.save_file()

        elif valid_result == 1:
            print("not valid signup")
            self.__signup_Dialog.setEnabled(False)
            self.show_error_box(self.__signup_Dialog, "빈 항목이 있습니다")

        elif valid_result == 2:
            print("not valid signup")
            self.__signup_Dialog.setEnabled(False)
            self.show_error_box(self.__signup_Dialog, "동일한 ID가 이미 존재합니다")

        elif valid_result == 3:
            print("not valid signup")
            self.__signup_Dialog.setEnabled(False)
            self.show_error_box(self.__signup_Dialog, "패스워드가 일치하지 않습니다")

        else:
            print("not valid signup")
            self.__signup_Dialog.setEnabled(False)
            self.show_error_box(self.__signup_Dialog, "주민번호가 이미 존재합니다")

    def login(self, id, pw):
        valid_result = self.isvalid_login(id, pw)
        if  valid_result == 0:
            self.__login_Dialog.close()

            self.__init_ui.init_login_btn.setText("로그아웃")
            self.__init_ui.init_signup_btn.setText("회원정보확인")

            member_table = table.Table("member_info")
            member_info = member_table.select_row((id,), ('member_id', 'password'
                                                          , 'name', 'ssn', 'account_number'
                                                          , 'email', 'phone_number', 'point'))

            if self.is_admin(id):
                self.__init_ui.init_game_manage_btn.setEnabled(True)
                self.__init_ui.init_signup_btn.setEnabled(False)
                self.__login_account = Admin.Admin(self.__init_ui, self.__init_window)

            else:
                self.__init_ui.init_bet_btn.setEnabled(True)
                self.__init_ui.init_bet_result_btn.setEnabled(True)
                self.__init_ui.init_game_status_btn.setEnabled(True)
                self.__init_ui.init_charge_point_btn.setEnabled(True)
                self.__init_ui.init_exchange_point_btn.setEnabled(True)

                self.__login_account = Member.Member(member_info[0], member_info[1]
                                                     , member_info[2], member_info[3]
                                                     , member_info[4], member_info[5]
                                                     , member_info[6], int(member_info[7])
                                                     , self.__init_ui, self.__init_window)

        elif valid_result == 1:
            print("not valid login")
            self.__login_Dialog.setEnabled(False)
            self.show_error_box(self.__login_Dialog, "빈 항목이 있습니다")
        elif valid_result == 2:
            print("not valid login")
            self.__login_Dialog.setEnabled(False)
            self.show_error_box(self.__login_Dialog, "존재하지 않는 ID 입니다")

        else:
            print("not valid login")
            self.__login_Dialog.setEnabled(False)
            self.show_error_box(self.__login_Dialog, "틀린 패스워드입니다")

    def logout(self):
        print("logout")
        self.__login_account = None

    def change_member_info(self, pw1, pw2, anum, email, pnum):
        print("change member info")
        valid_result = self.isvalid_change(pw1, pw2, anum,email, pnum)
        if valid_result == 0:
            logged_in_member = self.__login_account
            logged_in_member.password = pw1
            logged_in_member.account_number = anum
            logged_in_member.email = email
            logged_in_member.phone_number = pnum

            member_table = table.Table("member_info")
            popped_member = member_table.pop_row((logged_in_member.id,))

            popped_member.password= pw1
            popped_member.account_number = anum
            popped_member.email = email
            popped_member.phone_number = pnum

            member_table.append(popped_member)
            member_table.save_file()

            return True
        elif valid_result == 1:
            print("not valid change")
            self.__login_Dialog.setEnabled(False)
            self.show_error_box(self.__member_info_Dialog, "빈 항목이 있습니다")

            return False
        else:
            self.__member_info_ui.modify_flag = True
            self.__login_Dialog.setEnabled(False)
            self.show_error_box(self.__member_info_Dialog, "패스워드가 일치하지 않습니다")
            return False

    def save_member_info(self):
        ...

    def return_dividend(self):
        ...

    def isvalid_login(self, id, pw):
        """
        :return: 0 => Success
                  1 => empty input
                  2 => id not exist
                  3 => id, password not agree
        """
        print("isvalid_login")
        member_table = table.Table("member_info")
        member_table.load_file()
        id_pw_list = member_table.select_row((id,), ('member_id', 'password'))

        if id == "" or pw == "":
            return 1
        if not id_pw_list:
            return 2
        elif (id_pw_list[0] != id) or (id_pw_list[1] != pw):
            return 3
        else:
            return 0

    def isvalid_signup(self, input_member_info):
        """
        :return: 0 => success
                  1 => empty input
                  2 => duplicate id
                  3 => password not agree
                  4 => duplicate ssn
        """
        print("isvalid_signup")

        id_ = input_member_info[0]
        pw = input_member_info[1]
        pw_repeat = input_member_info[2]
        ssn = input_member_info[4]

        member_table = table.Table("member_info")
        member_table.load_file()
        id_list = [x[0] for x in member_table.select_all_row(('member_id',))]
        ssn_list = [x[0] for x in member_table.select_all_row(('ssn',))]

        if "" in input_member_info:
            return 1
        elif id_ in id_list:
            return 2
        elif pw != pw_repeat:
            return 3
        elif ssn in ssn_list:
            return 4
        else:
            return 0

    def is_admin(self, id):
        if id == "admin":
            return True
        else:
            return False

    def isvalid_change(self, pw1, pw2, anum, email, pnum):
        """
                :return: 0 => success
                          1 => empty input
                          2 => password not agree
        """
        print("isvalid_signup")

        if "" in [pw1, pw2, anum, email, pnum]:
            return 1
        elif pw1 != pw2:
            return 2
        else:
            return 0

    def isvalid_pw(self):
        ...