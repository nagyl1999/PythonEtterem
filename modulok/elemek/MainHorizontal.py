from PyQt4.QtGui import QHBoxLayout

class MainHorizontal(QHBoxLayout):
    def __init__(self):
        super(MainHorizontal, self).__init__()
        self.setSpacing(10)
