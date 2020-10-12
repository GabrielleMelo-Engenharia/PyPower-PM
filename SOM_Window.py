# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SOM_Window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
from evaporador_teste import Kohonen_ml,Data
from PIL import Image

class Ui_janela1(object):
    def setupUi(self, janela1):
        janela1.setObjectName("janela1")
        janela1.resize(1188, 865)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        janela1.setWindowIcon(icon)
        janela1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.522887 rgba(27, 29, 73, 255));\n"
"border-radius: 10px;\n"
"")
        self.centralwidget = QtWidgets.QWidget(janela1)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 70, 111, 21))
        self.label_4.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_4.setObjectName("label_4")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(250, 100, 91, 17))
        self.radioButton_2.setStyleSheet("\n"
"font: 75 12pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 280, 401, 22))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(440, 130, 113, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(150, 100, 91, 17))
        self.radioButton.setStyleSheet("\n"
"font: 75 12pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 160, 281, 21))
        self.label_6.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 160, 113, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 220, 401, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 250, 351, 21))
        self.label_8.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 130, 271, 21))
        self.label_5.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 190, 121, 21))
        self.label_7.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(620, 100, 41, 51))
        self.label_9.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("arrow (1).png"))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 90, 251, 71))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Calisto MT\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.pushButton.setObjectName("pushButton")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(620, 230, 41, 61))
        self.label_12.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("arrows.png"))
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(620, 170, 41, 61))
        self.label_10.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0113636 rgba(67, 0, 0, 255), stop:0.551136 rgba(67, 0, 0, 255));")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("search.png"))
        self.label_10.setObjectName("label_10")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 230, 251, 71))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Calisto MT\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 160, 251, 71))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Calisto MT\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(620, 100, 41, 51))
        self.label_11.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("arrow (1).png"))
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(620, 160, 41, 61))
        self.label_13.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("search.png"))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(620, 230, 41, 61))
        self.label_14.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("arrows.png"))
        self.label_14.setObjectName("label_14")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(780, 10, 61, 61))
        self.label_3.setStyleSheet("border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("computer.png"))
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 10, 131, 61))
        self.label.setStyleSheet("font: 8pt \"Calisto MT\";\n"
"border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 10, 71, 61))
        self.label_2.setStyleSheet("border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("technology.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(910, 90, 251, 20))
        self.label_15.setStyleSheet("font: 75 12pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_15.setObjectName("label_15")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(910, 90, 251, 211))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(430, 340, 531, 331))
        self.label_17.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(430, 320, 531, 20))
        self.label_16.setStyleSheet("font: 75 12pt \"Calisto MT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(52, 204, 199, 255), stop:0.528947 rgba(19, 177, 172, 255));")
        self.label_16.setObjectName("label_16")
        self.label_3.raise_()
        self.textEdit.raise_()
        self.label_4.raise_()
        self.radioButton_2.raise_()
        self.comboBox_2.raise_()
        self.lineEdit.raise_()
        self.radioButton.raise_()
        self.label_6.raise_()
        self.lineEdit_2.raise_()
        self.comboBox.raise_()
        self.label_8.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.pushButton.raise_()
        self.label_12.raise_()
        self.label_10.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.label_11.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_15.raise_()
        self.label_17.raise_()
        self.label_16.raise_()
        janela1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(janela1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1188, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        janela1.setMenuBar(self.menubar)
        self.actionUndo = QtWidgets.QAction(janela1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon1)
        self.actionUndo.setObjectName("actionUndo")
        self.actionQuit = QtWidgets.QAction(janela1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.menuOptions.addAction(self.actionUndo)
        self.menuOptions.addAction(self.actionQuit)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(janela1)
        self.actionQuit.triggered.connect(janela1.close)
        QtCore.QMetaObject.connectSlotsByName(janela1)

    def retranslateUi(self, janela1):
        _translate = QtCore.QCoreApplication.translate
        janela1.setWindowTitle(_translate("janela1", "PyPower PM"))
        self.label_4.setText(_translate("janela1", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Normalization:</span></p></body></html>"))
        self.radioButton_2.setText(_translate("janela1", "Standard"))
        self.comboBox_2.setItemText(0, _translate("janela1", "Pseudo-Gaussian"))
        self.comboBox_2.setItemText(1, _translate("janela1", "Mexican-Hat"))
        self.radioButton.setText(_translate("janela1", "Min Max"))
        self.label_6.setText(_translate("janela1", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Number of columns for the SOM grid:</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("janela1", "Euclidean"))
        self.comboBox.setItemText(1, _translate("janela1", "Manhattan"))
        self.comboBox.setItemText(2, _translate("janela1", "Mahalanobis"))
        self.comboBox.setItemText(3, _translate("janela1", "Tanimoto"))
        self.label_8.setText(_translate("janela1", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Formula of the neighborhood distance weight:</span></p></body></html>"))
        self.label_5.setText(_translate("janela1", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Number of rowns for the SOM grid:</span></p></body></html>"))
        self.label_7.setText(_translate("janela1", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Distance metric:</span></p></body></html>"))
        self.pushButton.setText(_translate("janela1", "  Load Data"))
        self.pushButton_3.setText(_translate("janela1", "   Save Figure"))
        self.pushButton_2.setText(_translate("janela1", "Cluster"))
        self.label.setText(_translate("janela1", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#0ce8d6;\">SOM</span></p></body></html>"))
        self.label_15.setText(_translate("janela1", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Information about the Data:</span></p></body></html>"))
        self.label_16.setText(_translate("janela1", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Graph view</span></p></body></html>"))
        self.menuOptions.setTitle(_translate("janela1", "Options"))
        self.actionUndo.setText(_translate("janela1", "Undo"))
        self.actionUndo.setShortcut(_translate("janela1", "Ctrl+Z"))
        self.actionQuit.setText(_translate("janela1", "Quit"))
        self.actionQuit.setShortcut(_translate("janela1", "Ctrl+C"))
        self.pushButton.clicked.connect(self.botao1_loadData_KOHONEN) #botão de carregar dados de Kohonen
        self.pushButton_2.clicked.connect(self.botao2_testandtrainKOHONEN) #botão de clusterizar Kohonen
        self.pushButton_3.clicked.connect(self.botao_saveKohonen) #botão de salvar a figura de KOHONEN
        self.actionUndo.triggered.connect(self.undo) #botão deesfazer
        
        
    def undo(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.textEdit.clear()
        self.label_17.clear()
        
    def botao1_loadData_KOHONEN(self):
        self.open_dialog_box2()
            
    def open_dialog_box2(self):
            
        self.filename2,_= QFileDialog.getOpenFileName()
        
        if self.filename2.endswith('xlsx'):
          self.dataframe2 = pd.read_excel(self.filename2,index_col=False)
          
        else:
          self.dataframe2 =pd.read_csv(self.filename2, index_col=False) 
          
                 
        num_colunas1= self.dataframe2.shape[1]
        self.y= self.dataframe2['target']
        self.labels1= self.y.unique()
        #num_variaveis1= num_colunas1-1 
        total_dados1= self.dataframe2.size
        dadosKohonen= "\n\n\n\nVariable Numbers: {one}\n\n\nSamples Numbers: {two}\n\n\nTotal Data: {three}".format(one=num_colunas1,two=self.dataframe2.shape[0],three=total_dados1)
        self.textEdit.setText(dadosKohonen)
        
    def botao2_testandtrainKOHONEN(self):
        
        if self.radioButton.isChecked():
            RB2='Min Max'
        else:
            RB2='Standard'
        
        
        E8= int(self.lineEdit_2.text()) #colunas
        E9= int(self.lineEdit.text()) #linhas
        
        C1=self.comboBox.currentIndex()
        C2=self.comboBox_2.currentIndex()
        
        if C1==0:
            distance_metric= "euclidean"
        elif C1==1:
            distance_metric=  "manhattan"
        elif C1==2:
            distance_metric= "mahalanobis"
        else:
            distance_metric= "tanimoto"
            
            
        if C2==0:
            formula= "pseudo-gaussian"
        else:
            formula= "mexican-hat"
            
        dados= Data(0,self.filename2,RB2,testSize=0.2,shuffle=True,output=None)
        data = dados.preprocessing()

        ml = Kohonen_ml(data,E9,E8,distance_metric,formula)
        ml.train()
        ml.plot()
        self.figure_Kohonen=self.label_17.setPixmap(QtGui.QPixmap("SOM.png"))
        self.im = Image.open( 'SOM.png' )
        
    def botao_saveKohonen(self):
        self.open_dialog_box_Kohonen()
        
        
    def open_dialog_box_Kohonen(self):
        
        
        fileName,_= QFileDialog.getSaveFileName() 
       
        self.im.save(fileName)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janela1 = QtWidgets.QMainWindow()
    ui = Ui_janela1()
    ui.setupUi(janela1)
    janela1.show()
    sys.exit(app.exec_())

