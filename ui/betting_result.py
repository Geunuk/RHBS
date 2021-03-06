# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'betting_result.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from db import table

class Ui_Dialog(object):
    def __init__(self, member, init_ui):
        self.__member = member
        self.__init_ui = init_ui
        self.__dialog = None
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
        Dialog.resize(700, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(700, 500))
        Dialog.setMaximumSize(QtCore.QSize(700, 500))
        Dialog.setToolTipDuration(0)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.betting_table = QtWidgets.QTableWidget(Dialog)
        self.betting_table.setObjectName("betting_table")
        self.betting_table.setColumnCount(7)
        self.betting_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.betting_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.betting_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.betting_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.betting_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.betting_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.betting_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.betting_table.setHorizontalHeaderItem(6, item)
        self.horizontalLayout.addWidget(self.betting_table)
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout.addWidget(self.ok_btn)
        self.set_betting_table()
        self.ok_btn.clicked.connect(self.ok_btn_clicked)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.betting_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

    def set_betting_table(self):
        count = 0
        for game in self.__game_manager.game_list:
            for bet_info in game.betting_info:
                if(self.__member.id == bet_info.member_id):
                    count +=1

        self.betting_table.setRowCount(count)
        i = 0
        for game in self.__game_manager.game_list:
            for bet_info in game.betting_info:
                if(self.__member.id == bet_info.member_id):
                    for r, horse in enumerate(game.horses):
                        if (bet_info.horse_name == horse.name):
                            idx = r

                    bet_money = int(bet_info.bet_money)
                    item = QtWidgets.QTableWidgetItem(bet_info.game_id)
                    self.betting_table.setItem(i, 0, item)
                    item = QtWidgets.QTableWidgetItem(bet_info.horse_name)
                    self.betting_table.setItem(i, 1, item)
                    re = None
                    if (game.proceeding == True):
                        msg = "경기 종료"
                        re = game.result.index(idx)
                        re += 1
                    else:
                        msg = "경기 전"
                    item = QtWidgets.QTableWidgetItem(msg)
                    self.betting_table.setItem(i, 2, item)
                    item = QtWidgets.QTableWidgetItem(str(re))
                    self.betting_table.setItem(i, 3, item)
                    item = QtWidgets.QTableWidgetItem("{:.2f}".format(game.dividend_rate[idx]))
                    self.betting_table.setItem(i, 4, item)
                    item = QtWidgets.QTableWidgetItem(bet_info.bet_money)
                    self.betting_table.setItem(i, 5, item)
                    item = QtWidgets.QTableWidgetItem(str(int(bet_money * game.dividend_rate[idx])))
                    self.betting_table.setItem(i, 6, item)
                    i += 1

            if i != 0:
                self.betting_table.selectRow(0)

    def ok_btn_clicked(self):
        print("확인 버튼 클릭")
        self.__dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "베팅 결과 확인"))
        item = self.betting_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "경기"))
        item = self.betting_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "말 이름"))
        item = self.betting_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "종료 여부"))
        item = self.betting_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "성적"))
        item = self.betting_table.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "배당률"))
        item = self.betting_table.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "베팅 금액"))
        item = self.betting_table.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "베당 금액"))
        self.ok_btn.setText(_translate("Dialog", "확인"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

