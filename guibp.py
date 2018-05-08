# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './guibp.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import serial
ser = serial.Serial('/dev/ttyUSB1', 9600)

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
        self.btnOpen.setGeometry(QtCore.QRect(290, 400, 99, 27))
        self.btnOpen.setObjectName(_fromUtf8("btnOpen"))
        self.txtsys = QtGui.QLineEdit(self.centralwidget)
        self.txtsys.setGeometry(QtCore.QRect(300, 50, 113, 27))
        self.txtsys.setObjectName(_fromUtf8("txtsys"))
        self.btnClose = QtGui.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(140, 400, 99, 27))
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.txtDias = QtGui.QLineEdit(self.centralwidget)
        self.txtDias.setGeometry(QtCore.QRect(300, 80, 113, 27))
        self.txtDias.setObjectName(_fromUtf8("txtDias"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 90, 68, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 50, 68, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btnRead = QtGui.QPushButton(self.centralwidget)
        self.btnRead.setGeometry(QtCore.QRect(290, 180, 99, 27))
        self.btnRead.setObjectName(_fromUtf8("btnRead"))
        self.txtPulso = QtGui.QLineEdit(self.centralwidget)
        self.txtPulso.setGeometry(QtCore.QRect(300, 120, 113, 27))
        self.txtPulso.setObjectName(_fromUtf8("txtPulso"))
        self.lblpulso = QtGui.QLabel(self.centralwidget)
        self.lblpulso.setGeometry(QtCore.QRect(190, 120, 68, 17))
        self.lblpulso.setObjectName(_fromUtf8("lblpulso"))
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
            datos = list(data)
            datos = bytes(datos).decode('utf8')
            print(datos)
            siastolica = datos[1] + datos[2] + datos[3]
            temp = str(datos[3])
            diastolica = datos[6] + datos[7] + datos[8]
            pulso = datos[11] + datos[12] + datos[13]
            self.txtsys.setText(_translate("MainWindow", siastolica, None))
            self.txtDias.setText(_translate("MainWindow", diastolica, None))
            self.txtPulso.setText(_translate("MainWindow", pulso, None))

    def close(self):
            ser.close()
            print("closed")

    def open(self):
            ser.open()

    print("opened")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnOpen.setText(_translate("MainWindow", "Open Port", None))
        self.txtsys.setText(_translate("MainWindow", "0", None))
        self.btnClose.setText(_translate("MainWindow", "Close Port", None))
        self.txtDias.setText(_translate("MainWindow", "0", None))
        self.label.setText(_translate("MainWindow", "Diastolic", None))
        self.label_2.setText(_translate("MainWindow", "Systolic", None))
        self.btnRead.setText(_translate("MainWindow", "Leer", None))
        self.txtPulso.setText(_translate("MainWindow", "0", None))
        self.lblpulso.setText(_translate("MainWindow", "Pulse", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

