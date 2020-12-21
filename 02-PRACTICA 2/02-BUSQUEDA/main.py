
#
# Clase MAIN 
# 
# Realizado por Marcelino Tena Blanco y Alejandro Díaz García
#  

from os import terminal_size
from aStar import aStar
from satelite import satelite
from nodo import nodo
import numpy as np
import time


def lecturaFichero ():
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
    f.close()
    return satelites, objetos

def escribirFichero(tiempoEjecucionAlgoritmo, costeTotal, LongitudPlan, nodosExpandidos):
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


"""------------------------ MAIN PROGRAMA -----------------------"""

def main():
    satelites, objetos = lecturaFichero()

    # Valores estáticos de los satelites
    datosEnergia = [[], []]
    for i in range(len(satelites)):
        datosEnergia[i].append(satelites[i][1][0]) # Observar
        datosEnergia[i].append(satelites[i][1][1]) # Transmitir
        datosEnergia[i].append(satelites[i][1][2]) # Girar
        datosEnergia[i].append(satelites[i][1][3]) # Uds nuevas de Energia
        datosEnergia[i].append(satelites[i][1][4]) # Total capacidad Bateria

    # --Creamos los estados Inical y Final --
    nBandas = 4  # Bandas que existen en el problema
    horas = 12  # Horas totales que pueden los satelites obtener y enviar datos

    # Matrices de observables
    obsInicial = np.zeros(shape=(nBandas, horas), dtype="int")

    # Añadir observables a la matriz de observables
    for i in range(len(objetos)):
        obsInicial[objetos[i][0]][objetos[i][1]] = i + 1

        # Crear Satelites y 
    sat1 = satelite(0, datosEnergia[0][4], [0, 1], [], "idle", obsInicial)
    sat2 = satelite(1, datosEnergia[1][4], [2, 3], [], "idle", obsInicial)

    # Crear estado Inicial
    nodoIncial = nodo(None, obsInicial, sat1, sat2, 0,0)

    # Creo el nuevo A estrella
    aEstrella = aStar(nodoIncial,  datosEnergia)

    # INICIA EL ALGORITMO 
    inicioAlgoritmo = time.time()

    aEstrella.algoritmo()

    finAlgoritmo = time.time()
    # FINALIZA EL ALGORITMO
    
    noTengoPadre = True
    actualNode = aEstrella.nodoFinal
    while noTengoPadre != False:
        print ("Hora ", actualNode.horaActual, "Satelite 1"," Operacion", actualNode.sat1.operacion, " \n"," Heuristica", actualNode.heuristica,"Coste: ", actualNode.coste, "\n Retransmisiones", actualNode.sat1.retransmisiones)
        print ("Hora ", actualNode.horaActual, "Satelite 2"," Operacion", actualNode.sat2.operacion, " \n"," Heuristica", actualNode.heuristica,"Coste: ", actualNode.coste)
        print(actualNode.matrizObservables, "\n")
        if actualNode.nodoRaiz == None:
            break
        else:
            actualNode = actualNode.nodoRaiz
    
    tiempoEjecucionAlgoritmo = finAlgoritmo - inicioAlgoritmo
    escribirFichero(tiempoEjecucionAlgoritmo, aEstrella.costeTotal, 0,aEstrella.nodosExpandidos)

main()