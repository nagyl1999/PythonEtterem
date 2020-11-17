import sys

class LayoutText:
    '''Szöveg a fő layoutokon belül'''
    def __init__(self, header_text, sub_text, button1_text, button2_text):
        self.header_text  = header_text
        self.sub_text     = sub_text
        self.button1_text = button1_text
        self.button2_text = button2_text

class Szamla:
    '''Számla'''
    def __init__(self, id):
        self.id     = id
        self.elemek = []

    def __len__(self):
        return sum([elem.ar for elem in self.elemek])

class Elem:
    '''Számla eleme'''
    def __init__(self, nev, ar):
        self.nev = nev
        self.ar  = int(ar)
