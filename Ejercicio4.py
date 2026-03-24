#Ejercicio 4:
#-------------------------SCAPE ROOM - LA BÓVEDA------------------------------------------

#Inicializar variables. No se piden al usuario

energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = "" 
forzar = 0

#Pedir nombre del agente
agente = input("Ingrese el nombre del agente: ").strip()

#Validar nombre del agente, que sólo contenga letras
while not agente.isalpha():
    print("Error: ha ingresado un nombre inválido. Recuerde ingresar sólo letras.")
    agente = input("Ingrese el nombre del agente: ").strip()

print()
#Bucle principal del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    #Mostrar status
    print(f"\nEnergía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas} | Alarma: {alarma}")
    print()
    #Mostrar menú
    print("----------MENU-------")
    print()
    print("""
        1. Forzar cerraduras
        2. Hackear panel
        3. Descansar
        """)
    
    #Pedir al usuario que ingrese una opción
    opcion_str = input("Ingrese una opción: ").strip()

    #Validar que la opción sea un dígito y se encuentre dentro del rango permitido
    while not opcion_str.isdigit() or int(opcion_str) < 1 or int(opcion_str) > 3:
        print("Error: elija una opción válida: ")
        opcion_str = input("Ingrese una opción: ")
    
    #Definir la opcion como entero
    opcion_int = int(opcion_str)

    #Establecer el recorrido del juego según la opción ingresada
    match opcion_int:
        case 1:
            energia -= 20
            tiempo -= 2

            if energia < 40:
                num = input("Elige un número del 1 al 3: ")
                while not num.isdigit() or int(num) < 1 or int(num) > 3:
                    num = input("Número inválido. Ingrese 1-3: ")
                if int(num) == 3:
                    alarma = True

            forzar += 1
            if forzar == 3:
                print("La cerradura se trabó. ¡Alarma activada!")
                alarma = True
                forzar = 0
            elif not alarma:
                cerraduras_abiertas += 1 

        case 2:
            energia -=10
            tiempo -= 3
            for i in range(4):
                letra = input("Ingrese una letra: ").strip()
                while not letra.isalpha():
                    print("Error. Debe ingresar una letra.")
                    letra = input("Ingrese una letra: ").strip()
                codigo_parcial += letra
            
            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                codigo_parcial = ""
            forzar = 0
        case 3:
            energia = min(100, energia + 15)
            tiempo -= 1
            if alarma:
                energia -=10
            forzar = 0

    #-----Condiciones de fin-----

    #Bloqueo por alarma
    if (alarma and tiempo <= 3) and cerraduras_abiertas < 3:
        print("¡¡¡ALERTA!!!! Sistema bloqueado. Fin del juego.")
        print("Has perdido y no puedes salir.")
        break

    #Victoria
    if cerraduras_abiertas == 3:
        print("¡¡¡FELICITACIONES!! Has logrado superar los obstáculos y salir de la bóveda. ")
        break

    #Derrota
    if energia <= 0 or tiempo <= 0:
        print("Te has quedado sin recursos. No lograste escapar.")
        break