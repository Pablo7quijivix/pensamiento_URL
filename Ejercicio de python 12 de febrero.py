# Pedimos al usuario que ingrese un número del 1 al 9
numero = int(input("Ingresa un número del 1 al 9: "))

# Verificamos si el número está dentro del rango permitido para que se pueda operar de buena manera
if numero >= 1 and numero <= 9:
    # Le asignamos sus equivalentes en romano para luego solo imprimirlo
    if numero == 1:
        romano = "I"
    elif numero == 2:
        romano = "II"
    elif numero == 3:
        romano = "III"
    elif numero == 4:
        romano = "IV"
    elif numero == 5:
        romano = "V"
    elif numero == 6:
        romano = "VI"
    elif numero == 7:
        romano = "VII"
    elif numero == 8:
        romano = "VIII"
    elif numero == 9:
        romano = "IX"

    # Imprimimos el número romano
    print("El número romano es:", romano)
else:
    # Si el número está fuera del rango, mostramos un mensaje de error
    print("El número ingresado no está dentro del rango permitido (1-9).")