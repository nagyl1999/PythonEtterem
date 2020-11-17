import sys
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QInputDialog, QMessageBox, QDialog

import modulok.file    as file
import modulok.elemek  as elemek

def CreatePopup(main):
    '''Asztalok számának bekérése indításkor'''
    return QInputDialog.getInt(main, 'Asztalok', 'Kérlek add meg az asztalok számát!')

def GetNewMenuItemData(main):
    '''Új étel bevitele'''
    name = QInputDialog.getText(main, 'Étel név', 'Add meg az étel nevét!')
    if(name[1]):
        value = QInputDialog.getInt(main, 'Étel ár', 'Add meg az étel árát!')
        if(value[1] and value[0] > 0):
            return name[0], value[0]
    return False

def GetNewFoglalasItemData(main):
    '''Új foglalás bevitele'''
    name = QInputDialog.getText(main, 'Foglalás név', 'Add meg a foglaló nevét!')
    if(name[1]):
        value = QInputDialog.getInt(main, 'Ülőhely', 'Add meg, hogy hányan jönnek!')
        if(value[1] and value[0] > 0):
            return name[0], value[0]
    return False

def ShowFoglalas(main):
    '''Felugró lista a foglalásokkal'''
    dialog = QDialog(None, Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
    dialog.setWindowTitle('Foglalások')
    dialog.setAttribute(Qt.WA_DeleteOnClose)
    layout = elemek.MainLayout.MainLayout()
    header = elemek.MainHeader.MainHeader()
    lista  = elemek.MainList.MainList()
    button = elemek.MainButton.MainButton()
    lista.setID(3)
    lista.setMain(main)
    header.setText('Foglalások')
    button.setText('Törlés')
    button.clicked.connect(lambda: file.delFoglalas(lista))
    layout.addWidget(header)
    layout.addWidget(lista)
    layout.addWidget(button)
    layout.setContentsMargins(10,10,10,10)
    file.readFoglalas(lista)
    dialog.setLayout(layout)
    dialog.exec()

def ErrorBox(header, message):
    '''Hibaüzenet'''
    error_box = QMessageBox()
    error_box.setIcon(QMessageBox.Critical)
    error_box.setText(message)
    error_box.setWindowTitle(header)
    error_box.exec()
