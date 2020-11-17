from PyQt4.QtGui import QVBoxLayout

class MainLayout(QVBoxLayout):
    def __init__(self):
        super(MainLayout, self).__init__()
        self.setContentsMargins(0,0,0,0)
        self.setSpacing(10)
