# Objeto Satélite 

class satelite():

    # Capacidad de bateria
    capacidadBateria = 0

    """ Coste de operacion
        0: idle
        1: observacion de terreno
        2: transmitir observacion
        3: girar
        4: recargar
    """
    costeOperacion = []

    # Energia disponible para cada satelite
    energiaDisponible = 0

    # Bandas que esta utilizando actualmente cada satelite
    bandasActuales = []

    # Banda Origen
    bandaOrigen = []

    # Son las observaciones pendientes de ser transmitidas, despues de ser observadas
    retransmisiones = []

    # Operacion realizada para conseguir este estado
    operacion = None

    def __init__(self, capacidadBateria, costeOperacion, energiaDisponible, bandasActuales, bandaOrigen, retransmisiones):
        self.capacidadBateria = capacidadBateria
        self.costeOperacion = costeOperacion
        self.energiaDisponible = energiaDisponible
        self.bandasActuales = bandasActuales
        self.bandaOrigen = bandaOrigen
        self.retransmisiones = retransmisiones

    def __init__(self):
        super().__init__()

    def getCapacidadBateria(self):
        return self.capacidadBateria

    def setCapacidadBateria(self, capacidadBateria):
        self.capacidadBateria = capacidadBateria

    def getcosteOperacion(self):
        return self.costeOperacion

    def setcosteOperacion(self, costeOperacion):
        self.costeOperacion = costeOperacion

    def getEnergiaDisponible(self):
        self.energiaDisponible = self.energiaDisponible

    def getEnergiaDisponible(self, energiaDisponibel):
        self.energiaDisponible = energiaDisponibel

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