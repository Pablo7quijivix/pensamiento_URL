#Ejercicio de Pensamiento computacional 12 de marzo, condicionales


consumoagua = int(input("Ingrese el consumo de agua en m3:"))
personas = int(input("Cuantas persona viven en su casa:"))

if consumoagua<15:
    precio = 5
elif 15 <= consumo <= 30:
    if personas > 3:
        precio = 4
    elif personas == 3:
        precio = 4.5
    else:
        precio = 5
else:  # consumo > 30
    if personas > 5:
        precio = 3.5
    elif personas % 2 == 0:
        precio = 4
    else:
        precio= 4.2

precio_total = consumoagua* precio
print("Lo que consumen total de agua es: Q",precio_total)


#Ejercicio numero 2 
añocarro=int(input("Ingrese el año de su vehículo: "))
placa=input("Ingrese el número de placa del vehículo: ")
ultimo_digito=int(placa[-1])

if añocarro>= 2001:
    if ultimo_digito in [0, 2, 4, 6, 8]:
        print("El vehículo no circula los lunes.")
    else:
        print("El vehículo no circula los viernes.")
    
    if añocarro% 2 == 0:
        print("El vehículo solo circula hasta el mediodía los sábados.")

if 2024 - añocarro> 25:
    print("¡Cuidado! El vehículo debe someterse a mantenimiento de manera obligatorio.")