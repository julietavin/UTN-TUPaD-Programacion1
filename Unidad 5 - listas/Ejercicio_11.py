#Ejercicio 11:

#Crear una lista con los nombres de 10 estudiantes. 
#   ● Solicitar al usuario que ingrese un nombre a buscar. 
#   ● Indicar si el nombre se encuentra en la lista. 
#   ●  Mostrar la posición en la que aparece. 
#   ● Si no se encuentra, informar que no está en la lista. 

#Declaro la lista de estudiantes
estudiantes = []

#Solicito al usuario que ingrese los nombres completos de los estudiantes
for i in range(10):
    nombre_completo = input("Ingrese el nombre y apellido del estudiante (Nombre + Apellido): ").strip().upper() #Elimino espacios al inicio y al final del nombre y transformo a mayúsculas para evitar errores

    while nombre_completo == "" or not nombre_completo.replace(" ","").isalpha(): #Valido que el valor ingresado por el usuario no sea una cadena vacía y que sólo contenga caracteres alfabéticos.
        print("El nombre ingresado no es válido. No puede ingresar un nombre vacío y sólo puede utilizar letras.")
        nombre_completo = input("Ingrese el nombre y apellido del estudiante (Nombre + Apellido): ").strip().upper()

    #Se ingresa un estudiante en cada iteración del bucle FOR
    estudiantes.append(nombre_completo)

print("")
#Se muestra la lista de estudiantes para control
print(estudiantes) 

#Solicito al usuario que ingrese un valor a buscar en la lista de estudiantes
estudiante_a_buscar = input("Ingrese el nombre a buscar en la lista (Nombre + Apellido): ").strip().upper() 

#Se valida que el nombre ingresado tenga un formato correcto
while estudiante_a_buscar == "" or not estudiante_a_buscar.replace(" ","").isalpha():
        print("El nombre ingresado no es válido. No puede ingresar un nombre vacío y sólo puede utilizar letras.")
        estudiante_a_buscar = input("Ingrese el nombre y apellido del estudiante (Nombre + Apellido): ").strip().upper()

#Si el nombre buscado se encuentra en la lista, se muestra que sí está y se indica en qué posición se encuentra.
if estudiante_a_buscar in estudiantes:
    print("El nombre ingresado está en la lista.")
    print(f"Se encuentra en la posición {estudiantes.index(estudiante_a_buscar) +1}.")
else:
    print("Valor no encontrado. El nombre buscado no se encuentra en la lista.") #Si el nombre no está en la lista, se muestra el mensaje de aviso y finaliza la ejecución.

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
