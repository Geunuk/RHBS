# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage_game.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from db import table

class Ui_Dialog(object):
    def __init__(self, admin, init_ui):
        self.__admin = admin
        self.__init_ui = init_ui
        self.__dialog = None
        self.__gm = None

    @property
    def game_manager(self):
        return self.__gm

    @game_manager.setter
    def game_manager(self, game_manager):
        self.__gm = game_manager

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(1000, 400))
        Dialog.setMaximumSize(QtCore.QSize(1000, 400))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.present_game_table = QtWidgets.QTableWidget(Dialog)
        self.present_game_table.setObjectName("present_game_table")
        self.present_game_table.setColumnCount(7)
        self.present_game_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.present_game_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.present_game_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.present_game_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.present_game_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.present_game_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.present_game_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.present_game_table.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.present_game_table, 0, 0, 2, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.game_add_btn = QtWidgets.QPushButton(Dialog)
        self.game_add_btn.setObjectName("game_add_btn")
        self.verticalLayout.addWidget(self.game_add_btn)
        self.game_delete_btn = QtWidgets.QPushButton(Dialog)
        self.game_delete_btn.setObjectName("game_delete_btn")
        self.verticalLayout.addWidget(self.game_delete_btn)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.present_game_table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.present_game_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.__dialog = Dialog
        self.game_add_btn.clicked.connect(self.game_add_btn_clicked_connect)
        self.game_delete_btn.clicked.connect(self.game_delete_btn_clicked_connect)
        self.set_game_table()
        self.present_game_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

    def set_game_table(self):
        print("set game table")
        #game_table= table.Table("game_info")
        game_table = self.__gm.game_list
        self.present_game_table.setRowCount(len(game_table))
        for row, game in enumerate(game_table):
            item = QtWidgets.QTableWidgetItem(str(game.id))
            self.present_game_table.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(game.start_time.strftime("%Y-%m-%d %H:%M:%S"))
            self.present_game_table.setItem(row, 1, item)
            item = QtWidgets.QTableWidgetItem(game.horses[0].name)
            self.present_game_table.setItem(row, 2, item)
            item = QtWidgets.QTableWidgetItem(game.horses[1].name)
            self.present_game_table.setItem(row, 3, item)
            item = QtWidgets.QTableWidgetItem(game.horses[2].name)
            self.present_game_table.setItem(row, 4, item)
            item = QtWidgets.QTableWidgetItem(game.horses[3].name)
            self.present_game_table.setItem(row, 5, item)
            item = QtWidgets.QTableWidgetItem(game.horses[4].name)
            self.present_game_table.setItem(row, 6, item)

        if len(game_table) != 0:
            self.present_game_table.selectRow(0)

    def game_add_btn_clicked_connect(self):
        print("game add btn clicked connect")
        self.__admin.show_game_add_box()

    def game_delete_btn_clicked_connect(self):
        print("game delete btn clicked connect")
        delete_idx = self.present_game_table.currentRow()
        self.__admin.delete_game(delete_idx)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "경기 관리"))
        item = self.present_game_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "경기"))
        item = self.present_game_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "시작 시간"))
        item = self.present_game_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "말1"))
        item = self.present_game_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "말2"))
        item = self.present_game_table.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "말3"))
        item = self.present_game_table.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "말4"))
        item = self.present_game_table.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "말5"))
        self.game_add_btn.setText(_translate("Dialog", "추가"))
        self.game_delete_btn.setText(_translate("Dialog", "삭제"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

