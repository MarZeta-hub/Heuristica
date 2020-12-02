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

"""
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
"""


# Creamos un diccionario para la resolucion de franjas horarias de cada satelite
# Las franjas estan codificadas como f1, f2, f3...
diccionarioFranjas = {'SAT1':"f1", 'SAT2':"f1", 'SAT3.1':"f2", 'SAT3.2':"f3", 'SAT4':"f4", 'SAT5':"f5", 'SAT6.1':"f6", 'SAT6.2':"f7"}


# Franjas que comienzan antes de las 12
franjas_antes12 = ['f1','f2','f5','f6']

# Franjas que comienzan despues de las 12
franjas_despues12 = ['f3','f4','f7']


# Restricciones
# En las restricciones se crea una funcion para cada una de ellas 

# Primera restriccion: SAT1 y SAT2 deben tener la misma antena
def mismaAntena12(sat1, sat2):
    if(sat1==sat2):
        return True
    
    return False

problem.addConstraint(mismaAntena12, ('SAT1','SAT2'))


# Segunda restriccion: SAT2, SAT4 y SAT5 tiene que tener asignadas antenas diferentes
def diferenteAntena245(sat2, sat4, sat5):
    if(sat2!=sat4 and sat2!=sat5 and sat4!=sat5):
        return True
    
    return False

problem.addConstraint(diferenteAntena245, ('SAT2','SAT4','SAT5'))


# Tercera restriccion: si SAT5 se comunica con ANT12, entonces SAT4 no se puede comunicar con ANT11
def comunicacionSAT54(sat5, sat4): 
    if(sat5=='ANT12' and sat4!='ANT11'):
        return True
    return False

problem.addConstraint(comunicacionSAT54, ('SAT5', 'SAT4'))

# Cuarta restriccion: si a una solucion se asignan las antenas ANT7 Y ANT12, se les deben asignar ambas a franjas horarias antes de las 12 o despues de las 12
#def restFranjas():
# COMPROBACION INICIAL DE SI HAN SALIDO ANT7 Y ANT12 EN LA SOLUCION, EN TAL CASO CONTINUAMOS:    
 #   if((sat32=='ANT7'or sat5=='ANT7' or sat61=='ANT7')and(sat4=='ANT12'or sat5=='ANT12')):


# Primero tenemos que comprobar que si sale por la mañana ANT7 , ENTONCES QUE SALGA POR LA MAÑANA ANT12


# Ejecucion del problema
print(problem.getSolutions())
