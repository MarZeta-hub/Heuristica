 

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
    heuristica = None

    # Valor del coste
    coste = None

    # Valor de la funcion heuristica
    f = 0

    def __init__(self, nodoRaiz, matrizObservables, sat1, sat2, hora, coste):
        self.matrizObservables = matrizObservables
        self.sat1 = sat1
        self.sat2 = sat2
        self.nodoRaiz = nodoRaiz
        self.horaActual = hora
        self.coste = coste
        
    def evaluarh1(self):
        # Sumamos todos los observables que estan por observar 
        totalObsevables = 0

        # self.getObservables()
        matrizObservable = self.matrizObservable
        for i in range(len(matrizObservable)):
            for j in range(len(matrizObservable[i])):
                if matrizObservable[i][j] != 0:
                    totalObsevables = totalObsevables + 1

        # Sumamos las transmisiones que tiene pendientes de hacer cada uno de los satelites
        ntrsat1 = len(self.sat1.getRetransmisiones())
        ntrsat2 = len(self.sat2.getRetransmisiones())

        valorh1 = totalObsevables + ntrsat1 + ntrsat2
        self.setH(valorh1)

    def evaluarh2(self):
        hora = self.horaActual
        diferencias = 0

        # Si no hay distancias a los objetos observables, quiere decir que no hay
        for i in range(len(self.matrizObservable)):
            for j in range(len(self.matrizObservable[i])):
                
                if(self.matrizObservable[i][j]!=0):
                    diferencias = diferencias + abs(j-hora)
                    diferencias = diferencias + min(abs(i-self.sat1.bandasActuales[0]),abs(i-self.sat1.bandasActuales[1]))
                    diferencias = diferencias + min(abs(i-self.sat2.bandasActuales[0]),abs(i-self.sat2.bandasActuales[1]))
        
        # Lo siguiente es comprobar si los objetos han sido retransmitidos 
        porRetransmitir = len(self.sat1.getRetransmisiones()) + len(self.sat2.getRetransmisiones()) 

        if(porRetransmitir>0):
            diferencias = diferencias + porRetransmitir
        
        self.setH(diferencias)

    def compare(self, estado2, modo):
        for i in range(len(self.matrizObservable)):
            for j in range(len(self.matrizObservable[i])):
                if self.matrizObservable[i][j] != estado2.matrizObservable[i][j]:
                    return False

        if len(self.sat1.getRetransmisiones() ) != len(estado2.sat1.getRetransmisiones() ):
            return False

        if len(self.sat2.getRetransmisiones() ) != len(estado2.sat2.getRetransmisiones() ):
            return False

        if modo == 1:

            """if self.getHoraActual() != estado2.getHoraActual():
                return False
            """
            """if self.sat1.getBandasActuales() != estado2.sat1.getBandasActuales():
                return False

            if self.sat2.getBandasActuales() != estado2.sat2.getBandasActuales():
                return False
            """

            if self.sat1.getOperacion() != estado2.sat1.getOperacion():
                return False

            if self.sat2.getOperacion() != estado2.sat2.getOperacion():
                return False

            for i in range(len (self.sat1.getRetransmisiones()) ):
                if self.sat1.getRetransmisiones() != estado2.sat1.getRetransmisiones():
                    return False

            for i in range(len (self.sat2.getRetransmisiones()) ):
                if self.sat2.getRetransmisiones() != estado2.sat2.getRetransmisiones():
                    return False

            if self.getF() < estado2.getF():
                return False
                
        return True
