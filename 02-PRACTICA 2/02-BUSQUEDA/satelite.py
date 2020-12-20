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

    # Constructor de satelite
    def __init__(self, idSat, energiaDisponible, bandaOrigen, retransmisiones, operacion):
        self.idSat = idSat
        self.energiaDisponible = energiaDisponible
        self.bandasActuales = [bandaOrigen[0], bandaOrigen[1]]
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