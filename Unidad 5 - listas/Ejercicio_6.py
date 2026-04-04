#Ejercicio 6:

#Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha 
#(el último pasa a ser el primero).

lista = [1,2,3,4,5,6,7]
lista_secundaria = lista[0:len(lista)-1]
lista_primer_elemento = [lista.pop()]
lista = lista_primer_elemento + lista_secundaria

print(lista)
#-------Otra forma de pensarlo-----------

lista2 = [1,2,3,4,5,6,7]
lista2.insert(0,lista2.pop())
print(lista2)

#////////////////////////////////////////////////////////////////////////////////////
