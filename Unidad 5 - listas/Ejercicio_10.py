#Ejercicio 10:

#   Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#   ● Mostrar el total vendido por cada producto. 
#   ● Mostrar el día con mayores ventas totales. 
#   ● Indicar cuál fue el producto más vendido en la semana. 

ventas = [
            [4,0,5,12,8,7,2],#Cada fila representa un producto y  las ventas por cada día de la semana
            [53,7,8,4,5,2,7],
            [6,1,8,5,7,9,2],
            [2,5,5,10,4,5,9],
            ]

valor_máximo = -1
dia_maximo = 0
producto_maximo = 0
valor_producto_maximo = -1

for i in range(len(ventas)):
    total_prod = 0
    for j in range(len(ventas[i])):
        total_prod += ventas[i][j]
    if total_prod > valor_producto_maximo:
        valor_producto_maximo = total_prod
        producto_maximo = i+1

    print(f"Total de ventas del producto {i+1}: {total_prod}")
print("-"*50)

for i in range(7):
    ventas_por_dia = 0
    for j in range(4):
        ventas_por_dia += ventas[j][i]
    if ventas_por_dia > valor_máximo:
        valor_máximo = ventas_por_dia
        dia_maximo = i
    print(f"Total de ventas del día {i+1}: {ventas_por_dia}")
        
print("")
print(f"El día con mayores ventas totales es el día {dia_maximo+1}")
print("-"*50)
print(f"El producto más vendido en la semana fue el producto {producto_maximo}")
print("-"*50)

#/////////////////////////////////////////////////////////////////////////////////////////////
