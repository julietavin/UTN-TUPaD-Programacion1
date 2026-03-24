#Ejercicio 3:
#--------------------

operador = input("Operador: ").strip()
opcion_str = "0"
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""
ocupado_lunes = 0
ocupado_martes = 0

while not operador.isalpha():
    print("Error: El operador debe contener solo letras.")
    operador = input("Operador: ").strip()

while opcion_str != "5":
    print("""
    -------MENU------
    1. Reservar turno 
    2. Cancelar turno (por nombre) 
    3. Ver agenda del día 
    4. Ver resumen general 
    5. Cerrar sistema 
    """)
    opcion_str = input("Ingrese la opción deseada: ").strip()

    while not opcion_str.isdigit() or int(opcion_str) < 1 or int(opcion_str) > 5:
        print("Error, ingrese una opción válida.")
        opcion_str = input("Ingrese la opción deseada: ").strip()

    opcion_int = int(opcion_str)

    match opcion_int:
        case 1:
            print("Para reservar un turno, ingrese el día:")
            print("""
            1 = Lunes
            2 = Martes
            """)
            dia = input().strip()

            while dia not in ("1","2"):
                print("Indique el día para reservar, recuerde ingresar 1 para Lunes o 2 para Martes: ")
                dia = input().strip()
            
            nombre_paciente = input("Ingrese el nombre del paciente: ").strip()
            while not nombre_paciente.isalpha():
                print("Error: el nombre sólo puede contener letras.")
                nombre_paciente = input("Ingrese nuevamente el nombre del paciente: ").strip()
            
            if dia == "1":
                if lunes1 == nombre_paciente or lunes2 == nombre_paciente or lunes3 == nombre_paciente  or lunes4 == nombre_paciente:
                    print("El paciente ya tiene turno asignado para el lunes.")
                else:
                    if lunes1 == "":
                        lunes1 = nombre_paciente
                        ocupado_lunes +=1
                    elif lunes2 == "":
                        lunes2 = nombre_paciente
                        ocupado_lunes +=1
                    elif lunes3 == "":
                        lunes3 = nombre_paciente
                        ocupado_lunes +=1
                    elif lunes4 == "":
                        lunes4 = nombre_paciente
                        ocupado_lunes +=1
                    else:
                        print("NO hay turnos disponibles para el lunes.")
            else:
                if martes1 == nombre_paciente or martes2 == nombre_paciente or martes3 == nombre_paciente:
                    print("El paciente ya tiene turno asignado para el martes. ")
                else:
                    if martes1 == "":
                        martes1 = nombre_paciente
                        ocupado_martes += 1
                    elif martes2 == "":
                        martes2 = nombre_paciente
                        ocupado_martes += 1
                    elif martes3 == "":
                        martes3 = nombre_paciente
                        ocupado_martes += 1
                    else:
                        print("No hay turnos disponibles para el martes.")

        case 2:
            print("Para cancelar un turno, ingrese el día y el nombre del paciente: ")
            print("""
            1 = Lunes
            2 = Martes
            """)
            dia = input().strip()

            while dia not in ("1","2"):
                print("Indique el día para cancelar un turno, recuerde ingresar 1 para Lunes o 2 para Martes: ")
                dia = input().strip()

            nombre_paciente = input("Ingrese el nombre del paciente: ").strip()
            while not nombre_paciente.isalpha():
                print("Error: el nombre sólo puede contener letras.")
                nombre_paciente = input("Ingrese nuevamente el nombre del paciente: ").strip()

            if dia == "1":
                if lunes1 == nombre_paciente:
                    lunes1 = ""
                    ocupado_lunes -= 1
                elif lunes2 == nombre_paciente:
                    lunes2 = ""
                    ocupado_lunes -= 1
                elif lunes3 == nombre_paciente:
                    lunes3 = ""
                    ocupado_lunes -= 1
                elif lunes4 == nombre_paciente:
                    lunes4 = ""
                    ocupado_lunes -= 1
                else:
                    print("El paciente no tiene turno asignado para el lunes.")
            else:
                if martes1 == nombre_paciente:
                    martes1 = ""
                    ocupado_martes -= 1
                elif martes2 == nombre_paciente:
                    martes2 = ""
                    ocupado_martes -= 1
                elif martes3 == nombre_paciente:
                    martes3 = ""
                    ocupado_martes -= 1
                else:
                    print("El paciente no tiene turno asignado para el martes.")

        case 3:
            print("Ingrese el día para consultar agenda: ")
            print("""
            1 = Lunes
            2 = Martes
            """)
            dia = input().strip()

            while dia not in ("1","2"):
                print("Indique el día para cancelar un turno, recuerde ingresar 1 para Lunes o 2 para Martes: ")
                dia = input().strip()

            print("-------AGENDA------") 
            if dia == "1":
                if lunes1 == "":
                    print("Lunes1: LIBRE.")
                else:
                    print(f"Lunes1: {lunes1}")
                if lunes2 == "":
                    print("Lunes2: LIBRE.")
                else:
                    print(f"Lunes2: {lunes2}")
                if lunes3 == "":
                    print("Lunes3: LIBRE.")
                else:
                    print(f"Lunes3: {lunes3}")
                if lunes4 == "":
                    print("Lunes4: LIBRE.")
                else:
                    print(f"Lunes4: {lunes4}")
            else:
                if martes1 == "":
                    print("Martes1: LIBRE.")
                else:
                    print(f"Martes1: {martes1}")
                if martes2 == "":
                    print("Martes2: LIBRE")
                else:
                    print(f"Martes2: {martes2}")
                if martes3 == "":
                    print("Martes3: LIBRE")
                else:
                    print(f"Martes3: {martes3}")

            print("-"*50)
        case 4:
            print("------------RESUMEN GENERAL-----------")
            print()
            print("LUNES")
            print("-"*20)
            print(f"""
                Turno 1: {lunes1}
                Turno 2: {lunes2}
                Turno 3: {lunes3}
                Turno 4: {lunes4}
                """)
            print("-"*50)
            print()
            print("MARTES")
            print("-"*20)
            print(f"""
                Turno 1: {martes1}
                Turno 2: {martes2}
                Turno 3: {martes3}
                """)
            print("-"*50)

            
            if ocupado_lunes > ocupado_martes:
                print("El día más ocupado es el Lunes.")
            elif ocupado_martes > ocupado_lunes:
                print("El día más ocupado es el Martes.")
            else:
                print("Ambos días tienen la misma cantidad de turnos asignados.")
            
        case 5: 
            print("Sesión terminada.")