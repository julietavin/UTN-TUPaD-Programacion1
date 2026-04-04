#Ejercicio 1:
#Crear una lista con las notas de 10 estudiantes.
#● Mostrar la lista completa. 
#● Calcular y mostrar el promedio. 
#● Indicar la nota más alta y la más baja. 

#Declarar e inicializar la lista
notas = [4,7,9,8.5,9,10,6,5.5,8,6]

#Declaro las variables para acumular la suma de las notas y a los valores máximos y mínimos los inicilizo con el primer elemento de la lista.
suma_notas = 0
nota_max = notas[0]
nota_min = notas[0]

#Recorro la lista con un bucle for.
for i in range(len(notas)):
    print(notas[i]) #Impresión de los elementos de la lista.
    suma_notas +=notas[i] #Acumulador de notas

    #A medida que recorro los elementos de la lista, se hacen comparaciones para establecer el valor máximo y el valor mínimo.
    if notas[i] > nota_max:
        nota_max = notas[i]
    if notas[i] < nota_min:
        nota_min = notas[i]

#Terminado el bucle for, puedo calcular el promedio 
promedio = (suma_notas/len(notas))

#Impresión de los datos solicitados
print(f"El promedio de las notas es: {promedio:.2f}")
print(f"La nota máxima es: {nota_max}")
print(f"La nota mínima es: {nota_min}")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
