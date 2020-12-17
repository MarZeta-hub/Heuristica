# Clase estado para la practica 2 parte 2

class estado():

    # Nodo del arbol padre (Para recorrerlo inversamente)
    nodoPadre = None

    # Hora actual en la que se encuentra el estado
    horaActual = 0
    
    # Energia disponible para cada satelite
    energiaDisponible = []
    
    # Bandas que esta utilizando actualmente cada satelite
    bandasActuales =[][]

    # Puntos de observacion disponibles (su posicion y hora) 
    observables = [][]
    
    # Son las observaciones pendientes de ser transmitidas, despues de ser observadas
    retransmisiones = [][]
    
    # Valor de la funcion heuristica 
    h = None

    # Valor de la funcion de coste utilizada
    g = None

    # Valor de la funcion de evaluacion
    f = None

    # Funcion constructor
    def __init__(self, nodoPadre ,horaActual, energiaDisponible, bandasActuales, observables, retransmisiones ):



