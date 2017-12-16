from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import re, os
import tkFileDialog as filedialog
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from gui import Ui_Dialog


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.thread = Worker()
        self.ui.closeButton.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.choosePath)
        self.ui.WholeWordSwitch.clicked.connect(self.WholeWord)
        self.ui.CaseSwitch.clicked.connect(self.MatchCase)
        self.ui.RexExSwitch.clicked.connect(self.RegEx)
        self.ui.WynTable.cellClicked.connect(self.OpenFile)

        self.connect(self.ui.SearchButt, SIGNAL("clicked()"), self.danedostart)
        self.connect(self.thread, SIGNAL("output(PyQt_PyObject)"), self.populateTable)

    def choosePath(self):
        foldername = str(QFileDialog.getExistingDirectory(self, "Wybierz katalog"))
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

    def populateTable(self, listaplik):
        self.ui.WynTable.setRowCount(len(listaplik))
        print len(listaplik)
        self.ui.WynTable.setColumnCount(2)
        self.ui.WynTable.setHorizontalHeaderLabels(['plik','strona'])
        i=0
        for key,value in listaplik.iteritems():
            #print key,value
            plik=QTableWidgetItem(key)
            strona=QTableWidgetItem(str(value))
            self.ui.WynTable.setItem(i,0,plik)
            self.ui.WynTable.setItem(i,1,strona)
            i+=1

    def OpenFile(self,row, column):
        filepath= unicode(self.ui.WynTable.item(row, column).text())
        print filepath
        os.startfile(r'"'+filepath+r'"')


    def danedostart(self):
        phrase = unicode(self.ui.lineEdit_2.text())
        path=self.ui.lineEdit.text()
        self.thread.ruszaj(phrase, path, self.WholeWord(), self.RegEx(), self.MatchCase())




class Worker(QThread):

    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.exiting = False

    def ruszaj(self, phrase, path, wholeword, regex, casesense):
        self.phrase = phrase
        self.path = path
        self.casesense = casesense
        self.regex = regex
        self.wholeword = wholeword
        self.start()


    def run(self):
        listaplik={}
        print self.phrase
        folder=os.listdir(self.path)
        for plik in folder:
            #print foldername+"/"+plik
            print plik
            if plik.endswith(".pdf"):
                self.convert_pdf_to_txt(self.path+r"/"+plik, self.phrase, listaplik)
                self.emit(SIGNAL("output(PyQt_PyObject)"),listaplik)       
        print listaplik
        #self.populateTable(listaplik)

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
            flags=re.UNICODE or re.IGNORECASE
        else:
            pass
        if wholeWord is True:
            phrase=r'\b'+phrase+r'\b'
        else:
            pass
        if regex is False:
            query=re.compile(r"("+phrase+r")", flags)
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