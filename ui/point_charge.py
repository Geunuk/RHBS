# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'point_charge.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self, member, init_ui):
        self.__member = member
        self.__init_ui = init_ui
        self.__dialog = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(450, 150))
        Dialog.setMaximumSize(QtCore.QSize(450, 150))
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(7, 10, 431, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.before = QtWidgets.QLabel(self.layoutWidget)
        self.before.setObjectName("before")
        self.horizontalLayout.addWidget(self.before)
        self.point_before = QtWidgets.QLabel(self.layoutWidget)
        self.point_before.setText("")
        self.point_before.setObjectName("point_before")
        self.horizontalLayout.addWidget(self.point_before)
        self.after = QtWidgets.QLabel(self.layoutWidget)
        self.after.setObjectName("after")
        self.horizontalLayout.addWidget(self.after)
        self.point_after = QtWidgets.QLabel(self.layoutWidget)
        self.point_after.setText("")
        self.point_after.setObjectName("point_after")
        self.horizontalLayout.addWidget(self.point_after)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.charge = QtWidgets.QLabel(self.layoutWidget)
        self.charge.setObjectName("charge")
        self.horizontalLayout_2.addWidget(self.charge)
        self.input_point = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_point.setObjectName("input_point")
        self.horizontalLayout_2.addWidget(self.input_point)
        self.point_charge_ok_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.point_charge_ok_btn.setObjectName("point_charge_ok_btn")
        self.horizontalLayout_2.addWidget(self.point_charge_ok_btn)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.point_before.setText(str(self.__member.point))
        self.point_after.setText(str(self.__member.point))
        self.input_point.textChanged.connect(self.point_changed)
        self.point_charge_ok_btn.clicked.connect(self.point_charge_ok_btn_clicked_connect)

    def point_changed(self):
        if self.input_point.text() == "":
            self.point_after.setText(str(self.__member.point))
        else:
            try:
                self.point_after.setText(str(self.__member.point\
                                           + int(self.input_point.text())))
            except ValueError:
                self.point_after.setText("????")

    def point_charge_ok_btn_clicked_connect(self):
        print("확인 버튼 클릭")
        charged_point = self.input_point.text()
        self.__member.charge_point(charged_point)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "포인트 충전"))
        self.before.setText(_translate("Dialog", "현재 포인트"))
        self.after.setText(_translate("Dialog", "충전 후 포인트"))
        self.charge.setText(_translate("Dialog", "충전할 포인트"))
        self.point_charge_ok_btn.setText(_translate("Dialog", "확인"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

