# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bet_select_horse.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

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

