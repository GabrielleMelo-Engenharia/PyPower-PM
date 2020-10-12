# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(639, 483)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(900, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.522887 rgba(27, 29, 73, 255));\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 131, 461))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 120, 131, 61))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    font: 75 20pt \"Calisto MT\";\n"
"    color: rgb(255, 255, 255);\n"
"    border: Opx solid;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 250, 131, 61))
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"   \n"
"    font: 75 20pt \"Calisto MT\";\n"
"    color: rgb(255, 255, 255);\n"
"    border: Opx solid;\n"
"   border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.frame_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(29, 141, 134, 255), stop:0.495595 rgba(41, 187, 187, 255));\n"
"border-radius: 10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.label.setStyleSheet("font: 75 14pt \"Calisto MT\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 410, 81, 31))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logoLabsia.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(130, 0, 531, 481))
        self.label_3.setStyleSheet("font: 75 14pt \"Calisto MT\";")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("PyPower PM (1).png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(130, 0, 541, 481))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("PyPower PM/Interfaceprincipal_Cilamce.png"))
        self.label_4.setObjectName("label_4")
        self.label_3.raise_()
        self.frame_2.raise_()
        self.label_4.raise_()
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyPower PM"))
        self.pushButton_2.setText(_translate("MainWindow", "SOM"))
        self.pushButton_3.setText(_translate("MainWindow", "SVM"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">MENU</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

