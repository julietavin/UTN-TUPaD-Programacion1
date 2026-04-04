#Ejercicio 7:

#Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana. 
#   ● Calcular el promedio de las mínimas y el de las máximas. 
#   ● Mostrar en qué día se registró la mayor amplitud térmica. 

#Declaro e inicializo una matriz de 7x2 [max,min]
temperatura = [ [13,3],
                [13,2],
                [13,4],
                [17,4],
                [17,5],
                [17,6],
                [19,6]
                ]

#Declaro las variables auxiliares para calcular los promedios y el día de mayor amplitud térmica
suma_minimas = 0
suma_maximas = 0
mayor_amplitud = 0
dia = 1

#Recorro cada fila de la matriz (dia) y de acuerdo a la posición de j se acumula la sumatoria de temperaturas máximas (j=0) o temperaturas mínimas (j=1)
for i in range(len(temperatura)):
    suma_maximas += temperatura[i][0]
    suma_minimas += temperatura[i][1]

    #En cada vuelta se analiza la amplitud térmica del día
    amplitud_termica = temperatura[i][0]-temperatura[i][1]

    #Se actualiza la amplitud mayor si corresponde
    if  amplitud_termica > mayor_amplitud:
        mayor_amplitud = amplitud_termica
        dia = i+1

    # Se muestra cada día con susrespectivas temperaturas
    print(f"Día {i+1}: ",temperatura[i])

#Declaración y asignación de los promedios
promedio_max = suma_maximas/len(temperatura)
promedio_min = suma_minimas/len(temperatura)

print(f"El promedio de las temperaturas máximas es: {promedio_max:.2f}")
print(f"El promedio de las tempeaturas mínimas es: {promedio_min:.2f}")
print(f"El día con mayor amplitud térmica es el día: {dia}")

#----------------------------------------------------------------------------------------------
