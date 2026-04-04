# Ejercicio 13:

#Dada la siguiente lista de puntajes de un videojuego: 
# puntajes = [450, 1200, 875, 990, 300, 1500, 640]
#   ● Mostrar el puntaje más alto y el más bajo. 
#   ● Mostrar la lista ordenada de mayor a menor (ranking). 
#   ● Indicar en qué posición del ranking se encuentra el puntaje 990.

puntajes = [450,1200,875,990,300,1500,640]

puntaje_min = puntajes[0]
puntaje_max = puntajes[0]

for valor in puntajes:
    if valor < puntaje_min:
        puntaje_min = valor
    if valor > puntaje_max:
        puntaje_max = valor

print("------PUNTAJE MÁS ALTO-----")
print(puntaje_max)
print("------PUNTAJE MÁS BAJO-----")
print(puntaje_min)

ranking = sorted(puntajes, reverse = True)
print("-----RANKING-----")

for i in range(len(ranking)):
    print(f"{i+1}. {ranking[i]}")

print("")

pos = ranking.index(990)
print(f"El puntaje 990 se encuentra en la posición {pos + 1}.")
