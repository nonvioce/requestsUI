import requests as req
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication,QLineEdit,QComboBox,QTextEdit,QLabel)

class MainUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lable1=QLabel('鍦板潃:',self)
        lable2=QLabel('瑙ｆ瀽鏂瑰紡:',self)
        lablef1=QLabel('',self)


        self.urlInputLineEdit=QLineEdit(self)
        self.outputTypeCombox=QComboBox(self)
        self.outputTypeCombox.addItem('Text')
        self.outputTypeCombox.addItem('Json')
        self.outputTypeCombox.addItem('Raw')
        self.outputTextEdit=QTextEdit(self)
        self.OKButton=QPushButton('OK')

        self.OKButton.clicked.connect(self.OKClicked)

        vbox0=QVBoxLayout()
        vbox1=QVBoxLayout()
        vbox2=QVBoxLayout()
        #vbox1.addStretch(1)
        vbox2.addStretch(1)
        vbox0.addWidget(lable1)
        vbox0.addWidget(lable2)
        vbox0.addWidget(lablef1)
        vbox1.addWidget(self.urlInputLineEdit)
        vbox1.addWidget(self.outputTypeCombox)
        vbox1.addWidget(self.OKButton)
        vbox2.addWidget(self.outputTextEdit)

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox0)
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        self.setLayout(hbox)

        #self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Requests')
        self.show()

    def OKClicked(self):
        self.outputTextEdit.setPlainText(self.getUrl(self.urlInputLineEdit.text(),self.outputTypeCombox.currentIndex()))

    def getUrl(self,url,ouputType):
        try:
            r=req.get(url,stream=True)
            if ouputType==0:
                return '璇锋眰鐘舵€佺爜:'+str(r.status_code)+'\n'+r.text
            if ouputType==1:
                try:
                   return '璇锋眰鐘舵€佺爜:'+str(r.status_code)+'\n'+str(r.json())
                except:
                   return '璇锋眰鐘舵€佺爜:'+str(r.status_code)+'\n'+'鏃犳硶鐢╦son瑙ｆ瀽'
            if ouputType==2:
                return '璇锋眰鐘舵€佺爜:'+str(r.status_code)+'\n'+str(r.raw)+'\n'+str(r.raw.read())
        except:
            return "璇疯緭鍏ュ悎娉曠殑閾炬帴\n(闇€瑕佷互http://鎴杊ttps://寮€澶?"





if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainUI()
    sys.exit(app.exec_())
