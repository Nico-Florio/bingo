# 109880 - Nicolas Florio Toursarkissian
# Algoritmos y Programacion I - Catedra Costa
# Trabajo Practico 1
# 2 Cuatrimestre 2022

'''BINGO'''

import os
import random
import time


def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def generar_carton():
    carton = []
    for i in range(9):
        carton.append([])
        for j in range(3):
            carton[i].append(0)
    for i in range(9):
        for j in range(3):
            if i == 0:
                carton[i][j] = random.randint(1, 11)
            elif i == 1:
                carton[i][j] = random.randint(12, 22)
            elif i == 2:
                carton[i][j] = random.randint(23, 33)
            elif i == 3:
                carton[i][j] = random.randint(34, 44)
            elif i == 4:
                carton[i][j] = random.randint(45, 55)
            elif i == 5:
                carton[i][j] = random.randint(56, 66)
            elif i == 6:
                carton[i][j] = random.randint(67, 77)
            elif i == 7:
                carton[i][j] = random.randint(78, 88)
            elif i == 8:
                carton[i][j] = random.randint(89, 99)
    return carton


def juego():
    cartones_del_jugador = []
    cls()
    nombre_de_jugador: str = input("Ingrese su nombre: ").capitalize()
    cantidad_de_cartones: str = input(f"{nombre_de_jugador}, ingrese la cantidad de cartones que quiere adquuirir: ")

    cartones = []
    for i in range(cantidad_de_cartones):
        cartones.append(generar_carton())
        print(cartones[i])


def menu_principal():
    opcion: str = input("Ingrese una opcion: ")
    while not opcion.isdigit():
        print("Opcion invalida")
        opcion: str = input("Ingrese una opcion: ")
    if opcion == 1:
        juego()
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        print("Gracias por jugar!")
        time.sleep(1)
        cls()
        exit()



def main():
    cls()
    time.sleep(1)
    print("cantalo...")
    time.sleep(1)
    print("cantalo...")
    time.sleep(1)
    print("BINGO!")
    time.sleep(1)
    print('''
[1] Jugar
[2] Tabla de premios
[3] Como Funciona
[4] Historial de partidas
[5] Salir''')
    menu_principal()



juego()
