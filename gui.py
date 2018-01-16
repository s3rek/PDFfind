# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1228, 801)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.WynTable = QtGui.QTableWidget(self.centralwidget)
        self.WynTable.setGeometry(QtCore.QRect(20, 10, 631, 761))
        self.WynTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.WynTable.setAutoFillBackground(False)
        self.WynTable.setStyleSheet(_fromUtf8("font: 12pt \"Microsoft Sans Serif\";"))
        self.WynTable.setLineWidth(2)
        self.WynTable.setObjectName(_fromUtf8("WynTable"))
        self.WynTable.setColumnCount(2)
        self.WynTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.WynTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.WynTable.setHorizontalHeaderItem(1, item)
        self.WynTable.verticalHeader().setStretchLastSection(True)
        self.WholeWordSwitch = QtGui.QCheckBox(self.centralwidget)
        self.WholeWordSwitch.setGeometry(QtCore.QRect(680, 170, 101, 20))
        self.WholeWordSwitch.setObjectName(_fromUtf8("WholeWordSwitch"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(660, 30, 471, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.CaseSwitch = QtGui.QCheckBox(self.centralwidget)
        self.CaseSwitch.setGeometry(QtCore.QRect(680, 230, 221, 20))
        self.CaseSwitch.setObjectName(_fromUtf8("CaseSwitch"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 10, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(660, 100, 371, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.closeButton = QtGui.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(1120, 730, 93, 28))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.SearchButt = QtGui.QPushButton(self.centralwidget)
        self.SearchButt.setGeometry(QtCore.QRect(1000, 730, 93, 28))
        self.SearchButt.setObjectName(_fromUtf8("SearchButt"))
        self.RexExSwitch = QtGui.QCheckBox(self.centralwidget)
        self.RexExSwitch.setGeometry(QtCore.QRect(680, 200, 151, 20))
        self.RexExSwitch.setObjectName(_fromUtf8("RexExSwitch"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 80, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1150, 30, 31, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.WynTable.raise_()
        self.WholeWordSwitch.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.CaseSwitch.raise_()
        self.lineEdit_2.raise_()
        self.closeButton.raise_()
        self.SearchButt.raise_()
        self.RexExSwitch.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.WynTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "plik", None))
        item = self.WynTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "strony", None))
        self.WholeWordSwitch.setText(_translate("MainWindow", "Cały wyraz", None))
        self.lineEdit.setText(_translate("MainWindow", "C:\\Users\\Koty-PC\\source\\repos\\testpdf\\testpdf\\pdf", None))
        self.CaseSwitch.setText(_translate("MainWindow", "Z uwzględnieniem wielkości liter", None))
        self.label.setText(_translate("MainWindow", "Szukaj w:", None))
        self.lineEdit_2.setText(_translate("MainWindow", "si", None))
        self.closeButton.setText(_translate("MainWindow", "Anuluj", None))
        self.SearchButt.setText(_translate("MainWindow", "Szukaj", None))
        self.RexExSwitch.setText(_translate("MainWindow", "Wyrażenia regularne", None))
        self.label_2.setText(_translate("MainWindow", "Szukany wyraz:", None))
        self.pushButton.setText(_translate("MainWindow", ">", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

