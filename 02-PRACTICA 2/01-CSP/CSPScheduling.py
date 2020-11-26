# Heuristica y Optimizacion. Practica 2. Parte 1: Asignacion de antenas de transmision a satelites   

from constraint import *

problem = Problem()

# Variables a introducir en el problema

# En nuestro caso seran los satelites las variables y tambien las antenas de comunicacion en tierra


"""
# Asi se definirian variables con el mismo dominio
variables = {'SAT1': 'the value of my first variable is',
             'SAT2': 'and my second variable gets'}
problem.addVariables (variables, range (10))
"""

# VARIABLES DE SATELITES
# Cada variable asociada a su dominio de horas en este caso
# TODO SE PUEDE HACER CON RANGE PERFECTAMENTE...
problem.addVariable('SAT1', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) 
problem.addVariable('SAT2', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
problem.addVariable('SAT3', [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
problem.addVariable('SAT4', [16, 17, 18, 19, 20, 21, 22, 23, 0])
problem.addVariable('SAT5', [6, 7, 8, 9, 10, 11, 12, 13])
problem.addVariable('SAT6', [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

# VARIABLES DE ANTENAS
problem.addVariable('ANT1', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
problem.addVariable('ANT2', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
problem.addVariable('ANT3', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
problem.addVariable('ANT4', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
problem.addVariable('ANT5', [13, 14, 15, 16, 17, 18, 19])
problem.addVariable('ANT6', [6, 7, 8, 9, 10, 11, 12])
problem.addVariable('ANT7', [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
problem.addVariable('ANT8', [16, 17, 18, 19, 20, 21, 22, 23, 0])
problem.addVariable('ANT9', [9, 10, 11, 12, 13, 14, 15, 16])
problem.addVariable('ANT10', [13, 14, 15, 16])
problem.addVariable('ANT11', [16, 17, 18, 19, 20, 21, 22, 23, 0])
problem.addVariable('ANT12', [6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 0])





# Restricciones
# En las restricciones se crea una funcion para cada una de ellas 





# Ejecucion del problema

print(problem.getSolutions())
