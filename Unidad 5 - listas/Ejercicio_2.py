#Ejercicio 2:

# Pedir al usuario que cargue 5 productos en una lista.
#● Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
#● Preguntar al usuario qué producto desea eliminar y actualizar la lista. 

#Declaro la lista
lista_productos = []

#Solicitamos al usuario que ingrese los 5 productos con 5 iteraciones
for i in range(5):
    producto_nuevo = input("Ingrese un producto: ").strip().lower()
    
    while producto_nuevo == "" or not producto_nuevo.replace(" ","").isalpha():
        print("Error, entrada inválida.")
        producto_nuevo = input("Ingrese un producto: ").strip().lower()
    lista_productos.append(producto_nuevo)


# Mostramos la lista ordenada con la función sorted()
print("LISTA ORDENADA")
lista_ordenada = sorted(lista_productos)
print(lista_ordenada)

#Le pedimos al usuario que ingrese el producto que quiere eliminar de la lista
producto_a_eliminar = input("Por favor, indique qué producto de la lista quiere eliminar: ").strip().lower()
while producto_a_eliminar == "" or not producto_a_eliminar.replace(" ","").isalpha():
    print("Error, entrada inválida.")
    producto_a_eliminar = input("Ingrese el producto que quiere eliminar: ").strip().lower()

if producto_a_eliminar in lista_productos:
    lista_productos.remove(producto_a_eliminar) #Eliminamos con el método remove()
else:
    print("El producto no se encuentra en la lista.")

#Mostramos la lista actualizada
print("LISTA ACTUALIZADA")
print(sorted(lista_productos))

#////////////////////////////////////////////////////////////////////////////////////////////////////////////
