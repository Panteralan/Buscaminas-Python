############################################################################################
# Funcion que imprime tableros
def ImprimirTablero(tablero):
# Estas lineas de código, estan para agregar la enumeración al tablero
    numero_columna = 1 # Arrancamos enumerando la primer columna
    for n in tablero:
        print("\t", numero_columna, end=" ") # Hacemos una tabulación y comenzamos a colocar el número en el mismo renglon
        numero_columna+=1 # Incrementamos el número en uno
    print("") # Una vez terminado lo anterior, hacemos un salto de linea, para no seguír imprimiendo en el mismo renglon
    
    numero_fila = 1 # Arrancamos enumerando la pimer fila
    for elemento in tablero:
        print(numero_fila, end=" ") # Colocamos el número de la fila en ese renglon
        for celda in elemento:
            print("\t",celda,end=" ") # Realizamos una tabulación e imprimimos el contenido de esa celda
        print() # Una vez hallamos imprimido toda esta fila, hacemos un salto de linea
        numero_fila+=1 # Incrementamos el número que nos indica la cantidad de filas en uno
############################################################################################

############################################################################################
# Genera el tablero vacío según el nivel
def GenerarTableroVacio(nivel):
    if nivel == 1:
        filas, columnas = 5,5
    elif nivel == 2:
        filas, columnas = 8,8
    elif nivel == 3:
        filas,columnas = 12,12
    else:
        filas, columnas = 5,5
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("⬜")
        tablero.append(fila)
    return tablero  # Retorna el tablero generado
############################################################################################

############################################################################################
# Función que coloca un 0 en cada posición del tablero, quedando el tablero todoe n cero
def TableroCero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            tablero[i][j] = 0
    return tablero
############################################################################################

import random

############################################################################################
# Funcion que coloca una canidad de bombas de forma aleatora, dependiendo el nivel elegído
# por el jugador.
def ColocarBombas(nivel, tablero):
    if nivel == 1:
        bombas = 2
    elif nivel == 2:
        bombas = 4
    elif nivel == 3:
        bombas = 8
    else:
        bombas = 2

    contador = 0
    coordenadas_bombas=[]
    
    while contador != bombas:
        # Generar índices aleatorios dentro del rango de filas y columnas
        fila_random = random.randint(0,len(tablero)-1)
        columna_random = random.randint(0, len(tablero)-1)
        # Solo colocar bomba si no hay una ya en esa posición
        if tablero[fila_random][columna_random] != "💣":
            tablero[fila_random][columna_random] = "💣"
            coordenadas_bombas.append((fila_random,columna_random))
            contador += 1
    return coordenadas_bombas #Retorna las coordenas donde las bombas fueron guardadas
############################################################################################

############################################################################################
#Obtiene una lista de celdas adyacentes a la celda(fila, columna)
def ObtenerAdyacentes(tablero, fila, columna):
    adyacentes = [] # posibles posiciones adyacentes
    posiciones_adyacentes = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0),
    (1,1)]
    for posicion in posiciones_adyacentes:
        posible_fila = fila + posicion[0]
        posible_columna = columna + posicion[1]
        if (EsValidaPosicion(tablero, posible_fila, posible_columna)):
            adyacentes.append((posible_fila, posible_columna))
    return (adyacentes)
############################################################################################

############################################################################################
#Valida una posición del tablero dada una fila y columna
def EsValidaPosicion(tablero, fila, columna):
    tamanio = len(tablero)
    es_valida = False
    if (0 <= fila) and (fila < tamanio):
        if (0 <= columna) and (columna < tamanio):
            es_valida = True
    return (es_valida)
############################################################################################

############################################################################################
# Funcion que enumera las casillas donde hay bombas
def EnumerarCasillas(tablero_sistema,coord_bombas):
    for i in coord_bombas:
        fila = i[0]
        columna = i[1]
        celdas_adyacentes = ObtenerAdyacentes(tablero_sistema,fila,columna)
        for j in celdas_adyacentes:
            if tablero_sistema[j[0]][j[1]] != "💣":
                tablero_sistema[j[0]][j[1]] += 1
############################################################################################

############################################################################################
# Función para descubrir las casillas en el tablero del jugador
def DescubrirCasillas(tablero_jugador, tablero_sistema, fila, columna):
    # Verifica si la casilla seleccionada es una bomba
    if tablero_sistema[fila][columna] == "💣":
        return False  # El juego podría terminar aquí si es una bomba

    # Utilizar una pila para explorar casillas
    pila = [(fila, columna)]

    # Mientras haya casillas en la pila
    while pila:
        i, j = pila.pop()
        
        # Si ya fue descubierta, continuamos
        if tablero_jugador[i][j] != "⬜":
            continue

        # Descubrir la casilla en el tablero del jugador
        tablero_jugador[i][j] = tablero_sistema[i][j]

        # Si la casilla no tiene bombas cercanas (es un 0), expandimos
        if tablero_sistema[i][j] == 0:
            # Obtener las celdas adyacentes
            celdas_adyacentes = ObtenerAdyacentes(tablero_sistema, i, j)
            for ady in celdas_adyacentes:
                # Agregamos a la pila solo las casillas no descubiertas y que no son bombas
                if tablero_jugador[ady[0]][ady[1]] == "⬜" and tablero_sistema[ady[0]][ady[1]] != "💣":
                    pila.append((ady[0], ady[1]))

    return True  # El juego continúa si no se ha encontrado una bomba
############################################################################################
