# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'betting_result.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
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
        Dialog.setToolTipDuration(0)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_btn = QtWidgets.QTableWidget(Dialog)
        self.ok_btn.setObjectName("ok_btn")
        self.ok_btn.setColumnCount(7)
        self.ok_btn.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ok_btn.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ok_btn.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ok_btn.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ok_btn.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ok_btn.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ok_btn.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.ok_btn.setHorizontalHeaderItem(6, item)
        self.horizontalLayout.addWidget(self.ok_btn)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "베팅 결과 확인"))
        item = self.ok_btn.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "경기"))
        item = self.ok_btn.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "말 이름"))
        item = self.ok_btn.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "종료 여부"))
        item = self.ok_btn.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "성적"))
        item = self.ok_btn.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "배당률"))
        item = self.ok_btn.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "베팅 금액"))
        item = self.ok_btn.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "베당 금액"))
        self.pushButton.setText(_translate("Dialog", "확인"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

