# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 23:38:05 2020

@author: gaby1
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:22:19 2020

@author: gaby1
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from principal_window import*
from SOM_Window import*
from SVM_Window import*






        
class janela2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_janela2()
        self.ui.setupUi(self)
        
class janela1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_janela1()
        self.ui.setupUi(self)

class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.jan2= janela1()
        
        self.ui.pushButton_2.clicked.connect(self.mudaJanela)
        
        self.jan3= janela2()
        
        self.ui.pushButton_3.clicked.connect(self.mudaJanela2)
        
    def mudaJanela(self):
        self.jan2.show()
        
    def mudaJanela2(self):
        self.jan3.show()
        
    
        
        
    
    
        
if __name__ == "__main__":
    app= QApplication(sys.argv)
    w= Tela()
    w.show()
    sys.exit(app.exec_())