from PyQt4.QtGui import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(1000, 600)
        self.setWindowTitle("Étterem")
        self.show()
