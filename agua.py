class Agua:
    '''Representa el agua y su contrucciones'''
    
    def __init__(self, naturaleza, construccion):
        self.naturaleza = naturaleza
        self.construccion = construccion


    def getNaturaleza(self):
        return self.naturaleza
    
    def getConstruccion(self):
        return self.construccion

    def __repr__(self) -> str:
        return "Agua"
    