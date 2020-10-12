# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SVM_Window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
from evaporador_teste import SVM, Data
from PIL import Image

class Ui_janela2(object):
    def setupUi(self, janela2):
        janela2.setObjectName("janela2")
        janela2.resize(1144, 788)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        janela2.setWindowIcon(icon)
        janela2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.522887 rgba(27, 29, 73, 255));\n"
" border-radius: 10px;\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(janela2)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(280, 90, 91, 17))
        self.radioButton_2.setStyleSheet("\n"
"font: 75 12pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(180, 90, 91, 17))
        self.radioButton.setStyleSheet("\n"
"font: 75 12pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 60, 111, 21))
        self.label_4.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 120, 111, 21))
        self.label_5.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 150, 111, 21))
        self.label_6.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 180, 171, 21))
        self.label_7.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(180, 220, 91, 21))
        self.label_9.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_9.setObjectName("label_9")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(180, 250, 341, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(180, 290, 221, 21))
        self.label_10.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(180, 320, 91, 21))
        self.label_11.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(180, 380, 131, 21))
        self.label_12.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_12.setObjectName("label_12")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(410, 120, 111, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 180, 113, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(410, 150, 113, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(410, 380, 111, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(410, 320, 111, 20))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(410, 290, 111, 20))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(920, 100, 241, 20))
        self.label_15.setStyleSheet("font: 75 12pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_15.setObjectName("label_15")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(920, 120, 241, 181))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 100, 271, 61))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Calisto MT\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.pushButton.setObjectName("pushButton")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(590, 110, 31, 41))
        self.label_14.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("arrow (1).png"))
        self.label_14.setObjectName("label_14")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 230, 271, 71))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Calisto MT\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(590, 180, 41, 41))
        self.label_17.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("business-and-finance.png"))
        self.label_17.setObjectName("label_17")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 160, 271, 71))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Calisto MT\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(590, 250, 41, 41))
        self.label_18.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("arrows.png"))
        self.label_18.setObjectName("label_18")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 10, 71, 61))
        self.label_2.setStyleSheet("border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("color (1).png"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(780, 10, 71, 61))
        self.label_3.setStyleSheet("border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("artificial-intelligence.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 10, 131, 61))
        self.label.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(650, 350, 451, 311))
        self.label_19.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(650, 330, 451, 20))
        self.label_16.setStyleSheet("font: 75 12pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_16.setObjectName("label_16")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(240, 440, 241, 20))
        self.label_20.setStyleSheet("font: 75 12pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_20.setObjectName("label_20")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 460, 241, 201))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(180, 350, 91, 21))
        self.label_13.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_13.setObjectName("label_13")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(410, 350, 111, 20))
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_2.raise_()
        self.radioButton_2.raise_()
        self.radioButton.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.comboBox.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_7.raise_()
        self.textEdit.raise_()
        self.label_15.raise_()
        self.pushButton.raise_()
        self.label_14.raise_()
        self.pushButton_3.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_19.raise_()
        self.label_16.raise_()
        self.label_20.raise_()
        self.textEdit_2.raise_()
        self.label_13.raise_()
        self.lineEdit_8.raise_()
        janela2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(janela2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1144, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        janela2.setMenuBar(self.menubar)
        self.actionUndo = QtWidgets.QAction(janela2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon1)
        self.actionUndo.setObjectName("actionUndo")
        self.actionQuit = QtWidgets.QAction(janela2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionUndo)
        self.menuOptions.addAction(self.actionQuit)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(janela2)
        self.actionQuit.triggered.connect(janela2.close)
        QtCore.QMetaObject.connectSlotsByName(janela2)

    def retranslateUi(self, janela2):
        _translate = QtCore.QCoreApplication.translate
        janela2.setWindowTitle(_translate("janela2", "PyPower PM"))
        self.radioButton_2.setText(_translate("janela2", "Standard"))
        self.radioButton.setText(_translate("janela2", "Min Max"))
        self.label_4.setText(_translate("janela2", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Normalization:</span></p></body></html>"))
        self.label_5.setText(_translate("janela2", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Iterations:</span></p></body></html>"))
        self.label_6.setText(_translate("janela2", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Tolerance:</span></p></body></html>"))
        self.label_7.setText(_translate("janela2", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Percentage to test (%):</span></p></body></html>"))
        self.label_9.setText(_translate("janela2", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Kernel:</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("janela2", "Radial Basis Function (RBF)"))
        self.comboBox.setItemText(1, _translate("janela2", "Sigmoid Function"))
        self.comboBox.setItemText(2, _translate("janela2", "Precomputed Function"))
        self.comboBox.setItemText(3, _translate("janela2", "Polynomial Function"))
        self.comboBox.setItemText(4, _translate("janela2", "Linear Function"))
        self.label_10.setText(_translate("janela2", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Regularization parameter (C):</span></p></body></html>"))
        self.label_11.setText(_translate("janela2", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Gamma:</span></p></body></html>"))
        self.label_12.setText(_translate("janela2", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Class column:</span></p></body></html>"))
        self.label_15.setText(_translate("janela2", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Information about the Data:</span></p></body></html>"))
        self.pushButton.setText(_translate("janela2", "  Load Data"))
        self.pushButton_3.setText(_translate("janela2", "   Save Figure"))
        self.pushButton_2.setText(_translate("janela2", "  Train and Test"))
        self.label.setText(_translate("janela2", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#0ce8d6;\">SVM</span></p></body></html>"))
        self.label_16.setText(_translate("janela2", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Graph view</span></p></body></html>"))
        self.label_20.setText(_translate("janela2", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SVM Evaluation:</span></p></body></html>"))
        self.label_13.setText(_translate("janela2", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Degree:</span></p></body></html>"))
        self.menuOptions.setTitle(_translate("janela2", "Options"))
        self.actionUndo.setText(_translate("janela2", "Undo"))
        self.actionUndo.setShortcut(_translate("janela2", "Ctrl+Z"))
        self.actionQuit.setText(_translate("janela2", "Quit"))
        self.actionQuit.setShortcut(_translate("janela2", "Ctrl+C"))
        self.pushButton.clicked.connect(self.botao3_loadData_MLP) #botão de carregar dados da MLP
        self.pushButton_2.clicked.connect(self.botao2_testandtrain_MLP) #botão de testar e treinar MLP
       
        self.pushButton_3.clicked.connect(self.botao_saveMLP) #botão de salvar a figura de MLP
        self.actionUndo.triggered.connect(self.undo) #botão deesfazer
        
        
    def undo(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.label_19.clear()
        
        
        
    '''BOTÃO DE CARREGAR DADOS PARA MLP'''
        
    def botao3_loadData_MLP(self):
        self.open_dialog_box1()
        
    def open_dialog_box1(self):
        self.filename1,_= QFileDialog.getOpenFileName()
        if self.filename1.endswith('xlsx'):
          self.dataframe1= pd.read_excel(self.filename1,index_col=False)  
        else:
          self.dataframe1=pd.read_csv(self.filename1, index_col=False)   
         
        num_colunas= self.dataframe1.shape[1]
        num_variaveis= num_colunas-1
        total_dados= self.dataframe1.size
        dadosdaMLP= "\n\n\n\nVariable Numbers: {one}\n\n\nSamples Numbers: {two}\n\n\nTotal Data: {three}".format(one=num_variaveis,two=self.dataframe1.shape[0],three=total_dados)
        self.textEdit.setText(dadosdaMLP)
        
#####################################################################################################
        
        
    '''BOTÃO DE TESTAR E TREINAR A MLP'''        
        
    def botao2_testandtrain_MLP(self):
        E1= int(self.lineEdit.text())  #iteracões
        E2= float(self.lineEdit_3.text())  #tolerancia
        E3= float(self.lineEdit_2.text())  #porcentagem de teste
        E4= self.lineEdit_5.text()  #class column
        E5= int(self.lineEdit_7.text()) #C
        E6= self.lineEdit_6.text()  #gamma
        E7= int(self.lineEdit_8.text())  #degree
        C2= self.comboBox.currentIndex() #kernel
       
        
        test= E3/100
            
            
        if C2==0:
            kernel= 'rbf'
            
        elif C2==1:
            kernel= 'sigmoid'
        elif C2==2:
            kernel='precomputed'
        elif C2==3:
            kernel= 'poly'
        else:
            kernel= 'linear'
            
                
                
      
            
            
        if self.radioButton.isChecked():
            RB1= 'Min Max'
        else:
            RB1= 'Standard'
        
        
        
        dados = Data(1,self.filename1,RB1,test,shuffle=True,output=E4)
        data = dados.preprocessing()
        labels = dados.getLabels()
        svm= SVM(data,E5,E7,E6,kernel,E1,E2)
       
        svm.train()
        scores= svm.evaluate()
        svm.plot(labels)
        f1, accuracy, precision,recall= scores[0], scores[1],scores[2],scores[3]
        evaluation_MLP= "\n\n\n {one}\n\n\n {two}\n\n\n {three}\n\n\n {four}".format(one=f1,two=accuracy,three=precision,four=recall)
        self.textEdit_2.setText(evaluation_MLP)
        svm.plot(labels) 
        self.figure_MLP= self.label_19.setPixmap(QtGui.QPixmap("ConfusionMatrix.png"))
        self.im1 = Image.open( 'ConfusionMatrix.png' )
        
################################################################################################################
    '''SAVE FIGURE_MLP'''
    
    def botao_saveMLP(self):
        self.open_dialog_box_MLP()
        
        
    def open_dialog_box_MLP(self):
        
        option= QFileDialog.Options()
        fileName1,_= QFileDialog.getSaveFileName() 
        self.im1.save(fileName1)
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janela2 = QtWidgets.QMainWindow()
    ui = Ui_janela2()
    ui.setupUi(janela2)
    janela2.show()
    sys.exit(app.exec_())

