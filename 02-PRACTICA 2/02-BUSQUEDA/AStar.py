# Clase AStar para la practica 2 parte 2

from estado import estado
from satelite import satelite

import numpy as np

import sys
import time


def crearNodos(currentState, openListActual):
    # Obtengo la hora del nodo actual
    nuevaHora = currentState.getHoraActual()

    # Obtengo los satelites
    sat1 = currentState.getSat1()
    sat2 = currentState.getSat2()

    # Creo las listas de los satelites para despues crear los nodos
    listaSat1 = []
    listaSat2 = []

    # Si el satelide debe regargar
    recargar(sat1, listaSat1, 1)
    recargar(sat2, listaSat2, 2)

    # Para crear satelites que tienen que transmitir
    retransmitir(currentState, sat1, listaSat1, 1)
    retransmitir(currentState, sat2, listaSat2, 2)

    # Para crear satelites que tienen que girar
    girar(currentState, sat1, listaSat1, 1)
    girar(currentState, sat2, listaSat2, 2)

    # Para crear satelites que no hacen nada
    idle(sat1, listaSat1, 1)
    idle(sat2, listaSat2, 2)

    # Para crear satelites que tienen que observar
    observar(nuevaHora, sat1, listaSat1, 1)
    observar(nuevaHora, sat2, listaSat2, 2)

    # Obtengo la nueva hora que tiene que tener el siguiente nodo
    nuevaHora = nuevaHora + 1
    coste = currentState.getG()+1
    # En el caso de que llegue a 12
    if(nuevaHora == 12):
        # Reseteo la hora a 0
        nuevaHora = 0
        coste = coste + 11

    # Ahora voy a crear los nuevos estados
    listaAbiertaNuevos = []
    # Un estado se compone  de dos satelites
    for satelite1 in listaSat1:
        for satelite2 in listaSat2:
            # TODO CREAR UNA MATRIZ TOTAL CON LAS COSAS DE AMBAS
            nextState = estado(currentState, nuevaHora, satelite1, satelite2, coste)# Creo el estado
            nextState.evaluarh1() # Evaluo la heuristica
            nextState.setEvaluacion() # Añado la funcion heuristica
            listaAbiertaNuevos.append(nextState) # Inserto el nodo en una lista auxiliar

    # Se ordena la lista bajo el criterio de la funcion de evaluacion al reves por despues
    # Voy a insertar los nodos de mayor a menor, haciendo que el que tenga menor heurisitica sea primero
    listaAbierta = sorted(listaAbiertaNuevos, key=lambda estado: estado.getF(), reverse=True)
    for elemento in listaAbierta:
        openListActual.insert(0,elemento)
    


""" FUNCION IDLE: ESPERA SIN GASTAR BATERIA """
def idle(sat, lista, idSat):
    # Creo el satelite
    satNuevo = satelite(idSat, sat.getEnergiaDisponible(), sat.getBandasActuales(), sat.getMatrizObservable(),sat.getRetransmisiones(), "idle")
    #print('SAT', sat.getId(), ' IDLE')
    lista.append(satNuevo) # Add el satelite a la lista de satelites



""" FUNCION GIRAR: EXISTE TRES FORMAS DE GIRAR, HACIA ARRIBA, HACIA ABAJO O VOLVER AL LUGAR INICIAL"""
def girar(currentState, sat, listaSat, idSat):
    idSat = idSat - 1 # Los arrays comienzan en 0 no en 1

    # Consigo el coste final de realizar la operacion GIRAR
    costeEnergia = sat.getEnergiaDisponible() - costeGiro[idSat]

    # Si existe suficiente energia
    if costeEnergia >= 0:

        # En el caso que la banda origen sea igual que las bandas actuales
        if bandaOrigen[idSat] == sat.getBandasActuales():

            # En el caso de que el MINIMO de TODAS LAS BANDAS ORIGENES sea menor que el MINIMO de las bandas actuales
            if min(min(bandaOrigen)) < min(sat.getBandasActuales()):
                bandasNuevas = sat.getBandasActuales().copy()

                 # Resto uno a todas las bandas actuales
                bandasNuevas[0] = bandasNuevas[0]-1
                bandasNuevas[1] = bandasNuevas[1]-1
                #print('SAT', sat.getId(), ' gira a ', bandasNuevas)

                # Creo el satelite y lo añado a la lista de satelites
                satNuevo = satelite(idSat+1, (sat.getEnergiaDisponible() - costeGiro[idSat]), bandasNuevas, sat.getMatrizObservable(), sat.getRetransmisiones(), "Girar")
                listaSat.append(satNuevo) # Add el satelite a la lista de satelites

            # En el caso de que el MAXIMO de TODAS LAS BANDAS ORIGENES sean mayores que el MAXIMO de las bandas actuales
            if max(max(bandaOrigen)) > max(sat.getBandasActuales()):
                bandasNuevas = sat.getBandasActuales().copy()

                # Sumo uno a todas las bandas actuales
                bandasNuevas[0] = bandasNuevas[0]+1
                bandasNuevas[1] = bandasNuevas[1]+1
                #print('SAT', sat.getId(), ' gira a ', bandasNuevas)

                # Creo el satelite y lo añado a la lista de satelites
                satNuevo = satelite(idSat+1, (sat.getEnergiaDisponible() - costeGiro[idSat]), bandasNuevas, sat.getMatrizObservable(), sat.getRetransmisiones(), "Girar")
                listaSat.append(satNuevo) # Add el satelite a la lista de satelites

        # En el caso que la banda origen sea DISTINTA  a las bandas actuales
        else:
            bandasNuevas = sat.getBandasActuales().copy()

            # Restauro las bandas
            bandasNuevas[0] = bandasNuevas[0]
            bandasNuevas[1] = bandasNuevas[1]

            print('SAT', sat.getId(), ' gira a ', bandasNuevas)

            # Creo el satelite y lo añado a la lista de satelites
            satNuevo = satelite(idSat+1, (sat.getEnergiaDisponible() - costeGiro[idSat]), bandasNuevas, sat.getRetransmisiones(), "Girar")
            listaSat.append(satNuevo) # Add el satelite a la lista de satelites



def retransmitir(currentState, sat, listaSat, idSat):

    # Obtengo la energia final una vez realizada la accion
    costeEnergia = sat.getEnergiaDisponible() - costeObservacion[idSat-1]

    # Si la energia es mayor que 0 o tengo cosas en transmisiones
    if costeEnergia >=0 and len(sat.getRetransmisiones()) > 0:
        
        # Copio la lista de transmisiones
        listaObs = sat.getRetransmisiones().copy()
        
        # Y lo transmito
        transmitido = listaObs.pop(0)
        #print('SAT', sat.idSat, ' transmite ', transmitido)

        # Creo el satelite y lo añado a la lista de satelites
        satNuevo = satelite(idSat, costeEnergia, sat.getBandasActuales(), sat.getMatrizObservable(), listaObs, "Retransmitir")
        listaSat.append(satNuevo) # Add el satelite a la lista de satelites



""" Solo se puede regargar de una forma """
def recargar(sat, listaSat, idSat):
    idSat = idSat-1 # Recorto idSat porque los arrays comienzan en 0 no en 1
    totalBateria = capacidadBateria[idSat] # Obtengo el total de la bateria
    carga = sat.getEnergiaDisponible()# Obtengo el valor actual de la bateria

    # Si el total de la bateria es mayor que la bateria disponible
    if totalBateria > sat.getEnergiaDisponible():
        carga = carga + udsRecarga[idSat] # Cargo la bateria

        # Si la bateria cargada es mayor que la capacidad
        if carga >= totalBateria:
            carga = totalBateria# Lo igualo a la capacidad
        print('SAT',sat.idSat,' ha recargado bateria')

        # Creo el satelite y lo añado a la lista de satelites
        satNuevo = satelite(idSat + 1, carga, sat.getBandasActuales(), sat.getMatrizObservable(),sat.getRetransmisiones(), "Recargar")
        listaSat.append(satNuevo) # Add el satelite a la lista de satelites



""" Se pueden observar dos bandas a la vez por lo que puedo obtener dos satelites """
def observar(hora, sat, listaSat, idSat):
    matrizObservable = sat.getMatrizObservable() # Obtengo la matriz de observables inicial
    bActual = sat.getBandasActuales() # Obtengo las bandas actuales donde está el satelite

    # Obtengo la energia final con la que se queda el satelite
    costeEnergia = sat.getEnergiaDisponible() - costeObservacion[idSat-1]

    if costeEnergia >= 0:
        # Si la celda es distinto de 0
        if matrizObservable[bActual[0]][hora] != 0:

            # Obtengo copias tanto de la lista de observables como la de transmisiones
            matrizNueva = matrizObservable.copy()
            listaObs = sat.getRetransmisiones().copy()

            #Añado el dato a la lista de transmisiones y lo elimino de la de observables
            nuevoDato = 'O'+str(matrizNueva[bActual[0]][hora])
            matrizNueva[bActual[0]][hora] = 0
            listaObs.append(nuevoDato)

            #print('SAT', sat.getId(), ' observa ', nuevoDato)
            
            # Creo el satelite y lo añado a la lista de satelites
            satNuevo = satelite(idSat, costeEnergia, bActual, matrizNueva, listaObs, "Observar")
            listaSat.append(satNuevo) # Add el satelite a la lista de satelites
        
        # Si la celda es distinto de 0
        if matrizObservable[bActual[1]][hora] != 0:

            # Obtengo copias tanto de la lista de observables como la de transmisiones
            matrizNueva = matrizObservable.copy()
            listaObs = sat.getRetransmisiones().copy()

            #Añado el dato a la lista de transmisiones y lo elimino de la de observables
            nuevoDato = 'O'+str(matrizNueva[bActual[1]][hora])
            matrizNueva[bActual[1]][hora] = 0
            listaObs.append(nuevoDato)
            #print('SAT', sat.getId(), ' observa ', nuevoDato)

            # Creo el satelite y lo añado a la lista de satelites
            satNuevo = satelite(idSat, costeEnergia, bActual, matrizNueva, listaObs, "Observar")
            listaSat.append(satNuevo) # Add el satelite a la lista de satelites



"""---------------------------------------------------------------------------------------------------------------"""



# Entrada de fichero
f = open('problema.prob')

# Obtenemos los observadores
inicio = f.read(5)

inicio = inicio[:3]

# Caso de error fallo de formato fichero de entrada
if(inicio != 'OBS'):
    raise Exception('Error, formato fichero de entrada incorrecto')

# Saltamos la cabecera de la primera linea de OBS y separamos por coordenadasS
# f.seek(5)
OBS = f.readline().split(';')

# Objetos es la lista de listas de numeros enteros que se corresponden con las coordenadas de los objetos visibles
objetos = []
for i in OBS:
    lista = []
    a = i.replace(')', '').replace('(', '').split(',')
    lista.append(int(a[0]))
    lista.append(int(a[1]))

    objetos.append(lista)

print(objetos)

# Obtencion de las caracteristicas de cada uno de los satelites

# Lista donde se van a guardar las caracteristicas de los satelites
satelites = []

# Sacamos los satelites que existen del fichero con sus caracteristicas con el formato: [id, [Caracteristicas]]
contador = 1
for reader in f:
    sat = []
    a = reader.split(' ')

    sat.append(contador)

    # Separamos por ; para obtener los parametros
    b = a[1].split(';')
    # Realizamos una conversion a numeros enteros
    c = []
    for j in b:
        c.append(int(j))

    sat.append(c)

    satelites.append(sat)
    contador = contador+1

print(satelites)

f.close()

# Variables globales para las estadisticas
nodosExpandidos = 0
costeTotal = 0
LongitudPlan = 0  # FIXME ESTO ES LA PROFUNDIDAD DEL ARBOL??

# --Creamos Los Satélites--
# Crear las variables
bandaOrigen = [[0, 1], [2, 3]]
costeObservacion = []
costeTransmision = []
costeGiro = []
udsRecarga = []
capacidadBateria = []
# Crear Transmisiones
transmisiones1 = []
transmisiones2 = []

# Valores estáticos de los satelites
for i in range(len(satelites)):
    costeObservacion.append(satelites[i][1][0])
    costeTransmision.append(satelites[i][1][1])
    costeGiro.append(satelites[i][1][2])
    udsRecarga.append(satelites[i][1][3])
    capacidadBateria.append(satelites[i][1][4])

# --Creamos los estados Inical y Final --
nBandas = 4  # Bandas que existen en el problema
horas = 12  # Horas totales que pueden los satelites obtener y enviar datos

# Matrices de observables
obsInicial = np.zeros(shape=(nBandas, 12), dtype="int")
obsFinal = np.zeros(shape=(nBandas, 12), dtype="int")

# Añadir observables a la matriz de observables
for i in range(len(objetos)):
    obsInicial[objetos[i][0]][objetos[i][1]] = i + 1

# Crear Satelites
sat1 = satelite(satelites[0][0], capacidadBateria[0], bandaOrigen[0], obsInicial, transmisiones1, "iddle")
sat2 = satelite(satelites[1][0], capacidadBateria[1], bandaOrigen[1], obsInicial, transmisiones2, "iddle")
estadoIncial = estado(None, 0, sat1, sat2, 0)

sat1 = satelite(satelites[0][0], capacidadBateria[0], bandaOrigen[0], obsFinal, transmisiones1, "iddle")
sat2 = satelite(satelites[1][0], capacidadBateria[1], bandaOrigen[1], obsFinal, transmisiones2, "iddle")
estadoFinal = estado(None, 0, sat1, sat2, 0)
# Crear estado Inicial y Final



isFound = False  # Si es solucion
openList = []  # Estados que faltan por analizar
closeList = []  # Estados ya analizados

# CALCULAR HEURISTICA INICIAL Y FINAL

# Algoritmo A* implementado


inicioAlgoritmo = time.time()


# Aqui se elige la heuristica que se va a utilizar
estadoIncial.evaluarh1()
estadoIncial.setEvaluacion()

openList.append(estadoIncial)

# Estado actual que va viendo cada
estadoActual = None
i=0
#while(len(openList) != 0):
while i < 10:
    
    estadoActual = openList.pop(0)
    i = i+1
    print ("hora", estadoActual.getHoraActual(), estadoActual.getSat1().getOperacion())
    print (estadoActual.getSat1().getEnergiaDisponible(), "\n")
    #print (estadoActual.getH())
    #print (estadoActual.getSat1().getMatrizObservable(),"\n")
    
    # TODO verificar si el nodo es igual a otro con menor coste que el generado, de no ser igual, se añade a la lista cerrada

    closeList.append(estadoActual)

    # FIXME ESTO TIENE QUE SER COMPARADO CON UNA FUNCION DE COMPARE PARA LOS PARAMETROS QUE SEAN NECESARIOS
    """if(estadoActual.compare(estadoFinal)):
        
        # Fin del problema
        estadoFinal = estadoActual
        isFound = True
        break"""
        
    crearNodos(estadoActual, openList )

"""
for i in closeList:
    print (i.getSat1().getMatrizObservable())"""

""" TODO 
def checkNode(node):
    for i in closeList:
        if(compare(i,node)):
"""

finAlgoritmo = time.time()


tiempoEjecucionAlgoritmo = finAlgoritmo - inicioAlgoritmo


# Salida del fichero de estadisticas

f = open("problema.prob.statistics", "w")

time = "Tiempo total: %f \n" % tiempoEjecucionAlgoritmo
totalcost = "Coste total: %i \n" % costeTotal
longPlan = "Longitud del plan: %i \n" % LongitudPlan
expandedNodes = "Nodos expandidos: %i \n" % nodosExpandidos

f.write(time)
f.write(totalcost)
f.write(longPlan)
f.write(expandedNodes)

f.close()
