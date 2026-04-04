# Ejercicio 9:

#Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#   ● Inicializarlo con guiones "-" representando casillas vacías. 
#   ● Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#   ● Mostrar el tablero después de cada jugada.

tateti = [
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]
        ]

JUGADOR_A = "O"
JUGADOR_B = "X"

partida = 0

print("-----¡ARRANCA EL JUEGO!------")

while partida < 9:
    if partida % 2 == 0:
        print("---TURNO JUGADOR A---")
        
        # Bucle para asegurar una entrada válida para la fila y columna del Jugador A
        while True:
            fila_str = input("Jugador A, ingrese un número del 0 al 2 para la fila: ")
            columna_str = input("Jugador A, ingrese un número del 0 al 2 para la columna: ")

            if not fila_str.isdigit() or not columna_str.isdigit():
                print("Entrada no válida. Por favor ingrese un número entero.")
                continue #Pedir las posiciones nuevamente
            
            fila = int(fila_str)
            columna = int(columna_str)
        
            #Validar que la fila y la columna esten dentro del rango del tablero de te-te-ti y que la celda esté vacía
            if 0 <= fila <= 2 and 0 <= columna <= 2:
                if tateti[fila][columna] == "-":
                    break
                else:
                    print("El lugar ya está ocupado o no es una posición válida. Vuelva a intentarlo")
            else:
                print("Posición inválida (fuera del rango 0-2). Vuelva a intentarlo.")

        tateti[fila][columna] = JUGADOR_A

        for i in range(len(tateti)):
            for j in range(len(tateti[i])):
                print(tateti[i][j], end=" ")
            print("")
        
        #Comprobar si el Jugador A ganó el juego
        if (
            (tateti[0][0] == tateti[0][1] == tateti[0][2] == "O") or 
            (tateti[1][0] == tateti[1][1] == tateti[1][2] == "O") or 
            (tateti[2][0] == tateti[2][1] == tateti[2][2] == "O") or 
            (tateti[0][0] == tateti[1][0] == tateti[2][0] == "O") or 
            (tateti[0][1] == tateti[1][1] == tateti[2][1] == "O") or 
            (tateti[0][2] == tateti[1][2] == tateti[2][2] == "O") or 
            (tateti[0][0] == tateti[1][1] == tateti[2][2] == "O") or 
            (tateti[0][2] == tateti[1][1] == tateti[2][0] == "O")):

            print("Felicitaciones!! El Jugador A ganó el juego!!!")
            break

    else:
        print("---TURNO JUGADOR B---")
        # Bucle para asegurar una entrada válida para la fila y columna del Jugador B
        while True:
            fila_str = input("Jugador B, ingrese un número del 0 al 2 para la fila: ")
            columna_str = input("Jugador B, ingrese un número del 0 al 2 para la columna: ")

            if not fila_str.isdigit() or not columna_str.isdigit():
                print("Entrada no válida. Por favor, ingrese un número entero.")
                continue # Pedir entrada de nuevo

            fila = int(fila_str)
            columna = int(columna_str)

            # Validar que la fila y columna estén dentro del rango y que la celda esté vacía
            if 0 <= fila <= 2 and 0 <= columna <= 2:
                if tateti[fila][columna] == "-":
                    break # Si la entrada es válida, salir del bucle de validación
                else:
                    print("El lugar ya está ocupado. Vuelva a intentarlo.")
            else:
                print("Posición inválida (fuera del rango 0-2). Vuelva a intentarlo.")

        tateti[fila][columna] = JUGADOR_B

        for i in range(len(tateti)):
            for j in range(len(tateti[i])):
                print(tateti[i][j], end=" ")
            print("")
        
        #Comprobar si el Jugador B ganó el juego
        if (
            (tateti[0][0] == tateti[0][1] == tateti[0][2] == "X") or 
            (tateti[1][0] == tateti[1][1] == tateti[1][2] == "X") or 
            (tateti[2][0] == tateti[2][1] == tateti[2][2] == "X") or 
            (tateti[0][0] == tateti[1][0] == tateti[2][0] == "X") or 
            (tateti[0][1] == tateti[1][1] == tateti[2][1] == "X") or 
            (tateti[0][2] == tateti[1][2] == tateti[2][2] == "X") or 
            (tateti[0][0] == tateti[1][1] == tateti[2][2] == "X") or 
            (tateti[0][2] == tateti[1][1] == tateti[2][0] == "X")):

            print("Felicitaciones!! El Jugador B ganó el juego!!!")
            break

    partida += 1
    if partida == 9:
        print("Fue una partida difícil!! Han empatado el Jugador A y el Jugador B ")

print("--------FIN DEL JUEGO--------")

#////////////////////////////////////////////////////////////////////////////////////////////////