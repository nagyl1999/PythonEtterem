
'''
Ikon:
    https://icons8.com/
    https://img.icons8.com/wired/2x/restaurant.png
'''

import sys
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QIcon

sys.dont_write_bytecode = True #__pyc__ mappák nem jönnek létre, később törölhető, de fejlesztés közben zavaró.

import modulok.startup as startup
import modulok.elemek  as elemek

def Controller(main_window, main_widget, main_horizont):
    '''Meghívja a fő beállító és beolvasó részeket'''
    startup.CreateMenuBar(main_window, main_widget)
    startup.LayoutManager(main_widget, main_horizont)
    startup.GetTables(main_widget)
    startup.ReadSaves(main_widget)
    startup.SetButtons(main_widget)
    startup.ShowFirstDesk(main_widget)

def main():
    '''Főprogramrész, főbb elemek meghívása, ikon beállítása'''
    app           = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./icon/icon.png'))
    main_widget   = elemek.MainWidget.MainWidget()
    main_window   = elemek.MainWindow.MainWindow()
    main_horizont = elemek.MainHorizontal.MainHorizontal()
    main_widget.setLayout(main_horizont)
    main_window.setCentralWidget(main_widget)
    Controller(main_window, main_widget, main_horizont)
    app.exec()

main()
