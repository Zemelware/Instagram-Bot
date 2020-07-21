# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Instagram_Bot_Application.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from Instagram_Bot import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 589)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.mainTitle.setFont(font)
        self.mainTitle.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.mainTitle.setObjectName("mainTitle")
        self.verticalLayout.addWidget(self.mainTitle)
        spacerItem = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.instagramLoginInfo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.instagramLoginInfo.sizePolicy().hasHeightForWidth())
        self.instagramLoginInfo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.instagramLoginInfo.setFont(font)
        self.instagramLoginInfo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.instagramLoginInfo.setObjectName("instagramLoginInfo")
        self.verticalLayout.addWidget(self.instagramLoginInfo)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.exportToFile = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exportToFile.setFont(font)
        self.exportToFile.setObjectName("exportToFile")
        self.gridLayout.addWidget(self.exportToFile, 8, 2, 1, 1)
        self.outputField = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.outputField.sizePolicy().hasHeightForWidth())
        self.outputField.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.outputField.setFont(font)
        self.outputField.setAutoFillBackground(False)
        self.outputField.setReadOnly(True)
        self.outputField.setAcceptRichText(True)
        self.outputField.setObjectName("outputField")
        self.gridLayout.addWidget(self.outputField, 0, 2, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, 0, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.usernameField = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.usernameField.sizePolicy().hasHeightForWidth())
        self.usernameField.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.usernameField.setFont(font)
        self.usernameField.setObjectName("usernameField")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.usernameField)
        self.username = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.username)
        self.passwordField = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordField.setFont(font)
        self.passwordField.setObjectName("passwordField")
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.passwordField)
        self.password = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.password)
        self.getNotFollowingBack = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.getNotFollowingBack.sizePolicy().hasHeightForWidth())
        self.getNotFollowingBack.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.getNotFollowingBack.setFont(font)
        self.getNotFollowingBack.setStyleSheet("")
        self.getNotFollowingBack.setObjectName("getNotFollowingBack")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.SpanningRole, self.getNotFollowingBack)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(
            2, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.alternateButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.alternateButton1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.alternateButton1.sizePolicy().hasHeightForWidth())
        self.alternateButton1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.alternateButton1.setFont(font)
        self.alternateButton1.setText("")
        self.alternateButton1.setObjectName("alternateButton1")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.SpanningRole, self.alternateButton1)
        self.alternateButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.alternateButton3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.alternateButton3.sizePolicy().hasHeightForWidth())
        self.alternateButton3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.alternateButton3.setFont(font)
        self.alternateButton3.setText("")
        self.alternateButton3.setObjectName("alternateButton3")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.SpanningRole, self.alternateButton3)
        self.alternateButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.alternateButton2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.alternateButton2.sizePolicy().hasHeightForWidth())
        self.alternateButton2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.alternateButton2.setFont(font)
        self.alternateButton2.setText("")
        self.alternateButton2.setObjectName("alternateButton2")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.SpanningRole, self.alternateButton2)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.alternateButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.alternateButton4.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.alternateButton4.setFont(font)
        self.alternateButton4.setText("")
        self.alternateButton4.setObjectName("alternateButton4")
        self.gridLayout.addWidget(self.alternateButton4, 8, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.instagramLoginInfo.raise_()
        self.mainTitle.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1002, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowTitle("Instagram Bot")
        self.mainTitle.setText(_translate("MainWindow", "Instagram Bot"))
        self.instagramLoginInfo.setText(_translate(
            "MainWindow", "Instagram Log in Information"))
        self.exportToFile.setText(_translate(
            "MainWindow", "Export To Text File (*.txt)"))
        self.username.setText(_translate("MainWindow", "Username"))
        self.password.setText(_translate("MainWindow", "Password"))
        self.getNotFollowingBack.setText(_translate(
            "MainWindow", "Get Not Following Back"))

        self.getNotFollowingBack.clicked.connect(
            self.getNotFollowingBackClicked)
        self.exportToFile.clicked.connect(self.saveFile)

    def saveFile(self):
        fileInfo = QtWidgets.QFileDialog.getSaveFileName(
            MainWindow, "Save File", "Not Following Back", "Text File (*.txt)")
        filePath = fileInfo[0]
        if filePath != "":
            with open(filePath, "w") as file:
                text = self.outputField.toPlainText()
                file.write(text)

    def popup(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowTitle("Error!")
        self.msg.setText(
            "An error occurred! This is likely because you entered the wrong username or password. Please try again.")
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)

        popupThread = threading.Thread(target=self.showPopup)
        popupThread.start()

    def showPopup(self):
        x = self.msg.exec_()

    def startBot(self):
        self.bot = InstaBot(self.usernameField.text(),
                            self.passwordField.text())

    def getNotFollowingBackClicked(self):
        self.outputField.clear()
        thread = threading.Thread(target=self.getNotFollowingBackFunc)
        thread.start()

    def getNotFollowingBackFunc(self):
        self.getNotFollowingBack.setEnabled(False)

        try:
            try:
                self.startBot()
            except selenium.common.exceptions.NoSuchElementException:
                self.getNotFollowingBack.setEnabled(True)
                print(
                    "You entered the wrong username or password, please try again.")
                self.popup()

            self.bot.get_not_following_back()

            # Put all the not_following_back into the output field
            for name in self.bot.not_following_back:
                self.outputField.append(name)
        except:
            self.getNotFollowingBack.setEnabled(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
