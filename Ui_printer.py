# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Printer.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 508)
        MainWindow.setMinimumSize(QtCore.QSize(200, 200))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 39, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 40, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 291, 221))
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 80, 291, 221))
        self.label_4.setText("")
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 320, 641, 121))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.layoutWidget = QtWidgets.QWidget(self.page)
        self.layoutWidget.setGeometry(QtCore.QRect(280, 20, 91, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Choose_img_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.Choose_img_btn.setObjectName("Choose_img_btn")
        self.verticalLayout.addWidget(self.Choose_img_btn)
        self.Take_pic_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.Take_pic_btn.setObjectName("Take_pic_btn")
        self.verticalLayout.addWidget(self.Take_pic_btn)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(280, 20, 91, 71))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Draw_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.Draw_btn.setObjectName("Draw_btn")
        self.verticalLayout_2.addWidget(self.Draw_btn)
        self.Cancel_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.Cancel_btn.setObjectName("Cancel_btn")
        self.verticalLayout_2.addWidget(self.Cancel_btn)
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Original Image:"))
        self.label_2.setText(_translate("MainWindow", "Drawing Preview:"))
        self.Choose_img_btn.setText(_translate("MainWindow", "Choose image"))
        self.Take_pic_btn.setText(_translate("MainWindow", "Take a picture"))
        self.Draw_btn.setText(_translate("MainWindow", "Draw"))
        self.Cancel_btn.setText(_translate("MainWindow", "Cancel"))