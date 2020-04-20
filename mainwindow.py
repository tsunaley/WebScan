# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scan.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 446)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.urlEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.urlEdit.setGeometry(QtCore.QRect(190, 90, 381, 31))
        self.urlEdit.setObjectName("urlEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 90, 81, 31))
        self.label.setLineWidth(2)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 360, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.login = QtWidgets.QRadioButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(190, 130, 161, 31))
        self.login.setObjectName("login")
        self.login.setChecked(True)
        self.loginUrl = QtWidgets.QLineEdit(self.centralwidget)
        self.loginUrl.setGeometry(QtCore.QRect(190, 169, 381, 31))
        self.loginUrl.setObjectName("loginUrl")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 170, 71, 31))
        self.label_2.setObjectName("label_2")
        # self.label_2.hide()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 240, 41, 31))
        self.label_3.setObjectName("label_3")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(190, 239, 381, 31))
        self.username.setObjectName("username")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 310, 41, 31))
        self.label_4.setObjectName("label_4")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(190, 309, 381, 31))
        self.password.setObjectName("password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.login.clicked.connect(self.check)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def check(self):
        if self.login.isChecked():
            self.loginUrl.show()
            self.label_2.show()
            self.label_3.show()
            self.username.show()
            self.label_4.show()
            self.password.show()
        else:
            self.loginUrl.hide()
            self.label_2.hide()
            self.label_3.hide()
            self.username.hide()
            self.label_4.hide()
            self.password.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "请输入URL"))
        self.pushButton.setText(_translate("MainWindow", "扫描"))
        self.login.setText(_translate("MainWindow", "是否需要登录"))
        self.label_2.setText(_translate("MainWindow", "登录网址"))
        self.label_3.setText(_translate("MainWindow", "用户名"))
        self.label_4.setText(_translate("MainWindow", "密码"))

