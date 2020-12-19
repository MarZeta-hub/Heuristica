# Clase estado para la practica 2 parte 2

from numpy.core import getlimits
from satelite import satelite


class estado():

    # Nodo del arbol padre (Para recorrerlo inversamente)
    nodoPadre = None

    # Hora actual en la que se encuentra el estado
    horaActual = 0

    # Puntos de observacion disponibles (su posicion y hora)
    franjas = []

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
    def __init__(self, nodoPadre ,horaActual, franjas,  sat1, sat2, coste):
        self.nodoPadre = nodoPadre
        self.horaActual = horaActual
        self.franjas = franjas
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

    def getFranjas(self):
        return self.franjas

    def setFranjas(self, franjas):
        self.franjas = franjas

    def getSat1(self):
        return self.sat1

    def getSat2(self):
        return self.sat2

    def getLimites(self):
        return [0, len(self.franjas)]

# Operaciones que pueden realizar los satelites

    def IDLE(self, sat):
        print('SAT',sat.idSat,' IDLE')

    # Metodo de cargar Bateria
    def carga(self, sat, total, udsRecarga):
        carga = sat.getEnergiaDisponible()
        if carga != total :
            carga = carga + udsRecarga
            if carga >= total:
                carga = total
            sat.setEnergiaDisponible(carga)
        print('SAT'+sat.idSat+' ha recargado bateria')
    
    # Girar hacia abajo
    def girarAbajo(self, sat, bActual):
        bActual[0] = bActual[0]+1
        bActual[1] = bActual[1]+1
        print('SAT', sat.getId(),' gira a ', bActual)

    # Girar hacia arriba
    def girarArriba(self, sat, bActual):
        bActual[0] = bActual[0]-1
        bActual[1] = bActual[1]-1
        print('SAT', sat.getId(),' gira a ', bActual)

    # Volver al estado inicial
    def girarEstadoInicial(self, sat, bOrigen, bActual):
        bActual[0] = bOrigen[0]
        bActual[1] = bOrigen[1]
        print('SAT', sat.getId(),' gira a ', bActual)

    # Observar un objeto en las bandas bajas del sat
    def observarArriba(self, sat):
        bActual = sat.getBandasActuales()
        hora = self.getHoraActual()
        observable = self.franjas[bActual[0]][hora]
        self.observar(observable,sat)

    # Observar un objeto en las bandas altas del sat
    def observarAbajo(self, sat):
        bActual = sat.getBandasActuales()
        hora = self.getHoraActual()
        observable = self.franjas[bActual[1]][hora]
        self.observar(observable,sat)

    # Transmite un observable que esta
    def transmitir(self, sat):
        lista = sat.getRetransmisiones()
        if len(lista) != 0:
            transmitido = lista.pop(0)
            print('SAT',sat.idSat,' transmite ',transmitido)
        else:
            print("no transmito nada")

    # Observar objeto
    def observar(self, observable, sat):
        lista = sat.getRetransmisiones()
        nuevoDato = 'O'+str(observable) 
        lista.append(nuevoDato)
        print('SAT',sat.getId(),' observa ',nuevoDato)
        return observable

    # Creamos las funciones heuristicas 
    def evaluarh1(self):
        # Sumamos todos los observables que estan por observar 
        totalObsevables = 0

       # self.getObservables()
        for i in range(len(self.franjas)):
            for j in range(len(self.franjas[i])):
                if self.franjas[i][j] != 0:
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
        for i in range(len(self.franjas)):
            for j in range(len(self.franjas[i])):
                
                if(self.franjas[i][j]!=0):
                    diferencias = diferencias + abs(j-hora)
                    diferencias = diferencias + min(abs(i-self.sat1.bandasActuales[0]),abs(i-self.sat1.bandasActuales[1]))
                    diferencias = diferencias + min(abs(i-self.sat2.bandasActuales[0]),abs(i-self.sat2.bandasActuales[1]))
        
        # Lo siguiente es comprobar si los objetos han sido retransmitidos 
        porRetransmitir = len(self.sat1.getRetransmisiones()) + len(self.sat2.getRetransmisiones())

        if(porRetransmitir>0):
            diferencias = diferencias + porRetransmitir
        
        self.setH(diferencias)


    def compare(self, estado2):
        if(self.franjas == estado2.franjas and self.sat1.retransmisiones == estado2.sat1.retransmisiones and self.sat2.bandaOrigen == estado2.sat2.retransmisiones):
            return True
        return False
