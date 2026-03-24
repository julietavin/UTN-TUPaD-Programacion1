#Ejercicio 1:

#-----------CAJA DEL KIOSCO-------------

#Solicitar nombre del cliente (sólo letras):

nombre = input("Ingrese el nombre del cliente: ").strip()

#Validar que el el nombre ingresado sólo contenga caracteres alfabéticos.
while not nombre.isalpha():
    print("Error: El nombre ingresado no es válido.")
    nombre = input("Ingrese el nombre del cliente: ").strip()

#Solicitar la cantidad de productos a ingresar de la venta.

cant_str = input("Ingrese la cantidad de productos: ").strip()

#Validar que la cantidad ingresada solo contenga números enteros positivos mayores a cero.


while not cant_str.isdigit() or int(cant_str) == 0:
    print("Error: La cantidad ingresada no es válida.")
    cant_str = input("Ingrese la cantidad de productos: ")

cant_int = int(cant_str)

#Inicializar las variables de totales
total_con_desc = 0
total_sin_desc = 0

#Solicitar el precio de cada producto

for i in range(cant_int):
    precio_str = input(f"Ingrese el precio del producto {i+1}: ").strip()
    while not precio_str.isdigit() or int(precio_str) == 0:
        print("Error: El precio ingresado no es válido.")
        precio_str = input("Ingrese un precio correcto, sin decimales y mayor a cero: ")
    
    precio_int = int(precio_str)

    #Acumulo en la variable total_sin descuento el precio de todos los productos
    total_sin_desc += precio_int

    #Consultar si el producto tiene descuento
    descuento = input("Indicar si tiene descuento S/N: ").lower()
    while descuento not in("s,n"):
        print("Error, ingrese una opción válida, S si tiene descuento, N en caso contrario: ")
        descuento = input("Indicar si tiene descuento S/N: ").lower()

    #Si el precio tiene descuento, se aplica el descuento y se suma a la variable total con descuento, en caso contrario se acumula el precio regular.
    if descuento == "s":
        total_con_desc += precio_int * 0.9
    else:
        total_con_desc += precio_int 
    
#----------FIN DEL CICLO FOR----------
#Mostrar totales

print(f"Total sin descuento: ${total_sin_desc}.")
print(f"Total con descuento: ${total_con_desc}.")
print(f"Ahorro total: ${total_sin_desc - total_con_desc}.")
print(f"Promedio por producto: $ {(total_con_desc/cant_int):.2f}")
    

#------------------------------------------------------------