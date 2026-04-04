#Ejercicio 8:

#Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#   ●  Mostrar el promedio de cada estudiante. 
#   ● Mostrar el promedio de cada materia. 

#Declaro la matriz de 5x3 (representan 5 estudiantes con 3 notas c/u)
notas = [
        [8,8,10],
        [7,9,7],
        [6,7,7],
        [9,9,9],
        [7,6,8]
        ]

#Declaro una matriz de 3 materias (filas) x 5 estudiantes (columnas) donde se van a almacenar las notas de las materias
materias =[[],[],[]]

#Entro al bucle para recorrer las listas de estudiantes
for i in range(len(notas)):
    sumatoria_estudiante = 0 # Declaro e inicializo en cero la variable para almacenar la sumatoria de las notas de cada estudiante

    #Ingreso al bucle de las notas de las materias de cada estudiante
    for j in range(len(notas[i])):
        sumatoria_estudiante += notas[i][j] #Actualizo la sumatoria de todas las notas de cada estudiante
        materias[j].append(notas[i][j])
    promedio_estudiante = sumatoria_estudiante/len(notas[i])

    print(f"Promedio del estudiante {i+1}: {promedio_estudiante:.2f}")

print("-----MATRIZ DE NOTAS-----")
print(notas)
print("-"*50)

for i in range(len(materias)):
    sumatoria_materia = 0

    for j in range(len(materias[i])):
        sumatoria_materia += materias[i][j]
    promedio_materia = sumatoria_materia/len(materias[i])    
        
    print(f"Promedio de la materia {i+1}: {promedio_materia:.2f}")

print("-----NOTAS POR MATERIA-----")
print(materias)
print("-"*50)

#//////////////////////////////////////////////////////////////////////////////////////////
