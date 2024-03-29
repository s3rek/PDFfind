from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import re, os
import tkFileDialog as filedialog
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
from gui3 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        #self.ui = uic.loadUi('gui.ui', self)
        self.ui.setupUi(self)
        self.thread = Worker()
        #self.ui.closeButton.clicked.connect(self.thread.stop)
        self.ui.pushButton.clicked.connect(self.choosePath)
        self.ui.WholeWordSwitch.clicked.connect(self.WholeWord)
        self.ui.CaseSwitch.clicked.connect(self.MatchCase)
        self.ui.RexExSwitch.clicked.connect(self.RegEx)
        self.ui.WynTable.cellClicked.connect(self.OpenFile)

        self.connect(self.ui.closeButton, SIGNAL("clicked()"), self.thread.stop)
        self.connect(self.ui.SearchButt, SIGNAL("clicked()"), self.danedostart)
        self.connect(self.thread, SIGNAL("output(PyQt_PyObject)"), self.populateTable)
        self.connect(self.thread, SIGNAL("noresult(PyQt_PyObject)"), self.PopUp)

    def choosePath(self):
        foldername = unicode(QFileDialog.getExistingDirectory(self, "Wybierz katalog"))
        print foldername
        self.ui.lineEdit.setText(foldername)

    def WholeWord(self):
        if self.ui.WholeWordSwitch.isChecked():
            wholeWord=True
        else:
            wholeWord=False
        print "WholeWord is %s" % wholeWord
        return wholeWord

    def RegEx(self):
        if self.ui.RexExSwitch.isChecked():
            regex=True
        else:
            regex=False
        print "RegEx is %s" % regex
        return regex

    def MatchCase(self):
        if self.ui.CaseSwitch.isChecked():
            caseSense=True
        else:
            caseSense=False
        print "MatchCase is %s" % caseSense
        return caseSense

    def MaxDepth(self):
        index = self.ui.depthField.currentIndex()
        if index == 6:
            maxdepth = 999
        else:
            maxdepth = index
        return maxdepth

    def populateTable(self, listaplik):
        self.ui.WynTable.setRowCount(len(listaplik))
        print len(listaplik)
        i=0
        for key,value in listaplik.iteritems():
            #print key,value
            plik=QTableWidgetItem(key)
            strona=QTableWidgetItem(str(value))
            self.ui.WynTable.setItem(i,0,plik)
            self.ui.WynTable.setItem(i,1,strona)
            i+=1

    def PopUp(self, listaplik):
        if listaplik=={}:
            QMessageBox.about(QMainWindow(), "Uwaga!","Nie znaleziono frazy.")

    def OpenFile(self,row, column):
        filepath= unicode(self.ui.WynTable.item(row, column).text())
        print filepath
        os.startfile(r'"'+filepath+r'"')


    def danedostart(self):
        phrase = unicode(self.ui.lineEdit_2.text())
        path=self.ui.lineEdit.text()
        maxdepth =self.MaxDepth()
        self.thread.runs= True
        self.thread.ruszaj(phrase, path, self.WholeWord(), self.RegEx(), self.MatchCase(), maxdepth)


class Worker(QThread):

    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.exiting = False #usunac?????
        self.runs = True

    def stop(self):
        self.runs = False

    def ruszaj(self, phrase, path, wholeword, regex, casesense, maxdepth):
        self.phrase = phrase
        self.path = path
        self.casesense = casesense
        self.regex = regex
        self.wholeword = wholeword
        self.maxdepth = maxdepth
        self.start()

    def run(self):
        listaplik={}
        print self.phrase
        for root,dirs,files in os.walk(unicode(self.path)):
            print root
            if root.count(os.sep) >= self.maxdepth+self.path.count(os.sep):
                del dirs[:]
            for name in files:
                sciezka =os.path.join(root, name)
                if sciezka.endswith(".pdf") and self.runs:
                        self.convert_pdf_to_txt(sciezka, self.phrase, listaplik)
                        self.emit(SIGNAL("output(PyQt_PyObject)"),listaplik)
        print listaplik
        self.emit(SIGNAL("noresult(PyQt_PyObject)"),listaplik)

    def convert_pdf_to_txt(self, path, phrase, listaplik):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = file(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = False
        pagenos=set()
    
        listapage=[]
        pagenum=0
        text=""
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            pagenum+=1
            print pagenum
            interpreter.process_page(page)
            starytextlen = len(text)
            text = retstr.getvalue()
            nowytextlen=len(text)
            if starytextlen != 0:
                przec=starytextlen-nowytextlen
            else:
                przec=0
            wyn = self.Searcher(phrase, text[przec:].decode("utf-8"), self.wholeword, self.regex, self.casesense)
            if wyn:
                listapage.append(pagenum)
                listaplik.update({path:listapage})

        fp.close()
        device.close()
        retstr.close()
     

    def Searcher(self, phrase, text, wholeWord, regex, caseSense):
        flags=re.UNICODE
        print ("caseSense : %s" % caseSense)
        print ("regex : %s" % regex)
        print ("wholeword : %s" % wholeWord)
        if caseSense is False:
            flags |= re.IGNORECASE
        else:
            pass
        if wholeWord is True:
            phrase=r'\b'+phrase+r'\b'
        else:
            pass
        if regex is False:
            phrase=re.escape(phrase)
            query=re.compile(phrase, flags)
            wyn=query.findall(text)
        else:
            query=re.compile(phrase, flags)
            wyn=query.findall(text)
        try:
            print wyn.group(0)
        except:
            pass
        print wyn
        return wyn



if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())