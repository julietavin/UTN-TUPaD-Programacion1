# Ejercicio 5
#----------------------------“Escape Room:"La Arena del Gladiador"----------------------------

#Inicializar variables estadísticas
vida_gladiador = 100 
vida_enemigo = 100
pociones = 3
dano_base_gladiador = 15 
dano_base_enemigo = 12 
turno_gladiador = True

#Inicializar constantes
GOLPE_CRITICO = 1.5


print("-----BIENVENIDO A LA ARENA------")
#Soliictar nombre del gladiador
nombre_gladiador = input("Nombre del gladiador: ").strip()

#Validar nombre del gladiador
while not nombre_gladiador.isalpha():
    print("Error: sólo se permiten letras")
    nombre_gladiador = input("Nombre del gladiador: ").strip()

print("===INICIO DEL COMBATE===")
# Ciclo de combate: inicia sólo si gladiador y enemigo no se quedaron sin vidas
while vida_gladiador > 0 and vida_enemigo > 0:
    if turno_gladiador:
        # Mostrar status
        print(f"\n{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        print("_"*30)
        #Mostrar menú
        print("""==Elige Acción==
            1. Ataque pesado
            2. Ráfaga veloz
            3. Curar
            """)
    
        #Inicializar opción del juego
        opcion_str = input("Indique el próximo paso: ")

        #Validar menú contrrolando que sea dígito y no esté fuera de rango
        while not opcion_str.isdigit() or int(opcion_str) < 1 or int(opcion_str) > 3:
            print("La opción ingresada no es válida. Ingrese 1 - Ataque pesado | 2 - Ráfaga veloz | 3 - Curar")
            opcion_str = input("Indique el próximo paso: ")
    
        #Convertir la opción a número entero
        opcion_int = int(opcion_str)

        # ---------------ACCIONES------------------
        match opcion_int:
            case 1:
                print("----Opción: A----")
                if vida_enemigo < 20:
                    vida_enemigo -= (dano_base_gladiador * GOLPE_CRITICO)
                    print(f"Atacaste al enemigo por {dano_base_gladiador * GOLPE_CRITICO} puntos de daño!!!")
                else:
                    vida_enemigo -= dano_base_gladiador
                    print(f"Atacaste al enemigo por {dano_base_gladiador} puntos de daño!!!")
            case 2:
                print("----Opción B----")
                print("Inicias una ráfaga de golpes!")
                for i in range(3):
                    vida_enemigo -=5
                    print("Golpe conectado por 5 de daño.")
                #print(f"El enemigo contraataca por {dano_base_enemigo} de daño!!")
            case 3:
                print("----Opción C----")
                if pociones > 0:
                    vida_gladiador = min(100, vida_gladiador + 30)
                    pociones -= 1
                else:
                    print("No quedan pociones!")
                    
        turno_gladiador = False
    else:
        if vida_enemigo > 0:
            print("-----TURNO DEL ENEMIGO-----")
            vida_gladiador -= dano_base_enemigo
            print("El enemigo te atacó por 12 puntos de daño!")
            turno_gladiador = True

if vida_gladiador > 0:
    print(F"¡VICTORIA!!! {nombre_gladiador} ha ganado la batalla. ")
else:
    print(f"¡DERROTA!! Has caído en combate.")