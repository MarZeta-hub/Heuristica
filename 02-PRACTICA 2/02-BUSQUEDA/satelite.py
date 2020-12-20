# Objeto Satélite 

class satelite():
    
    # Es un coste de las operaciones que puede realizar el satelite [OBSERVACION, TRANSMISION, GIRO, UDSRECARGADAS]
    idSat = None

    # Energia disponible para cada satelite
    energiaDisponible = 0

    # Bandas que esta utilizando actualmente cada satelite (X1,X2)
    bandasActuales = []

    # Son las observaciones pendientes de ser transmitidas, despues de ser observadas
    retransmisiones = []

    # Operacion realizada para conseguir este estado
    operacion = None

    # Matriz de observables
    matrizObservables = None

    # Constructor de satelite
    def __init__(self, idSat, energiaDisponible, bandaOrigen, matrizObservables, retransmisiones, operacion):
        self.idSat = idSat
        self.energiaDisponible = energiaDisponible
        self.bandaOrigen = bandaOrigen
        self.bandasActuales = [bandaOrigen[0], bandaOrigen[1]]
        self.matrizObservables = matrizObservables
        self.retransmisiones = retransmisiones
        self.operacion = operacion

    
# Getters y setters necesarios

    def getEnergiaDisponible(self):
        return self.energiaDisponible

    def setEnergiaDisponible(self, energiaDisponible):
        self.energiaDisponible = energiaDisponible

    def getBandasActuales(self):
        return self.bandasActuales

    def setBandasActuales(self, bandasAcuales):
        self.bandasActuales = bandasAcuales

    def getRetransmisiones(self):
        return self.retransmisiones
    
    def setRetransmisiones(self, retransmisiones):
        self.retransmisiones =retransmisiones

    def getOperacion(self):
        return self.operacion

    def setOperacion(self, operacion):
        self.operacion = operacion

    def getId(self):
        return self.idSat

    def getMatrizObservable(self):
        return self.matrizObservables

    def setMatrizObservable(self, matrizObservable):
        self.matrizObservables = matrizObservable