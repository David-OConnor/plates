# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\David\Desktop\Programming\Seymour Plates\seymour_plates_gui.ui'
#
# Created: Sat Apr 27 17:57:14 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName(_fromUtf8("Main"))
        Main.resize(588, 310)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/MyPrefix/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        Main.setStatusTip(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(Main)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.download_btn = QtGui.QPushButton(self.centralwidget)
        self.download_btn.setGeometry(QtCore.QRect(180, 200, 221, 51))
        self.download_btn.setObjectName(_fromUtf8("download_btn"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 160, 341, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 7, 563, 146))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.cb5 = QtGui.QCheckBox(self.layoutWidget)
        self.cb5.setChecked(True)
        self.cb5.setObjectName(_fromUtf8("cb5"))
        self.gridLayout_3.addWidget(self.cb5, 1, 1, 1, 1)
        self.cb9 = QtGui.QCheckBox(self.layoutWidget)
        self.cb9.setChecked(True)
        self.cb9.setObjectName(_fromUtf8("cb9"))
        self.gridLayout_3.addWidget(self.cb9, 2, 1, 1, 1)
        self.cb14 = QtGui.QCheckBox(self.layoutWidget)
        self.cb14.setChecked(True)
        self.cb14.setObjectName(_fromUtf8("cb14"))
        self.gridLayout_3.addWidget(self.cb14, 3, 2, 1, 1)
        self.cb8 = QtGui.QCheckBox(self.layoutWidget)
        self.cb8.setChecked(True)
        self.cb8.setObjectName(_fromUtf8("cb8"))
        self.gridLayout_3.addWidget(self.cb8, 2, 0, 1, 1)
        self.cb10 = QtGui.QCheckBox(self.layoutWidget)
        self.cb10.setChecked(True)
        self.cb10.setObjectName(_fromUtf8("cb10"))
        self.gridLayout_3.addWidget(self.cb10, 2, 2, 1, 1)
        self.cb7 = QtGui.QCheckBox(self.layoutWidget)
        self.cb7.setChecked(True)
        self.cb7.setObjectName(_fromUtf8("cb7"))
        self.gridLayout_3.addWidget(self.cb7, 1, 3, 1, 1)
        self.cb6 = QtGui.QCheckBox(self.layoutWidget)
        self.cb6.setChecked(True)
        self.cb6.setObjectName(_fromUtf8("cb6"))
        self.gridLayout_3.addWidget(self.cb6, 1, 2, 1, 1)
        self.cb12 = QtGui.QCheckBox(self.layoutWidget)
        self.cb12.setChecked(True)
        self.cb12.setObjectName(_fromUtf8("cb12"))
        self.gridLayout_3.addWidget(self.cb12, 3, 0, 1, 1)
        self.cb11 = QtGui.QCheckBox(self.layoutWidget)
        self.cb11.setChecked(True)
        self.cb11.setObjectName(_fromUtf8("cb11"))
        self.gridLayout_3.addWidget(self.cb11, 2, 3, 1, 1)
        self.cb1 = QtGui.QCheckBox(self.layoutWidget)
        self.cb1.setChecked(True)
        self.cb1.setObjectName(_fromUtf8("cb1"))
        self.gridLayout_3.addWidget(self.cb1, 0, 0, 1, 1)
        self.cb0 = QtGui.QCheckBox(self.layoutWidget)
        self.cb0.setChecked(True)
        self.cb0.setObjectName(_fromUtf8("cb0"))
        self.gridLayout_3.addWidget(self.cb0, 1, 0, 1, 1)
        self.cb13 = QtGui.QCheckBox(self.layoutWidget)
        self.cb13.setChecked(True)
        self.cb13.setObjectName(_fromUtf8("cb13"))
        self.gridLayout_3.addWidget(self.cb13, 3, 1, 1, 1)
        self.cb15 = QtGui.QCheckBox(self.layoutWidget)
        self.cb15.setChecked(True)
        self.cb15.setObjectName(_fromUtf8("cb15"))
        self.gridLayout_3.addWidget(self.cb15, 3, 3, 1, 1)
        self.cb2 = QtGui.QCheckBox(self.layoutWidget)
        self.cb2.setChecked(True)
        self.cb2.setObjectName(_fromUtf8("cb2"))
        self.gridLayout_3.addWidget(self.cb2, 0, 1, 1, 1)
        self.cb16 = QtGui.QCheckBox(self.layoutWidget)
        self.cb16.setChecked(True)
        self.cb16.setObjectName(_fromUtf8("cb16"))
        self.gridLayout_3.addWidget(self.cb16, 4, 0, 1, 1)
        self.cb17 = QtGui.QCheckBox(self.layoutWidget)
        self.cb17.setChecked(True)
        self.cb17.setObjectName(_fromUtf8("cb17"))
        self.gridLayout_3.addWidget(self.cb17, 4, 1, 1, 1)
        self.cb4 = QtGui.QCheckBox(self.layoutWidget)
        self.cb4.setChecked(True)
        self.cb4.setObjectName(_fromUtf8("cb4"))
        self.gridLayout_3.addWidget(self.cb4, 0, 3, 1, 1)
        self.cb3 = QtGui.QCheckBox(self.layoutWidget)
        self.cb3.setChecked(True)
        self.cb3.setObjectName(_fromUtf8("cb3"))
        self.gridLayout_3.addWidget(self.cb3, 0, 2, 1, 1)
        self.save_btn = QtGui.QPushButton(self.layoutWidget)
        self.save_btn.setObjectName(_fromUtf8("save_btn"))
        self.gridLayout_3.addWidget(self.save_btn, 4, 3, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 150, 561, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.all_btn = QtGui.QPushButton(self.centralwidget)
        self.all_btn.setGeometry(QtCore.QRect(500, 170, 61, 23))
        self.all_btn.setObjectName(_fromUtf8("all_btn"))
        self.none_btn = QtGui.QPushButton(self.centralwidget)
        self.none_btn.setGeometry(QtCore.QRect(500, 200, 61, 23))
        self.none_btn.setObjectName(_fromUtf8("none_btn"))
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        Main.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Main)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Main.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(Main)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionCombine = QtGui.QAction(Main)
        self.actionCombine.setCheckable(True)
        self.actionCombine.setChecked(True)
        self.actionCombine.setObjectName(_fromUtf8("actionCombine"))
        self.menuOptions.addAction(self.actionCombine)
        self.menuOptions.addAction(self.actionAbout)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(_translate("Main", "Seymour Plates", None))
        self.download_btn.setText(_translate("Main", "Download Plates", None))
        self.label.setText(_translate("Main", "<html><head/><body><p><span style=\" font-size:12pt;\">Plate version: Error</span></p></body></html>", None))
        self.cb5.setText(_translate("Main", "Kinston ILS 5", None))
        self.cb9.setText(_translate("Main", "Shaw HI-ILS 22R", None))
        self.cb14.setText(_translate("Main", "Langley HI-TAC 8", None))
        self.cb8.setText(_translate("Main", "Shaw HI-ILS 4L", None))
        self.cb10.setText(_translate("Main", "Shaw HI-TAC 4L", None))
        self.cb7.setText(_translate("Main", "Cherry HI-TAC Z 32L", None))
        self.cb6.setText(_translate("Main", "Cherry HI-TAC Y 32L", None))
        self.cb12.setText(_translate("Main", "Langley HI-ILS 8", None))
        self.cb11.setText(_translate("Main", "Shaw HI-TAC 22R", None))
        self.cb1.setText(_translate("Main", "Seymour HI-ILS 8", None))
        self.cb0.setText(_translate("Main", "Seymour One", None))
        self.cb13.setText(_translate("Main", "Langley HI-ILS 26", None))
        self.cb15.setText(_translate("Main", "Langley HI-TAC 26", None))
        self.cb2.setText(_translate("Main", "Seymour HI-ILS 26", None))
        self.cb16.setText(_translate("Main", "Oceana HI-TAC 5R", None))
        self.cb17.setText(_translate("Main", "Oceana HI-TAC 23L/R", None))
        self.cb4.setText(_translate("Main", "Seymour HI-TAC 26", None))
        self.cb3.setText(_translate("Main", "Seymour HI-TAC 8", None))
        self.save_btn.setText(_translate("Main", "Save selections", None))
        self.all_btn.setText(_translate("Main", "All", None))
        self.none_btn.setText(_translate("Main", "None", None))
        self.menuOptions.setTitle(_translate("Main", "Menu", None))
        self.actionAbout.setText(_translate("Main", "About", None))
        self.actionCombine.setText(_translate("Main", "Combine", None))

import seymour_plates_rc
