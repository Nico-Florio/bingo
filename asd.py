from random import *

for e in range(10):

    valores_posibles:list = [] # lista 
    for i in range(9):
        tira_de_numeros = []
        for j in range((11*i)+1,(11*(i+1))+1):
            tira_de_numeros.append(j)
        valores_posibles.append(tira_de_numeros)

    carton = []
    for i in range(3):
        fila = []
        for j in range(9):
            numero_a_agregar = choice(valores_posibles[j])
            fila.append(numero_a_agregar)
            valores_posibles[j].remove(numero_a_agregar)
        carton.append(fila)
    for fila in carton:
        print(fila)
    print()