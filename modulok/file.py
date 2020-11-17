import sys
from PyQt4.QtCore import Qt
from PyQt4.QtGui  import QLabel

import modulok         as modulok
import modulok.popup   as popup
import modulok.classes as classes

'''Globális változók'''
menu_file = './mentesek/menu.csv'
fogl_file = './mentesek/foglalas.csv'

def FileNotFoundErrorMessage(filename):
    popup.ErrorBox('Hiba!', 'A fájl nem található!\n{0}'.format(filename))
    return False

def SomethingWrongErrorMessage():
    popup.ErrorBox('Hiba!', 'Valami hiba történt!')
    return False

def readFile(filename):
    '''Fájl beolvasása'''
    try:
        file = open(filename, 'r')
        text = file.readlines()
        file.close() #Nem kerülhet finally-be, mert ha nem található a file, akkor nincs mit bezárni.
    except FileNotFoundError:
        return FileNotFoundErrorMessage(filename)
    except:
        return SomethingWrongErrorMessage()
    return text

def writeFile(filename, text):
    '''Fájl írása'''
    try:
        file = open(filename, 'w')
        file.write(text + '\n')
        file.close()
    except FileNotFoundError:
        return FileNotFoundErrorMessage(filename)
    except:
        return SomethingWrongErrorMessage()

def appendFile(filename, text):
    '''Hozzáfűzés'''
    try:
        file = open(filename, 'a')
        file.write(text)
        file.close()
    except FileNotFoundError:
        return FileNotFoundErrorMessage(filename)
    except:
        return SomethingWrongErrorMessage()

def readMenu(listview):
    '''Menü beolvas'''
    listview.clear()
    text = readFile(menu_file)
    if not text:
        return False
    for sor in text:
        sor = sor.strip()
        if(sor != ''):
            sor = sor.split(';')
            sor = ' - '.join(sor)
            listview.addItem(sor)
    listview.sortItems()
    listview.last_clicked = None

def addMenu(main, lists):
    '''Menü elem hozzáadása'''
    data = popup.GetNewMenuItemData(main)
    if(data != False):
        if(';' in data[0].strip()):
            popup.ErrorBox('Hiba!', 'Tiltott karakter ";"!')
            return False
        text = readFile(menu_file)
        if not text:
            return False
        for sor in text:
            sor = sor.split(';')
            sor = sor[0].strip()
            if(sor.lower() == data[0].strip().lower()):
                popup.ErrorBox('Hiba!', 'Már létezik!')
                return False
        appendFile(menu_file, '{0};{1}\n'.format(data[0], data[1]))
        readMenu(lists[2])
    else:
        return False
        
def delMenu(lists):
    '''Menü elem törlése'''
    if(lists[2].last_clicked is None):
        popup.ErrorBox('Hiba!', 'Nincs kiválasztott elem!')
        return False
    item  = lists[2].last_clicked.text().split('-')[0].strip()
    items = []
    text  = readFile(menu_file)
    if not text:
        return False
    for sor in text:
        sor = sor.strip()
        sor = sor.split(';')
        if(sor[0].lower() != item.lower()):
            sor = ';'.join(sor)
            items.append(sor)
    writeFile(menu_file, '\n'.join(items))
    readMenu(lists[2])

def readFoglalas(listview):
    '''Foglalások beolvasása'''
    listview.clear()
    text = readFile(fogl_file)
    if not text:
        return False
    fogl = []
    for sor in text:
        sor = sor.strip()
        if(sor != ''):
            sor = sor.split(';')
            sor = ' - '.join(sor)
            fogl.append(sor)
    '''A legújabb foglalás megy előre'''
    fogl = fogl[::-1]
    for sor in fogl:
        listview.addItem(sor)
    listview.last_clicked = None

def addFoglalas(main):
    '''Foglalás hozzáadása'''
    data = popup.GetNewFoglalasItemData(main)
    if(data != False):
        if(';' in data[0].strip()):
            popup.ErrorBox('Hiba!', 'Tiltott karakter ";"!')
            return False
        '''Foglalhat két azonos nevű vendég'''
        item = '{0};{1}\n'.format(data[0].strip(), data[1])
        appendFile(fogl_file, item)
        return True
    return False

def delFoglalas(listview):
    '''Foglalás törlése'''
    if(listview.last_clicked is None):
        popup.ErrorBox('Hiba!', 'Nincs kiválasztott elem!')
        return False
    item  = listview.last_clicked
    text  = readFile(fogl_file)[::-1]
    if not text:
        return False
    for i in range(0, listview.count()):
        if(item == listview.item(i)):
            del text[i]
    text = [item.strip() for item in text]
    text = '\n'.join(text[::-1])
    writeFile(fogl_file, text)
    readFoglalas(listview)

def addTable(lists):
    '''Asztal hozzáadása'''
    num = int(lists[0].item(lists[0].count()-1).text().split('.')[0].strip())
    lists[0].addItem('{0}. Asztal'.format(num+1))
    modulok.szamlak.append(classes.Szamla(num+1))

def addTablesAtStart(lists, num):
    '''Asztalok hozzáadása kezdésnél'''
    if(num > 0):
        for i in range(1, num+1):
            lists[0].addItem('{0}. Asztal'.format(i))
            modulok.szamlak.append(classes.Szamla(i))
        return True
    return False

def delTable(lists):
    '''Asztal törlése'''
    if(lists[0].last_clicked is not None):
        if(lists[0].count() > 1):
            items  = lists[0].findItems(lists[0].last_clicked.text(), Qt.MatchExactly)
            for item in items:
                lists[0].takeItem(lists[0].row(item))
            number = int(lists[0].last_clicked.text().strip().split('.')[0].strip())
            for i in range(0, len(modulok.szamlak)):
                if(modulok.szamlak[i].id == number):
                    del modulok.szamlak[i]
                    break
            asztal_id = int(lists[0].last_clicked.text().strip().split('.')[0])
            szamla_id = int(lists[0].last_szamla)
            if(asztal_id == szamla_id):
                ShowAnotherSzamla(lists)
            lists[0].last_clicked = None
        else:
            popup.ErrorBox('Hiba!', 'Nem törölhető minden elem!')
            return False
    else:
        popup.ErrorBox('Hiba!', 'Nincs kiválasztott elem!')
        return False

def findSzamla(number):
    '''Megkeresi az adott ID-vel rendelkező számlaobjektumot'''
    for szamla in modulok.szamlak:
        if(szamla.id == number):
            return szamla
    return None

def showSzamla(lists, number):
    '''Betölti a kiválasztott számlát'''
    lists[1].clear()
    szamla = findSzamla(number)
    if szamla is not None:
        if(len(szamla.elemek) > 0):
            for i in range(0, len(szamla.elemek)):
                lists[1].addItem('{0} - {1}'.format(szamla.elemek[i].nev, szamla.elemek[i].ar))
            lists[1].sortItems()
            lists[1].addItem('')
            lists[1].addItem('Végösszeg: {0}Ft'.format(len(szamla)))
            return True
        else:
            lists[1].addItem('Nincs tétel')
            return True
    else:
        return False

def addSzamla(lists, item, number):
    '''Elemet ad a számlához'''
    item   = item.text().split('-')
    szamla = findSzamla(number)
    if szamla is not None:
        szamla.elemek.append(classes.Elem(item[0].strip(), item[1].strip()))
        return showSzamla(lists, number)
    return False

def delSzamla(lists):
    '''Elemet töröl a számláról'''
    szamla = findSzamla(lists[0].last_szamla)
    if(lists[1].last_clicked is not None and szamla is not None):
        etel = lists[1].last_clicked.text().split('-')[0].strip()
        for i in range(0, len(szamla.elemek)):
            if(etel == szamla.elemek[i].nev):
                del szamla.elemek[i]
                break
        lists[1].last_clicked = None
        return showSzamla(lists, lists[0].last_szamla)
    popup.ErrorBox('Hiba!', 'Nincs kiválasztva elem!')
    return False

def ShowAnotherSzamla(lists):
    '''Másik számla mutatása'''
    num                  = int(lists[0].item(0).text().split('.')[0].strip())
    lists[0].last_szamla = num
    lists[0].parent().parent().findChildren(QLabel)[3].setText('{0}. Asztal'.format(num))
    showSzamla(lists, num)

def Refresh(listview):
    '''Frissíti a menüt'''
    return readMenu(listview)
