# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sbm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(50, 40))
        self.frame_4.setStyleSheet("background-color: rgb(0, 0, 248);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_menu = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_menu.sizePolicy().hasHeightForWidth())
        self.Btn_menu.setSizePolicy(sizePolicy)
        self.Btn_menu.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.Btn_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagens/hamburger-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_menu.setIcon(icon)
        self.Btn_menu.setIconSize(QtCore.QSize(30, 30))
        self.Btn_menu.setObjectName("Btn_menu")
        self.verticalLayout_2.addWidget(self.Btn_menu)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setStyleSheet("background-color: rgb(99, 99, 99);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_esquerda = QtWidgets.QFrame(self.frame_6)
        self.frame_esquerda.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_esquerda.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_esquerda.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame_esquerda.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_esquerda.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_esquerda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_esquerda.setObjectName("frame_esquerda")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_esquerda)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_9 = QtWidgets.QFrame(self.frame_esquerda)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Btn_build = QtWidgets.QPushButton(self.frame_9)
        self.Btn_build.setMinimumSize(QtCore.QSize(150, 50))
        self.Btn_build.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Btn_build.setFont(font)
        self.Btn_build.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Btn_build.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    background-position: center left;\n"
"    padding-left: -30px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imagens/aws-codebuild.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_build.setIcon(icon1)
        self.Btn_build.setIconSize(QtCore.QSize(35, 35))
        self.Btn_build.setObjectName("Btn_build")
        self.verticalLayout_3.addWidget(self.Btn_build)
        self.Btn_pipeline = QtWidgets.QPushButton(self.frame_9)
        self.Btn_pipeline.setMinimumSize(QtCore.QSize(150, 50))
        self.Btn_pipeline.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Btn_pipeline.setFont(font)
        self.Btn_pipeline.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    background-position: center left;\n"
"    padding-left: -13px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 255);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imagens/aws-codepipeline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_pipeline.setIcon(icon2)
        self.Btn_pipeline.setIconSize(QtCore.QSize(35, 35))
        self.Btn_pipeline.setObjectName("Btn_pipeline")
        self.verticalLayout_3.addWidget(self.Btn_pipeline)
        self.Btn_s3 = QtWidgets.QPushButton(self.frame_9)
        self.Btn_s3.setMinimumSize(QtCore.QSize(150, 50))
        self.Btn_s3.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Btn_s3.setFont(font)
        self.Btn_s3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"    background-position: center left;\n"
"    padding-left: -25px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 255);\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imagens/amazon-s3-bucket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_s3.setIcon(icon3)
        self.Btn_s3.setIconSize(QtCore.QSize(35, 35))
        self.Btn_s3.setObjectName("Btn_s3")
        self.verticalLayout_3.addWidget(self.Btn_s3)
        self.verticalLayout_4.addWidget(self.frame_9, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_4.addWidget(self.frame_esquerda)
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setStyleSheet("background-color: rgb(76, 76, 76);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_8)
        self.stackedWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_11 = QtWidgets.QFrame(self.page1)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_11.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"background-color: rgb(179, 179, 179);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.verticalLayout_7.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.page1)
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.line = QtWidgets.QFrame(self.frame_12)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_6.addWidget(self.line)
        self.frame_7 = QtWidgets.QFrame(self.frame_12)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6.addWidget(self.frame_7)
        self.line_2 = QtWidgets.QFrame(self.frame_12)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_6.addWidget(self.line_2)
        self.frame_10 = QtWidgets.QFrame(self.frame_12)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit.setGeometry(QtCore.QRect(40, 80, 161, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.frame_10)
        self.line_3 = QtWidgets.QFrame(self.frame_12)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_6.addWidget(self.line_3)
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_15 = QtWidgets.QFrame(self.frame_13)
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton = QtWidgets.QPushButton(self.frame_15)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"    border: none;\n"
"    padding-top: 2px;\n"
"    background-color: rgb(0, 85, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_9.addWidget(self.pushButton)
        self.Btn_carboncrm_back = QtWidgets.QPushButton(self.frame_15)
        self.Btn_carboncrm_back.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Btn_carboncrm_back.setFont(font)
        self.Btn_carboncrm_back.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"    border: none;\n"
"    padding-top: 2px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 85, 255);\n"
"}")
        self.Btn_carboncrm_back.setObjectName("Btn_carboncrm_back")
        self.verticalLayout_9.addWidget(self.Btn_carboncrm_back)
        self.Btn_carboncrm_front = QtWidgets.QPushButton(self.frame_15)
        self.Btn_carboncrm_front.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Btn_carboncrm_front.setFont(font)
        self.Btn_carboncrm_front.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"    border: none;\n"
"    padding-top: 2px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 85, 255);\n"
"}")
        self.Btn_carboncrm_front.setObjectName("Btn_carboncrm_front")
        self.verticalLayout_9.addWidget(self.Btn_carboncrm_front)
        self.verticalLayout_6.addWidget(self.frame_15)
        self.line_5 = QtWidgets.QFrame(self.frame_13)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_6.addWidget(self.line_5)
        self.frame_14 = QtWidgets.QFrame(self.frame_13)
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"    border: none;\n"
"    padding-top: 2px;\n"
"    background-color: rgb(0, 85, 255);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_10.addWidget(self.pushButton_4)
        self.Btn_ifoodtm_back = QtWidgets.QPushButton(self.frame_14)
        self.Btn_ifoodtm_back.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Btn_ifoodtm_back.setFont(font)
        self.Btn_ifoodtm_back.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"    border: none;\n"
"    padding-top: 2px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 85, 255);\n"
"}")
        self.Btn_ifoodtm_back.setObjectName("Btn_ifoodtm_back")
        self.verticalLayout_10.addWidget(self.Btn_ifoodtm_back)
        self.Btn_ifoodtm_front = QtWidgets.QPushButton(self.frame_14)
        self.Btn_ifoodtm_front.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Btn_ifoodtm_front.setFont(font)
        self.Btn_ifoodtm_front.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"    border: none;\n"
"    padding-top: 2px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 85, 255);\n"
"}")
        self.Btn_ifoodtm_front.setObjectName("Btn_ifoodtm_front")
        self.verticalLayout_10.addWidget(self.Btn_ifoodtm_front)
        self.verticalLayout_6.addWidget(self.frame_14)
        self.horizontalLayout_6.addWidget(self.frame_13)
        self.line_4 = QtWidgets.QFrame(self.frame_12)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_6.addWidget(self.line_4)
        self.verticalLayout_7.addWidget(self.frame_12)
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.label_2 = QtWidgets.QLabel(self.page2)
        self.label_2.setGeometry(QtCore.QRect(210, 90, 81, 31))
        self.label_2.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.label_2.setObjectName("label_2")
        self.Btn_start_pipeline = QtWidgets.QPushButton(self.page2)
        self.Btn_start_pipeline.setGeometry(QtCore.QRect(170, 150, 101, 31))
        self.Btn_start_pipeline.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.Btn_start_pipeline.setObjectName("Btn_start_pipeline")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.label_3 = QtWidgets.QLabel(self.page3)
        self.label_3.setGeometry(QtCore.QRect(230, 80, 111, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.label_3.setObjectName("label_3")
        self.Btn_download_s3 = QtWidgets.QPushButton(self.page3)
        self.Btn_download_s3.setGeometry(QtCore.QRect(150, 170, 141, 41))
        self.Btn_download_s3.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.Btn_download_s3.setObjectName("Btn_download_s3")
        self.stackedWidget.addWidget(self.page3)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.frame_8)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn_build.setText(_translate("MainWindow", "   CodeBuild"))
        self.Btn_pipeline.setText(_translate("MainWindow", "   CodePipeline"))
        self.Btn_s3.setText(_translate("MainWindow", "    S3 Bucket"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p>PROJETOS DE COMPILAÇÃO</p></body></html>"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/>PROJETOS DE COMPILAÇÃO</p></body></html>"))
        self.label.setText(_translate("MainWindow", "PROJETOS DE COMPILAÇÃO"))
        self.pushButton.setText(_translate("MainWindow", "CARBON CRM"))
        self.Btn_carboncrm_back.setText(_translate("MainWindow", "BUILD BACKEND"))
        self.Btn_carboncrm_front.setText(_translate("MainWindow", "BUILD FRONTEND"))
        self.pushButton_4.setText(_translate("MainWindow", "IFOOD TM"))
        self.Btn_ifoodtm_back.setText(_translate("MainWindow", "BUILD BACKEND"))
        self.Btn_ifoodtm_front.setText(_translate("MainWindow", "BUILD FRONTEND"))
        self.label_2.setText(_translate("MainWindow", "Pipeline"))
        self.Btn_start_pipeline.setText(_translate("MainWindow", "start pipeline"))
        self.label_3.setText(_translate("MainWindow", "S3"))
        self.Btn_download_s3.setText(_translate("MainWindow", "download bucket"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
