from nodo import nodo
from satelite import satelite

class aStar():

    # Estado del cual partir
    nodoIncial = None

    nodoFinal = None

    # Lista donde se guardan los nodos segun su heuristica
    openList = []

    # Lista donde se guardan los nodos ya visitados
    closeList = []

    # Para escoger la heuristica para resolver el poblema
    elegirHeuristica = None

    #Gasto de energia por cada satelite
    gastoEnergia = None

# -------------------------Estadisticas---------------------------
    # Tiempo total que tarda el algoritmo en encontrar solucion
    tiempoAlgoritmo = None

    # Total de nodos que ha expandido el algoritmo
    nodosExpandidos = None

    # Coste total de la solucion
    costeTotal = None

    
    # Constructor
    def __init__ (self, nodoIncial,  gastoEnergia):
        self.nodoIncial = nodoIncial
        self.gastoEnergia = gastoEnergia
        self.openList = []
        self.costeTotal = []
        self.elegirHeuristica = None
        self.nodosExpandidos = 0
        self.tiempoAlgoritmo = 0
        self.costeTotal = 0
        self.openList.append(nodoIncial)

    def algoritmo(self):
        isFound = False
        estadoActual = None
        while not isFound and len(self.openList) != 0:
            estadoActual = self.openList.pop(0)
            #self.printEstado(estadoActual)
            if self.isNOTSameACloseListNode(estadoActual):
                self.closeList.append(estadoActual)
                if self.isFinal(estadoActual):
                    #print ("NOOOOO")
                    isFound = True
                self.crearNodos(estadoActual)

        if not isFound:
            raise Exception("No se ha encontrado solucion")
        self.nodoFinal = estadoActual


    def crearNodos(self, nodoActual):
        
        # Obtengo datos relativos a todos los nodos
        satelites = [nodoActual.sat1, nodoActual.sat2]
        hora = nodoActual.horaActual
        matrizObservables = nodoActual.matrizObservables

        listaSat = []
        bOrigen = [ [0,1], [2,3] ]
        listaAcciones = [[],[]]

        # Busco todas las operaciones que puede hacer los satelites
        for i in range (0,2):
            tmp = []
            # Bandas del satelite i
            bandas = satelites[i].bandasActuales
            listaObs = satelites[i].retransmisiones
                   
            # Girar
            if self.gastoEnergia[i][2] <= satelites[i].energiaDisponible:
                listaAcciones[i].append("Girar")
                if bOrigen[i] == bandas:
                    if min(min(bOrigen)) < min(bandas):
                        bandasNuevas = bandas.copy()

                        # Resto uno a todas las bandas actuales
                        bandasNuevas[0] = bandasNuevas[0]-1
                        bandasNuevas[1] = bandasNuevas[1]-1

                        # Creo el satelite y lo añado a la lista de satelites
                        gastoEnergia =  satelites[i].energiaDisponible - self.gastoEnergia[i][2]
                        satNuevo = satelite(i, gastoEnergia, bandasNuevas, listaObs, "Girar", matrizObservables)
                        tmp.append(satNuevo) # Add el satelite a la lista de satelites

                    # En el caso de que el MAXIMO de TODAS LAS BANDAS ORIGENES sean mayores que el MAXIMO de las bandas actuales
                    if max(max(bOrigen)) > max(bandas):
                        bandasNuevas = bandas.copy()

                        # Sumo uno a todas las bandas actuales
                        bandasNuevas[0] = bandasNuevas[0]+1
                        bandasNuevas[1] = bandasNuevas[1]+1

                        # Creo el satelite y lo añado a la lista de satelites
                        gastoEnergia =  satelites[i].energiaDisponible - self.gastoEnergia[i][2]
                        satNuevo = satelite(i, gastoEnergia, bandasNuevas, listaObs, "Girar", matrizObservables)
                        tmp.append(satNuevo) # Add el satelite a la lista de satelites

                    # En el caso que la banda origen sea DISTINTA  a las bandas actuales
                else:
                    bandasNuevas =  bandas.copy()

                    # Restauro las bandas
                    bandasNuevas[0] = bOrigen[i][0]
                    bandasNuevas[1] = bOrigen[i][1]

                    # Creo el satelite y lo añado a la lista de satelites
                    gastoEnergia = satelites[i].energiaDisponible - self.gastoEnergia[i][2]  
                    satNuevo = satelite(i, gastoEnergia, bandasNuevas, listaObs, "Girar", matrizObservables)
                    tmp.append(satNuevo) # Add el satelite a la lista de satelites
            
            # IDDLE
            # No hacer Nada / IDLE
            # Creo el satelite y lo añado a la lista de satelites
            listaAcciones[i].append("IDDLE")
            satNuevo = satelite(i, satelites[i].energiaDisponible, bandas, listaObs, "IDLE", matrizObservables)
            tmp.append(satNuevo) # Add el satelite a la lista de satelites

            # Transmitir
            if self.gastoEnergia[i][1] <= satelites[i].energiaDisponible:
                if len(satelites[i].retransmisiones) > 0:
                    listaAcciones[i].append("Retransmitir")
                    # Creo la nueva lista de observables
                    listaObsN = satelites[i].retransmisiones.copy()
                    listaObsN.pop(0)

                    # Creo el satelite y lo añado a la lista de satelites
                    gastoEnergia =  satelites[i].energiaDisponible - self.gastoEnergia[i][1]
                    satNuevo = satelite(i, gastoEnergia, bandas, listaObsN, "Retransmitir", matrizObservables)
                    tmp.append(satNuevo) # Add el satelite a la lista de satelites
                    
            # Recargar
            if self.gastoEnergia[i][4] > satelites[i].energiaDisponible:
                listaAcciones[i].append("Recargar")
                carga = satelites[i].energiaDisponible  # Obtengo el valor actual de la bateria
                carga = carga + self.gastoEnergia[i][3] # Cargo la bateria

                # Si la bateria cargada es mayor que la capacidad
                if carga >= self.gastoEnergia[i][4]:
                    carga = self.gastoEnergia[i][4]    # Lo igualo a la capacidad

                # Creo el satelite y lo añado a la lista de satelites
                satNuevo = satelite(i, carga, bandas, listaObs, "Recargar",matrizObservables)
                tmp.append(satNuevo) # Add el satelite a la lista de satelites

             # Observar
            if self.gastoEnergia[i][0] <= satelites[i].energiaDisponible:
                for j in range(0,2):
                    if matrizObservables[bandas[j]][hora] != 0:
                        listaAcciones[i].append("Observar a "+ str(matrizObservables[bandas[j]][hora]))
                        # Creo la matriz nueva 
                        matriz = matrizObservables.copy()

                        # Lista de observables nueva por añado uno nuevo
                        listaObsN = satelites[i].retransmisiones.copy()
                        nuevoDato = 'O'+str(matrizObservables[bandas[j]][hora])
                        listaObsN.append(nuevoDato)
                        matriz[bandas[j]][hora] = 0
                        
                        # Creo el satelite y lo añado a la lista de satelites
                        
                        gastoEnergia =  satelites[i].energiaDisponible - self.gastoEnergia[i][0]
                        satNuevo = satelite(i, gastoEnergia, bandas, listaObsN, "Observar", matriz)
                        tmp.append(satNuevo) # Add el satelite a la lista de satelites
            listaSat.append(tmp)


        # Obtengo la nueva hora que tiene que tener el siguiente nodo
        nuevaHora = hora + 1
        costeTotal = nodoActual.coste + 1
        # En el caso de que llegue a 12
        if(nuevaHora == 12):
            # Reseteo la hora a 0
            nuevaHora = 0
            costeTotal = costeTotal + 11

        # Ahora voy a crear los nuevos estados
        listaAbiertaNuevos = []

        # Un estado se compone  de dos satelites
        for satelite1 in listaSat[0]:
            for satelite2 in listaSat[1]:
                matrizFinal = matrizObservables
                if satelite2.operacion == "Observar" and satelite1.operacion == "Observar":
                    matrizFinal = self.matrizIgualada(satelite1.matrizObservables, satelite2.matrizObservables)
                else:
                    if satelite1.operacion == "Observar":
                        matrizFinal = satelite1.matrizObservables
                    if satelite2.operacion == "Observar":
                        matrizFinal = satelite2.matrizObservables
                nextState = nodo(nodoActual, matrizFinal, satelite1, satelite2, nuevaHora, costeTotal, listaAcciones)# Creo el estado
                #nextState.evaluarh1(elegirHeuristica) # Evaluo la heuristica
                nextState.evaluar()
                listaAbiertaNuevos.append(nextState) # Inserto el nodo en una lista auxiliar

        # Se ordena la lista bajo el criterio de la funcion de evaluacion al reves por despues
        # Voy a insertar los nodos de mayor a menor, haciendo que el que tenga menor heurisitica sea primero
        listaAbierta = sorted(listaAbiertaNuevos, key=lambda estado: estado.f, reverse=True)
        for elemento in listaAbierta:
            self.openList.insert(0,elemento)


    def isNOTSameACloseListNode(self, nodoActual):
        for nodoClose in self.closeList:
            if nodoActual.compare(nodoClose) == True:
                if nodoActual.f > nodoClose.f:
                    return False
        return True

    def isFinal(self, nodoActual):
        for i in range(len(nodoActual.matrizObservables)):
            for j in range(len(nodoActual.matrizObservables[i])):
                if nodoActual.matrizObservables[i][j] != 0:
                    return False

        if len(nodoActual.sat1.retransmisiones ) > 0 :
            #print (nodoActual.sat1.retransmisiones ) 
            return False

        if len(nodoActual.sat2.retransmisiones ) > 0 :
            return False

        return True

    def matrizIgualada(self, matriz1, matriz2):
        matrizFinal = matriz1.copy()
        for i in range(len(matriz1)):
            for j in range(len(matriz1[i])):
                if matriz1[i][j] != matriz2[i][j]:
                    matrizFinal[i][j] = 0
        return matrizFinal

    def printEstado(self, actualNode):
            print ("Satelite 1","BANDAS", actualNode.sat1.bandasActuales," Operacion", actualNode.sat1.operacion, "\n Retransmisiones", actualNode.sat1.retransmisiones)
            print ("Satelite 2","BANDAS", actualNode.sat2.bandasActuales," Operacion", actualNode.sat2.operacion, "\n Retransmisiones", actualNode.sat2.retransmisiones)
            print("Hora ", actualNode.horaActual," Heuristica", actualNode.heuristica,"Coste: ", actualNode.f, "\nLista de acciones", actualNode.acciones, "\n",actualNode.matrizObservables, "\n")