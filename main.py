# 109880 - Nicolas Florio Toursarkissian
# Algoritmos y Programacion I - Catedra Costa
# Trabajo Practico 1
# 2 Cuatrimestre 2022

'''BINGO'''

import os
import random
import msvcrt
import time
from colorama import *


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


def generar_bolillero():
    bolillero = []
    for i in range(1, 100):
        bolillero.append(i)
    return bolillero


def jugada(bolillero):
    bolilla = random.choice(bolillero)
    return bolilla


def juego():
    partida_terminada:bool = False
    while not partida_terminada:
        cls()
        ronda: int = 1
        bolillero = generar_bolillero()
        nombre_de_jugador: str = input("Ingrese su nombre: ").capitalize()
        cantidad_de_cartones: str = input(f"{nombre_de_jugador}, ingrese la cantidad de cartones(min 1, max 5) que quiere adquuirir: ")
        cartones_del_jugador = []
        cartones_de_la_maquina = []
        for i in range(int(cantidad_de_cartones)):
            cartones_del_jugador.append(generar_carton())
        for i in range(10 - int(cantidad_de_cartones)):
            cartones_de_la_maquina.append(generar_carton())
        for i in range(len(cartones_del_jugador)):
            print()
            print()
            print(f"Carton {i+1}:")
            print()
            for j in range(9):
                print(cartones_del_jugador[i][j])
        comenzar: str = input("Presione cualquier tecla para comenzar a jugar: ")
        msvcrt.getch()
        cls()
        time.sleep(1)
        print("Comienza el juego!")
        time.sleep(3)
        cls()
        print(Fore.BLUE + '''
        COMANDOS: 
        coordenadas x,y para marcar, 
        m para ver tableros de la maquina, j para ver tableros del jugador,"
        "bingo o linea para cantar bingo o linea, 
        enter para continuar''' + Style.RESET_ALL)

        print(f"RONDA {ronda}")
        time.sleep(1)
        tirada: int = jugada(bolillero)
        print(f"La bolilla es: {tirada}")
        for i in range(len(cartones_de_la_maquina)):
            for j in range(9):
                for k in range(3):
                    if cartones_de_la_maquina[i][j][k] == tirada:
                        cartones_de_la_maquina[i][j][k] = "x"
        comando: str = input("ingrese un comando: ")
        while comando != "":
            if comando.isnumeric():
                coordenadas = comando.split(",")
                x = int(coordenadas[0])
                y = int(coordenadas[1])
                if cartones_del_jugador[x][y] == tirada:
                    cartones_del_jugador[x][y] = "x"
                comando: str = input("ingrese un comando: ")
            elif comando == "m":
                for i in range(len(cartones_de_la_maquina)):
                    print()
                    print()
                    print(f"Carton {i+1}:")
                    print()
                    for j in range(9):
                        print(cartones_de_la_maquina[i][j])
                        comando: str = input("ingrese un comando: ")
            elif comando == "j":
                for i in range(len(cartones_del_jugador)):
                    print()
                    print()
                    print(f"Carton {i+1}:")
                    print()
                    for j in range(9):
                        print(cartones_del_jugador[i][j])
                comando: str = input("ingrese un comando: ")
            elif comando == "bingo":
                pass
            elif comando == "linea":
                pass




def tabla_de_premios():
    cls()

    time.sleep(1)
    print('''
PREMIOS:
Linea: 2000 pesos
Bingo: 58000 pesos''')
    time.sleep(2)
    continuar = input("Presione cualquier tecla para continuar...")
    msvcrt.getch()
    cls()


def como_funciona():
    cls()
    time.sleep(1)
    print('''
COMO FUNCIONA:
Este trabajo práctico consiste en crear un juego de Bingo para ser jugado contra la PC.''')
    time.sleep(2)
    print('''
El mismo consiste en que un jugador pueda adquirir entre 1 a 5 cartones entre un total de 10 
(no pueden existir cartones iguales), de modo que el resto de los cartones sean jugados por 
la PC, por ejemplo si el usuario adquiere 2 cartones, la máquina jugará con 8.''')
    time.sleep(2)
    print('''
Los cartones estarán formados por 9 columnas y 3 filas, haciendo un total de 27 celdas. Cada 
cartón contará con 5 números por cada fila, haciendo un total de 15 números por cartón. La 
columna 1 podrá tener del 1 al 11 como valores posibles, la 2 del 12 al 22… así hasta 
completar todas las columnas. Los mismos no pueden estar repetidos dentro de un cartón. Los 
cartones tanto del usuario como de la máquina se generan aleatoriamente. ''')
    time.sleep(2)
    print('''
La cantidad de bolillas disponibles serán de 1 a 99, y en cada jugada se sacará una al azar, 
automáticamente la máquina tachará sus casilleros y en cambio el usuario lo hará en forma 
manual. ''')
    time.sleep(2)
    print('''
El usuario en cada jugada tendrá la posibilidad de cantar línea o Bingo (Ver tabla de premios), 
en forma manual, mientras que la PC lo hará en forma automática y al finalizar la partida el 
juego deberá mostrar quién fue el ganador y el valor en $ ganado. ''')
    time.sleep(2)
    print('''
El usuario canta línea o bingo ingresando por teclado alguna opción que lo permita entre jugada 
y jugada.''')
    time.sleep(2)
    print('''
El usuario tacha una celda en forma manual, en caso que el usuario tachara una celda incorrecta 
la misma será validada al final al momento de que se cante bingo ya sea por parte de la máquina 
o del usuario. Si al validarse los números del cartón hubiese un error el participante quedará 
descalificado y se deberá emitir un mensaje “Ud. Ha sido descalificado, posee el cartón nro 
“…..” y el valor “…..” que no corresponde a una bolilla sacada durante el juego”.''')
    time.sleep(2)
    print('''
JUGADAS ESPECIALES''')
    time.sleep(2)
    print('''
Cada 4 jugadas se deberá lanzar una moneda, si cae seca el usuario podrá tachar un número de 
alguno de los cartones, si cae cara perderá un cartón (esté tachado o no) y recibirá uno 
nuevo. La elección de este cartón queda a consideración del programador.''')
    time.sleep(2)
    print('''
CONTROLES:''')
    time.sleep(2)
    print('''
1. Para tachar una celda se deberá ingresar el número de la celda que se desea tachar,
   por ejemplo si se desea tachar la celda 1,2 se deberá ingresar 12 y presionar enter.
2. Para cantar línea o bingo se deberá ingresar la palabra “linea” o “bingo” y presionar enter.
3. Para ver los tableros de la maquina se debera ingresar la letra “m” y presionar enter.
4. Para pasar a la siguiente tirada, se debera presionar la tecla “enter”.''')

    print()
    continuar = input("Presione cualquier tecla para continuar...")
    msvcrt.getch()
    cls()

def menu_principal():
    cerrar: bool = False
    while not cerrar:
        print('''
[1] Jugar
[2] Tabla de premios
[3] Como Funciona
[4] Historial de partidas
[5] Salir''')
        opcion: str = input("Ingrese una opcion: ")
        while not opcion.isdigit():
            print("Opcion invalida")
            opcion: str = input("Ingrese una opcion: ")
        opcion = int(opcion)
        if opcion == 1:
            juego()
        elif opcion == 2:
            tabla_de_premios()
        elif opcion == 3:
            como_funciona()
        elif opcion == 4:
            pass
        elif opcion == 5:
            print("Gracias por jugar!")
            time.sleep(1)
            cls()
            cerrar = True
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
    menu_principal()



main()
