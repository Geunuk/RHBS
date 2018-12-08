# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
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

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 370)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(400, 370))
        Dialog.setMaximumSize(QtCore.QSize(400, 370))
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
        self.pw_repeat_label = QtWidgets.QLabel(Dialog)
        self.pw_repeat_label.setObjectName("pw_repeat_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pw_repeat_label)
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.ssn_label = QtWidgets.QLabel(Dialog)
        self.ssn_label.setObjectName("ssn_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.ssn_label)
        self.account_number_label = QtWidgets.QLabel(Dialog)
        self.account_number_label.setObjectName("account_number_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.account_number_label)
        self.email_label = QtWidgets.QLabel(Dialog)
        self.email_label.setObjectName("email_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.email_label)
        self.phone_number_label = QtWidgets.QLabel(Dialog)
        self.phone_number_label.setObjectName("phone_number_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.phone_number_label)
        self.input_id = QtWidgets.QLineEdit(Dialog)
        self.input_id.setObjectName("input_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_id)
        self.input_pw = QtWidgets.QLineEdit(Dialog)
        self.input_pw.setObjectName("input_pw")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_pw)
        self.input_pw_repeat = QtWidgets.QLineEdit(Dialog)
        self.input_pw_repeat.setObjectName("input_pw_repeat")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_pw_repeat)
        self.input_name = QtWidgets.QLineEdit(Dialog)
        self.input_name.setObjectName("input_name")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.input_name)
        self.input_ssn = QtWidgets.QLineEdit(Dialog)
        self.input_ssn.setObjectName("input_ssn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.input_ssn)
        self.input_account_number = QtWidgets.QLineEdit(Dialog)
        self.input_account_number.setObjectName("input_account_number")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.input_account_number)
        self.input_email = QtWidgets.QLineEdit(Dialog)
        self.input_email.setObjectName("input_email")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.input_email)
        self.input_phone_number = QtWidgets.QLineEdit(Dialog)
        self.input_phone_number.setObjectName("input_phone_number")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.input_phone_number)
        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)
        self.signup_ok_btn = QtWidgets.QPushButton(Dialog)
        self.signup_ok_btn.setObjectName("signup_ok_btn")
        self.gridLayout.addWidget(self.signup_ok_btn, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.__dialog = Dialog
        self.signup_ok_btn.clicked.connect(self.signup_ok_btn_clicked_connect)

    def signup_ok_btn_clicked_connect(self):
        print("회원가입 확인 버튼 클릭")
        id = self.input_id.text()
        pw = self.input_pw.text()
        pw_repeat = self.input_pw_repeat.text()
        name = self.input_name.text()
        ssn = self.input_ssn.text()
        account_number = self.input_account_number.text()
        email = self.input_email.text()
        phone_number = self.input_phone_number.text()
        member_info = (id, pw, pw_repeat, name, ssn
                       ,account_number, email, phone_number)
        self.__am.signup(member_info)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "회원가입"))
        self.id_label.setText(_translate("Dialog", "ID"))
        self.pw_label.setText(_translate("Dialog", "패스워드"))
        self.pw_repeat_label.setText(_translate("Dialog", "패스워드 재입력"))
        self.name_label.setText(_translate("Dialog", "이름"))
        self.ssn_label.setText(_translate("Dialog", "주민번호"))
        self.account_number_label.setText(_translate("Dialog", "계좌번호"))
        self.email_label.setText(_translate("Dialog", "이메일"))
        self.phone_number_label.setText(_translate("Dialog", "전화번호"))
        self.signup_ok_btn.setText(_translate("Dialog", "회원 가입"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

