# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(777, 431)
        self.closeButton = QtGui.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(650, 390, 93, 28))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.SearchButt = QtGui.QPushButton(Dialog)
        self.SearchButt.setGeometry(QtCore.QRect(530, 390, 93, 28))
        self.SearchButt.setObjectName(_fromUtf8("SearchButt"))
        self.WholeWordSwitch = QtGui.QCheckBox(Dialog)
        self.WholeWordSwitch.setGeometry(QtCore.QRect(430, 180, 101, 20))
        self.WholeWordSwitch.setObjectName(_fromUtf8("WholeWordSwitch"))
        self.RexExSwitch = QtGui.QCheckBox(Dialog)
        self.RexExSwitch.setGeometry(QtCore.QRect(430, 210, 151, 20))
        self.RexExSwitch.setObjectName(_fromUtf8("RexExSwitch"))
        self.CaseSwitch = QtGui.QCheckBox(Dialog)
        self.CaseSwitch.setGeometry(QtCore.QRect(430, 240, 221, 20))
        self.CaseSwitch.setObjectName(_fromUtf8("CaseSwitch"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(390, 30, 331, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(390, 10, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 100, 201, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(390, 80, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(730, 30, 31, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.WynTable = QtGui.QTableWidget(Dialog)
        self.WynTable.setGeometry(QtCore.QRect(10, 10, 371, 411))
        self.WynTable.setObjectName(_fromUtf8("WynTable"))
        self.WynTable.setColumnCount(0)
        self.WynTable.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.closeButton.setText(_translate("Dialog", "Anuluj", None))
        self.SearchButt.setText(_translate("Dialog", "Szukaj", None))
        self.WholeWordSwitch.setText(_translate("Dialog", "Cały wyraz", None))
        self.RexExSwitch.setText(_translate("Dialog", "Wyrażenia regularne", None))
        self.CaseSwitch.setText(_translate("Dialog", "Z uwzględnieniem wielkości liter", None))
        self.lineEdit.setText(_translate("Dialog", "C:\\Users\\Koty-PC\\source\\repos\\testpdf\\testpdf\\pdf", None))
        self.label.setText(_translate("Dialog", "Szukaj w:", None))
        self.lineEdit_2.setText(_translate("Dialog", "si", None))
        self.label_2.setText(_translate("Dialog", "Szukany wyraz:", None))
        self.pushButton.setText(_translate("Dialog", ">", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

