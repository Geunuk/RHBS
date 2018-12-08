# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage_game_add.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from db import table, horse_info

class Ui_Dialog(object):
    def __init__(self, admin, init_ui):
        self.__admin = admin
        self.__init_ui = init_ui
        self.__dialog = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.input_horse3_2 = QtWidgets.QLabel(Dialog)
        self.input_horse3_2.setObjectName("input_horse3_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.input_horse3_2)
        self.input_game_name = QtWidgets.QLineEdit(Dialog)
        self.input_game_name.setObjectName("input_game_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_game_name)
        self.start_time_label = QtWidgets.QLabel(Dialog)
        self.start_time_label.setObjectName("start_time_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.start_time_label)
        self.horse1_label = QtWidgets.QLabel(Dialog)
        self.horse1_label.setObjectName("horse1_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.horse1_label)
        self.input_horse1 = QtWidgets.QComboBox(Dialog)
        self.input_horse1.setObjectName("input_horse1")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.input_horse1)
        self.horse2_label = QtWidgets.QLabel(Dialog)
        self.horse2_label.setObjectName("horse2_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.horse2_label)
        self.horse3_label = QtWidgets.QLabel(Dialog)
        self.horse3_label.setObjectName("horse3_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.horse3_label)
        self.horse4_label = QtWidgets.QLabel(Dialog)
        self.horse4_label.setObjectName("horse4_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.horse4_label)
        self.horse5_label = QtWidgets.QLabel(Dialog)
        self.horse5_label.setObjectName("horse5_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.horse5_label)
        self.input_horse2 = QtWidgets.QComboBox(Dialog)
        self.input_horse2.setObjectName("input_horse2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.input_horse2)
        self.input_horse5 = QtWidgets.QComboBox(Dialog)
        self.input_horse5.setObjectName("input_horse5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.input_horse5)
        self.input_horse3 = QtWidgets.QComboBox(Dialog)
        self.input_horse3.setObjectName("input_horse3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.input_horse3)
        self.input_horse4 = QtWidgets.QComboBox(Dialog)
        self.input_horse4.setObjectName("input_horse4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.input_horse4)

        now = datetime.datetime.now()
        hour, min, sec = now.hour, now.minute, now.second
        self.input_start_time = QtWidgets.QDateTimeEdit(QtCore.QTime(hour, min, sec),Dialog)
        self.input_start_time.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))

        self.input_start_time.setObjectName("input_start_time")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_start_time)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.add_game_ok_btn = QtWidgets.QPushButton(Dialog)
        self.add_game_ok_btn.setObjectName("add_game_ok_btn")
        self.gridLayout.addWidget(self.add_game_ok_btn, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.add_game_ok_btn.clicked.connect(self.add_game_ok_btn_clicked_connect)
        self.set_input_horse_combo_box()

    def set_input_horse_combo_box(self):
        combos = [self.input_horse1, self.input_horse2, self.input_horse3
                 ,self.input_horse4, self.input_horse5]
        horse_table= table.Table("horse_info")
        horses = [ls[0] for ls in horse_table.select_all_row(("name",))]
        for combo in combos:
            combo.addItems(horses)

    def add_game_ok_btn_clicked_connect(self):
        print("확인 버튼 클릭")
        game_id = self.input_game_name.text()
        start_time = self.input_start_time.text()

        horse1_name = self.input_horse1.currentText()
        horse2_name = self.input_horse2.currentText()
        horse3_name = self.input_horse3.currentText()
        horse4_name = self.input_horse4.currentText()
        horse5_name = self.input_horse5.currentText()
        horses = [horse1_name, horse2_name, horse3_name, horse4_name
                  ,horse5_name]
        self.__admin.register_game(game_id, start_time, horses)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "경기 추가"))
        self.input_horse3_2.setText(_translate("Dialog", " 경기 이름"))
        self.start_time_label.setText(_translate("Dialog", "시작시간"))
        self.horse1_label.setText(_translate("Dialog", "말1"))
        self.horse2_label.setText(_translate("Dialog", "말2"))
        self.horse3_label.setText(_translate("Dialog", "말3"))
        self.horse4_label.setText(_translate("Dialog", "말4"))
        self.horse5_label.setText(_translate("Dialog", "말5"))
        self.add_game_ok_btn.setText(_translate("Dialog", "추가"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

