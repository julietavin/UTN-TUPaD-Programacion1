#Ejercicio 2:
#-------------"ACCESO AL CAMPUS Y MENU SEGURO"-----------------------

#Definir credenciales de acceso (constantes):
usuario_guardado = "alumno"
clave_guardada = "python123"

#Solicitar al usuario usuario y contraseña y validar. Para que pueda ingresar al sistema, ambas credenciales deben ser correctas.

intentos = 0 #Al tercer intento incorrecto, se bloquea
ingreso = False #Bandera
opcion_str = "0" #Opción del menú

while (intentos <3) and (not ingreso): #Ambas condiciones deben ser verdaderas para continuar con el ciclo de pedir credenciales
    #Solicitar al usuario las credenciales de acceso
    print(f"Intento {intentos + 1}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    #Si se ingresa usuario y clave válidas, se puede acceder al menú y se corta el ciclo cambiando el valor de verdad de la bandera
    if usuario == usuario_guardado and clave == clave_guardada:
        print("Acceso concedido.")
        ingreso = True
        #Menú
        while opcion_str != 4:
            print("-------------MENU-------------")
            print("")
            print("""
            1) Ver estado de inscripción.
            2) Cambiar clave.
            3) Mostrar mensaje motivacional.
            4) Salir
            """)
            print("")
            opcion_str = input("Ingrese la opción deseada: ")
            print("")
            while not opcion_str.isdigit() or int(opcion_str) < 1 or int(opcion_str) > 4:
                print("Error, opción fuera de rango.")
                opcion_str = input("Ingrese la opción deseada: ")

            opcion_int = int(opcion_str)
            match opcion_int:
                case 1:
                    print("Inscripto.")
                    print("➡️➡️➡️➡️➡️➡️➡️➡️")
                case 2:
                    clave_nueva = input("Ingrese la nueva clave: ").strip()
                    while len(clave_nueva) < 6:
                        print("Error, la clave debe tener 6 caracteres.")
                        clave_nueva = input("Ingrese la nueva clave: ").strip()

                    clave_nueva_confirmada = input("Confirme la nueva clave: ").strip()

                    while clave_nueva_confirmada != clave_nueva:
                        print("Error, las claves no coinciden.")
                        clave_nueva_confirmada = input("Confirme la nueva clave: ").strip()

                    clave_guardada = clave_nueva
                    print("La clave ha sido cambiada.")
                    print("(●'◡'●)")

                case 3:
                    print("No esperes a que todo sea perfecto. Empieza ahora y házlo posible!!💪")
                    print("❤️^_+❤️")
                case 4:
                    print("Se ha cerrado la sesión.")
                    break
    #Si las credenciales ingresadas no son válidas, debemos verificar que no se hayan cumplido los tres intentos. De ser así, se bloquea el acceso
    else:
        if intentos < 2:
            print("Error, usuario o clave incorrectos. Vuelva a ingresar sus claves de acceso.")
            intentos +=1
        else:
            print("Cuenta bloqueada.")
            intentos += 1
