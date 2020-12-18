# Objeto Satélite 

class satelite():
    
    # Es un coste de las operaciones que puede realizar el satelite [OBSERVACION, TRANSMISION, GIRO, UDSRECARGADAS]
    idSat = None

    # Atributos de costes 
    costeObservacion = 0
    costeTransmision = 0
    costeGiro = 0
    udsRecarga = 0
    capacidadBateria = 0


    # Energia disponible para cada satelite
    energiaDisponible = 0

    # Bandas que esta utilizando actualmente cada satelite (X1,X2)
    bandasActuales = []

    # Banda Origen de la que parte el satelite (X1,X2)
    bandaOrigen = []

    # Son las observaciones pendientes de ser transmitidas, despues de ser observadas
    retransmisiones = []

    # Operacion realizada para conseguir este estado
    operacion = None

    # Constructor de satelite
    def __init__(self, idSat,costeObservacion, costeTransmision, costeGiro, udsRecarga, capacidadBateria, bandaOrigen, retransmisiones):
        
        self.idSat = idSat
        self.costeObservacion = costeObservacion
        self.costeTransmision = costeTransmision
        self.costeGiro = costeGiro
        self.udsRecarga = udsRecarga
        self.capacidadBateria = capacidadBateria
        self.energiaDisponible = capacidadBateria
        self.bandaOrigen = bandaOrigen
        self.bandasActuales = bandaOrigen
        self.retransmisiones = retransmisiones

    

# Getters y setters necesarios

    def getCosteObservacion(self):
        return self.costeObservacion
    
    def getCosteTransmision(self):
        return self.costeTransmision
    
    def getCosteGiro(self):
        return self.costeGiro

    def getUdsRecarg(self):
        return self.udsRecarga

    def getCapacidadBateria(self):
        return self.capacidadBateria


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


# Operaciones que pueden realizar los satelites

    def IDLE(self):
        print('SAT'+self.idSat+' IDLE')

    def carga(self):
        carga  = self.energiaDisponible
        self.energiaDisponible = carga+self.udsRecarga
        if(self.energiaDisponible>self.capacidadBateria):
            self.energiaDisponible=self.capacidadBateria
        print('SAT'+self.idSat+' ha recargado bateria')
    
    #TODO HACER METODO DE GIRO
    def girar(self):
        print('SAT'+self.idSat+' gira a ')

    #TODO HACER METODO DE OBSERVAR
    def observar(self):
        print('SAT'+self.idSat+' observa ')

    #TODO HACER METODO DE TRANSMITIR OBSERVACIONES
    def transmitir(self):
        print('SAT'+self.idSat+' transmite ')