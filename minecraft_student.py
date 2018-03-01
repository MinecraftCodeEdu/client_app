# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtNetwork import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 956)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 400, 40))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setFont(QFont('',15,QtGui.QFont.Bold))
        self.label.setObjectName("label")


        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 40, 89, 25))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 40, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 40, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 1150, 800))


        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.web_index = Browser()
        self.verticalLayout.addWidget(self.web_index)
        self.web_index.load(QUrl("http://coedu.twbuddy.com:7070"))


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        self.pushButton_1.clicked.connect(self.handler_view1)
        self.pushButton_2.clicked.connect(self.handler_view2)
        self.pushButton_3.clicked.connect(self.handler_view3)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "마인크래프트 에디터"))
        self.pushButton_1.setText(_translate("MainWindow", "스테이지1"))
        self.pushButton_2.setText(_translate("MainWindow", "스테이지2"))
        self.pushButton_3.setText(_translate("MainWindow", "스테이지3"))
        self.label.setText(_translate("MainWindow", "마인크래프트 블록코딩"))
        self.menu.setTitle(_translate("MainWindow", "학생용"))

    def closeEvent_Main(self):
        for i in range(self.verticalLayout.count()):
            item = self.verticalLayout.itemAt(i)
            widget = item.widget()
            if widget:
                try:
                    widget.close()
                except:
                    pass

    def handler_view1(self):
        self.web_main = Browser()
        self.closeEvent_Main()
        self.verticalLayout.addWidget(self.web_main)

        self.web_main.load(QUrl("http://coedu.twbuddy.com:7070"))

    def handler_view2(self):
        self.web_main = Browser()
        self.closeEvent_Main()
        self.verticalLayout.addWidget(self.web_main)

        self.web_main.load(QUrl("http://coedu.twbuddy.com:7071"))

    def handler_view3(self):
        self.web_main = Browser()
        self.closeEvent_Main()
        self.verticalLayout.addWidget(self.web_main)

        self.web_main.load(QUrl("http://coedu.twbuddy.com"))

class Browser(QWebView):
    def __init__(self):
        self.view = QWebView.__init__(self)
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)


    def load(self, url):
        self.setUrl(QUrl(url))

    def adjustTitle(self):
        self.setWindowTitle(self.title())

    def disableJS(self):
        settings = QWebSettings.globalSettings()
        settings.setAttribute(QWebSettings.JavascriptEnabled, False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

