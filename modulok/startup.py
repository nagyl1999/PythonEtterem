import sys
from PyQt4.QtCore import Qt
from PyQt4.QtGui  import QApplication, QLabel, QVBoxLayout, QAction, QListWidget, QPushButton, QInputDialog, QIcon

import modulok.classes as classes
import modulok.elemek  as elemek
import modulok.popup   as popup
import modulok.file    as file
import modulok.payment as payment

def CreateTables(main, num):
    '''Asztalok bevitele a program indítása után'''
    if(num[1] and num[0] > 0):
        lists = main.findChildren(QListWidget)
        return file.addTablesAtStart(lists, num[0])
    else:
        return False

def CreateLayout(main_widget, layout, text, i):
    '''A három fő layout itt készül'''
    main    = elemek.MainLayout.MainLayout()
    header  = elemek.MainHeader.MainHeader()
    sub     = QLabel()
    lista   = elemek.MainList.MainList()
    cont    = elemek.MainHorizontal.MainHorizontal()
    button1 = elemek.MainButton.MainButton()
    button2 = elemek.MainButton.MainButton()
    header.setText(text.header_text)
    sub.setAlignment(Qt.AlignCenter)
    sub.setText(text.sub_text)
    lista.setID(i)
    lista.setMain(main_widget)
    button1.setText(text.button1_text)
    button2.setText(text.button2_text)
    cont.addWidget(button1)
    cont.addWidget(button2)
    main.addWidget(header)
    main.addWidget(sub)
    main.addWidget(lista)
    main.addLayout(cont)
    layout.addLayout(main)

def LayoutManager(main, layout):
    '''Itt hozza létre őket a program'''
    text = [classes.LayoutText('Asztalok', 'Asztal', 'Hozzáadás', 'Törlés'), classes.LayoutText('Számla', 'Asztal','Fizetés','Törlés'), classes.LayoutText('Menü','Név - Ár','Hozzáadás','Törlés')]
    for i in range(0, len(text)):
        CreateLayout(main, layout, text[i], i)

def CreateMenuBar(window, main):
    '''Menubar létrehozása'''
    menu = window.menuBar()
    fil  = menu.addMenu('&File')
    fris = QAction('&Frissítés', window)
    fris.triggered.connect(lambda: file.Refresh(main.findChildren(QListWidget)[2]))
    fil.addAction(fris)
    pont = menu.addMenu('&Foglalások')
    fogl = QAction('&Foglalások', window)
    hozz = QAction('&Foglalás Hozzáadása', window)
    fogl.triggered.connect(lambda: popup.ShowFoglalas(main))
    hozz.triggered.connect(lambda: file.addFoglalas(main))
    pont.addAction(fogl)
    pont.addAction(hozz)
    kile = menu.addMenu('&Kilépés')
    beza = QAction('&Kilépés', window)
    beza.triggered.connect(lambda: sys.exit())
    kile.addAction(beza)

def GetTables(main_widget):
    '''Asztalok száma'''
    if(CreateTables(main_widget, popup.CreatePopup(main_widget))):
        return True
    else:
        sys.exit()

def ReadSaves(main):
    '''Beolvassa a fájlokban tárolt adatokat'''
    lists = main.findChildren(QListWidget)
    file.readMenu(lists[2])

def ShowFirstDesk(main):
    '''Első asztal számlájának betöltése'''
    lists  = main.findChildren(QListWidget)
    labels = main.findChildren(QLabel)
    labels[3].setText('1. Asztal')
    lists[0].last_szamla = 1
    file.showSzamla(lists, 1)

def SetButtons(main):
    '''Gombokhoz rendel funkciókat'''
    lists   = main.findChildren(QListWidget)
    buttons = main.findChildren(QPushButton)
    buttons[0].clicked.connect(lambda: file.addTable(lists))
    buttons[1].clicked.connect(lambda: file.delTable(lists))
    buttons[2].clicked.connect(lambda: payment.startPayment(lists))
    buttons[3].clicked.connect(lambda: file.delSzamla(lists))
    buttons[4].clicked.connect(lambda: file.addMenu(main, lists))
    buttons[5].clicked.connect(lambda: file.delMenu(lists))
