# Clase AStar para la practica 2 parte 2

from estado import estado
from satelite import satelite

import numpy as np

import sys
import time

def crearNodos(currentState):
    nuevaHora = currentState.getHoraActual()
    sat1 = currentState.getSat1()
    sat2 = currentState.getSat2()
    listaSat1 = []
    listaSat2 = []

    # Si el satelide debe regargar
    recargar(currentState, sat1, listaSat1, 1)
    recargar(currentState, sat2, listaSat2, 2)

    observables1 = observar(currentState, nuevaHora, sat1, listaSat1, 1)
    observables2 = observar(currentState, nuevaHora, sat2, listaSat2, 2)

    retransmitir(currentState, sat1, listaSat1, 1)
    retransmitir(currentState, sat2, listaSat2, 2)

    girar(currentState, sat1, listaSat1, 1)
    girar(currentState, sat2, listaSat2, 2)

    iddle(currentState, sat1, listaSat1, 1)
    iddle(currentState, sat2, listaSat2, 2)

    nuevaHora = nuevaHora + 1
    for satelite1 in listaSat1:
        if satelite1.getOperacion() == "Observar":
            nuevosDatos = observables1
        else:
            nuevosDatos = currentState.getFranjas()
        for satelite2 in listaSat2:
            if satelite2.getOperacion() == "Observar":
                nuevosDatos = observables1 + observables2
            print ("NodoNuevo")
            nextState = estado(currentState, nuevaHora, nuevosDatos, satelite1, satelite2, currentState.getG() + nuevaHora)


def iddle(currentState, sat, lista, idSat):
    satNuevo = satelite(idSat, sat.getEnergiaDisponible(), sat.getBandasActuales(), sat.getRetransmisiones(), "Girar")
    currentState.IDLE(sat)
    lista.append(satNuevo)

def girar(currentState, sat, listaSat, idSat):
    idSat = idSat - 1
    if sat.getEnergiaDisponible() >= costeGiro[idSat]:
        if  bandaOrigen[idSat] == sat.getBandasActuales():
            if  min(min(bandaOrigen)) < min(sat.getBandasActuales()):
                bandasNuevas = sat.getBandasActuales()[:]
                satNuevo = satelite(idSat+1, sat.getEnergiaDisponible(), bandasNuevas, sat.getRetransmisiones(), "Girar")
                currentState.girarArriba(sat, bandasNuevas)
                listaSat.append(satNuevo)
            if max(max(bandaOrigen)) > max(sat.getBandasActuales()):
                bandasNuevas = sat.getBandasActuales()[:]
                satNuevo = satelite(idSat+1, sat.getEnergiaDisponible(), bandasNuevas, sat.getRetransmisiones(), "Girar")
                currentState.girarAbajo(sat, bandasNuevas)
                listaSat.append(satNuevo)
        else:
            bandasNuevas = sat.getBandasActuales()[:]
            satNuevo = satelite(idSat+1, sat.getEnergiaDisponible(), bandasNuevas, sat.getRetransmisiones(), "Girar")
            currentState.girarEstadoInicial(sat, bandaOrigen[idSat], bandasNuevas)
            listaSat.append(satNuevo)


def retransmitir(currentState, sat,listaSat, idSat):
    if sat.getEnergiaDisponible() >= costeTransmision[idSat-1] and len(sat.getRetransmisiones()) > 0:
        listaObs = sat.getRetransmisiones()[:]
        satNuevo = satelite(idSat, sat.getEnergiaDisponible(), sat.getBandasActuales(), listaObs, "Retransmitir")
        currentState.transmitir(satNuevo)
        listaSat.append(satNuevo)

# En el caso de que un satelite pueda recargar
def recargar(currentState, sat, listaSat, idSat):
    idSat = idSat-1
    if capacidadBateria[idSat] > sat.getEnergiaDisponible():
        satNuevo = satelite(idSat + 1, sat.getEnergiaDisponible(), sat.getBandasActuales(), sat.getRetransmisiones(), "Recargar")
        currentState.carga(satNuevo, capacidadBateria[idSat], udsRecarga[idSat])
        listaSat.append(satNuevo)

def observar(currentState, horaActual, sat, listaSat, idSat):
    franjas = currentState.getFranjas()
    devolverFranjas = []
    if sat.getEnergiaDisponible() >= costeObservacion[idSat-1]: 
        if franjas[sat.getBandasActuales()[0]][horaActual] != 0:
            listaObs = sat.getRetransmisiones()[:]
            satNuevo = satelite(idSat, sat.getEnergiaDisponible(), sat.getBandasActuales(), listaObs, "Observar")
            devolverFranjas = currentState.observarArriba(satNuevo)
            listaSat.append(satNuevo)
        if franjas[sat.getBandasActuales()[1]][horaActual] != 0:
            listaObs = sat.getRetransmisiones()[:]
            satNuevo = satelite(idSat, sat.getEnergiaDisponible(), sat.getBandasActuales(), listaObs, "Observar")
            devolverFranjas = currentState.observarAbajo(satNuevo)
            listaSat.append(satNuevo)
    return devolverFranjas



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
bandaOrigen = [[0,1], [2,3]]
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

# Crear Satelites
sat1 = satelite(satelites[0][0], capacidadBateria[0], bandaOrigen[0], transmisiones1, "iddle")
sat2 = satelite(satelites[1][0], capacidadBateria[1], bandaOrigen[1], transmisiones2, "iddle")

# --Creamos los estados Inical y Final --
nBandas = 4  # Bandas que existen en el problema
horas = 12  # Horas totales que pueden los satelites obtener y enviar datos

# Matrices de observables
obsInicial = np.zeros(shape=(nBandas, 12), dtype="int")
obsFinal = np.zeros(shape=(nBandas, 12), dtype="int")

# Añadir observables a la matriz de observables
for i in range(len(objetos)):
    obsInicial[objetos[i][0]][objetos[i][1]] = i + 1

# Crear estado Inicial y Final
estadoIncial = estado(None, 0, obsInicial, sat1, sat2, 0)
estadoFinal = estado(None, 0,  obsFinal, sat1, sat2, 0)

iFound = False  # Si es solucion
openList = []  # Estados que faltan por analizar
closeList = []  # Estados ya analizados

# CALCULAR HEURISTICA INICIAL Y FINAL

# Algoritmo A* implementado

inicioAlgoritmo = time.time()

crearNodos(estadoIncial)

""" TODO INSERTAR AQUI ALGORITMO """


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


