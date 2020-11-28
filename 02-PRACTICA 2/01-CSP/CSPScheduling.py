# Heuristica y Optimizacion. Practica 2. Parte 1: Asignacion de antenas de transmision a satelites   

from constraint import *

problem = Problem()

# Variables a introducir en el problema

# VARIABLES DE SATELITES

problem.addVariable('SAT1', ['ANT1', 'ANT2', 'ANT3', 'ANT4']) 
problem.addVariable('SAT2', ['ANT1', 'ANT2', 'ANT3'])
problem.addVariable('SAT3.1', ['ANT4', 'ANT6'])
problem.addVariable('SAT3.2', ['ANT7', 'ANT9', 'ANT10'])
problem.addVariable('SAT4', ['ANT8', 'ANT11', 'ANT12'])
problem.addVariable('SAT5', ['ANT1', 'ANT7', 'ANT12'])
problem.addVariable('SAT6.1', ['ANT7', 'ANT9'])
problem.addVariable('SAT6.2', ['ANT3', 'ANT4', 'ANT5'])


# VARIABLES DE ANTENAS
problem.addVariable('ANT1', ['f1','f5'])
problem.addVariable('ANT2', ['f1'])
problem.addVariable('ANT3', ['f1','f7'])
problem.addVariable('ANT4', ['f1','f2','f7'])
problem.addVariable('ANT5', ['f7'])
problem.addVariable('ANT6', ['f2'])
problem.addVariable('ANT7', ['f3','f5','f6'])
problem.addVariable('ANT8', ['f4'])
problem.addVariable('ANT9', ['f3','f6'])
problem.addVariable('ANT10', ['f3'])
problem.addVariable('ANT11', ['f4'])
problem.addVariable('ANT12', ['f4','f5'])


# Franjas que comienzan antes de las 12
franjas_antes12 = ['f1','f2','f5','f6']

# Franjas que comienzan despues de las 12
franjas_despues12 = ['f3','f4','f7']


# Restricciones
# En las restricciones se crea una funcion para cada una de ellas 

# Primera restriccion SAT1 y SAT2 deben tener la misma antena
def mismaAntena12(sat1, sat2):
    if(sat1==sat2):
        return True
    
    return False

problem.addConstraint(mismaAntena12, ('SAT1','SAT2'))


# Segunda restriccion


# Ejecucion del problema

print(problem.getSolutionS())
