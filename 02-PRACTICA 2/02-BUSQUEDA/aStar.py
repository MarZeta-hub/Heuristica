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
#-----------------------------------------------------------------

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
            self.nodosExpandidos +=1

            # Comprobar si el nodo es igual en la lista de cerrados

            # Comprobar si el nodo es Final
            self.closeList.append(estadoActual)

            self.crearNodos(estadoActual)



    def crearNodos(self, nodoActual):
        
        # Obtengo datos relativos a todos los nodos
        satelites = [nodoActual.sat1, nodoActual.sat2]
        hora = nodoActual.horaActual
        matrizObservables = nodoActual.matrizObservables
        listaSat = []
        bOrigen = [ [0,1], [2,3] ]

        # Busco todas las operaciones que puede hacer los satelites
        for i in range (0,2):
            tmp = []
            # Bandas del satelite i
            bandas = satelites[i].bandasActuales
            listaObs = satelites[i].retransmisiones
            # Observar
            if self.gastoEnergia[i][0] <= satelites[i].energiaDisponible:
                for j in range(0,2):
                    if matrizObservables[bandas[j]][hora] != 0:

                        # Creo la matriz nueva 
                        matriz = matrizObservables.copy()

                        # Lista de observables nueva por añado uno nuevo
                        listaObsN = satelites[i].retransmisiones.copy()
                        nuevoDato = 'O'+str(matrizObservables[bandas[i]][hora])
                        listaObsN.append(nuevoDato)
                        matriz[bandas[i]][hora] = 0
                        
                        # Creo el satelite y lo añado a la lista de satelites
                        gastoEnergia =  satelites[i].energiaDisponible - self.gastoEnergia[i][0]
                        satNuevo = satelite(i, gastoEnergia, bandas, listaObsN, "Observar")
                        tmp.append(satNuevo) # Add el satelite a la lista de satelites

            # Transmitir
            if self.gastoEnergia[i][1] <= satelites[i].energiaDisponible:
                
                if len(satelites[i].retransmisiones.copy()) != 0:

                    # Creo la nueva lista de observables
                    listaObsN = satelites[i].retransmisiones.copy()
                    listaObsN.pop(0)

                    # Creo el satelite y lo añado a la lista de satelites
                    gastoEnergia =  satelites[i].energiaDisponible - self.gastoEnergia[i][1]
                    satNuevo = satelite(i, gastoEnergia, bandas, listaObsN, "Retransmitir")
                    tmp.append(satNuevo) # Add el satelite a la lista de satelites
                   
            # Girar
            if self.gastoEnergia[i][2] <= satelites[i].energiaDisponible:
                if bOrigen[i] == bandas:
                    if min(min(bOrigen)) < min(bandas):
                        bandasNuevas = bandas.copy()

                        # Resto uno a todas las bandas actuales
                        bandasNuevas[0] = bandasNuevas[0]-1
                        bandasNuevas[1] = bandasNuevas[1]-1

                        # Creo el satelite y lo añado a la lista de satelites
                        gastoEnergia =  satelites[i].energiaDisponible - self.gastoEnergia[i][2]
                        satNuevo = satelite(i, gastoEnergia, bandasNuevas, listaObs, "Girar")
                        tmp.append(satNuevo) # Add el satelite a la lista de satelites

                    # En el caso de que el MAXIMO de TODAS LAS BANDAS ORIGENES sean mayores que el MAXIMO de las bandas actuales
                    if max(max(bOrigen)) > max(bandas):
                        bandasNuevas = bandas.copy()

                        # Sumo uno a todas las bandas actuales
                        bandasNuevas[0] = bandasNuevas[0]+1
                        bandasNuevas[1] = bandasNuevas[1]+1

                        # Creo el satelite y lo añado a la lista de satelites
                        gastoEnergia =  satelites[i].energiaDisponible - self.gastoEnergia[i][2]
                        satNuevo = satelite(i, gastoEnergia, bandasNuevas, listaObs, "Girar")
                        tmp.append(satNuevo) # Add el satelite a la lista de satelites

                    # En el caso que la banda origen sea DISTINTA  a las bandas actuales
                else:
                    bandasNuevas =  bandas.copy()

                    # Restauro las bandas
                    bandasNuevas[0] = bandasNuevas[0]
                    bandasNuevas[1] = bandasNuevas[1]

                    # Creo el satelite y lo añado a la lista de satelites
                    gastoEnergia = satelites[i].energiaDisponible - self.gastoEnergia[i][2]  
                    satNuevo = satelite(i, gastoEnergia, bandasNuevas, listaObs, "Girar")
                    tmp.append(satNuevo) # Add el satelite a la lista de satelites

            # Recargar
            if self.gastoEnergia[i][4] > satelites[i].energiaDisponible:
                    carga = satelites[i].energiaDisponible  # Obtengo el valor actual de la bateria
                    carga = carga + self.gastoEnergia[i][3] # Cargo la bateria

                    # Si la bateria cargada es mayor que la capacidad
                    if carga >= self.gastoEnergia[i][4]:
                        carga = self.gastoEnergia[i][4]    # Lo igualo a la capacidad

                    # Creo el satelite y lo añado a la lista de satelites
                    satNuevo = satelite(i, carga, bandas, listaObs, "Recargar")
                    tmp.append(satNuevo) # Add el satelite a la lista de satelites

            # No hacer Nada / IDLE
            # Creo el satelite y lo añado a la lista de satelites
            satNuevo = satelite(i, satelites[i].energiaDisponible, bandas, listaObs, "Recargar")
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
        matrizFinal = matrizObservables
        # Un estado se compone  de dos satelites
        for satelite1 in listaSat[0]:
            for satelite2 in listaSat[1]:
                nextState = nodo(nodoActual, matrizFinal, satelite1, satelite2, nuevaHora, costeTotal)# Creo el estado
                #nextState.evaluarh1() # Evaluo la heuristica
                listaAbiertaNuevos.append(nextState) # Inserto el nodo en una lista auxiliar

        # Se ordena la lista bajo el criterio de la funcion de evaluacion al reves por despues
        # Voy a insertar los nodos de mayor a menor, haciendo que el que tenga menor heurisitica sea primero
        listaAbierta = sorted(listaAbiertaNuevos, key=lambda estado: estado.f, reverse=True)
        for elemento in listaAbierta:
            self.openList.insert(0,elemento)    



            
