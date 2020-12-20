# Clase estado para la practica 2 parte 2

from numpy.core import getlimits
from satelite import satelite


class estado():

    # Nodo del arbol padre (Para recorrerlo inversamente)
    nodoPadre = None

    # Hora actual en la que se encuentra el estado
    horaActual = 0

    # Datos del satelite 1
    sat1 = None

    # Datos del satelite 2
    sat2 = None

    # Valor de la funcion heuristica
    h = None

    # Valor de la funcion de coste utilizada
    g = None

    # Valor de la funcion de evaluacion f = g + h
    f = None

    # Funcion constructor
    def __init__(self, nodoPadre ,horaActual, sat1, sat2, coste):
        self.nodoPadre = nodoPadre
        self.horaActual = horaActual
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

    def setEvaluacion(self):
        self.setF(self.getG() + self.getH())

    def setH(self, h):
        self.h = h

    def getF(self):
        return self.f
    
    def setF(self, f):
        self.f = f

    def getSat1(self):
        return self.sat1

    def getSat2(self):
        return self.sat2

    # Creamos las funciones heuristicas 
    def evaluarh1(self):
        # Sumamos todos los observables que estan por observar 
        totalObsevables = 0

       # self.getObservables()
        matrizObservable = self.sat1.getMatrizObservable()
        for i in range(len(matrizObservable)):
            for j in range(len(matrizObservable[i])):
                if matrizObservable[i][j] != 0:
                    totalObsevables = totalObsevables + 1

        # Multiplicamos por 2 los observables para que influya de forma mas negativa en la heuristica
        totalObsevables = totalObsevables*2
        # Sumamos las transmisiones que tiene pendientes de hacer cada uno de los satelites
        ntrsat1 = len(self.sat1.getRetransmisiones())
        ntrsat2 = len(self.sat2.getRetransmisiones())
        valorh1 = totalObsevables + ntrsat1 + ntrsat2
        self.setH(valorh1)


    def evaluarh2(self):
        hora = self.horaActual
        diferencias = 0

        # Si no hay distancias a los objetos observables, quiere decir que no hay
        for i in range(len(self.sat1.getMatrizObservable())):
            for j in range(len(self.sat1.getMatrizObservable()[i])):
                
                if(self.sat1.getMatrizObservable()[i][j]!=0):
                    diferencias = diferencias + abs(j-hora)
                    diferencias = diferencias + min(abs(i-self.sat1.bandasActuales[0]),abs(i-self.sat1.bandasActuales[1]))
                    diferencias = diferencias + min(abs(i-self.sat2.bandasActuales[0]),abs(i-self.sat2.bandasActuales[1]))
        
        # Lo siguiente es comprobar si los objetos han sido retransmitidos 
        porRetransmitir = len(self.sat1.getRetransmisiones()) + len(self.sat2.getRetransmisiones())

        if(porRetransmitir>0):
            diferencias = diferencias + porRetransmitir
        
        self.setH(diferencias)


    def compare(self, estado2):
        for i in range(len(self.sat1.getMatrizObservable())):
            for j in range(len(self.sat1.getMatrizObservable()[i])):
                if self.sat1.getMatrizObservable()[i][j] != estado2.sat1.getMatrizObservable()[i][j]:
                    return False

        if len(self.sat1.getRetransmisiones() ) != len(estado2.sat1.getRetransmisiones() ):
            return False

        if len(self.sat2.getRetransmisiones() ) != len(estado2.sat2.getRetransmisiones() ):
            return False

        for i in range(len (self.sat1.getRetransmisiones()) ):
            if self.sat1.getRetransmisiones() != estado2.sat1.getRetransmisiones():
                return False

        for i in range(len (self.sat2.getRetransmisiones()) ):
            if self.sat2.getRetransmisiones() != estado2.sat2.getRetransmisiones():
                return False
        
        return True
