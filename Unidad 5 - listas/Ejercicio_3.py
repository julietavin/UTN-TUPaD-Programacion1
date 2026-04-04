#Ejercicio 3:
# Generar una lista con 15 números enteros al azar entre 1 y 100.

import random

# Declaro listas vacías para almacenar:
# 1. Los 15 números aleatorios
lista_enteros = []

# 2. Los números pares
lista_pares = []

# 3. Los números impares
lista_impares = []


# Itero 15 veces para generar y agregar a la lista números aleatorios entre 1 y 100
for i in range(15):
    num = random.randrange(1, 101)
    lista_enteros.append(num)

    #En el mismo bucle, voy completando las listas de pares e impares 
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

#Muestro la lista de 15 elementos
print("Lista de 15 números enteros entre 1 y 100")
print(lista_enteros)
print()

#Muestro la lista de números pares
print("Lista de pares")
print(lista_pares)
print(f"Hay {len(lista_pares)} números pares.")
print()


#Muestro la lista de números impares
print("Lista de impares")
print(lista_impares)
print(f"Hay {len(lista_impares)} números impares.")
print()

#////////////////////////////////////////////////////////////////////////////////////////////////
