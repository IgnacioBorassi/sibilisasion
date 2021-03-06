from sibilisasion import civilizacion
class Jugador:
    '''Representa las cosas que tiene el jugador por fuera de la civilizacion como la energia, comida, turno'''
    
    def __init__(self):
        self.energia = 0
        self.comida = 0
        self.turno = True
        self.cantTurno = 0
        self.civilizacion = civilizacion()
        self.muerte = False
    
    
    def getPiedra(self):
        return self.civilizacion.getPiedra()

    def getComida(self):
        return self.comida

    def agregarMadera(self, cant):
        self.civilizacion.agregarMadera(cant)
    
    def restarMadera(self,cant):
        self.civilizacion.restarMadera(cant)
    
    def agregarPiedra(self, cant):
        self.civilizacion.agregarPiedra(cant)
    
    def restarPiedra(self, cant):
        self.civilizacion.restarMadera(cant)

    def restarEnergia(self, cant):
        '''Resta la energia total'''
        self.energia -= cant
        if self.energia < 0:
            self.energia = 0
        
    def restarComida(self, cant):
        '''Resta la comida total'''
        self.comida -= cant
        if self.comida <= 0:
            self.muerte = True
            
    def setEnergia(self, cant):
        self.energia = cant

    def setComida(self, cant):
        self.comida = cant

    def crearBarco(self):
        self.civilizacion.CrearBarco()

    def getMadera(self):
        return self.civilizacion.getMadera()

    def restarMadera(self, cant):
        self.civilizacion.restarMadera(cant)

    def agregarComida(self, cant):
        self.comida += cant

    def agregarEnergia(self, cant):
        self.energia += cant

    def restarPiedra(self, cant):
        self.civilizacion.restarPiedra(cant)

    def getEnergia(self):
        return self.energia

    def getBarco(self):
        return self.civilizacion.getBarco()
    
    def agregarBarco(self, cant):
        self.civilizacion.agregarUsoBarco(cant)

    def restarUsoBarco(self):
        self.civilizacion.restarUsoBarco()

    def getUsosBarco(self):
        return self.civilizacion.getUsosBarco()

    def hacerCasa(self):
        self.civilizacion.hacerCasa()
    
    def getFundadorActivo(self):
        return self.civilizacion.getFundadorActivo()

    def getGuerrerorActivo(self):
        return self.civilizacion.getGuerrerorActivo()
    
    def getArqueroActivo(self):
        return self.civilizacion.getArqueroActivo()
    
    def getObreroActivo(self):
        return self.civilizacion.getObreroActivo()
    
    def matarFundador(self):
        self.civilizacion.matarFundador()
    
    def ponerGuerrero(self):
        self.civilizacion.ponerGuerrero()
    
    def ponerArquero(self):
        self.civilizacion.ponerArquero()
    
    def ponerObreros(self):
        self.civilizacion.ponerObreros()

    def hacerPuerto(self):
        self.civilizacion.hacerPuerto()
    
    def hacerCorral(self):
        self.civilizacion.hacerCorral()

    def hacerCultivo(self):
        self.civilizacion.hacerCultivo()

    def hacerMina(self):
        self.civilizacion.hacerMina()

    def setTurno(self, cantComida):
        '''Lleva la cuenta de todos los turnos'''
        if self.energia > 0:
            self.turno = True
        else:
            self.turno = False
            self.restarComida(cantComida)
            self.cantTurno += 1

    
    def getTurno(self):
        return self.turno
    
    def getCantTurno(self):
        return self.cantTurno
    
    def reiniciarTurno(self):
        self.cantTurno = 0
        self.turno = True

    def reiniciar(self):
        self.cantTurno = 0
        self.turno = True
        self.energia = 500
        self.comida = 30
        self.civilizacion.reiniciarRecursos()

    def getMuerte(self):
        return self.muerte