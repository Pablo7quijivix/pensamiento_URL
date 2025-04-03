'''
#___________________________Codigo numero 1____________________________________________
n= int(input('ingrese el tamaño del array:')) # cualquier numero para el tamaño
m= int( input('Ingrese los multiplos del mismo:')) #cualquier numero que el usuario quiera de base
salida=[] #salida o impresion de nuestro vector
for i in range (0,n): #le especificamos de donde inicia y hasta que valor trabaja "n"
    salida.append(i*m)  #aplicacion de la funcion "append" esta nos servia para agregar este valor al final del vector
    print (salida) #imprimimos
'''    
'''   
#_________________________________Codigo numero 2____________________________________________
n= int(input('ingrese el tamaño del array para los 2 vectores:')) # ingresamos el tamaño de nuestro array junto con su tamaño y base

nombres=[] # para guardar nuestros nombres
longitud=[] # para guardar o almacenar la longitud de nuestro vector (no. de nombres que ingresaremos)

for i in range (n):
    nombre= input(f"Ingrese los nombres {i+1}:")
    nombres.append(nombre) #aplicacion de la funcion "append" agregamos al final del vector, nuestro vector
    longitud.append(len(nombre)) #aplicamos doble funcion, 1 append y 2 len, nos servira para de nuevo agregar el valor y len para contar el numero de elementos de un objeto
    
    print ("nombres:",nombres)
    print (f"longiud de los nombres:",longitud)
    
'''
'''

#_____________________________codigo numero 3, del escenario numero 1__________________________________________

def analizar_evaluaciones(evaluaciones):
    """
    Analiza un arreglo de evaluaciones de clientes y muestra estadísticas.

    Args:
        evaluaciones (list): Lista de evaluaciones de clientes (números enteros).
    """

    # a) Total de respuestas por tipo
    conteo_respuestas = {
        1: 0,  # Malo
        2: 0,  # Regular
        3: 0,  # Buena
        4: 0,  # Muy Buena
        5: 0,  # Excelente
    }
    for evaluacion in evaluaciones:
        conteo_respuestas[evaluacion] += 1

    print("a) Total de respuestas por tipo:")
    for respuesta, cantidad in conteo_respuestas.items():
        if respuesta == 1:
            tipo = "Malo"
        elif respuesta == 2:
            tipo = "Regular"
        elif respuesta == 3:
            tipo = "Buena"
        elif respuesta == 4:
            tipo = "Muy Buena"
        else:
            tipo = "Excelente"
        print(f"{tipo}: {cantidad}")

    # b) La respuesta más frecuente
    respuesta_mas_frecuente = max(conteo_respuestas, key=conteo_respuestas.get)
    print(f"\nb) Más frecuente: {respuesta_mas_frecuente}")

    # c) Clientes con evaluaciones menores al promedio
    promedio = sum(evaluaciones) / len(evaluaciones)
    print(f"\nc) Promedio: {promedio:.2f}")

    clientes_menor_promedio = [
        i + 1 for i, evaluacion in enumerate(evaluaciones) if evaluacion < promedio
    ]
    porcentaje_menor_promedio = (
        len(clientes_menor_promedio) / len(evaluaciones) * 100
    )
    print(f"   Porcentaje menor al promedio: {porcentaje_menor_promedio:.2f}%")


# Ejemplo de uso
evaluaciones = [5, 2, 4, 5, 3, 4, 1, 5, 4, 3, 2, 5, 4, 4, 5]
analizar_evaluaciones(evaluaciones)


'''