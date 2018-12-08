# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self, account_manager, init_ui):
        self.__am = account_manager
        self.__init_ui = init_ui
        self.__dialog = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(400, 150))
        Dialog.setMaximumSize(QtCore.QSize(400, 150))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.error_label = QtWidgets.QLabel(Dialog)
        self.error_label.setText("")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.gridLayout.addWidget(self.error_label, 0, 0, 1, 1)
        self.error_ok_btn = QtWidgets.QPushButton(Dialog)
        self.error_ok_btn.setObjectName("error_ok_btn")
        self.gridLayout.addWidget(self.error_ok_btn, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.__dialog = Dialog
        self.error_ok_btn.clicked.connect(self.error_ok_btn_clicked_connect)

    def error_ok_btn_clicked_connect(self):
        print("확인 버튼 클릭")
        self.__dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Error"))
        self.error_ok_btn.setText(_translate("Dialog", "확인"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

