# Clase estado para la practica 2 parte 2

class estado():

    # Nodo del arbol padre (Para recorrerlo inversamente)
    nodoPadre = None

    # Hora actual en la que se encuentra el estado
    horaActual = 0

    # Energia disponible para cada satelite
    energiaDisponible = []

    # Bandas que esta utilizando actualmente cada satelite
    bandasActuales = []

    # Puntos de observacion disponibles (su posicion y hora)
    observables = []

    # Son las observaciones pendientes de ser transmitidas, despues de ser observadas
    retransmisiones = []

    #Operacion realizada para conseguir este estado
    operacion = None

    # Valor de la funcion heuristica
    h = None

    # Valor de la funcion de coste utilizada
    g = None

    # Valor de la funcion de evaluacion
    f = None

    # Funcion constructor
    def __init__(self, nodoPadre ,horaActual, energiaDisponible, bandasActuales, observables, retransmisiones,coste):
        self.nodoPadre = nodoPadre
        self.horaActual = horaActual
        self.energiaDisponible = energiaDisponible
        self.bandasActuales = bandasActuales
        self.observables = observables
        self.retransmisiones = retransmisiones
        if self.nodoPadre == None:
            self.g = coste
        else:
            self.g = coste + self.nodoPadre.getG()



    # A partir de aquí se implementan los getters y setters

    def getnodoPadre(self):
        return self.nodoPadre

    def setnodoPadre(self, nodoPadre):
        self.nodoPadre = nodoPadre

    def getHoraActual(self):
        return self.horaActual

    def setHoraActual(self, horaActual):
        self.horaActual = horaActual

    def getEnergiaDisponible(self):
        self.energiaDisponible = self.energiaDisponible

    def getEnergiaDisponible(self, energiaDisponibel):
        self.energiaDisponible = energiaDisponibel

    def getBandasActuales(self):
        return self.bandasActuales

    def setBandasActuales(self, bandasAcuales):
        self.bandasActuales = bandasAcuales

    def getObservables(self):
        return self.observables

    def setObservables(self, observables):
        self.observables = observables

    def getRetransmisiones(self):
        return self.retransmisiones
    
    def setRetransmisiones(self, retransmisiones):
        self.retransmisiones =retransmisiones

    def getOperacion(self):
        return self.operacion

    def setOperacion(self, operacion):
        self.operacion = operacion

    def getG(self):
        return self.g
    
    def setG(self, g):
        self.g = g

    def getH(self):
        return self.h

    def setHeuristica(self, value):
        self.setH(value)
        self.setF(self.getG() + self.getH())

    def setH(self, h):
        self.h = h

    def getF(self):
        return self.f
    
    def setF(self, f):
        self.f = f