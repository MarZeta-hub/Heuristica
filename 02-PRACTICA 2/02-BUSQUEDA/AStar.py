# Clase AStar para la practica 2 parte 2

f = open('problema.prob')

# Obtenemos los observadores
f.seek(5)
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

