# 109880 - Nicolas Florio Toursarkissian
# Algoritmos y Programacion I - Catedra Costa
# Trabajo Practico 1
# 2 Cuatrimestre 2022

'''BINGO'''

import os # para poder limpiar la pantalla
import random # para los tableros y las bolillas
import msvcrt # para poder usar la funcion getch() en windows
import time
from unicodedata import category # para poder usar la funcion sleep()
from colorama import * # para poder usar colores en la consola


# Fuccion para limpiar la pantalla
def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Funcion que le solicita al usuario la cantidad de cartones que desea jugar
# PRE: la cantidad debe ser un numero entero entre 1 y 5
# POST: devuelve la cantidad de cartones que el usuario desea jugar
def validar_numeros_cartones(nombre_de_jugador: str)-> int:
    numero: str = input(f"{nombre_de_jugador}, ingrese la cantidad de cartones(min 1, max 5) que quiere adquuirir: ")
    if not numero.isdigit():
        print("Cantidad invalida")
        numero: str = input(f"{nombre_de_jugador}, ingrese la cantidad de cartones(min 1, max 5) que quiere adquuirir: ")
    if int(numero) < 1 or int(numero) > 5:
        print("Cantidad invalida")
        numero: str = input(f"{nombre_de_jugador}, ingrese la cantidad de cartones(min 1, max 5) que quiere adquuirir: ")
    numero = int(numero)
    return numero


# Funcion que genera los cartones de forma aleatoria. Los cartones no tienen numeros repetidos
# PRE: -
# POST: devuelve una lista de cartones
def generar_carton():
    numeros: dict = {}
    for i in range(0,9):
        posibles_espacios_vacios: list = []
        for e in range(0,9):
            posibles_espacios_vacios.append(e)
        lista_de_numeros: list = []
        for j in range((11*i)+1, (11*(i+1))+1):
            lista_de_numeros.append(j)
        numeros[i] = lista_de_numeros
    carton = []
    for i in range(3):
        carton.append([])
        for j in range(9):
            carton[i].append(0)
    for i in range(3):
        for j in range(9):
            carton[i][j] = random.choice(numeros[j])
            numeros[j].remove(carton[i][j])
        posibles_espacios_vacios: list = []
        for e in range(9):
            posibles_espacios_vacios.append(e)
        for k in range(1,5):
            espacio_vacio: int = random.choice(posibles_espacios_vacios)
            posibles_espacios_vacios.remove(espacio_vacio)
            carton[i][espacio_vacio] = "  "
    return carton


# Funcion que modifica las ganancias del jugador
# PRE: recibe el diccionario de ganancias y el comando ingresado por el usuario
# POST: modifica el diccionario de ganancias
def modificar_ganancias(ganancias:dict, comando:str) -> dict:
    if "bingo" in comando:
        ganancias["jugador"] += 58000
    elif "linea" in comando:
        ganancias["jugador"] += 2000


# Funcion que imprime en pantalla los cartones indicados(Sean los del jugador o los de la maquina)
# PRE: la funcion recibe un diccionario con los cartones a imprimir
# POST: devuelve una impresion en pantalla de los cartones ingresados.
def mostrar_carton(cartones: dict):
    for i in range(len(cartones)):
        print(f"Carton {i+1}")
        for fila in cartones[i]:
            print("----------------------------------------------")
            print("|", end=" ")
            for columna in fila:
                print(f"{columna}", end=" | ")
            print("")
        print("----------------------------------------------")
        print()




# Funcion que genera una lista de numeros del 1 al 99 para el bolillero
def generar_bolillero():
    bolillero = []
    for i in range(1, 100):
        bolillero.append(i)
    return bolillero


# Funcion que elije la bolilla que saldra en el turno
# PRE: recibe la lista que genera la funcion generar_bolillero(), que contiene los numeros del 1 al 99
# POST: devuelve el numero que saldra en el turno y lo sustrae de la lista
def jugada(bolillero):
    bolilla = random.choice(bolillero)
    bolillero.remove(bolilla)
    return bolilla


# Funcion que imprime en pantalla una ayuda para el usuario, mostrandole en color verde los comandos para jugar
# PRE: Recibe la cantidad de cartones que el usuario haya decidido jugar
# POST: Devuelve una impresion en pantalla de los comandos para jugar, con un mensaje personalizado dependiendo de la cantidad de cartones que tenga el usuario
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


# Funcion que marca el carton de la maquina
# PRE: recibe el carton de la maquina y el numero que salio en el turno
# POST: devuelve el carton de la maquina con el numero marcado
def jugada_de_la_maquina(cartones: dict, bolita: int):
    for i in range(len(cartones)):
        for j in range(3):
            for k in range(9):
                if cartones[i][j][k] == bolita:
                    cartones[i][j][k] = "x"
    return cartones


# Funcion que verifica si la maquina tiene linea
# PRE: recibe el carton de la maquina
# POST: devuelve True si la maquina tiene linea, False si no la tiene
def validar_linea(cartones: dict):
    for i in range(len(cartones)):
        for j in range(3):
            if cartones[i][0].count("x") == 5 or cartones[i][1].count("x") == 5 or cartones[i][2].count("x") == 5:
                return True
            else:
                return False


# Funcion que verifica si la maquina tiene bingo
# PRE: recibe el carton de la maquina
# POST: devuelve True si la maquina tiene bingo, False si no lo tiene
def validar_bingo(cartones: dict):
    for i in range(len(cartones)):
        if cartones[i][0].count("x") == 5 and cartones[i][1].count("x") == 5 and cartones[i][2].count("x") == 5:
            return True
        else:
            return False


# Funcion que se encarga de marcar el carton del jugador si la ronda no es multiplo de 4
# PRE: recibe el nombre, el numero de rondas, la bolita que salio en esa ronda, los cartones de ambos y el diccionario de ganancias
# POST: la funcion imprime o modifica los cartones dependiendo el comando ingresado por el usuario y devuelve las rondas modificadas
def comando(nombre_de_jugador: str, rondas:int, tirada: int, cartones_del_jugador: dict,cartones_de_la_maquina: dict, ganancias: dict):
    comando: str = input("ingrese un comando: ").lower()
    while comando != "":
        if comando.isnumeric():
            if len(comando) != 3:
                print("Comando invalido")
                comando: str = input("ingrese un comando: ").lower()
            else:
                carton: int = int(comando[0])
                fila: int = int(comando[1])
                columna: int = int(comando[2])
                if carton > len(cartones_del_jugador) or carton < 1:
                    print("Comando invalido")
                    comando: str = input("ingrese un comando: ").lower()
                else:
                    if cartones_del_jugador[carton-1][fila-1][columna-1] == tirada:
                        cartones_del_jugador[carton-1][fila-1][columna-1] = "x"
                        cls()
                        mensaje_de_ayuda(cartones_del_jugador)
                        comando = input("ingrese un comando: ")
                    else:
                        print("Comando invalido")
                        comando: str = input("ingrese un comando: ").lower()
        elif comando == "m":
            cls()
            mensaje_de_ayuda(cartones_del_jugador)
            print(f"La bolilla es: {tirada}")
            print(Fore.BLUE + "CARTONES DE LA MAQUINA")
            mostrar_carton(cartones_de_la_maquina)
            print(Style.RESET_ALL)
            comando: str = input("ingrese un comando: ").lower()
        elif comando == "j":
            cls()
            mensaje_de_ayuda(cartones_del_jugador)
            print(f"La bolilla es: {tirada}")
            print(Fore.RED + f"Cartones de {nombre_de_jugador}:")
            mostrar_carton(cartones_del_jugador)
            print(Style.RESET_ALL)
            comando: str = input("ingrese un comando: ").lower()
        elif comando.isalnum() and "linea" in comando:
            if len(comando) == 6:
                carton: int = int(comando[5])
                if carton > len(cartones_del_jugador) or carton < 1:
                    print("Comando invalido")
                    comando: str = input("ingrese un comando: ").lower()
                else:
                    for i in range(3):
                        if cartones_del_jugador[carton-1][i].count("x") == 5:
                            modificar_ganancias(ganancias, comando)
                            print(f"{nombre_de_jugador} cantó Linea!")
                        else:
                            print("No hay linea")
                            comando: str = input("ingrese un comando: ").lower()
            else:
                print("Comando invalido")
                comando: str = input("ingrese un comando: ").lower()

        elif comando.isalnum() and "bingo" in comando :
            if len(comando) == 6:
                carton: int = int(comando[5])
                if carton > len(cartones_del_jugador) or carton < 1:
                    print("Comando invalido")
                    comando: str = input("ingrese un comando: ").lower()
                else:
                    cantidad_de_x: int = 0
                    for i in range(3):
                        if cartones_del_jugador[carton-1][i].count("x") == 5:
                            cantidad_de_x += 5
                    if cantidad_de_x == 15:
                        modificar_ganancias(ganancias, comando)
                        print(f"{nombre_de_jugador} cantó Bingo!")
                        time.sleep(3)
                        rondas = 100
                        return rondas
                    else:
                        print("USTED HIZO TRAMPA!")
                        time.sleep(3)
                        ganancias["jugador"] = 0
                        ganancias["maquina"] = 58000
                        rondas = 100
                        return rondas
            else:
                print("Comando invalido")
                comando: str = input("ingrese un comando: ").lower()
    if comando == "":
        rondas += 1
        return rondas
    


# Funcion que se encarga de modificar los cartones si la ronda es multiplo de 4
# PRE: recibe el nombre, el numero de rondas ,los cartones del jugador y las bolillas que ya salieron.
# POST: la funcion modifica los cartones dependiendo de como caiga la moneda y devuelve las rondas modificadas
def ronda_tweak(nombre_de_jugador: str, rondas: int, cartones_del_jugador: dict, bolillas: list):
    moneda: int = random.randint(1, 2)
    if moneda == 1:
        moneda: str = "cara"
    else:
        moneda: str = "seca"
    
    if moneda == "cara":
        print("La moneda cayo en Cara!")
        time.sleep(1)
        print(Fore.RED + f"Cartones de {nombre_de_jugador}:")
        mostrar_carton(cartones_del_jugador)
        print(Style.RESET_ALL)
        carton_elegido: int = int(input("Elija un carton: "))
        while carton_elegido > len(cartones_del_jugador) or carton_elegido < 1:
            print("Comando invalido")
            carton_elegido: int = int(input("Elija un carton: "))
        fila_elegida: int = int(input("Elija una fila: "))
        while fila_elegida > 3 or fila_elegida < 1:
            print("Comando invalido")
            fila_elegida: int = int(input("Elija una fila: "))
        columna_elegida: int = int(input("Elija una columna: "))
        while columna_elegida > 9 or columna_elegida < 1:
            print("Comando invalido")
            columna_elegida: int = int(input("Elija una columna: "))
        bolillas.append(cartones_del_jugador[carton_elegido-1][fila_elegida-1][columna_elegida-1])
        cartones_del_jugador[carton_elegido-1][fila_elegida-1][columna_elegida-1] = "x"
        cls()
    elif moneda == "seca":
        print("La moneda cayo en Seca!")
        time.sleep(1)
        print(Fore.RED + f"Cartones de {nombre_de_jugador}:")
        mostrar_carton(cartones_del_jugador)
        print(Style.RESET_ALL)
        carton_elegido: int = int(input("Elija un carton para ser modificado: "))
        while carton_elegido > len(cartones_del_jugador) or carton_elegido < 1:
            print("Comando invalido")
            carton_elegido: int = int(input("Elija un carton para ser modificado: "))
        cartones_del_jugador[carton_elegido-1] = generar_carton()
        for j in range(3):
            for k in range(9):
                if cartones_del_jugador[carton_elegido-1][j][k] in bolillas:
                    cartones_del_jugador[carton_elegido-1][j][k] = "x"
        cls()
    time.sleep(1)
    print(Fore.RED + f"Cartones de {nombre_de_jugador}:")
    mostrar_carton(cartones_del_jugador)
    print(Style.RESET_ALL)
    print("presione enter para continuar")
    msvcrt.getch()
    rondas += 1
    return rondas
        

# Funcion que ejecuta el juego
# PRE: recibe el diccionario con las ganancias de cada jugador, el numero de partida y el diccionario de partidas
# POST: devuelve el diccionario con las ganancias de cada jugador actualizado
def juego(ganancias:dict, partida: int, partidas:dict ) -> dict:
        cls()
        rondas: int = 1
        bolillas_que_salieron: list = []
        bolillero = generar_bolillero()
        cartones_del_jugador: dict = {}
        cartones_de_la_maquina: dict = {}
        nombre_de_jugador: str = input("Ingrese su nombre: ").capitalize()
        cantidad_de_cartones: int = validar_numeros_cartones(nombre_de_jugador)
        print()
        for i in range(cantidad_de_cartones):
            cartones_del_jugador[i] = (generar_carton())
        cantidad_de_cartones_maquina: int = 10 - cantidad_de_cartones
        for i in range(cantidad_de_cartones_maquina):
            cartones_de_la_maquina[i] = (generar_carton())
        print(Fore.RED + f"Cartones de {nombre_de_jugador}:")
        mostrar_carton(cartones_del_jugador)
        print(Style.RESET_ALL)
        print()
        print(Fore.BLUE + "CARTONES DE LA MAQUINA")
        mostrar_carton(cartones_de_la_maquina)
        print(Style.RESET_ALL)
        print()
        print("Presione cualquier tecla para comenzar a jugar: ")
        msvcrt.getch()
        cls()
        partida_terminada:bool = False
        while not partida_terminada:
            while rondas % 4 != 0:
                cls()
                mensaje_de_ayuda(cartones_del_jugador)
                print(f"RONDA {rondas}")
                time.sleep(1)
                tirada: int = jugada(bolillero)
                bolillas_que_salieron.append(tirada)
                print(f"La bolilla es: {tirada}")
                cartones_de_la_maquina = jugada_de_la_maquina(cartones_de_la_maquina, tirada)
                bingo_de_la_maquina: bool = validar_bingo(cartones_de_la_maquina)
                if bingo_de_la_maquina:
                    ganancias['maquina'] += 58000
                    print(Fore.BLUE + "La maquina cantó bingo!" + Style.RESET_ALL)
                    time.sleep(1)
                    partida_terminada = True
                linea_de_la_maquina: bool = validar_linea(cartones_de_la_maquina)
                if linea_de_la_maquina:
                    ganancias['maquina'] += 2000
                    print(Fore.BLUE + "La maquina cantó linea!" + Style.RESET_ALL)
                    time.sleep(1)
                rondas = comando(nombre_de_jugador, rondas, tirada, cartones_del_jugador,cartones_de_la_maquina, ganancias)
            cls()
            while rondas % 4 == 0 and rondas != 100:
                cls()
                print("RONDA TWEAK")
                time.sleep(1)
                print("SE TIRARA UNA MONEDA, BUENA SUERTE!")
                time.sleep(1)
                print("la moneda cayo en...")
                time.sleep(3)
                rondas = ronda_tweak(nombre_de_jugador, rondas, cartones_del_jugador, bolillas_que_salieron)
            if rondas == 100:
                partida_terminada = True
                partidas[partida] = ganancias
                print("La partida termino!")
                time.sleep(1)
                print("Presione cualquier tecla para continuar")
                msvcrt.getch()
                cls()
                return partidas

# Funcion que imprime en pantalla la tabla de premios
# PRE: -
# POST: -
def tabla_de_premios():
    cls()
    time.sleep(1)
    print('''
PREMIOS:
Linea: 2000 pesos
Bingo: 58000 pesos''')
    time.sleep(2)
    print()
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()
    cls()


# Funcion que imprime en pantalla las reglas del juego y los controles necesarios para poder jugarlo
# PRE: -
# POST: -
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
   por ejemplo si se desea tachar en el carton 1, fila 1, columna 2 se deberá ingresar 112
   y presionar enter.
2. Para cantar línea o bingo se deberá ingresar la palabra “linea” o “bingo” seguido del 
   número de cartón
3. Para ver los tableros de la maquina se debera ingresar la letra “m” y presionar enter.
4. Para pasar a la siguiente tirada, se debera presionar la tecla “enter”.''')

    print()
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()
    cls()


# Funcion que imprime en pantalla el historial de partidas
# PRE: Recibe la cantidad de partidas jugadas(entero) y el diccionario de partidas
# POST: Imprime la cantidad de partidas jugadas y las ganancias de cada jugador
def historial_de_partidas(partidas_jugadas:int, partidas:dict):
    cls()
    if partidas_jugadas > 0:
        time.sleep(1)
        print('''
HISTORIAL DE PARTIDAS:''')
        time.sleep(1)
        print(f'''
Partidas jugadas: {partidas_jugadas}''')
        time.sleep(2)
        print()
        print(partidas)

    else:
        print("no se jugaron partidas")
    print()
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()
    cls()



# Funcion que imprime el menu principal
# PRE: -
# POST: ejecuta la opcion elegida por el usuario
def menu_principal():
    partidas: dict = {}
    partidas_jugadas: int = 0
    cerrar: bool = False
    while not cerrar:
        print(Fore.LIGHTGREEN_EX + "BINGO" + Style.RESET_ALL+ '''

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
            ganancias: dict = {"jugador": 0, "maquina": 0}
            partidas_jugadas += 1
            juego(ganancias, partidas_jugadas, partidas)
        elif opcion == 2:
            tabla_de_premios()
        elif opcion == 3:
            como_funciona()
        elif opcion == 4:
            historial_de_partidas(partidas_jugadas, partidas)
        elif opcion == 5:
            print("Gracias por jugar!")
            time.sleep(1)
            cls()
            cerrar = True
            exit()
        

# Funcion principal
# PRE: -
# POST: ejecuta el menu principal
def main():
    cls()
    time.sleep(1)
    print("cantalo...")
    time.sleep(1)
    print("cantalo...")
    time.sleep(1)
    menu_principal()


main()
