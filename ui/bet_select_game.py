# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bet_select_game.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from db import table
from ui import dialog,bet_select_horse,error

class Ui_Dialog(object):
    def __init__(self, member, init_ui,init_window):
        self.__member = member
        self.__init_ui = init_ui
        self.__init_window = init_window
        self.__dialog = None
        self.__game_table = None
        self.__game_manager = None

    @property
    def game_manager(self):
        return self.__game_manager

    @game_manager.setter
    def game_manager(self, game_manager):
        self.__game_manager = game_manager

    def setupUi(self, Dialog):
        self.__dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 250)
        Dialog.setMinimumSize(QtCore.QSize(500, 500))
        Dialog.setMaximumSize(QtCore.QSize(500, 500))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.game_table = QtWidgets.QTableWidget(Dialog)
        self.game_table.setObjectName("game_table")
        self.game_table.setColumnCount(2)
        self.game_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.game_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.game_table.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.game_table, 0, 0, 1, 1)
        self.choice_game_btn = QtWidgets.QPushButton(Dialog)
        self.choice_game_btn.setObjectName("choice_game_btn")
        self.gridLayout.addWidget(self.choice_game_btn, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.game_table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.game_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        self.set_game_table()
        self.choice_game_btn.clicked.connect(self.choice_game_btn_clicked_connect)
        self.game_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.game_table.horizontalHeader().setStretchLastSection(True)

    def choice_game_btn_clicked_connect(self):
        print("경기 선택")
        self.__dialog.setEnabled(False)
        choice_idx = self.game_table.currentRow()
        if(self.__game_manager.game_list[choice_idx].proceeding == False):
            self.__bet_select_horse_Dialog = dialog.Dialog_Modified(self.__dialog)
            self.__bet_select_horse_ui = bet_select_horse.Ui_Dialog(self.__member, self.__init_ui,choice_idx)
            self.__bet_select_horse_ui.game_manager = self.__game_manager
            self.__bet_select_horse_ui.setupUi(self.__bet_select_horse_Dialog)
            self.__bet_select_horse_Dialog.show()
        else :
            self.__error_Dialog = dialog.Dialog_Modified(self.__dialog)
            self.__error_ui = error.Ui_Dialog(self, self.__dialog)
            self.__error_ui.setupUi(self.__error_Dialog)
            self.__error_ui.error_label.setText("종료된 경기입니다.")
            self.__error_Dialog.show()

    def set_game_table(self):
        self.game_table.setRowCount(len(self.__game_manager.game_list))
        for row, game in enumerate(self.__game_manager.game_list):
            item = QtWidgets.QTableWidgetItem(str(game.id))
            self.game_table.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(game.start_time.strftime("%Y-%m-%d %H:%M:%S"))
            self.game_table.setItem(row, 1, item)

        if len(self.__game_manager.game_list) != 0:
            self.game_table.selectRow(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "게임 선택"))
        item = self.game_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "경기"))
        item = self.game_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "시작 시간"))
        self.choice_game_btn.setText(_translate("Dialog", "경기 선택"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

