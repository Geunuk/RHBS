# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bet_select_game.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from db import table
from ui import dialog,bet_select_horse


class Ui_Dialog(object):
    def __init__(self, member, init_ui,init_window):
        self.__member = member
        self.__init_ui = init_ui
        self.__init_window = init_window
        self.__dialog = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(500, 400))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        #self.tableWidget.setGeometry(QtCore.QRect(10, 10, 171, 91))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        '''self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()'''
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()

        '''self.tableWidget.setItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, item)
        item = QtWidgets.QTableWidgetItem()'''


        self.gridLayout.addWidget(self.tableWidget, 0, 0, 2, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.choice_game_btn = QtWidgets.QPushButton(Dialog)
        self.choice_game_btn.setObjectName("choice game")
        self.verticalLayout.addWidget(self.choice_game_btn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        self.set_game_table()
        self.choice_game_btn.clicked.connect(self.choice_game_btn_clicked_connect)

    def choice_game_btn_clicked_connect(self):
        print("game choice")
        choice_idx = self.tableWidget.currentRow()
        print("show betting horse box")

        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__bet_select_horse_Dialog = dialog.Dialog_Modified(self.__init_window)
        self.__bet_select_horse_ui = bet_select_horse.Ui_Dialog(self.__member, self.__init_ui,choice_idx)
        self.__bet_select_horse_ui.setupUi(self.__bet_select_horse_Dialog)
        self.__bet_select_horse_Dialog.show()

    def set_game_table(self):
        print("set game table")
        game_table = table.Table("game_info")
        self.tableWidget.setRowCount(len(game_table))
        for row, game in enumerate(game_table):
            item = QtWidgets.QTableWidgetItem(str(game.game_id))
            self.tableWidget.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(game.start_time.strftime("%Y-%m-%d %H:%M:%S"))
            self.tableWidget.setItem(row, 1, item)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "게임 리스트"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "경기"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "시작 시간"))
        self.choice_game_btn.setText(_translate("Dialog", "선택"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

