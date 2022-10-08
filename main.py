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
    numeros_fila_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    numeros_fila_2 = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    numeros_fila_3 = [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
    numeros_fila_4 = [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
    numeros_fila_5 = [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
    numeros_fila_6 = [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
    numeros_fila_7 = [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]
    numeros_fila_8 = [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]
    numeros_fila_9 = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    for i in range(9):
        carton.append([])
        for j in range(3):
            carton[i].append(0)
    for i in range(9):
        for j in range(3):
            if i == 0:
                
                carton[i][j] = random.choice(numeros_fila_1)
                numeros_fila_1.remove(carton[i][j])
            elif i == 1:
                carton[i][j] = random.choice(numeros_fila_2)
                numeros_fila_2.remove(carton[i][j])
            elif i == 2:
                carton[i][j] = random.choice(numeros_fila_3)
                numeros_fila_3.remove(carton[i][j])
            elif i == 3:
                carton[i][j] = random.choice(numeros_fila_4)
                numeros_fila_4.remove(carton[i][j]) 
            elif i == 4:
                carton[i][j] = random.choice(numeros_fila_5)
                numeros_fila_5.remove(carton[i][j])
            elif i == 5:
                carton[i][j] = random.choice(numeros_fila_6)
                numeros_fila_6.remove(carton[i][j])
            elif i == 6:
                carton[i][j] = random.choice(numeros_fila_7)
                numeros_fila_7.remove(carton[i][j])
            elif i == 7:
                carton[i][j] = random.choice(numeros_fila_8)
                numeros_fila_8.remove(carton[i][j])
            elif i == 8:
                carton[i][j] = random.choice(numeros_fila_9)
                numeros_fila_9.remove(carton[i][j])
    return carton


def generar_bolillero():
    bolillero = []
    for i in range(1, 100):
        bolillero.append(i)
    return bolillero


def jugada(bolillero):
    bolilla = random.choice(bolillero)
    return bolilla


def mensaje_de_ayuda(cantidad_de_cartones: list ):
    if len(cantidad_de_cartones) == 1:
        print(Fore.GREEN + '''
COMANDOS: 
ingrese 1, seguido del numero de fila y de la columna para marcar el carton (ejemplo: 153) 
m para ver tableros de la maquina, j para ver tableros del jugador,"
linea + carton para cantar linea,
bingo + carton para cantar bingo,
enter para continuar''' + Style.RESET_ALL)
    else:
        print(Fore.GREEN + f'''
COMANDOS:
ingrese un numero del 1 al {len(cantidad_de_cartones)}, seguido del numero de fila y de la columna para marcar el carton (ejemplo: 392)
m para ver tableros de la maquina, j para ver tableros del jugador,"
linea + carton para cantar linea,
bingo + carton para cantar bingo,
enter para continuar''' + Style.RESET_ALL)
    print()


def juego(ganancias:dict):
        ganancias: dict = {'jugador': 0, 'maquina': 0}	
        cls()
        ronda: int = 1
        bolillero = generar_bolillero()
        nombre_de_jugador: str = input("Ingrese su nombre: ").capitalize()
        cantidad_de_cartones: str = input(f"{nombre_de_jugador}, ingrese la cantidad de cartones(min 1, max 5) que quiere adquuirir: ")
        cartones_del_jugador = []
        cartones_de_la_maquina = []
        if not cantidad_de_cartones.isdigit():
            print("Cantidad invalida")
            cantidad_de_cartones: str = input(f"{nombre_de_jugador}, ingrese la cantidad de cartones(min 1, max 5) que quiere adquuirir: ")
        if int(cantidad_de_cartones) < 1 or int(cantidad_de_cartones) > 5:
            print("Cantidad invalida")
            cantidad_de_cartones: str = input(f"{nombre_de_jugador}, ingrese la cantidad de cartones(min 1, max 5) que quiere adquuirir: ")
        cantidad_de_cartones = int(cantidad_de_cartones)
        print()
        for i in range(cantidad_de_cartones):
            cartones_del_jugador.append(generar_carton())
        cantidad_de_cartones_maquina: int = 10 - cantidad_de_cartones
        for i in range(cantidad_de_cartones_maquina):
            cartones_de_la_maquina.append(generar_carton())
        print(Fore.RED + f"Cartones de {nombre_de_jugador}:")
        for i in range(len(cartones_del_jugador)):
            print()
            print(f"Carton {i+1}:")
            print()
            for j in range(9):
                print(cartones_del_jugador[i][j])
        print(Style.RESET_ALL)
        print()
        print(Fore.BLUE + "CARTONES DE LA MAQUINA")
        for i in range(len(cartones_de_la_maquina)):
            print()
            print(f"Carton {i+1}:")
            print()
            for j in range(9):
                print(cartones_de_la_maquina[i][j])
        print(Style.RESET_ALL)
        print("Presione cualquier tecla para comenzar a jugar: ")
        msvcrt.getch()
        cls()
        time.sleep(1)
        print("Comienza el juego!")
        time.sleep(3)
        partida_terminada:bool = False
        while not partida_terminada:
            while ronda % 4 != 0:
                cls()
                mensaje_de_ayuda(cartones_del_jugador)
                print(f"RONDA {ronda}")
                time.sleep(1)
                tirada: int = jugada(bolillero)
                print(f"La bolilla es: {tirada}")
                cantidad_x_de_la_maquina_por_carton:dict = {}
                for i in range(len(cartones_de_la_maquina)):
                    cantidad_x_de_la_maquina_por_carton[i] = 0
                    for j in range(9):
                        for k in range(3):
                            if cartones_de_la_maquina[i][j][k] == tirada:
                                cartones_de_la_maquina[i][j][k] = "x"
                                cantidad_x_de_la_maquina_por_carton[i] += 1
                        if cartones_de_la_maquina[i][j][0] == "x" and cartones_de_la_maquina[i][j][1] == "x" and cartones_de_la_maquina[i][j][2] == "x":
                            ganancias["maquina"] += 2000
                    if cantidad_x_de_la_maquina_por_carton[i] == 27:
                        ganancias["maquina"] += 58000
                        print("BINGO DE LA MAQUINA!")
                        time.sleep(3)
                        partida_terminada = True
                        return ganancias

                comando: str = input("ingrese un comando: ")
                while comando != "":
                    if comando.isnumeric():
                        if len(comando) != 3:
                            print("Comando invalido")
                            comando: str = input("ingrese un comando: ")
                        else:
                            carton: int = int(comando[0])
                            fila: int = int(comando[1])
                            columna: int = int(comando[2])
                            if carton > len(cartones_del_jugador) or carton < 1:
                                print("Comando invalido")
                                comando: str = input("ingrese un comando: ")
                            else:
                                if cartones_del_jugador[carton-1][fila-1][columna-1] == tirada:
                                    cartones_del_jugador[carton-1][fila-1][columna-1] = "x"
                                    cls()
                                    mensaje_de_ayuda(cartones_del_jugador)
                                    comando = input("ingrese un comando: ")
                                else:
                                    print("Comando invalido")
                                    comando: str = input("ingrese un comando: ")
                            
                    elif comando == "m":
                        cls()
                        mensaje_de_ayuda(cartones_del_jugador)
                        print(f"La bolilla es: {tirada}")
                        print(Fore.BLUE + "CARTONES DE LA MAQUINA")
                        for i in range(len(cartones_de_la_maquina)):
                            print()
                            print(f"Carton {i+1}:")
                            print()
                            for j in range(9):
                                print(cartones_de_la_maquina[i][j])
                        print(Style.RESET_ALL)
                        comando: str = input("ingrese un comando: ")
                    elif comando == "j":
                        cls()
                        mensaje_de_ayuda(cartones_del_jugador)
                        print(f"La bolilla es: {tirada}")
                        print(Fore.RED + f"Cartones de {nombre_de_jugador}:")
                        for i in range(len(cartones_del_jugador)):
                            print()
                            print()
                            print(f"Carton {i+1}:")
                            print()
                            for j in range(9):
                                print(cartones_del_jugador[i][j])
                        print(Style.RESET_ALL)
                        comando: str = input("ingrese un comando: ")
                    elif comando.isalnum() and "linea" in comando:
                        if len(comando) == 6:
                            carton: int = int(comando[6])
                            if carton > len(cartones_del_jugador) or carton < 1:
                                print("Comando invalido")
                                comando: str = input("ingrese un comando: ")
                            else:
                                ganancias["jugador"] += 2000
                    elif comando.isalnum() and "bingo" in comando:
                        if len(comando) == 6:
                            carton: int = int(comando[6])
                            if carton > len(cartones_del_jugador) or carton < 1:
                                print("Comando invalido")
                                comando: str = input("ingrese un comando: ")
                            else:
                                cantidad_de_x_carton_jugador: int = 0
                                for i in range(9):
                                    for j in range(3):
                                        if cartones_del_jugador[carton-1][i][j] == "x":
                                            cantidad_de_x_carton_jugador += 1
                                if cantidad_de_x_carton_jugador == 27:
                                    ganancias["jugador"] += 58000
                                    print("BINGO!")
                                    time.sleep(3)
                                    partida_terminada = True
                                    return ganancias
                                else:
                                    print("USTED HIZO TRAMPA!")
                                    time.sleep(3)
                                    ganancias["jugador"] = 0
                                    partida_terminada = True
                                    return ganancias
                if comando == "":
                    ronda += 1
                    cls()
            while ronda % 4 == 0:
                cls()
                print("RONDA TWEAK")
                time.sleep(1)
                print("SE TIRARA UNA MONEDA, BUENA SUERTE!")
                time.sleep(1)
                moneda: int = random.randint(1,2)
                if moneda == 1:
                    moneda: str = "cara"
                else:
                    moneda: str = "seca"
                
                if moneda == "cara":
                    print("Cara!")
                    time.sleep(1)
                    print(Fore.RED + f"Cartones de {nombre_de_jugador}:")
                    for i in range(len(cartones_del_jugador)):
                        print()
                        print()
                        print(f"Carton {i+1}:")
                        print()
                        for j in range(9):
                            print(cartones_del_jugador[i][j])
                    print(Style.RESET_ALL)
                    carton_elegido: int = int(input("Elija un carton: "))
                    while carton_elegido > len(cartones_del_jugador) or carton_elegido < 1:
                        carton_elegido: int = int(input("Elija un carton: "))
                    fila_elegida: int = int(input("Elija una fila: "))
                    while fila_elegida > 9 or fila_elegida < 1:
                        fila_elegida: int = int(input("Elija una fila: "))
                    columna_elegida: int = int(input("Elija una columna: "))
                    while columna_elegida > 3 or columna_elegida < 1:
                        columna_elegida: int = int(input("Elija una columna: "))
                    cartones_del_jugador[carton_elegido-1][fila_elegida-1][columna_elegida-1] = "x"
                    cls()
                elif moneda == "seca":
                    print("Seca!")
                    time.sleep(1)
                    print(Fore.RED + f"Cartones de {nombre_de_jugador}:")
                    for i in range(len(cartones_del_jugador)):
                        print()
                        print()
                        print(f"Carton {i+1}:")
                        print()
                        for j in range(9):
                            print(cartones_del_jugador[i][j])
                    print(Style.RESET_ALL)
                    carton_elegido: int = int(input("Elija un carton: "))
                    while carton_elegido > len(cartones_de_la_maquina) or carton_elegido < 1:
                        carton_elegido: int = int(input("Elija un carton: "))
                    cartones_del_jugador[carton_elegido-1] = generar_carton()
                    cls()
                time.sleep(1)
                print(Fore.RED + f"Cartones de {nombre_de_jugador}:")
                for i in range(len(cartones_del_jugador)):
                    print()
                    print()
                    print(f"Carton {i+1}:")
                    print()
                    for j in range(9):
                        print(cartones_del_jugador[i][j])
                print(Style.RESET_ALL)
                print("presione enter para continuar")
                msvcrt.getch()
                ronda += 1
        

def tabla_de_premios():
    cls()
    time.sleep(1)
    print('''
PREMIOS:
Linea: 2000 pesos
Bingo: 58000 pesos''')
    time.sleep(2)
    print("Presione cualquier tecla para continuar...")
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
   por ejemplo si se desea tachar en el carton 1, fila 1, columna 2 se deberá ingresar 112 y presionar enter.
2. Para cantar línea o bingo se deberá ingresar la palabra “linea” o “bingo” seguido del número de cartón
3. Para ver los tableros de la maquina se debera ingresar la letra “m” y presionar enter.
4. Para pasar a la siguiente tirada, se debera presionar la tecla “enter”.''')

    print()
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()
    cls()


def historial_de_partidas(partidas_jugadas:int, ganancias:dict):
    cls()
    time.sleep(1)
    print('''
HISTORIAL DE PARTIDAS:''')
    time.sleep(2)
    print(f'''
Partidas jugadas: {partidas_jugadas}''')
    time.sleep(2)
    print('''
Ganancias:''')
for ente in ganancias:
    print(f'''
    {ente}: {ganancias[ente]}''')
    time.sleep(2)
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()
    cls()



def menu_principal(partidas_jugadas: int):
    ganancias: dict = {"jugador": 0, "maquina": 0}
    partidas_jugadas: int = 0
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
            partidas_jugadas += 1
            juego(ganancias)
        elif opcion == 2:
            tabla_de_premios()
        elif opcion == 3:
            como_funciona()
        elif opcion == 4:
            historial_de_partidas(partidas_jugadas, ganancias)
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
    print(Fore.LIGHTGREEN_EX + "BINGO!" + Style.RESET_ALL)
    time.sleep(1)
    menu_principal()



main()
