# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(726, 395)
        Form.setStyleSheet("background-color: rgb(249, 246, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 706, 375))
        self.scrollAreaWidgetContents.setStyleSheet("QTabBar::tab {\n"
"    background-color: rgb(222, 217, 238);\n"
"    color: black;\n"
"}\n"
"QTabBar::tab:selected {\n"
"       background-color: rgb(204, 193, 238);\n"
"    color: black;\n"
"}")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setStyleSheet("")
        self.page_1.setObjectName("page_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.page1_label = QtWidgets.QLabel(self.page_1)
        self.page1_label.setObjectName("page1_label")
        self.verticalLayout_3.addWidget(self.page1_label, 0, QtCore.Qt.AlignHCenter)
        self.neck_groupbox = QtWidgets.QGroupBox(self.page_1)
        self.neck_groupbox.setObjectName("neck_groupbox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.neck_groupbox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.nackimg_hbox = QtWidgets.QHBoxLayout()
        self.nackimg_hbox.setContentsMargins(-1, -1, -1, 0)
        self.nackimg_hbox.setSpacing(50)
        self.nackimg_hbox.setObjectName("nackimg_hbox")
        self.neckimg_1 = QtWidgets.QLabel(self.neck_groupbox)
        self.neckimg_1.setStyleSheet("border-image: url(:/Neck/resource/neck/neck1.png);")
        self.neckimg_1.setText("")
        self.neckimg_1.setObjectName("neckimg_1")
        self.nackimg_hbox.addWidget(self.neckimg_1)
        self.neckimg_2 = QtWidgets.QLabel(self.neck_groupbox)
        self.neckimg_2.setStyleSheet("border-image: url(:/Neck/resource/neck/neck2.png);")
        self.neckimg_2.setText("")
        self.neckimg_2.setObjectName("neckimg_2")
        self.nackimg_hbox.addWidget(self.neckimg_2)
        self.neckimg_3 = QtWidgets.QLabel(self.neck_groupbox)
        self.neckimg_3.setStyleSheet("border-image: url(:/Neck/resource/neck/neck3.png);")
        self.neckimg_3.setText("")
        self.neckimg_3.setObjectName("neckimg_3")
        self.nackimg_hbox.addWidget(self.neckimg_3)
        self.verticalLayout_4.addLayout(self.nackimg_hbox)
        self.neckbtn_hbox = QtWidgets.QHBoxLayout()
        self.neckbtn_hbox.setObjectName("neckbtn_hbox")
        self.neckbtn_1 = QtWidgets.QRadioButton(self.neck_groupbox)
        self.neckbtn_1.setObjectName("neckbtn_1")
        self.neckbtn_hbox.addWidget(self.neckbtn_1, 0, QtCore.Qt.AlignHCenter)
        self.neckbtn_2 = QtWidgets.QRadioButton(self.neck_groupbox)
        self.neckbtn_2.setObjectName("neckbtn_2")
        self.neckbtn_hbox.addWidget(self.neckbtn_2, 0, QtCore.Qt.AlignHCenter)
        self.neckbtn_3 = QtWidgets.QRadioButton(self.neck_groupbox)
        self.neckbtn_3.setObjectName("neckbtn_3")
        self.neckbtn_hbox.addWidget(self.neckbtn_3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addLayout(self.neckbtn_hbox)
        self.verticalLayout_4.setStretch(0, 3)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.neck_groupbox)
        self.neckadj_groupBox = QtWidgets.QGroupBox(self.page_1)
        self.neckadj_groupBox.setObjectName("neckadj_groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.neckadj_groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.neck_adjbtn_1 = QtWidgets.QCheckBox(self.neckadj_groupBox)
        self.neck_adjbtn_1.setObjectName("neck_adjbtn_1")
        self.verticalLayout_5.addWidget(self.neck_adjbtn_1)
        self.verticalLayout_3.addWidget(self.neckadj_groupBox)
        self.verticalLayout_3.setStretch(1, 5)
        self.verticalLayout_3.setStretch(2, 1)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.page2_label = QtWidgets.QLabel(self.page_2)
        self.page2_label.setObjectName("page2_label")
        self.verticalLayout_6.addWidget(self.page2_label, 0, QtCore.Qt.AlignHCenter)
        self.trunk_groupbox = QtWidgets.QGroupBox(self.page_2)
        self.trunk_groupbox.setObjectName("trunk_groupbox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.trunk_groupbox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.trunkimg_hbox = QtWidgets.QHBoxLayout()
        self.trunkimg_hbox.setObjectName("trunkimg_hbox")
        self.trunkimg_1 = QtWidgets.QLabel(self.trunk_groupbox)
        self.trunkimg_1.setAutoFillBackground(False)
        self.trunkimg_1.setStyleSheet("border-image: url(:/Trunk/resource/trunk/trunk1.png);")
        self.trunkimg_1.setText("")
        self.trunkimg_1.setObjectName("trunkimg_1")
        self.trunkimg_hbox.addWidget(self.trunkimg_1)
        self.trunkimg_2 = QtWidgets.QLabel(self.trunk_groupbox)
        self.trunkimg_2.setStyleSheet("border-image: url(:/Trunk/resource/trunk/trunk2.png);")
        self.trunkimg_2.setText("")
        self.trunkimg_2.setObjectName("trunkimg_2")
        self.trunkimg_hbox.addWidget(self.trunkimg_2)
        self.trunkimg_3 = QtWidgets.QLabel(self.trunk_groupbox)
        self.trunkimg_3.setStyleSheet("border-image: url(:/Trunk/resource/trunk/trunk3.png);")
        self.trunkimg_3.setText("")
        self.trunkimg_3.setObjectName("trunkimg_3")
        self.trunkimg_hbox.addWidget(self.trunkimg_3)
        self.trunkimg_4 = QtWidgets.QLabel(self.trunk_groupbox)
        self.trunkimg_4.setStyleSheet("border-image: url(:/Trunk/resource/trunk/trunk4.png);")
        self.trunkimg_4.setText("")
        self.trunkimg_4.setObjectName("trunkimg_4")
        self.trunkimg_hbox.addWidget(self.trunkimg_4)
        self.trunkimg_5 = QtWidgets.QLabel(self.trunk_groupbox)
        self.trunkimg_5.setStyleSheet("border-image: url(:/Trunk/resource/trunk/trunk5.png);")
        self.trunkimg_5.setText("")
        self.trunkimg_5.setObjectName("trunkimg_5")
        self.trunkimg_hbox.addWidget(self.trunkimg_5)
        self.verticalLayout_7.addLayout(self.trunkimg_hbox)
        self.trunkbtn_hbox = QtWidgets.QHBoxLayout()
        self.trunkbtn_hbox.setObjectName("trunkbtn_hbox")
        self.trunkbtn_1 = QtWidgets.QRadioButton(self.trunk_groupbox)
        self.trunkbtn_1.setObjectName("trunkbtn_1")
        self.trunkbtn_hbox.addWidget(self.trunkbtn_1, 0, QtCore.Qt.AlignHCenter)
        self.trunkbtn_2 = QtWidgets.QRadioButton(self.trunk_groupbox)
        self.trunkbtn_2.setObjectName("trunkbtn_2")
        self.trunkbtn_hbox.addWidget(self.trunkbtn_2, 0, QtCore.Qt.AlignHCenter)
        self.trunkbtn_3 = QtWidgets.QRadioButton(self.trunk_groupbox)
        self.trunkbtn_3.setObjectName("trunkbtn_3")
        self.trunkbtn_hbox.addWidget(self.trunkbtn_3, 0, QtCore.Qt.AlignHCenter)
        self.trunkbtn_4 = QtWidgets.QRadioButton(self.trunk_groupbox)
        self.trunkbtn_4.setObjectName("trunkbtn_4")
        self.trunkbtn_hbox.addWidget(self.trunkbtn_4, 0, QtCore.Qt.AlignHCenter)
        self.trunkbtn_5 = QtWidgets.QRadioButton(self.trunk_groupbox)
        self.trunkbtn_5.setObjectName("trunkbtn_5")
        self.trunkbtn_hbox.addWidget(self.trunkbtn_5, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addLayout(self.trunkbtn_hbox)
        self.verticalLayout_7.setStretch(0, 3)
        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_6.addWidget(self.trunk_groupbox)
        self.trunkadj_groupBox = QtWidgets.QGroupBox(self.page_2)
        self.trunkadj_groupBox.setObjectName("trunkadj_groupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.trunkadj_groupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.trunkadj_1 = QtWidgets.QCheckBox(self.trunkadj_groupBox)
        self.trunkadj_1.setObjectName("trunkadj_1")
        self.verticalLayout_8.addWidget(self.trunkadj_1)
        self.verticalLayout_6.addWidget(self.trunkadj_groupBox)
        self.verticalLayout_6.setStretch(1, 5)
        self.verticalLayout_6.setStretch(2, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.page3_label = QtWidgets.QLabel(self.page)
        self.page3_label.setObjectName("page3_label")
        self.verticalLayout_10.addWidget(self.page3_label, 0, QtCore.Qt.AlignHCenter)
        self.page3_splitter = QtWidgets.QSplitter(self.page)
        self.page3_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.page3_splitter.setObjectName("page3_splitter")
        self.legs_groupbox = QtWidgets.QGroupBox(self.page3_splitter)
        self.legs_groupbox.setObjectName("legs_groupbox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.legs_groupbox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.legsimg_hbox = QtWidgets.QHBoxLayout()
        self.legsimg_hbox.setObjectName("legsimg_hbox")
        self.legsimg_1 = QtWidgets.QLabel(self.legs_groupbox)
        self.legsimg_1.setStyleSheet("border-image: url(:/Legs/resource/legs/legs1.png);")
        self.legsimg_1.setText("")
        self.legsimg_1.setObjectName("legsimg_1")
        self.legsimg_hbox.addWidget(self.legsimg_1)
        self.legsimg_2 = QtWidgets.QLabel(self.legs_groupbox)
        self.legsimg_2.setStyleSheet("border-image: url(:/Legs/resource/legs/legs2.png);")
        self.legsimg_2.setText("")
        self.legsimg_2.setObjectName("legsimg_2")
        self.legsimg_hbox.addWidget(self.legsimg_2)
        self.verticalLayout_9.addLayout(self.legsimg_hbox)
        self.legsbtn_hbox = QtWidgets.QHBoxLayout()
        self.legsbtn_hbox.setObjectName("legsbtn_hbox")
        self.legsbtn_1 = QtWidgets.QRadioButton(self.legs_groupbox)
        self.legsbtn_1.setObjectName("legsbtn_1")
        self.legsbtn_hbox.addWidget(self.legsbtn_1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.legsbtn_2 = QtWidgets.QRadioButton(self.legs_groupbox)
        self.legsbtn_2.setObjectName("legsbtn_2")
        self.legsbtn_hbox.addWidget(self.legsbtn_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout_9.addLayout(self.legsbtn_hbox)
        self.verticalLayout_9.setStretch(0, 3)
        self.verticalLayout_9.setStretch(1, 1)
        self.legsadj_groupbox = QtWidgets.QGroupBox(self.page3_splitter)
        self.legsadj_groupbox.setObjectName("legsadj_groupbox")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.legsadj_groupbox)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.legsadjimg_hbox = QtWidgets.QHBoxLayout()
        self.legsadjimg_hbox.setObjectName("legsadjimg_hbox")
        self.legsimg_3 = QtWidgets.QLabel(self.legsadj_groupbox)
        self.legsimg_3.setStyleSheet("border-image: url(:/Legs/resource/legs/legs3.png);")
        self.legsimg_3.setText("")
        self.legsimg_3.setObjectName("legsimg_3")
        self.legsadjimg_hbox.addWidget(self.legsimg_3)
        self.legsimg_4 = QtWidgets.QLabel(self.legsadj_groupbox)
        self.legsimg_4.setStyleSheet("border-image: url(:/Legs/resource/legs/legs4.png);")
        self.legsimg_4.setText("")
        self.legsimg_4.setObjectName("legsimg_4")
        self.legsadjimg_hbox.addWidget(self.legsimg_4)
        self.legsimg_5 = QtWidgets.QLabel(self.legsadj_groupbox)
        self.legsimg_5.setStyleSheet("border-image: url(:/Legs/resource/legs/legs5.png);")
        self.legsimg_5.setText("")
        self.legsimg_5.setObjectName("legsimg_5")
        self.legsadjimg_hbox.addWidget(self.legsimg_5)
        self.verticalLayout_13.addLayout(self.legsadjimg_hbox)
        self.legsadjbtn_hbox = QtWidgets.QHBoxLayout()
        self.legsadjbtn_hbox.setObjectName("legsadjbtn_hbox")
        self.legsadj_1 = QtWidgets.QRadioButton(self.legsadj_groupbox)
        self.legsadj_1.setObjectName("legsadj_1")
        self.legsadjbtn_hbox.addWidget(self.legsadj_1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.legsadj_2 = QtWidgets.QRadioButton(self.legsadj_groupbox)
        self.legsadj_2.setObjectName("legsadj_2")
        self.legsadjbtn_hbox.addWidget(self.legsadj_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.legsadj_3 = QtWidgets.QRadioButton(self.legsadj_groupbox)
        self.legsadj_3.setObjectName("legsadj_3")
        self.legsadjbtn_hbox.addWidget(self.legsadj_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout_13.addLayout(self.legsadjbtn_hbox)
        self.verticalLayout_13.setStretch(0, 3)
        self.verticalLayout_13.setStretch(1, 1)
        self.verticalLayout_10.addWidget(self.page3_splitter)
        self.verticalLayout_10.setStretch(1, 2)
        self.stackedWidget.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.page4_label = QtWidgets.QLabel(self.page_4)
        self.page4_label.setObjectName("page4_label")
        self.verticalLayout_11.addWidget(self.page4_label, 0, QtCore.Qt.AlignHCenter)
        self.upperarm_groupbox = QtWidgets.QGroupBox(self.page_4)
        self.upperarm_groupbox.setObjectName("upperarm_groupbox")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.upperarm_groupbox)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.upperarmimg_hbox = QtWidgets.QHBoxLayout()
        self.upperarmimg_hbox.setObjectName("upperarmimg_hbox")
        self.upperarmimg_1 = QtWidgets.QLabel(self.upperarm_groupbox)
        self.upperarmimg_1.setStyleSheet("border-image: url(:/Upper Arm/resource/upperarms/upperarms1.png);")
        self.upperarmimg_1.setText("")
        self.upperarmimg_1.setObjectName("upperarmimg_1")
        self.upperarmimg_hbox.addWidget(self.upperarmimg_1)
        self.upperarmimg_2 = QtWidgets.QLabel(self.upperarm_groupbox)
        self.upperarmimg_2.setStyleSheet("border-image: url(:/Upper Arm/resource/upperarms/upperarms2.png);")
        self.upperarmimg_2.setText("")
        self.upperarmimg_2.setObjectName("upperarmimg_2")
        self.upperarmimg_hbox.addWidget(self.upperarmimg_2)
        self.upperarmimg_3 = QtWidgets.QLabel(self.upperarm_groupbox)
        self.upperarmimg_3.setStyleSheet("border-image: url(:/Upper Arm/resource/upperarms/upperarms3.png);")
        self.upperarmimg_3.setText("")
        self.upperarmimg_3.setObjectName("upperarmimg_3")
        self.upperarmimg_hbox.addWidget(self.upperarmimg_3)
        self.upperarmimg_4 = QtWidgets.QLabel(self.upperarm_groupbox)
        self.upperarmimg_4.setStyleSheet("border-image: url(:/Upper Arm/resource/upperarms/upperarms4.png);")
        self.upperarmimg_4.setText("")
        self.upperarmimg_4.setObjectName("upperarmimg_4")
        self.upperarmimg_hbox.addWidget(self.upperarmimg_4)
        self.upperarmimg_5 = QtWidgets.QLabel(self.upperarm_groupbox)
        self.upperarmimg_5.setStyleSheet("border-image: url(:/Upper Arm/resource/upperarms/upperarms5.png);")
        self.upperarmimg_5.setText("")
        self.upperarmimg_5.setObjectName("upperarmimg_5")
        self.upperarmimg_hbox.addWidget(self.upperarmimg_5)
        self.verticalLayout_12.addLayout(self.upperarmimg_hbox)
        self.upperarmbtn_hbox = QtWidgets.QHBoxLayout()
        self.upperarmbtn_hbox.setObjectName("upperarmbtn_hbox")
        self.upperarmbtn_1 = QtWidgets.QRadioButton(self.upperarm_groupbox)
        self.upperarmbtn_1.setObjectName("upperarmbtn_1")
        self.upperarmbtn_hbox.addWidget(self.upperarmbtn_1, 0, QtCore.Qt.AlignHCenter)
        self.upperarmbtn_2 = QtWidgets.QRadioButton(self.upperarm_groupbox)
        self.upperarmbtn_2.setObjectName("upperarmbtn_2")
        self.upperarmbtn_hbox.addWidget(self.upperarmbtn_2, 0, QtCore.Qt.AlignHCenter)
        self.upperarmbtn_3 = QtWidgets.QRadioButton(self.upperarm_groupbox)
        self.upperarmbtn_3.setObjectName("upperarmbtn_3")
        self.upperarmbtn_hbox.addWidget(self.upperarmbtn_3, 0, QtCore.Qt.AlignHCenter)
        self.upperarmbtn_4 = QtWidgets.QRadioButton(self.upperarm_groupbox)
        self.upperarmbtn_4.setObjectName("upperarmbtn_4")
        self.upperarmbtn_hbox.addWidget(self.upperarmbtn_4, 0, QtCore.Qt.AlignHCenter)
        self.upperarmbtn_5 = QtWidgets.QRadioButton(self.upperarm_groupbox)
        self.upperarmbtn_5.setAutoFillBackground(False)
        self.upperarmbtn_5.setStyleSheet("")
        self.upperarmbtn_5.setObjectName("upperarmbtn_5")
        self.upperarmbtn_hbox.addWidget(self.upperarmbtn_5, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_12.addLayout(self.upperarmbtn_hbox)
        self.verticalLayout_12.setStretch(0, 3)
        self.verticalLayout_12.setStretch(1, 1)
        self.verticalLayout_11.addWidget(self.upperarm_groupbox)
        self.upperarmadj_groupbox = QtWidgets.QGroupBox(self.page_4)
        self.upperarmadj_groupbox.setObjectName("upperarmadj_groupbox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.upperarmadj_groupbox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.upperarmadj_1 = QtWidgets.QCheckBox(self.upperarmadj_groupbox)
        self.upperarmadj_1.setObjectName("upperarmadj_1")
        self.horizontalLayout_2.addWidget(self.upperarmadj_1)
        self.upperarmadj_2 = QtWidgets.QCheckBox(self.upperarmadj_groupbox)
        self.upperarmadj_2.setObjectName("upperarmadj_2")
        self.horizontalLayout_2.addWidget(self.upperarmadj_2)
        self.upperarmadj_3 = QtWidgets.QCheckBox(self.upperarmadj_groupbox)
        self.upperarmadj_3.setObjectName("upperarmadj_3")
        self.horizontalLayout_2.addWidget(self.upperarmadj_3)
        self.verticalLayout_11.addWidget(self.upperarmadj_groupbox)
        self.verticalLayout_11.setStretch(1, 5)
        self.verticalLayout_11.setStretch(2, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.page5_label = QtWidgets.QLabel(self.page_5)
        self.page5_label.setObjectName("page5_label")
        self.verticalLayout_15.addWidget(self.page5_label, 0, QtCore.Qt.AlignHCenter)
        self.splitter = QtWidgets.QSplitter(self.page_5)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lowerarm_groupbox = QtWidgets.QGroupBox(self.splitter)
        self.lowerarm_groupbox.setObjectName("lowerarm_groupbox")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.lowerarm_groupbox)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.lowerarmimg_hbox = QtWidgets.QHBoxLayout()
        self.lowerarmimg_hbox.setSpacing(100)
        self.lowerarmimg_hbox.setObjectName("lowerarmimg_hbox")
        self.lowerarmimg_1 = QtWidgets.QLabel(self.lowerarm_groupbox)
        self.lowerarmimg_1.setStyleSheet("border-image: url(:/Lower Arm/resource/lowerarms/lowerarms1.png);")
        self.lowerarmimg_1.setText("")
        self.lowerarmimg_1.setObjectName("lowerarmimg_1")
        self.lowerarmimg_hbox.addWidget(self.lowerarmimg_1)
        self.lowerarmimg_2 = QtWidgets.QLabel(self.lowerarm_groupbox)
        self.lowerarmimg_2.setStyleSheet("border-image: url(:/Lower Arm/resource/lowerarms/lowerarms2.png);")
        self.lowerarmimg_2.setText("")
        self.lowerarmimg_2.setObjectName("lowerarmimg_2")
        self.lowerarmimg_hbox.addWidget(self.lowerarmimg_2)
        self.verticalLayout_16.addLayout(self.lowerarmimg_hbox)
        self.lowerarmbtn_hbox = QtWidgets.QHBoxLayout()
        self.lowerarmbtn_hbox.setObjectName("lowerarmbtn_hbox")
        self.lowerarmbtn_1 = QtWidgets.QRadioButton(self.lowerarm_groupbox)
        self.lowerarmbtn_1.setObjectName("lowerarmbtn_1")
        self.lowerarmbtn_hbox.addWidget(self.lowerarmbtn_1, 0, QtCore.Qt.AlignHCenter)
        self.lowerarmbtn_2 = QtWidgets.QRadioButton(self.lowerarm_groupbox)
        self.lowerarmbtn_2.setObjectName("lowerarmbtn_2")
        self.lowerarmbtn_hbox.addWidget(self.lowerarmbtn_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_16.addLayout(self.lowerarmbtn_hbox)
        self.verticalLayout_16.setStretch(0, 3)
        self.verticalLayout_16.setStretch(1, 1)
        self.verticalLayout_15.addWidget(self.splitter)
        self.verticalLayout_15.setStretch(1, 5)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.page6_label = QtWidgets.QLabel(self.page_6)
        self.page6_label.setObjectName("page6_label")
        self.verticalLayout_14.addWidget(self.page6_label, 0, QtCore.Qt.AlignHCenter)
        self.wrist_groupbox = QtWidgets.QGroupBox(self.page_6)
        self.wrist_groupbox.setObjectName("wrist_groupbox")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.wrist_groupbox)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.wristimg_hbox = QtWidgets.QHBoxLayout()
        self.wristimg_hbox.setSpacing(100)
        self.wristimg_hbox.setObjectName("wristimg_hbox")
        self.wristimg_1 = QtWidgets.QLabel(self.wrist_groupbox)
        self.wristimg_1.setStyleSheet("border-image: url(:/Wrist/resource/wrist/wrist1.png);")
        self.wristimg_1.setText("")
        self.wristimg_1.setObjectName("wristimg_1")
        self.wristimg_hbox.addWidget(self.wristimg_1)
        self.wristimg_2 = QtWidgets.QLabel(self.wrist_groupbox)
        self.wristimg_2.setStyleSheet("border-image: url(:/Wrist/resource/wrist/wrist2.png);")
        self.wristimg_2.setText("")
        self.wristimg_2.setObjectName("wristimg_2")
        self.wristimg_hbox.addWidget(self.wristimg_2)
        self.verticalLayout_17.addLayout(self.wristimg_hbox)
        self.wristbtn_hbox = QtWidgets.QHBoxLayout()
        self.wristbtn_hbox.setObjectName("wristbtn_hbox")
        self.wristbtn_1 = QtWidgets.QRadioButton(self.wrist_groupbox)
        self.wristbtn_1.setObjectName("wristbtn_1")
        self.wristbtn_hbox.addWidget(self.wristbtn_1, 0, QtCore.Qt.AlignHCenter)
        self.wristbtn_2 = QtWidgets.QRadioButton(self.wrist_groupbox)
        self.wristbtn_2.setObjectName("wristbtn_2")
        self.wristbtn_hbox.addWidget(self.wristbtn_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_17.addLayout(self.wristbtn_hbox)
        self.verticalLayout_17.setStretch(0, 3)
        self.verticalLayout_17.setStretch(1, 1)
        self.verticalLayout_14.addWidget(self.wrist_groupbox)
        self.wrist_groupbox_2 = QtWidgets.QGroupBox(self.page_6)
        self.wrist_groupbox_2.setObjectName("wrist_groupbox_2")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.wrist_groupbox_2)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.wristadj_1 = QtWidgets.QCheckBox(self.wrist_groupbox_2)
        self.wristadj_1.setObjectName("wristadj_1")
        self.verticalLayout_22.addWidget(self.wristadj_1)
        self.verticalLayout_14.addWidget(self.wrist_groupbox_2)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.page_7)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.page7_label = QtWidgets.QLabel(self.page_7)
        self.page7_label.setObjectName("page7_label")
        self.verticalLayout_19.addWidget(self.page7_label, 0, QtCore.Qt.AlignHCenter)
        self.forceload_groupbox = QtWidgets.QGroupBox(self.page_7)
        self.forceload_groupbox.setObjectName("forceload_groupbox")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.forceload_groupbox)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.forcebtn_hbox = QtWidgets.QHBoxLayout()
        self.forcebtn_hbox.setObjectName("forcebtn_hbox")
        self.forcebtn_1 = QtWidgets.QRadioButton(self.forceload_groupbox)
        self.forcebtn_1.setObjectName("forcebtn_1")
        self.forcebtn_hbox.addWidget(self.forcebtn_1)
        self.forcebtn_2 = QtWidgets.QRadioButton(self.forceload_groupbox)
        self.forcebtn_2.setObjectName("forcebtn_2")
        self.forcebtn_hbox.addWidget(self.forcebtn_2)
        self.forcebtn_3 = QtWidgets.QRadioButton(self.forceload_groupbox)
        self.forcebtn_3.setObjectName("forcebtn_3")
        self.forcebtn_hbox.addWidget(self.forcebtn_3)
        self.verticalLayout_18.addLayout(self.forcebtn_hbox)
        self.forceadj_1 = QtWidgets.QCheckBox(self.forceload_groupbox)
        self.forceadj_1.setObjectName("forceadj_1")
        self.verticalLayout_18.addWidget(self.forceadj_1)
        self.verticalLayout_19.addWidget(self.forceload_groupbox)
        self.coupling_groupbox = QtWidgets.QGroupBox(self.page_7)
        self.coupling_groupbox.setObjectName("coupling_groupbox")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.coupling_groupbox)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.couplingbtn_1 = QtWidgets.QRadioButton(self.coupling_groupbox)
        self.couplingbtn_1.setObjectName("couplingbtn_1")
        self.horizontalLayout.addWidget(self.couplingbtn_1)
        self.couplingbtn_2 = QtWidgets.QRadioButton(self.coupling_groupbox)
        self.couplingbtn_2.setObjectName("couplingbtn_2")
        self.horizontalLayout.addWidget(self.couplingbtn_2)
        self.couplingbtn_3 = QtWidgets.QRadioButton(self.coupling_groupbox)
        self.couplingbtn_3.setObjectName("couplingbtn_3")
        self.horizontalLayout.addWidget(self.couplingbtn_3)
        self.couplingbtn_4 = QtWidgets.QRadioButton(self.coupling_groupbox)
        self.couplingbtn_4.setObjectName("couplingbtn_4")
        self.horizontalLayout.addWidget(self.couplingbtn_4)
        self.verticalLayout_21.addLayout(self.horizontalLayout)
        self.verticalLayout_19.addWidget(self.coupling_groupbox)
        self.activity_groupbox = QtWidgets.QGroupBox(self.page_7)
        self.activity_groupbox.setObjectName("activity_groupbox")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.activity_groupbox)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.activity_hbox = QtWidgets.QVBoxLayout()
        self.activity_hbox.setObjectName("activity_hbox")
        self.activitybtn_1 = QtWidgets.QCheckBox(self.activity_groupbox)
        self.activitybtn_1.setObjectName("activitybtn_1")
        self.activity_hbox.addWidget(self.activitybtn_1)
        self.activitybtn_2 = QtWidgets.QCheckBox(self.activity_groupbox)
        self.activitybtn_2.setObjectName("activitybtn_2")
        self.activity_hbox.addWidget(self.activitybtn_2)
        self.activitybtn_3 = QtWidgets.QCheckBox(self.activity_groupbox)
        self.activitybtn_3.setObjectName("activitybtn_3")
        self.activity_hbox.addWidget(self.activitybtn_3)
        self.verticalLayout_20.addLayout(self.activity_hbox)
        self.verticalLayout_19.addWidget(self.activity_groupbox)
        self.verticalLayout_19.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page_7)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.activitybtn_hbox = QtWidgets.QHBoxLayout()
        self.activitybtn_hbox.setSpacing(20)
        self.activitybtn_hbox.setObjectName("activitybtn_hbox")
        self.clearbtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.clearbtn.setStyleSheet("QPushButton {\n"
"    background-color: #ded9ee; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #cbc1ee;\n"
"}")
        self.clearbtn.setObjectName("clearbtn")
        self.activitybtn_hbox.addWidget(self.clearbtn)
        self.historybtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.historybtn.setStyleSheet("QPushButton {\n"
"    background-color: #ded9ee; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #cbc1ee;\n"
"}")
        self.historybtn.setObjectName("historybtn")
        self.activitybtn_hbox.addWidget(self.historybtn)
        self.calculatebtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.calculatebtn.setStyleSheet("QPushButton {\n"
"    background-color: #ded9ee; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #cbc1ee;\n"
"}")
        self.calculatebtn.setObjectName("calculatebtn")
        self.activitybtn_hbox.addWidget(self.calculatebtn)
        self.pagechange_hbox = QtWidgets.QHBoxLayout()
        self.pagechange_hbox.setSpacing(3)
        self.pagechange_hbox.setObjectName("pagechange_hbox")
        self.prevBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.prevBtn.setStyleSheet("QPushButton {\n"
"    background-color: #ded9ee; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #cbc1ee;\n"
"}")
        self.prevBtn.setObjectName("prevBtn")
        self.pagechange_hbox.addWidget(self.prevBtn)
        self.nextBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.nextBtn.setStyleSheet("QPushButton {\n"
"    background-color: #ded9ee; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #cbc1ee;\n"
"}")
        self.nextBtn.setObjectName("nextBtn")
        self.pagechange_hbox.addWidget(self.nextBtn)
        self.activitybtn_hbox.addLayout(self.pagechange_hbox)
        self.activitybtn_hbox.setStretch(0, 1)
        self.activitybtn_hbox.setStretch(1, 1)
        self.activitybtn_hbox.setStretch(2, 3)
        self.activitybtn_hbox.setStretch(3, 1)
        self.verticalLayout_2.addLayout(self.activitybtn_hbox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.page1_label.setText(_translate("Form", "1"))
        self.neck_groupbox.setTitle(_translate("Form", "Neck"))
        self.neckbtn_1.setText(_translate("Form", "0-20° Flexion"))
        self.neckbtn_2.setText(_translate("Form", "in Extension"))
        self.neckbtn_3.setText(_translate("Form", "20° Flexion"))
        self.neckadj_groupBox.setTitle(_translate("Form", "Adjustment"))
        self.neck_adjbtn_1.setText(_translate("Form", "Twisted or Side-Bending"))
        self.page2_label.setText(_translate("Form", "2"))
        self.trunk_groupbox.setTitle(_translate("Form", "Trunk"))
        self.trunkbtn_1.setText(_translate("Form", "Standing Still"))
        self.trunkbtn_2.setText(_translate("Form", "in Extension"))
        self.trunkbtn_3.setText(_translate("Form", "0°-20° Flexion"))
        self.trunkbtn_4.setText(_translate("Form", "20°-60° Flexion"))
        self.trunkbtn_5.setText(_translate("Form", ">60° Flexion"))
        self.trunkadj_groupBox.setTitle(_translate("Form", "Adjustment"))
        self.trunkadj_1.setText(_translate("Form", "Twisted or Side Bending"))
        self.page3_label.setText(_translate("Form", "3"))
        self.legs_groupbox.setTitle(_translate("Form", "Legs"))
        self.legsbtn_1.setText(_translate("Form", "Balanced"))
        self.legsbtn_2.setText(_translate("Form", "Unbalanced"))
        self.legsadj_groupbox.setTitle(_translate("Form", "Adjustment"))
        self.legsadj_1.setText(_translate("Form", "None"))
        self.legsadj_2.setText(_translate("Form", "30°-60° Degrees Flexion"))
        self.legsadj_3.setText(_translate("Form", ">60° Flexion"))
        self.page4_label.setText(_translate("Form", "4"))
        self.upperarm_groupbox.setTitle(_translate("Form", "Upper Arm"))
        self.upperarmbtn_1.setText(_translate("Form", "0°-20° Extension/Flexion"))
        self.upperarmbtn_2.setText(_translate("Form", ">20° Extension"))
        self.upperarmbtn_3.setText(_translate("Form", "20°-45° Flexion"))
        self.upperarmbtn_4.setText(_translate("Form", "45°-90° Flexion"))
        self.upperarmbtn_5.setText(_translate("Form", ">90° Flexion"))
        self.upperarmadj_groupbox.setTitle(_translate("Form", "Adjustment"))
        self.upperarmadj_1.setText(_translate("Form", "Abducted Upper Arm"))
        self.upperarmadj_2.setText(_translate("Form", "Raised Shoulder"))
        self.upperarmadj_3.setText(_translate("Form", "Supported Arm/Leaning Position"))
        self.page5_label.setText(_translate("Form", "5"))
        self.lowerarm_groupbox.setTitle(_translate("Form", "Lower Arm"))
        self.lowerarmbtn_1.setText(_translate("Form", "60°-100° Flexion"))
        self.lowerarmbtn_2.setText(_translate("Form", "<60° Flex/>100°Flex"))
        self.page6_label.setText(_translate("Form", "6"))
        self.wrist_groupbox.setTitle(_translate("Form", "Wrist"))
        self.wristbtn_1.setText(_translate("Form", "0°-15° Extend/Flex"))
        self.wristbtn_2.setText(_translate("Form", ">15° Extend/Flex"))
        self.wrist_groupbox_2.setTitle(_translate("Form", "Adjustment"))
        self.wristadj_1.setText(_translate("Form", "Bent Wrist"))
        self.page7_label.setText(_translate("Form", "7"))
        self.forceload_groupbox.setTitle(_translate("Form", "Force/Load  Score"))
        self.forcebtn_1.setText(_translate("Form", "<5 kg"))
        self.forcebtn_2.setText(_translate("Form", "5-10 kg"))
        self.forcebtn_3.setText(_translate("Form", ">10  kg"))
        self.forceadj_1.setText(_translate("Form", "Shock Force, Rapid Buildup, or Sudden Exertion"))
        self.coupling_groupbox.setTitle(_translate("Form", "Coupling"))
        self.couplingbtn_1.setText(_translate("Form", "Good Handling"))
        self.couplingbtn_2.setText(_translate("Form", "Acceptable Handling"))
        self.couplingbtn_3.setText(_translate("Form", "Poor Handling"))
        self.couplingbtn_4.setText(_translate("Form", "Unacceptable Handling"))
        self.activity_groupbox.setTitle(_translate("Form", "Activity Score"))
        self.activitybtn_1.setText(_translate("Form", "1 or more body parts are held for longer than 1 minute (static)"))
        self.activitybtn_2.setText(_translate("Form", "Repeated small range actions, such as repeating an action more than 4x per minute (except walking)"))
        self.activitybtn_3.setText(_translate("Form", "Action causes rapid large range changes in posture or unstable base"))
        self.clearbtn.setText(_translate("Form", "Clear"))
        self.historybtn.setText(_translate("Form", "Show History"))
        self.calculatebtn.setText(_translate("Form", "Calculate REBA Score"))
        self.prevBtn.setText(_translate("Form", "<<<"))
        self.nextBtn.setText(_translate("Form", ">>>"))
import resources_from_qt_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
