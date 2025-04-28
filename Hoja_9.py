'''
#Ejercicio 1:
Crea un procedimiento: es_par_o_impar(n)  
Que diga si un número es par o impar. Solo debe mostrar el resultado en pantalla, no 
devolverlo


def par_impar (num ):
    if num % 2 == 0:
        print ("par")
    else:    
        print("impar")
par_impar (10)



_____2do codigo_______

Ejercicio 2: 
Crea una función suma_lista(lista) que reciba una lista de números y devuelva la suma total.

def suma_lista(lista):
    return sum(lista)
lista = [1,2,3,4,5]
resultado = suma_lista (lista)
print ("La sumatoria es igual a: ", resultado)



codigo numero 3 
Ejercicio 3: 
Cuenta regresiva: Crea una función recursiva cuenta_regresiva(n) que imprima desde n 
hasta 0. 


def cuenta_regresiva (num):
    
    if num < 0:
        print ("Cuenta regresiva terminada")
    else:
        print (f"El numero de la cuenta regresiva comienza en: {num}")
        cuenta_regresiva (num - 1 )
cuenta_regresiva(4)

Codigo no.4 
Ejercicio 4 
Crear una función recursiva que imprima los números del 1 hasta n 
# Resultado esperado:  cuenta_ascendente(4): 


def imprimir_hasta(n):

  if n > 0:
    imprimir_hasta(n - 1)  
    print(f"Ascendiendo -> {n}")

numero_limite = int(input("Ingresa un número entero positivo: "))
imprimir_hasta(numero_limite)


_________codigo5_____________________
def suma_hasta(n):
  if n == 1:
    return 1  
  else:
    return n + suma_hasta(n - 1) 

numero = 10
resultado = suma_hasta(numero)
print(f"La suma desde 1 hasta {numero} es: {resultado}")

___________________________Codigo_6_________________


def factorial(n):
  if n == 0:
    return 1  
  else:
    return n * factorial(n - 1)  

numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")


_______________codigo_7___________

def minimo(lista):
  
  if len(lista) == 1:
    return lista[0]  
  else:
    primer_elemento = lista[0]
    resto_de_la_lista = lista[1:]
    minimo_del_resto = minimo(resto_de_la_lista)
    if primer_elemento < minimo_del_resto:
      return primer_elemento
    else:
      return minimo_del_resto

numeros = [5, 3, 8, 1, 2]
valor_minimo = minimo(numeros)
print(f"El valor mínimo en la lista {numeros} es: {valor_minimo}")

________________juego________________________
'''
import random
import time

def adivina_el_numero(numero_secreto, intentos, tiempo_inicio):

  if intentos == 0:
    tiempo_final = time.time()
    tiempo_total = round(tiempo_final - tiempo_inicio, 2)
    print(f"\n¡Se te acabaron los intentos! El número secreto era {numero_secreto}.")
    print(f"Tiempo total de juego: {tiempo_total} segundos.")
    return

  try:
    intento = int(input(f"Intento #{6 - intentos}: Ingresa tu número (entre 1 y 100): "))
    if 1 <= intento <= 100:
      if intento == numero_secreto:
        tiempo_final = time.time()
        tiempo_total = round(tiempo_final - tiempo_inicio, 2)
        print(f"\n¡Felicidades! ¡Adivinaste el número {numero_secreto} en {6 - intentos} intentos!")
        print(f"Tiempo total de juego: {tiempo_total} segundos.")
        return
      elif intento < numero_secreto:
        print("Demasiado bajo. ¡Intenta de nuevo!")
      else:
        print("Demasiado alto. ¡Intenta de nuevo!")
      adivina_el_numero(numero_secreto, intentos - 1, tiempo_inicio)  # Llamada recursiva
    else:
      print("¡Número fuera de rango! Debe estar entre 1 y 100.")
      adivina_el_numero(numero_secreto, intentos, tiempo_inicio) # Llamada recursiva sin perder intento
  except ValueError:
    print("¡Entrada inválida! Por favor, ingresa un número entero.")
    adivina_el_numero(numero_secreto, intentos, tiempo_inicio) # Llamada recursiva sin perder intento

# Iniciar el juego
print("Bienvenido al juego de Adivina el Número.")
print("Estoy pensando en un número entre 1 y 100.")
print("Tienes 5 intentos para adivinarlo.")
print("¡Buena suerte!")

numero_secreto = random.randint(1, 100)
tiempo_inicio = time.time()  # Marca el inicio del tiempo
adivina_el_numero(numero_secreto, 5, tiempo_inicio)

