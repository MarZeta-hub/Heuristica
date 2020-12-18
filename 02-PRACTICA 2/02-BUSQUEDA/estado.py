# Clase estado para la practica 2 parte 2

from satelite import satelite


class estado():

    # Nodo del arbol padre (Para recorrerlo inversamente)
    nodoPadre = None

    # Hora actual en la que se encuentra el estado
    horaActual = 0

    # Puntos de observacion disponibles (su posicion y hora)
    observables = []

    # Datos del satelite 1
    sat1 = satelite()

    # Datos del satelite 2
    sat2 = satelite()

    # Valor de la funcion heuristica
    h = None

    # Valor de la funcion de coste utilizada
    g = None

    # Valor de la funcion de evaluacion
    f = None

    # Funcion constructor
    def __init__(self, nodoPadre ,horaActual, observables,  sat1, sat2, coste):
        self.nodoPadre = nodoPadre
        self.horaActual = horaActual
        self.observables = observables
        self.sat1 = sat1
        self.sat2 = sat2
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

    def getObservables(self):
        return self.observables

    def setObservables(self, observables):
        self.observables = observables

    def getSat1(self):
        return self.sat1

    def getSat2(self):
        return self.sat2