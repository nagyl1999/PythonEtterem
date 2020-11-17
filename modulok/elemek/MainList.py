import modulok.file as file
from PyQt4.QtGui import QListWidget, QLabel

class MainList(QListWidget):
    def __init__(self):
        super(MainList, self).__init__()
        self.id           = None
        self.main         = None
        self.last_szamla  = None
        self.last_clicked = None
        self.itemClicked.connect(self.singleClicked)
        self.itemDoubleClicked.connect(self.doubleClicked)
        self.show()

    def setID(self, id):
        self.id   = id

    def setMain(self, main):
        self.main = main

    def singleClicked(self, item):
        self.last_clicked = item

    def doubleClicked(self, item):
        if(self.id == 0):
            labels = self.main.findChildren(QLabel)
            lists  = self.main.findChildren(QListWidget)
            labels[3].setText(item.text())
            number = int(item.text().strip().split('.')[0].strip())
            self.last_szamla = number
            file.showSzamla(lists, number)
        if(self.id == 1):
            return False
        if(self.id == 2):
            lists  = self.main.findChildren(QListWidget)
            if(lists[0].last_szamla is not None):
                file.addSzamla(lists, item, lists[0].last_szamla)
            
