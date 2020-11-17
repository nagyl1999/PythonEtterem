import sys
import datetime
import operator

import modulok       as modulok
import modulok.popup as popup
import modulok.file  as file

def getDate():
    '''Dátum most'''
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def clearSzamla(szamla):
    '''Számla ürítése fizetés után'''
    szamla.elemek = []

def startPayment(lists):
    '''Fizetés'''
    spaces = 24
    number = lists[0].last_szamla
    szamla = file.findSzamla(number)
    szamla.elemek.sort(key=operator.attrgetter('nev'))
    if(len(szamla.elemek) > 0):
        print(
            f'|-------------------------|'    ,
            f'\n|         Étterem         |'  ,
            f'\n|Étterem utca 12, Budapest|'  ,
            f'\n|                         |'  ,
            f'\n|{"Asztal:":<15}{number:>10}|',
            f'\n|----------Nyugta---------|'
            )
        for i in range(len(szamla.elemek)):
            print(f'|{szamla.elemek[i].nev:<13}{szamla.elemek[i].ar:>10}Ft|')
        print(
            f'|-------------------------|',
            f'\n|{"Összesen:":<15}{len(szamla):>8}Ft|',
            f'\n|                         |',
            f'\n|   '  + getDate() +  '   |',
            f'\n|       AP123456789       |',
            f'\n|-------------------------|'
            )
        clearSzamla(szamla)
        file.showSzamla(lists, number)
    else:
        popup.ErrorBox('Hiba!', 'Üres a számla!')
