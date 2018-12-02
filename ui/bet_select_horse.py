# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bet_select_horse.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from db import table

class Ui_Dialog(object):
    def __init__(self, member, init_ui,choice_idx):
        self.__member = member
        self.__init_ui = init_ui
        self.__dialog = None
        self.__idx = choice_idx
        self.__game_table = None
        self.__game = None

    def setupUi(self, Dialog):
        self.__dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(400, 250))
        Dialog.setMaximumSize(QtCore.QSize(400, 250))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horse_table = QtWidgets.QTableWidget(Dialog)
        self.horse_table.setEnabled(True)
        self.horse_table.setMinimumSize(QtCore.QSize(0, 0))
        self.horse_table.setObjectName("horse_table")
        self.horse_table.setColumnCount(3)
        self.horse_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.horse_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.horse_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.horse_table.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.horse_table, 0, 0, 1, 2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, -1, 0, -1)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.input_point = QtWidgets.QLineEdit(Dialog)
        self.input_point.setObjectName("input_point")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_point)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.input_pw = QtWidgets.QLineEdit(Dialog)
        self.input_pw.setObjectName("input_pw")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_pw)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.betting_btn = QtWidgets.QPushButton(Dialog)
        self.betting_btn.setObjectName("betting_btn")
        self.gridLayout.addWidget(self.betting_btn, 1, 1, 1, 1)
        self.horse_table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.horse_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        self.set_horse_table()
        self.betting_btn.clicked.connect(self.betting_btn_clicked)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def set_horse_table(self):
        print("set horse table")
        self.__game_table = table.Table("game_info")
        self.__game = self.__game_table[self.__idx]
        #print(self.__idx)
        self.horse_table.setRowCount(5)
        for row in range(5):
            item = QtWidgets.QTableWidgetItem(self.__game.horses[row].name)
            self.horse_table.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(self.__game.horses[row].feature)
            self.horse_table.setItem(row, 1, item)
            item = QtWidgets.QTableWidgetItem(str(self.__game.dividend_rate[row]))
            self.horse_table.setItem(row, 2, item)

    def betting_btn_clicked(self):
        print("betting btn clicked")
        choice_idx = self.horse_table.currentRow()
        bet_point = self.input_point.text()
        pw = self.input_pw.text()
        horse_name = self.__game.horses[choice_idx].name
        game_id = self.__game.game_id

        self.__member.bet(bet_point,pw,game_id,horse_name,self.__dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "베팅"))
        item = self.horse_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "말이름"))
        item = self.horse_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "소개"))
        item = self.horse_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "배당률"))
        self.label.setText(_translate("Dialog", "베팅 금액"))
        self.label_2.setText(_translate("Dialog", "패스워드 재입력"))
        self.betting_btn.setText(_translate("Dialog", "베팅"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

