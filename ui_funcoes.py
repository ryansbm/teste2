from main import *
from sbm import Ui_MainWindow


class UIFunctions(MainWindow):

    def expandirmenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_esquerda.width()
            maxExtend = maxWidth
            standard = 50

            # SET MAX WIDTH
            if width == 50:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(
            self.ui.frame_esquerda, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutCirc)
            self.animation.start()
            
    #def Linhas(self):
     #   x = self.ui.lineEdit.text()
      #  print(x)