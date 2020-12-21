 

class nodo():

    # Nodo padre del nodo actual
    nodoRaiz = None

    # Hora actual en la que se encuentra el estado
    horaActual = 0

    # Matriz de observables
    matrizObservables = None

    # Datos del Satelite 1
    sat1 = None

    # Datos del Satelite 2
    sat2 = None

    # Valor de la heuristica
    heuristica = 0

    # Valor del coste
    coste = None

    # Valor de la funcion heuristica
    f = 0

    # Acciones
    acciones = None

    def __init__(self, nodoRaiz, matrizObservables, sat1, sat2, hora, coste, acciones):
        self.matrizObservables = matrizObservables
        self.sat1 = sat1
        self.sat2 = sat2
        self.nodoRaiz = nodoRaiz
        self.horaActual = hora
        self.coste = coste
        self.acciones = acciones
        
    def evaluarh1(self):
        # Sumamos todos los observables que estan por observar 
        totalObsevables = 0

        # self.getObservables()
        matrizObservable = self.matrizObservables
        for i in range(len(matrizObservable)):
            for j in range(len(matrizObservable[i])):
                if matrizObservable[i][j] != 0:
                    totalObsevables = totalObsevables + 1

        # Sumamos las transmisiones que tiene pendientes de hacer cada uno de los satelites
        ntrsat1 = len(self.sat1.retransmisiones)
        ntrsat2 = len(self.sat2.retransmisiones)

        valorh1 = totalObsevables*10 + ntrsat1*5 + ntrsat2*5
        self.heuristica= valorh1

    def evaluar(self):
        self.f = self.heuristica + self.coste

    def evaluarh2(self):
        hora = self.horaActual
        diferencias = 0

        # Si no hay distancias a los objetos observables, quiere decir que no hay
        for i in range(len(self.matrizObservables)):
            for j in range(len(self.matrizObservables[i])):
                
                if(self.matrizObservables[i][j]!=0):
                    diferencias = diferencias + abs(j-hora)
                    diferencias = diferencias + min(abs(i-self.sat1.bandasActuales[0]),abs(i-self.sat1.bandasActuales[1]))
                    diferencias = diferencias + min(abs(i-self.sat2.bandasActuales[0]),abs(i-self.sat2.bandasActuales[1]))
        
        # Lo siguiente es comprobar si los objetos han sido retransmitidos 
        porRetransmitir = len(self.sat1.retransmisiones) + len(self.sat2.retransmisiones) 

        if(porRetransmitir>0):
            diferencias = diferencias + porRetransmitir
        
        #self.setH(diferencias)

    def compare(self, estado2):

        for i in range(len(self.matrizObservables)):
            for j in range(len(self.matrizObservables[i])):
                if self.matrizObservables[i][j] != estado2.matrizObservables[i][j]:
                    return False

        if len(self.sat1.retransmisiones ) != len(estado2.sat1.retransmisiones ):
            return False

        if len(self.sat2.retransmisiones ) != len(estado2.sat2.retransmisiones ):
            return False

        if self.horaActual != estado2.horaActual:
            return False
      
        if self.sat1.bandasActuales != estado2.sat1.bandasActuales:
            return False

        if self.sat2.bandasActuales != estado2.sat2.bandasActuales:
            return False
        """
        if self.sat1.operacion != estado2.sat1.operacion :
            return False

        if self.sat2.operacion  != estado2.sat2.operacion :
            return False
        """
        for i in range(len (self.sat1.retransmisiones) ):
            if self.sat1.retransmisiones != estado2.sat1.retransmisiones:
                return False

        for i in range(len (self.sat2.retransmisiones) ):
            if self.sat2.retransmisiones != estado2.sat2.retransmisiones:
                return False
        
        return True
