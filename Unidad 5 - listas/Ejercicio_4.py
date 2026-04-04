#Ejercicio 4:
# Dada una lista con valores repetidos: datos = [1,3,5,3,7,1,9,5,3]
#   ● Crear una nueva lista sin elementos repetidos. 
#   ● Mostrar el resultado. 

# Declaro la lista y la inicializo con valores duplicados
datos = [1,3,5,3,7,1,9,5,3]
print("-----LISTA ORIGINAL-----")
print(datos)

#Declaro la nueva lista donde voy a guardar los elementos sin repetir
datos_sin_repetir = []

#Con un bucle  for voy recorriendo la lista original elemento a elemento
for num in datos:
    if num not in datos_sin_repetir: #Si el elemento no está en la lista nueva, lo agrego
        datos_sin_repetir.append(num)

# Al finalizar las iteraciones, la lista resultante solo contiene los valores de la lista original sin repetir elementos.
print("-----LISTA SIN DATOS REPETIDOS------")
print(datos_sin_repetir)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
