#Ejercicio 12:

#Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista. 
#   ● Mostrar la lista original. 
#   ● Mostrar la lista ordenada de menor a mayor. 
#   ● Mostrar la lista ordenada de mayor a menor. 
#   ● Investigar el uso de sorted() y del parámetro reverse. 
#     * sorted(iterable) devuelve una nueva lista ordenada sin modificar la lista original.
#     * El parámetro reverse=True ordena en sentido descendente (equivale a invertir el orden ascendente).


#Declaro la lista que contendrá números enteros
lista_enteros = []

#Inicio del bucle para completar la lista
for i in range(8):
    num_str = input("Ingrese un número entero: ").strip()

    while not (num_str.lstrip("-").isdigit() and num_str != "-"):
        print("El valor ingresado no es válido.")
        num_str = input("Ingrese un número entero: ").strip()
    
    num_entero = int(num_str)
    lista_enteros.append(num_entero)

print("")
print("-------LISTA DE NÚMEROS ENTEROS ORIGINAL---------")
print(lista_enteros)
print("")
print("------LISTA ORDENADA ASCENDENTE-------")
lista_ascendente = sorted(lista_enteros)
print(lista_ascendente)
print("")
print("------LISTA ORDENADA DESCENDENTE-------")
lista_descendente = sorted(lista_enteros, reverse = True)
print(lista_descendente)
print("")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////
