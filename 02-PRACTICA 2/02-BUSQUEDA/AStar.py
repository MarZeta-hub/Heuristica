# Clase AStar para la practica 2 parte 2

from estado import estado

import sys
import time


# Entrada de fichero
f = open('problema.prob')

# Obtenemos los observadores
inicio = f.read(5)

inicio = inicio[:3]

# Caso de error fallo de formato fichero de entrada
if(inicio != 'OBS'):
    raise Exception ('Error, formato fichero de entrada incorrecto')
    


# Saltamos la cabecera de la primera linea de OBS y separamos por coordenadasS
#f.seek(5)
OBS =f.readline().split(';')

# Objetos es la lista de listas de numeros enteros que se corresponden con las coordenadas de los objetos visibles
objetos = []
for i in OBS:
    lista = []
    a = i.replace(')','').replace('(','').split(',')
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
    b= a[1].split(';')
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




# Algoritmo A* implementado 
inicioAlgoritmo = time.time()









""" TODO INSERTAR AQUI ALGORITMO """








finAlgoritmo = time.time()


tiempoEjecucionAlgoritmo = finAlgoritmo - inicioAlgoritmo



# Salida del fichero de estadisticas

f = open("problema.prob.statistics", "w")

time = "Tiempo total: %f \n"%tiempoEjecucionAlgoritmo
totalcost = "Coste total: %i \n"%costeTotal
longPlan = "Longitud del plan: %i \n"%LongitudPlan
expandedNodes = "Nodos expandidos: %i \n"%nodosExpandidos

f.write(time)
f.write(totalcost)
f.write(longPlan)
f.write(expandedNodes)

f.close()