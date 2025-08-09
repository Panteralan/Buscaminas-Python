from funciones9D import *

#######################################################
# Mensaje de selección de nivel
def MensajeNivel():
    print("Seleccione el nivel deseado")
    print("1 - Fácil")
    print("2 - Intermedio")
    print("3 - Difícil")
#######################################################

#######################################################
def MensajeBienvenida():
    print("######################################################")
    print("#                                                    #")
    print("#           ¡BIENVENIDO AL JUEGO BUSCAMINAS!         #")
    print("#                                                    #")
    print("#       ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓   #")
    print("#      ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓  #")
    print("#     ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓ #")
    print("#      ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓  #")
    print("#       ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓      ▓▓▓▓▓▓   #")
    print("#                                                    #")
    print("#      ¡Descubre las casillas y evita las bombas!    #")
    print("#                                                    #")
    print("######################################################")
    print("\nCreado por: Alan Placeres")
    print("Vamos a inicializar todas las variables. ¡Suerte en el juego!")

#######################################################

#######################################################
# Mensaje para indicar coordenadas
def MensajeIndicaCoordenadas():
    print("Deberás indicar las coordenadas para jugar")
    print("Primero la fila, luego la columna")
    print("A continuación podrás ingresar cada valor.")
#######################################################

#######################################################
# Mensaje para pedirle al usuario la fila
def MensajeIndicaFila():
    print("Indica la fila:")
#######################################################

#######################################################
# Mensaje para pedirle al usuario la columna
def MensajeIndicaColumna():
    print("Indica la columna:")
#######################################################

#######################################################
# Mensaje para pedirle al usuario que haga algo
def MensajeIndicaJugada():
    print("Deberás indicar el tipo de jugada que quieres realizar:")
    print("M - marcar casilla")
    print("D - descubrir casilla")
    print("Q - quitar casilla")
    print("Indica tu movimiento:")
#######################################################
