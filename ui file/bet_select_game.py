# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bet_select_game.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 250)
        Dialog.setMinimumSize(QtCore.QSize(300, 250))
        Dialog.setMaximumSize(QtCore.QSize(300, 250))
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

