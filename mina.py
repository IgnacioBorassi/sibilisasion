import random
class Mina:
    '''Representa una mina'''

    def __init__(self, mina):
        self.mina = mina
    

    def ponerMina(self):
        self.mina = True
    
    def getMina(self):
        return self.mina

    def __repr__(self) -> str:
        return "Mina"
