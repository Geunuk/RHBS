import Member
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

    def show_member_info_box(self):
        print("show member info box")
        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__member_info_Dialog = dialog.Dialog_Modified(self.__init_window)
        self.__member_info_ui = mem_info.Ui_Dialog(self, self.__init_ui)
        self.__member_info_ui.setupUi(self.__member_info_Dialog)
        self.__member_info_Dialog.show()

    def show_login_box(self):
        print("show login box")
        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__login_Dialog = dialog.Dialog_Modified(self.__init_window)
        self.__login_ui = login.Ui_Dialog(self, self.__init_ui)
        self.__login_ui.setupUi(self.__login_Dialog)
        self.__login_Dialog.show()

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
        id_ = input_member_info[0]
        pw = input_member_info[1]
        pw_repeat = input_member_info[2]
        ssn = input_member_info[4]

        if self.isvalid_signup(id_, pw, pw_repeat, ssn):
            print("valid signup")
            self.__signup_Dialog.close()
            member_table = table.Table("member_info")
            member = member_info.Member_Info(input_member_info[0], input_member_info[1]
                                             ,input_member_info[3], input_member_info[4]
                                             ,input_member_info[5], input_member_info[6]
                                             ,input_member_info[7])

            member_table.append(member)
            member_table.save_file()

        else:
            print("not valid signup")
            self.__signup_Dialog.setEnabled(False)
            self.show_error_box(self.__signup_Dialog, "유효하지 않은 입력입니다")

    def login(self, id, pw):
        if  self.isvalid_login(id, pw):
            self.__login_Dialog.close()

            self.__init_ui.init_login_btn.setText("로그아웃")
            self.__init_ui.init_signup_btn.setText("회원정보확인")

            if self.is_admin(id):
                self.__init_ui.init_game_manage_btn.setEnabled(True)
            else:
                self.__init_ui.init_bet_btn.setEnabled(True)
                self.__init_ui.init_bet_result_btn.setEnabled(True)
                self.__init_ui.init_game_status_btn.setEnabled(True)
                self.__init_ui.init_charge_point_btn.setEnabled(True)
                self.__init_ui.init_exchange_point_btn.setEnabled(True)

            member_table = table.Table("member_info")
            member_info = member_table.select_row((id,), ('member_id', 'password'
                                                           ,'name', 'ssn', 'account_number'
                                                           ,'email', 'phone_number', 'point'))

            self.__login_account = Member.Member(member_info[0], member_info[1]
                                                 ,member_info[2], member_info[3]
                                                 ,member_info[4], member_info[5]
                                                 ,member_info[6], int(member_info[7])
                                                 ,self.__init_ui, self.__init_window)

        else:
            print("not valid login")
            self.__login_Dialog.setEnabled(False)
            self.show_error_box(self.__login_Dialog, "유효하지 않은 입력입니다")

    def logout(self):
        print("logout")
        self.__login_account = None

    def change_member_info(self, pw1, pw2, anum, email, pnum):
        print("change member info")
        if self.isvalid_change(pw1, pw2, anum,email, pnum):
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
        else:
            print("not valid change")
            self.__login_Dialog.setEnabled(False)
            self.show_error_box(self.__login_Dialog, "유효하지 않은 입력입니다")

    def show_member_info(self):
        ...

    def save_member_info(self):
        ...

    def return_dividend(self):
        ...

    def isvalid_login(self, id, pw):
        print("isvalid_login")
        member_table = table.Table("member_info")
        member_table.load_file()
        result = member_table.select_row((id,), ('member_id', 'password'))

        if result:
            if result[0] == id and result[1] == pw:
                return True
            else:
                return False
        else:
            return False

    def isvalid_signup(self, id, pw1, pw2, ssn):
        return True

    def is_admin(self, id):
        if id == "admin":
            return True
        else:
            return False

    def isvalid_change(self, pw1, pw2, anum, email, pnum):
        return True

    def isvalid_pw(self):
        ...