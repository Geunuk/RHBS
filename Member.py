from ui import point_charge, point_exchange, dialog, error
from db import table


class Member():
    def __init__(self, id, pw, name, ssn, anum,  email, pnum, point, init_ui, init_window):
        self.__id = id
        self.__password = pw
        self.__name = name
        self.__ssn = ssn
        self.__account_number = anum
        self.__email = email
        self.__phone_number = pnum
        self.__point = point

        self.__init_ui = init_ui
        self.__init_window = init_window
        self.__point_charge_Dialog = None
        self.__point_charge_ui = None
        self.__point_exchange_Dialog = None
        self.__point_exchange_ui = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, point):
        self.__point = point

    @property
    def ssn(self):
        return self.__ssn

    @ssn.setter
    def ssn(self, ssn):
        self.__id = ssn

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    def show_point_charge_box(self):
        print("show point charge box")
        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__point_charge_Dialog = dialog.Dialog_Modified(self.__init_window)
        self.__point_charge_ui = point_charge.Ui_Dialog(self, self.__init_ui)
        self.__point_charge_ui.setupUi(self.__point_charge_Dialog)
        self.__point_charge_Dialog.show()

    def show_point_exchange_box(self):
        print("show point exchange box")
        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__point_exchange_Dialog = dialog.Dialog_Modified(self.__init_window)
        self.__point_exchange_ui = point_exchange.Ui_Dialog(self, self.__init_ui)
        self.__point_exchange_ui.setupUi(self.__point_exchange_Dialog)
        self.__point_exchange_Dialog.show()

    def show_error_box(self, prev_dialog, msg):
        print("show error box")
        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__error_Dialog = dialog.Dialog_Modified(prev_dialog)
        self.__error_ui = error.Ui_Dialog(self, prev_dialog)
        self.__error_ui.setupUi(self.__error_Dialog)
        self.__error_ui.error_label.setText(msg)
        self.__error_Dialog.show()

    def charge_point(self, charged_point):
        print("charge point")
        if self.isvalid_point(charged_point,"charge"):
            self.__point = self.__point + int(charged_point)
            self.__point_charge_Dialog.close()

            member_table = table.Table("member_info")
            popped_member = member_table.pop_row((self.id,))

            popped_member.point = self.__point
            member_table.append(popped_member)
            member_table.save_file()

        else:
            print("charge point failed")
            self.__point_charge_Dialog.setEnabled(False)
            self.show_error_box(self.__point_charge_Dialog, "유효하지 않은 입력입니다")


    def exchange_point(self, exchanged_point):
        print("exchange point")
        if self.isvalid_point(exchanged_point, "exchange"):
            self.__point = self.__point - int(exchanged_point)
            self.__point_exchange_Dialog.close()

            member_table = table.Table("member_info")
            popped_member = member_table.pop_row((self.id,))

            popped_member.point = self.__point
            member_table.append(popped_member)
            member_table.save_file()

        else:
            print("exchange point failed")
            self.__point_exchange_Dialog.setEnabled(False)
            self.__ashow_error_box(self.__point_exchange_Dialog, "유효하지 않은 입력입니다")

    def isvalid_point(self, changed_point, mode):
         try:
             changed_point = int(changed_point)
             if mode == "exchange" and changed_point > self.__point:
                 return False

             if changed_point > 0:
                return True
             else:
                 return False

         except ValueError:
             return False