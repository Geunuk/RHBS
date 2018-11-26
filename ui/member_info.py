# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'member_info_change.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self, account_manager, init_ui):
        self.__am = account_manager
        self.__init_ui = init_ui
        self.__dialog = None
        self.__modify_flag = False

        self.pw_repeat_label = None
        self.input_pw_repeat = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(400, 400))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.id_label = QtWidgets.QLabel(Dialog)
        self.id_label.setObjectName("id_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.id_label)
        self.pw_label = QtWidgets.QLabel(Dialog)
        self.pw_label.setObjectName("pw_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pw_label)

        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.ssnlabel = QtWidgets.QLabel(Dialog)
        self.ssnlabel.setObjectName("ssnlabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ssnlabel)
        self.account_number_label = QtWidgets.QLabel(Dialog)
        self.account_number_label.setObjectName("account_number_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.account_number_label)
        self.email_label = QtWidgets.QLabel(Dialog)
        self.email_label.setObjectName("email_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.email_label)
        self.phone_number_label = QtWidgets.QLabel(Dialog)
        self.phone_number_label.setObjectName("phone_number_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.phone_number_label)
        self.input_id = QtWidgets.QLineEdit(Dialog)
        self.input_id.setEnabled(False)
        self.input_id.setObjectName("input_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_id)
        self.input_pw = QtWidgets.QLineEdit(Dialog)
        self.input_pw.setEnabled(False)
        self.input_pw.setObjectName("input_pw")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_pw)

        self.input_name = QtWidgets.QLineEdit(Dialog)
        self.input_name.setEnabled(False)
        self.input_name.setObjectName("input_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_name)
        self.input_ssn = QtWidgets.QLineEdit(Dialog)
        self.input_ssn.setEnabled(False)
        self.input_ssn.setObjectName("input_ssn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.input_ssn)
        self.input_account_number = QtWidgets.QLineEdit(Dialog)
        self.input_account_number.setEnabled(False)
        self.input_account_number.setObjectName("input_account_number")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.input_account_number)
        self.input_email = QtWidgets.QLineEdit(Dialog)
        self.input_email.setEnabled(False)
        self.input_email.setObjectName("input_email")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.input_email)
        self.input_phone_number = QtWidgets.QLineEdit(Dialog)
        self.input_phone_number.setEnabled(False)
        self.input_phone_number.setObjectName("input_phone_number")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.input_phone_number)
        self.point_label = QtWidgets.QLabel(Dialog)
        self.point_label.setObjectName("point_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.point_label)
        self.input_point = QtWidgets.QLineEdit(Dialog)
        self.input_point.setEnabled(False)
        self.input_point.setObjectName("input_point")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.input_point)
        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)
        self.member_info_ok_btn = QtWidgets.QPushButton(Dialog)
        self.member_info_ok_btn.setObjectName("member_info_ok_btn")
        self.gridLayout.addWidget(self.member_info_ok_btn, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.__dialog = Dialog
        self.member_info_ok_btn.clicked.connect(self.member_info_ok_btn_clicked_connect)
        self.input_set_text()

    def input_set_text(self):
        member = self.__am.login_account

        self.input_id.setText(member.id)
        self.input_pw.setText(member.password)
        self.input_name.setText(member.name)
        self.input_ssn.setText(member.ssn)
        self.input_account_number.setText(member.account_number)
        self.input_email.setText(member.email)
        self.input_phone_number.setText(member.phone_number)
        self.input_point.setText(str(member.point))

        if self.__modify_flag:
            self.input_pw_repeat.setText(member.password)

    def member_info_ok_btn_clicked_connect(self):
        if not self.__modify_flag:
            self.__modify_flag = True
            self.__dialog.setWindowTitle("개인정보수정")

            self.pw_repeat_label = QtWidgets.QLabel(self.__dialog)
            self.pw_repeat_label.setObjectName("pw_repeat_label")
            self.pw_repeat_label.setText("패스워드 재입력")

            self.input_pw_repeat = QtWidgets.QLineEdit(self.__dialog)
            self.input_pw_repeat.setEnabled(True)
            self.input_pw_repeat.setObjectName("input_pw_repeat")
            self.input_pw_repeat.setText(self.__am.login_account.password)

            self.input_pw.setEnabled(True)
            self.input_account_number.setEnabled(True)
            self.input_email.setEnabled(True)
            self.input_phone_number.setEnabled(True)

            self.member_info_ok_btn.setText("확인")
            self.formLayout.insertRow(2, self.pw_repeat_label, self.input_pw_repeat)

        else:
            self.__modify_flag = False

            pw1 = self.input_pw.text()
            pw2 = self.input_pw_repeat.text()
            anum = self.input_account_number.text()
            email = self.input_email.text()
            pnum = self.input_phone_number.text()
            self.__am.change_member_info(pw1, pw2, anum, email, pnum)

            self.formLayout.removeRow(2)
            self.__dialog.setWindowTitle("회원정보확인")
            self.member_info_ok_btn.setText("수정")

            self.input_pw.setEnabled(False)
            self.input_account_number.setEnabled(False)
            self.input_email.setEnabled(False)
            self.input_phone_number.setEnabled(False)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "회원정보확인"))
        self.id_label.setText(_translate("Dialog", "ID"))
        self.pw_label.setText(_translate("Dialog", "패스워드"))

        self.name_label.setText(_translate("Dialog", "이름"))
        self.ssnlabel.setText(_translate("Dialog", "주민번호"))
        self.account_number_label.setText(_translate("Dialog", "계좌번호"))
        self.email_label.setText(_translate("Dialog", "이메일"))
        self.phone_number_label.setText(_translate("Dialog", "전화번호"))
        self.point_label.setText(_translate("Dialog", "포인트"))
        self.member_info_ok_btn.setText(_translate("Dialog", "수정"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

