from PyQt4.QtGui import QLabel, QFont
from PyQt4.QtCore import Qt

class MainHeader(QLabel):
    def __init__(self):
        super(MainHeader, self).__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont('Arial', 25))
        self.show()
