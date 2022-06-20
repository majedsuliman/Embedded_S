from PyQt5.QtWidgets import QApplication, QWidget,QStackedWidget, QPushButton, QVBoxLayout,QGraphicsView, QWizard, QMainWindow, QLabel,QDialog, QFileDialog,QMessageBox

from PyQt5 import QtGui
from PyQt5 import uic
import sys
import qdarkstyle
from Functions import *
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Ui_printer import Ui_MainWindow
Filename = ''
class UI:
    def __init__(self):
        self.Main = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.Main)

        # Initialize 
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.Choose_img_btn.clicked.connect(self.BrowseImage)
        self.ui.Draw_btn.clicked.connect(self.Draw)
        self.ui.Cancel_btn.clicked.connect(self.Cancel)
        self.ui.label_3.setStyleSheet("border: 1px solid black;")
        self.ui.label_4.setStyleSheet("border: 1px solid black;")
        self.Main.show()



    def BrowseImage(self):
        fname = QFileDialog.getOpenFileName(None,'Open File', 'c:\\', 'Image files (*.jpg *png *.jpeg)')
        global Filename
        imagepth = fname[0]
        if(imagepth == ""):
            return

        else:
            self.ui.stackedWidget.setCurrentIndex(1)
            head ,tail = os.path.split(imagepth)    
            filename = tail.split('.')
        
            pixmap = QtGui.QPixmap(imagepth)
            self.ui.label_3.setPixmap(QtGui.QPixmap(imagepth))
            img2bmp(imagepth,filename)
            CovertToPBM(0.5,filename)
        
            pixmap1 = QtGui.QPixmap('./PBM images/'+filename[0]+'.pbm')
            self.ui.label_4.setPixmap(pixmap1)
            Filename = filename[0]
          
           
            
            
            
    def Cancel(self):
        self.ui.stackedWidget.setCurrentIndex(0)
       

    def Draw(self):
        
        if self.ui.label_3.pixmap()== None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Choose image first')
            msg.setWindowTitle("Error")
    
            x= msg.exec_()
        else:
            global Filename
            ConvertToSVG(Filename)
            FixSvgHeader(Filename)
            ConvertToGCode(Filename)
         

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    UImain = UI()
    sys.exit(app.exec_())