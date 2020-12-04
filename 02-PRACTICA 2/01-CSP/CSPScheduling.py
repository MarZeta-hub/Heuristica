# Heuristica y Optimizacion. Practica 2. Parte 1: Asignacion de antenas de transmision a satelites   

from constraint import *
import numpy as np

problem = Problem()

# VARIABLES DE SATELITES
satelites = ['SAT1','SAT2','SAT3.1','SAT3.2','SAT4','SAT5','SAT6.1','SAT6.2']

problem.addVariable('SAT1', ['ANT1', 'ANT2', 'ANT3', 'ANT4']) 
problem.addVariable('SAT2', ['ANT1', 'ANT2', 'ANT3'])
problem.addVariable('SAT3.1', ['ANT4', 'ANT6'])
problem.addVariable('SAT3.2', ['ANT7', 'ANT9', 'ANT10'])
problem.addVariable('SAT4', ['ANT8', 'ANT11', 'ANT12'])
problem.addVariable('SAT5', ['ANT1', 'ANT7', 'ANT12'])
problem.addVariable('SAT6.1', ['ANT7', 'ANT9'])
problem.addVariable('SAT6.2', ['ANT3', 'ANT4', 'ANT5'])

# Restricciones
# En las restricciones se crea una funcion para cada una de ellas 

# Primera restriccion: SAT1 y SAT2 deben tener la misma antena

# Se puede hacer con una restriccion ya creada
problem.addConstraint(AllEqualConstraint(),['SAT1','SAT2'])


# Se puede usar una restriccion ya incluida en python constraint
problem.addConstraint(AllDifferentConstraint(), ['SAT2','SAT4','SAT5'])


# Tercera restriccion: si SAT5 se comunica con ANT12, entonces SAT4 no se puede comunicar con ANT11
def comunicacionSAT54(sat5, sat4): 

    if(sat5=='ANT12' and sat4=='ANT11'): 
        return False
    return True

problem.addConstraint(comunicacionSAT54, ('SAT5', 'SAT4'))


# Cuarta restriccion: si a una solucion se asignan las antenas ANT7 Y ANT12, se les deben asignar ambas a franjas horarias antes de las 12 o despues de las 12
# FIXME HACER GENERALIZABLE LA RESTRICCION, SINO QUITA PUNTOS???
def restFranjas(sat32, sat5, sat61, sat4):

    if(sat32=='ANT7' and sat5=='ANT12'):
        return False
    if(sat5=='ANT7' and sat4=='ANT12'):
        return False
    if(sat61=='ANT7' and sat4=='ANT12'):
        return False
    return True
    

problem.addConstraint(restFranjas, ('SAT3.2','SAT5','SAT6.1','SAT4'))


# Ejecucion del problema

solution = problem.getSolution()
print(solution)

solutions = problem.getSolutions()
print(len(solutions))


# Salida por archivo con todas las soluciones

f = open("solutions.txt", "w")
np.savetxt(f,solutions, delimiter='   ', fmt='%s')
f.close()

# TODO -LIMPIAR CODIGO