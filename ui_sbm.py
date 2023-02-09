# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sbm.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(788, 372)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(50, 40))
        self.frame_4.setStyleSheet(u"background-color: rgb(0, 0, 248);")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_menu = QPushButton(self.frame_4)
        self.Btn_menu.setObjectName(u"Btn_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_menu.sizePolicy().hasHeightForWidth())
        self.Btn_menu.setSizePolicy(sizePolicy)
        self.Btn_menu.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        icon = QIcon()
        icon.addFile(u"imagens/hamburger-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_menu.setIcon(icon)
        self.Btn_menu.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.Btn_menu)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(99, 99, 99);")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_esquerda = QFrame(self.frame_6)
        self.frame_esquerda.setObjectName(u"frame_esquerda")
        self.frame_esquerda.setMinimumSize(QSize(50, 0))
        self.frame_esquerda.setMaximumSize(QSize(50, 16777215))
        self.frame_esquerda.setSizeIncrement(QSize(0, 0))
        self.frame_esquerda.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_esquerda.setFrameShape(QFrame.NoFrame)
        self.frame_esquerda.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_esquerda)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_esquerda)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Btn_build = QPushButton(self.frame_9)
        self.Btn_build.setObjectName(u"Btn_build")
        self.Btn_build.setMinimumSize(QSize(150, 50))
        self.Btn_build.setMaximumSize(QSize(150, 50))
        font = QFont()
        font.setPointSize(10)
        self.Btn_build.setFont(font)
        self.Btn_build.setLayoutDirection(Qt.LeftToRight)
        self.Btn_build.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	background-position: center left;\n"
"	padding-left: -30px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"imagens/aws-codebuild.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_build.setIcon(icon1)
        self.Btn_build.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.Btn_build)

        self.Btn_pipeline = QPushButton(self.frame_9)
        self.Btn_pipeline.setObjectName(u"Btn_pipeline")
        self.Btn_pipeline.setMinimumSize(QSize(150, 50))
        self.Btn_pipeline.setMaximumSize(QSize(150, 50))
        self.Btn_pipeline.setFont(font)
        self.Btn_pipeline.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	background-position: center left;\n"
"	padding-left: -13px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 85, 255);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"imagens/aws-codepipeline.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_pipeline.setIcon(icon2)
        self.Btn_pipeline.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.Btn_pipeline)

        self.Btn_s3 = QPushButton(self.frame_9)
        self.Btn_s3.setObjectName(u"Btn_s3")
        self.Btn_s3.setMinimumSize(QSize(150, 50))
        self.Btn_s3.setMaximumSize(QSize(150, 50))
        self.Btn_s3.setFont(font)
        self.Btn_s3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	background-position: center left;\n"
"	padding-left: -25px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 85, 255);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"imagens/amazon-s3-bucket.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_s3.setIcon(icon3)
        self.Btn_s3.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.Btn_s3)


        self.verticalLayout_4.addWidget(self.frame_9, 0, Qt.AlignTop)


        self.horizontalLayout_4.addWidget(self.frame_esquerda)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(76, 76, 76);")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_8)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLayoutDirection(Qt.RightToLeft)
        self.stackedWidget.setLineWidth(1)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_7 = QVBoxLayout(self.page1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.page1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 40))
        self.frame_11.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"background-color: rgb(179, 179, 179);")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_11)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)


        self.verticalLayout_7.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.page1)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.frame_12)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line)

        self.frame_7 = QFrame(self.frame_12)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_7)

        self.line_2 = QFrame(self.frame_12)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_2)

        self.frame_10 = QFrame(self.frame_12)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame_10)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 80, 161, 21))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.frame_10)

        self.line_3 = QFrame(self.frame_12)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_3)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_13)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_15)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16777215, 30))
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	padding-top: 2px;\n"
"    background-color: rgb(0, 85, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.pushButton)

        self.Btn_carboncrm_back = QPushButton(self.frame_15)
        self.Btn_carboncrm_back.setObjectName(u"Btn_carboncrm_back")
        self.Btn_carboncrm_back.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        self.Btn_carboncrm_back.setFont(font2)
        self.Btn_carboncrm_back.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	padding-top: 2px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.Btn_carboncrm_back)

        self.Btn_carboncrm_front = QPushButton(self.frame_15)
        self.Btn_carboncrm_front.setObjectName(u"Btn_carboncrm_front")
        self.Btn_carboncrm_front.setMaximumSize(QSize(16777215, 30))
        self.Btn_carboncrm_front.setFont(font2)
        self.Btn_carboncrm_front.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	padding-top: 2px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.Btn_carboncrm_front)


        self.verticalLayout_6.addWidget(self.frame_15)

        self.line_5 = QFrame(self.frame_13)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_5)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_14)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_14)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(16777215, 30))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	padding-top: 2px;\n"
"    background-color: rgb(0, 85, 255);\n"
"}")

        self.verticalLayout_10.addWidget(self.pushButton_4)

        self.Btn_ifoodtm_back = QPushButton(self.frame_14)
        self.Btn_ifoodtm_back.setObjectName(u"Btn_ifoodtm_back")
        self.Btn_ifoodtm_back.setMaximumSize(QSize(16777215, 30))
        self.Btn_ifoodtm_back.setFont(font2)
        self.Btn_ifoodtm_back.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	padding-top: 2px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"}")

        self.verticalLayout_10.addWidget(self.Btn_ifoodtm_back)

        self.Btn_ifoodtm_front = QPushButton(self.frame_14)
        self.Btn_ifoodtm_front.setObjectName(u"Btn_ifoodtm_front")
        self.Btn_ifoodtm_front.setMaximumSize(QSize(16777215, 30))
        self.Btn_ifoodtm_front.setFont(font2)
        self.Btn_ifoodtm_front.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	padding-top: 2px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"}")

        self.verticalLayout_10.addWidget(self.Btn_ifoodtm_front)


        self.verticalLayout_6.addWidget(self.frame_14)


        self.horizontalLayout_6.addWidget(self.frame_13)

        self.line_4 = QFrame(self.frame_12)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_4)


        self.verticalLayout_7.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.label_2 = QLabel(self.page2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 90, 81, 31))
        self.label_2.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.Btn_start_pipeline = QPushButton(self.page2)
        self.Btn_start_pipeline.setObjectName(u"Btn_start_pipeline")
        self.Btn_start_pipeline.setGeometry(QRect(170, 150, 101, 31))
        self.Btn_start_pipeline.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.label_3 = QLabel(self.page3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 80, 111, 41))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 85, 0);")
        self.Btn_download_s3 = QPushButton(self.page3)
        self.Btn_download_s3.setObjectName(u"Btn_download_s3")
        self.Btn_download_s3.setGeometry(QRect(150, 170, 141, 41))
        self.Btn_download_s3.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.stackedWidget.addWidget(self.page3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.frame_8)


        self.horizontalLayout_3.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_menu.setText("")
        self.Btn_build.setText(QCoreApplication.translate("MainWindow", u"   CodeBuild", None))
        self.Btn_pipeline.setText(QCoreApplication.translate("MainWindow", u"   CodePipeline", None))
        self.Btn_s3.setText(QCoreApplication.translate("MainWindow", u"    S3 Bucket", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>PROJETOS DE COMPILA\u00c7\u00c3O</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/>PROJETOS DE COMPILA\u00c7\u00c3O</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("MainWindow", u"PROJETOS DE COMPILA\u00c7\u00c3O", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"CARBON CRM", None))
        self.Btn_carboncrm_back.setText(QCoreApplication.translate("MainWindow", u"BUILD BACKEND", None))
        self.Btn_carboncrm_front.setText(QCoreApplication.translate("MainWindow", u"BUILD FRONTEND", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"IFOOD TM", None))
        self.Btn_ifoodtm_back.setText(QCoreApplication.translate("MainWindow", u"BUILD BACKEND", None))
        self.Btn_ifoodtm_front.setText(QCoreApplication.translate("MainWindow", u"BUILD FRONTEND", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pipeline", None))
        self.Btn_start_pipeline.setText(QCoreApplication.translate("MainWindow", u"start pipeline", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"S3", None))
        self.Btn_download_s3.setText(QCoreApplication.translate("MainWindow", u"download bucket", None))
    # retranslateUi

