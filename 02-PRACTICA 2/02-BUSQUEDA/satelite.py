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

    # Puntero a su MatrizObservables
    matrizObservables = None

    # Constructor de satelite
    def __init__(self, idSat, energiaDisponible, bandaOrigen, retransmisiones, operacion, matrizObservables):
        self.idSat = idSat
        self.energiaDisponible = energiaDisponible
        self.bandasActuales = [bandaOrigen[0], bandaOrigen[1]]
        self.retransmisiones = retransmisiones
        self.operacion = operacion
        self.matrizObservables = matrizObservables
