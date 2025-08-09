from funciones import*
from mensajes import*
MensajeBienvenida()
MensajeNivel()
nivel = int(input())
tablero_sistema = GenerarTableroVacio(nivel)  # Asigna el tablero retornado
tablero_jugador = GenerarTableroVacio(nivel)
tablero_sistema = TableroCero(tablero_sistema)
filas = len(tablero_sistema)
columnas = len(tablero_sistema)
coord_bombas = ColocarBombas(nivel,tablero_sistema)
chequeo_bombas = len(coord_bombas)
EnumerarCasillas(tablero_sistema,coord_bombas)
#ImprimirTablero(tablero_sistema)
print("____________________________________________________________________")
print("____________________________________________________________________")
print("____________________________________________________________________")
print("____________________________________________________________________")
ImprimirTablero(tablero_jugador)
print("____________________________________________________________________")
print("____________________________________________________________________")
print("____________________________________________________________________")
print("____________________________________________________________________")
MensajeIndicaCoordenadas()
fila , columna = 0,0
respuesta = True
while respuesta != False:
    contador_M = 0
    MensajeIndicaFila()
    fila = int(input())
    MensajeIndicaColumna()
    columna = int(input())
    MensajeIndicaJugada()
    jugada = str(input())
    if jugada == "M":
        tablero_jugador[fila-1][columna-1] = "🚩"
    elif jugada == "Q":
        tablero_jugador[fila-1][columna-1]= "⬜"
    elif jugada == "D":
        respuesta = DescubrirCasillas(tablero_jugador,tablero_sistema,fila-1,columna-1)
    print("######################################################")
    print("#                                                    #")
    print("#                                                    #")
    print("#       ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓   #")
    print("#      ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓  #")
    print("#     ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓ #")
    print("#      ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓  #")
    print("#       ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓   #")
    print("#                                                    #")
    print("#                                                    #")
    print("######################################################")
    ImprimirTablero(tablero_jugador)
    print("######################################################")
    print("#                                                    #")
    print("#                                                    #")
    print("#       ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓   #")
    print("#      ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓  #")
    print("#     ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓ #")
    print("#      ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓  #")
    print("#       ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓   #")
    print("#                                                    #")
    print("#                                                    #")
    print("######################################################")

    for i in coord_bombas:
        if tablero_jugador[i[0]][i[1]] == "🚩":
            contador_M +=1
    if contador_M == chequeo_bombas:
        print("¡¡¡FELICITACIONES GANASTE!!!")
        ImprimirTablero(tablero_sistema)
        break

if respuesta == False:
    print("¡Ups, perdiste!")