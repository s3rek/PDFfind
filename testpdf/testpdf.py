from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import re, os
from Tkinter import *
import tkFileDialog as filedialog
from PyQt4.QtGui import *
from gui import Ui_Dialog

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.closeButton.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.choosePath)
        self.ui.SearchButt.clicked.connect(self.runSearch)
        self.ui.WholeWordSwitch.clicked.connect(self.WholeWord)



    def runSearch(self):
        listaplik={}
        phrase = self.ui.lineEdit_2.text()
        print phrase
        path=self.ui.lineEdit.text()
        folder=os.listdir(path)
        for plik in folder:
            #print foldername+"/"+plik
            print plik
            if plik.endswith(".pdf"):
                self.convert_pdf_to_txt(path+r"/"+plik, str(phrase), listaplik)
        print listaplik
        self.populateTable(listaplik)

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
            wyn = self.Searcher(phrase, text[przec:], self.WholeWord() )
            if wyn:
                listapage.append(pagenum)
                listaplik.update({path:listapage})

        fp.close()
        device.close()
        retstr.close()
     

    def Searcher(self, phrase, text, wholeWord):
        caseSense=False
        regexoff=False
        flag=None
        if caseSense is False:
            flag=re.IGNORECASE
        else:
            pass
        if wholeWord is True:
            phrase=r'\b'+phrase+r'\b'
        else:
            pass
        if regexoff is True:
            wyn=text.find(phrase)
            if wyn==-1:
                wyn=None
        else:
            query=re.compile(phrase, re.UNICODE or flag)
            wyn=query.findall(text)
        try:
            print wyn.group(0)
        except:
            pass
        print wyn
        return wyn

    def populateTable(self, listaplik):
        self.ui.WynTable.setRowCount(len(listaplik))
        print len(listaplik)
        self.ui.WynTable.setColumnCount(2)
        self.ui.WynTable.setHorizontalHeaderLabels(['plik','strona'])
        i=0
        for key,value in listaplik.iteritems():
            print key,value
            plik=QTableWidgetItem(key)
            strona=QTableWidgetItem(str(value))
            self.ui.WynTable.setItem(i,0,plik)
            self.ui.WynTable.setItem(i,1,strona)
            i+=1

    def choosePath(self):
        foldername = str(QFileDialog.getExistingDirectory(self, "Wybierz katalog"))
        print foldername
        self.ui.lineEdit.setText(foldername)

    def WholeWord(self):
        if self.ui.WholeWordSwitch.isChecked():
            wholeWord=True
        else:
            wholeWord=False
        print ("wholeword : %s" % wholeWord)
        return wholeWord



if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())