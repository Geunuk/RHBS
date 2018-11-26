# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'init.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self, account_manager=None, game_manager=None):
        self.__am = account_manager
        self.__gm = game_manager
        self.__main_window = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.init_login_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.init_login_btn.sizePolicy().hasHeightForWidth())
        self.init_login_btn.setSizePolicy(sizePolicy)
        self.init_login_btn.setObjectName("init_login_btn")
        self.horizontalLayout_2.addWidget(self.init_login_btn)
        self.init_signup_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.init_signup_btn.sizePolicy().hasHeightForWidth())
        self.init_signup_btn.setSizePolicy(sizePolicy)
        self.init_signup_btn.setObjectName("init_signup_btn")
        self.horizontalLayout_2.addWidget(self.init_signup_btn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.login_msg = QtWidgets.QLabel(self.centralwidget)
        self.login_msg.setText("")
        self.login_msg.setObjectName("login_msg")
        self.gridLayout.addWidget(self.login_msg, 0, 1, 2, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.init_bet_btn = QtWidgets.QPushButton(self.centralwidget)
        self.init_bet_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.init_bet_btn.sizePolicy().hasHeightForWidth())
        self.init_bet_btn.setSizePolicy(sizePolicy)
        self.init_bet_btn.setObjectName("init_bet_btn")
        self.verticalLayout_2.addWidget(self.init_bet_btn)
        self.init_bet_result_btn = QtWidgets.QPushButton(self.centralwidget)
        self.init_bet_result_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.init_bet_result_btn.sizePolicy().hasHeightForWidth())
        self.init_bet_result_btn.setSizePolicy(sizePolicy)
        self.init_bet_result_btn.setObjectName("init_bet_result_btn")
        self.verticalLayout_2.addWidget(self.init_bet_result_btn)
        self.init_game_status_btn = QtWidgets.QPushButton(self.centralwidget)
        self.init_game_status_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.init_game_status_btn.sizePolicy().hasHeightForWidth())
        self.init_game_status_btn.setSizePolicy(sizePolicy)
        self.init_game_status_btn.setObjectName("init_game_status_btn")
        self.verticalLayout_2.addWidget(self.init_game_status_btn)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.init_charge_point_btn = QtWidgets.QPushButton(self.centralwidget)
        self.init_charge_point_btn.setEnabled(False)
        self.init_charge_point_btn.setObjectName("init_charge_point_btn")
        self.verticalLayout_5.addWidget(self.init_charge_point_btn)
        self.init_exchange_point_btn = QtWidgets.QPushButton(self.centralwidget)
        self.init_exchange_point_btn.setEnabled(False)
        self.init_exchange_point_btn.setObjectName("init_exchange_point_btn")
        self.verticalLayout_5.addWidget(self.init_exchange_point_btn)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.init_game_manage_btn = QtWidgets.QPushButton(self.centralwidget)
        self.init_game_manage_btn.setEnabled(False)
        self.init_game_manage_btn.setObjectName("init_game_manage_btn")
        self.verticalLayout.addWidget(self.init_game_manage_btn)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 2, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.__main_window = MainWindow
        self.init_login_btn.clicked.connect(
            self.init_login_btn_clicked)
        self.init_signup_btn.clicked.connect(
            self.init_signup_btn_clicked)
        self.init_bet_btn.clicked.connect(self.init_bet_btn_clicked)
        self.init_bet_result_btn.clicked.connect(
            self.init_bet_result_btn_clicked)
        self.init_game_status_btn.clicked.connect(
            self.init_game_manage_btn_clicked)
        self.init_charge_point_btn.clicked.connect(
            self.init_charge_point_btn_clicked)
        self.init_exchange_point_btn.clicked.connect(
            self.init_exchange_point_btn_clicked)
        self.init_game_manage_btn.clicked.connect(
            self.init_game_manage_btn_clicked)

    @property
    def main_window(self):
        return self.__main_window

    def init_login_btn_clicked(self):
        if self.__am.login_account:
            self.init_login_btn.setText("로그인")
            self.init_signup_btn.setText("회원가입")

            self.init_signup_btn.setEnabled(True)
            self.init_bet_btn.setEnabled(False)
            self.init_bet_result_btn.setEnabled(False)
            self.init_game_status_btn.setEnabled(False)
            self.init_charge_point_btn.setEnabled(False)
            self.init_exchange_point_btn.setEnabled(False)
            self.init_game_manage_btn.setEnabled(False)

            self.__am.logout()
        else :
            self.__am.show_login_box()

    def init_signup_btn_clicked(self):
        if self.__am.login_account :
            self.__am.show_member_info_box()
        else:
            self.__am.show_signup_box()

    def init_bet_btn_clicked(self):
        logged_in_member = self.__am.login_account
        logged_in_member.bet()

    def init_bet_result_btn_clicked(self):
        self.__gm.show_bet_result()

    def init_game_status_btn_clicked(self):
        self.__gm.show_game_status()

    def init_charge_point_btn_clicked(self):
        print("init charge point btn clicked")
        logged_in_member = self.__am.login_account
        logged_in_member.show_point_charge_box()

    def init_exchange_point_btn_clicked(self):
        print("init exchange point btn clicked")
        logged_in_member = self.__am.login_account
        logged_in_member.show_point_exchange_box()

    def init_game_manage_btn_clicked(self):
        logged_in_admin = self.__am.login_account
        logged_in_admin.show_game()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Race Horse Betting System"))
        self.init_login_btn.setText(_translate("MainWindow", "로그인"))
        self.init_signup_btn.setText(_translate("MainWindow", "회원 가입"))
        self.init_bet_btn.setText(_translate("MainWindow", "베팅"))
        self.init_bet_result_btn.setText(_translate("MainWindow", "베팅 결과 확인"))
        self.init_game_status_btn.setText(_translate("MainWindow", "경기 상황 확인"))
        self.init_charge_point_btn.setText(_translate("MainWindow", "포인트 충전"))
        self.init_exchange_point_btn.setText(_translate("MainWindow", "포인트 환전"))
        self.init_game_manage_btn.setText(_translate("MainWindow", "경기 관리"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

