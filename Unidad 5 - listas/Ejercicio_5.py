#Ejercicio 5:
#Crear una lista con los nombres de 8 estudiantes presentes en clase.
#   ● Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#   ● Mostrar la lista final actualizada.

# Declaro e inicializo la lista según lo que pide el enunciado
estudiantes = ["Julieta Vinsenzo", "Marina Castro", "Romina Araneda", "Daniela Almaza", "Mariana Bellina", "Ivana Delfino", "Melina Ullua", "Estefanía Geoffroy"]

#Inicilizo la variable continuar en True para usar como bandera en el menú de opciones
continuar = True

#Muestro la lista inicial
print("-----------ESTUDIANTES----------")
print("")

for i in estudiantes:
    print(i)
print("")
print("-"*50)

#Comienza el ciclo del menú hasta que el usuario ingrese la opción 3 para finalizar la ejecución
while continuar:
    #Muestro al usuario las opciones
    print("""Para agregar o eliminar un estudiante, ingrese la opción deseada:

        1. Agregar un estudiante a la lista
        2. Eliminar un estudiante de la lista
        3. Salir

    """)
    opcion_abm_str = input().strip() 

    #Valido la entrada al menú
    while opcion_abm_str not in ("1", "2" ,"3"):
        print("La opción ingresada es inválida. Por favor, ingrese una opción correcta: ")
        opcion_abm_str = input().strip()

    # Una vez que el usuario ingresa una opción válida, transformo el tipo de dato de la variable opción a entero
    opcion_abm_int = int(opcion_abm_str)
    print("")

    match opcion_abm_int:
        case 1:
            #Verifico que el nombre del estudiante que ingresa el usuario no sea una cadena vacía
            nuevo_estudiante = input("Para agregar un estudiante ingrese su nombre: ").strip()
            if nuevo_estudiante:
                estudiantes.append(nuevo_estudiante) #Agrego el nuevo estudiante a la lista
                print("")
                print("-----------ESTUDIANTES----------") #Imprimo la lista nueva
                print("")
                for i in estudiantes:
                    print(i)
                print("")
            else:
                print("El nombre del estudiante no puede estar vacío.")
                print("")

        case 2:
            estudiante_a_eliminar = input("Para eliminar un estudiante ingrese su nombre: ").strip()
            #Verifico que el estudiante que se quiere eliminar esté en la lista
            if estudiante_a_eliminar in estudiantes:
                estudiantes.remove(estudiante_a_eliminar)
                print("")
                print("-----------ESTUDIANTES----------")
                print("")
                for i in estudiantes:
                    print(i)
                print("")
            else:
                print("El estudiante ingresado no se encuentra en la lista")
                print("")
        case 3:
            print("-----------ESTUDIANTES----------")
            print("")
            for i in estudiantes:
                print(i)
            print("")
            print("Sesión finalizada")

            # Modifico el valor de la bandera para detener la ejecución
            continuar = False
            break

#////////////////////////////////////////////////////////////////////////////////////////////////