class PeludoCasa:
    def __init__(self, activo):
        self.activo = activo
        
    

    def ponerPeludoCasa(self):
        self.activo = True
    
    def getPeludoCasa(self):
        return self.activo

    def __repr__(self) -> str:
        return "PeludoCasa"