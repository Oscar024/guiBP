# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './guibp.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnOpen = QtGui.QPushButton(self.centralwidget)
        self.btnOpen.setGeometry(QtCore.QRect(460, 410, 99, 27))
        self.btnOpen.setObjectName(_fromUtf8("btnOpen"))
        self.txtsys = QtGui.QLineEdit(self.centralwidget)
        self.txtsys.setGeometry(QtCore.QRect(280, 260, 113, 27))
        self.txtsys.setText(_fromUtf8(""))
        self.txtsys.setObjectName(_fromUtf8("txtsys"))
        self.btnClose = QtGui.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(290, 410, 99, 27))
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.txtDias = QtGui.QLineEdit(self.centralwidget)
        self.txtDias.setGeometry(QtCore.QRect(280, 190, 113, 27))
        self.txtDias.setObjectName(_fromUtf8("txtDias"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 200, 68, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 260, 68, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btnRead = QtGui.QPushButton(self.centralwidget)
        self.btnRead.setGeometry(QtCore.QRect(370, 340, 99, 27))
        self.btnRead.setObjectName(_fromUtf8("btnRead"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btnRead, QtCore.SIGNAL(_fromUtf8("clicked()")), self.read)
        QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)
        QtCore.QObject.connect(self.btnOpen, QtCore.SIGNAL(_fromUtf8("clicked()")), self.open)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def read(self):
        data = ser.readline()
        if data:
           print(data)
        self.txtsys.setText(_translate("MainWindow", "65", None))
        self.txtDias.setText(_translate("MainWindow", "25", None))

    def close(self):
            ser.close()
            print("closed")

    def open(self):
            ser.open()
            print("opened")



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnOpen.setText(_translate("MainWindow", "Open Port", None))
        self.btnClose.setText(_translate("MainWindow", "Close Port", None))
        self.label.setText(_translate("MainWindow", "Diastolic", None))
        self.label_2.setText(_translate("MainWindow", "Systolic", None))
        self.btnRead.setText(_translate("MainWindow", "Leer", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

