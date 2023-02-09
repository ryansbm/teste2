from main import *
from sbm import Ui_MainWindow


class linhas(QMainWindow):
    
    def teste(self,x):
        x = self.ui.lineEdit.text()
        if x =='ryan':
            print('login correto')
        else:
            print('error')
