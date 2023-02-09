
from sbm import Ui_MainWindow
import sys
import traceback
import os
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal

# importar funções
from ui_funcoes import *
from ui_build import *
from ui_s3 import *
from linhas import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Btn_menu.clicked.connect(
            lambda: UIFunctions.expandirmenu(self, 150, True))

        self.ui.Btn_build.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page1))

        self.ui.Btn_pipeline.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page2))

        self.ui.Btn_s3.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page3))

        # self.ui.Btn_carboncrm_back.clicked.connect(ProjetosBuild.build)

        self.ui.Btn_download_s3.clicked.connect(S3bucket.bucket)
        
        self.ui.Btn_ifoodtm_back.clicked.connect(
            lambda : linhas.teste(self, self.x))
        self.ui.lineEdit.returnPressed.connect(
            lambda : linhas.teste(self, self.x))
        
        self.show()
    
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
