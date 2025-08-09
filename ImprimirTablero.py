# Dado un tablero cualquiera
# puedo imprimirlo y verificar que funciona
import funciones
# tablero 1 de 2x2
tablero1 = [[1,2], [3,4]]
print("Tablero 1:")
print()
funciones.ImprimirTablero(tablero1)
print("===============================================================")
print()

# tablero 2 de 3x3
tablero2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Tablero 2:")
print()
funciones.ImprimirTablero(tablero2)
print("===============================================================")
print()

# tablero 3 de 7x7
tablero3 = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 1, 2, 3, 4, 5], [5, 6, 7, 8, 9, 0, 1], [2, 3, 4, 5, 6, 7, 8], [9, 0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 0, 1, 2], [3, 4, 5, 6, 7, 8, 9]]
print("Tablero 3:")
print()
funciones.ImprimirTablero(tablero3)
print("===============================================================")
print()

# tablero 4 de 2x2
tablero4 = [[6, 2], [3, 5]]
print("Tablero 4:")
print()
funciones.ImprimirTablero(tablero4)
print("===============================================================")
print()

# tablero 5 de 4x4
print("Tablero 5:")
print()
tablero5 = [[4, 2, 7, 5], [3, 1, 8, 9], [2, 2, 1, 5], [6, 3, 7, 2]]
funciones.ImprimirTablero(tablero5)