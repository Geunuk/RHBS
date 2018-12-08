# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_status_show.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from db import table, game_info
from ui import game_result_show, dialog, error

class Ui_Dialog(object):
    def __init__(self, game_manager, init_ui, init_window):
        self.__gm = game_manager
        self.__init_ui = init_ui
        self.__dialog = None
        self.__init_window = init_window
        self.__game_result_show_Dialog = None
        self.__game_table = None
        self.__error_Dialog = None
        self.__error_ui = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(700, 500))
        Dialog.setMaximumSize(QtCore.QSize(700, 500))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("결과확인")

        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.__dialog = Dialog
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.pushButton.clicked.connect(self.exit_btn_clicked)
        self.pushButton_2.clicked.connect(self.game_result_btn_clicked)
        self.set_game_table()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

    def exit_btn_clicked(self):
        self.__dialog.close()

    def show_error_box(self, prev_dialog, msg):
        print("에러 박스 표시")
        main_window = self.__init_ui.main_window
        main_window.setEnabled(False)

        self.__error_Dialog = dialog.Dialog_Modified(prev_dialog)
        self.__error_ui = error.Ui_Dialog(self, prev_dialog)
        self.__error_ui.setupUi(self.__error_Dialog)
        self.__error_ui.error_label.setText(msg)
        self.__error_Dialog.show()

    def game_result_btn_clicked(self):
        print("경기 결과 버튼 클릭")
        current_idx = self.tableWidget.currentRow()
        self.__dialog.setEnabled(False)

        if self.__gm.game_list[current_idx].proceeding == True:
            self.__game_result_show_Dialog = dialog.Dialog_Modified(self.__dialog)
            self.__game_result_show_ui = game_result_show.Ui_Dialog(self.__gm, self.__init_ui, current_idx)

            self.__game_result_show_ui.setupUi(self.__game_result_show_Dialog)
            self.__game_result_show_Dialog.show()
        else:
            self.__dialog.setEnabled(False)
            self.show_error_box(self.__dialog, "경기 종료 전입니다.")

    def set_game_table(self):
        self.tableWidget.setRowCount(len(self.__gm.game_list))

        for row, game in enumerate(self.__gm.game_list):
            item = QtWidgets.QTableWidgetItem(str(game.id))
            self.tableWidget.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(game.start_time.strftime("%Y-%m-%d %H:%M:%S"))
            self.tableWidget.setItem(row, 1, item)
            if (game.proceeding == True):
                msg = "경기 종료"
            else:
                msg = "경기 시작전"
            item = QtWidgets.QTableWidgetItem(msg)
            self.tableWidget.setItem(row, 2, item)

        if len(self.__gm.game_list) != 0:
            self.tableWidget.selectRow(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "경기 상황 확인"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "경기"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "시작 시작"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "종료 여부"))
        self.pushButton_2.setText(_translate("Dialog", "결과 확인"))
        self.pushButton.setText(_translate("Dialog", "종료"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

