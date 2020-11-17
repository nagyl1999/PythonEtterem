from PyQt4.QtGui import QPushButton, QCursor
from PyQt4.QtCore import Qt

class MainButton(QPushButton):
    def __init__(self):
        super(MainButton, self).__init__()
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setMinimumSize(50, 50)
        self.show()
