# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_result_show.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from db import table

class Ui_Dialog(object):
    def __init__(self, game_manager, init_ui,current_idx):
        self.__gm = game_manager
        self.__init_ui = init_ui
        self.__dialog = None
        self.__current_idx = current_idx

    def setupUi(self, Dialog):
        self.__dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(380,400)
        Dialog.setFixedSize(380,400)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.resize(380,400)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)


        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        self.pushButton.clicked.connect(self.exit_btn_clicked)

        self.set_game_table()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

    def set_game_table(self):
        print("set game table")
        #game_table= table.Table("game_info")
        game = self.__gm.game_list[self.__current_idx]
        print(1)
        self.tableWidget.setRowCount(5)
        for row in range(5):
            item = QtWidgets.QTableWidgetItem(str(row + 1))
            self.tableWidget.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(game.horses[game.result[row]].name)
            self.tableWidget.setItem(row, 1, item)
            item = QtWidgets.QTableWidgetItem("{:.2f}".format(game.dividend_rate[game.result[row]]))
            self.tableWidget.setItem(row, 2, item)

        if len(game.horses) != 0:
            self.tableWidget.selectRow(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "순위"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "말"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "배당률"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Dialog", "확인"))
        Dialog.setWindowTitle(_translate("Dialog", "경기 결과 확인"))


    def exit_btn_clicked(self):
        print("종료버튼")
        self.__dialog.close()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

