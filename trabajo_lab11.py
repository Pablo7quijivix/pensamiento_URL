'''
_____ejercicio___1


import math

class ExperimentoFisico:
   
    def realizar_experimento(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

class CaidaLibre(ExperimentoFisico):
    
    def __init__(self, altura, gravedad=9.8):
       
        if altura < 0:
            raise ValueError("La altura no puede ser negativa.")
        if gravedad == 0:
            raise ValueError("La gravedad no puede ser cero.")
        self.altura = altura
        self.gravedad = gravedad

    def calcular_tiempo_caida(self):
        """
        Calcula el tiempo de caída del objeto.

        Returns:
            float: El tiempo de caída en segundos.
        """
        tiempo = math.sqrt((2 * self.altura) / self.gravedad)
        return tiempo

    def realizar_experimento(self):
        """
        Realiza el experimento de caída libre y muestra el resultado.
        """
        try:
            tiempo_caida = self.calcular_tiempo_caida()
            print(f"Simulación de Caída Libre:")
            print(f"  Altura inicial: {self.altura} metros")
            print(f"  Aceleración debido a la gravedad: {self.gravedad} m/s^2")
            print(f"  Tiempo de caída calculado: {tiempo_caida:.2f} segundos")
        except ValueError as e:
            print(f"Error en la simulación: {e}")

# Ejemplo de uso:
if __name__ == "__main__":
    try:
        experimento1 = CaidaLibre(altura=10.0)
        experimento1.realizar_experimento()

        print("\n---")

        experimento2 = CaidaLibre(altura=20.0, gravedad=9.81)
        experimento2.realizar_experimento()

        print("\n---")

        experimento_error_altura = CaidaLibre(altura=-5.0)
        experimento_error_altura.realizar_experimento()

        print("\n---")

        experimento_error_gravedad = CaidaLibre(altura=10.0, gravedad=0)
        experimento_error_gravedad.realizar_experimento()

    except ValueError as e:
        print(f"Error al crear el experimento: {e}")

        

______ejercicio2_______________
'''
import math

class OperacionCientifica:
    
    def calcular(self, *args):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

class RaizCuadrada(OperacionCientifica):
    
    def calcular(self, numero):
        if numero < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        return math.sqrt(numero)

class Potencia(OperacionCientifica):
    
    def calcular(self, base, exponente):
        return math.pow(base, exponente)

class Logaritmo(OperacionCientifica):
    
    def calcular(self, numero):
        if numero <= 0:
            raise ValueError("No se puede calcular el logaritmo de un número no positivo.")
        return math.log(numero)

class Factorial(OperacionCientifica):
    
    def calcular(self, numero):
        if not isinstance(numero, int) or numero < 0:
            raise ValueError("No se puede calcular el factorial de un número negativo o no entero.")
        return math.factorial(numero)

def realizar_operacion(operacion, *args):
    
    try:
        resultado = operacion.calcular(*args)
        return resultado
    except ValueError as e:
        print(f"Error en la operación: {e}")
        return None

def calculadora_cientifica():
    """
    Función principal que presenta la calculadora científica personalizada.
    """
    operaciones = {
        "raiz": RaizCuadrada(),
        "potencia": Potencia(),
        "logaritmo": Logaritmo(),
        "factorial": Factorial()
    }

    while True:
        print("\nCalculadora Científica Personalizada")
        print("Operaciones disponibles:")
        for nombre in operaciones:
            print(f"- {nombre}")
        print("- salir")

        seleccion = input("Selecciona una operación: ").lower()

        if seleccion == "salir":
            print("¡Gracias por usar la calculadora científica!")
            break
        elif seleccion in operaciones:
            operacion = operaciones[seleccion]
            try:
                if seleccion == "raiz":
                    numero = float(input("Ingresa el número: "))
                    resultado = realizar_operacion(operacion, numero)
                elif seleccion == "potencia":
                    base = float(input("Ingresa la base: "))
                    exponente = float(input("Ingresa el exponente: "))
                    resultado = realizar_operacion(operacion, base, exponente)
                elif seleccion == "logaritmo":
                    numero = float(input("Ingresa el número: "))
                    resultado = realizar_operacion(operacion, numero)
                elif seleccion == "factorial":
                    numero = int(input("Ingresa el número entero: "))
                    resultado = realizar_operacion(operacion, numero)

                if resultado is not None:
                    print(f"El resultado de {seleccion} es: {resultado}")

            except ValueError:
                print("Error: Entrada inválida. Por favor, ingresa un número válido.")
        else:
            print("Operación no válida. Por favor, selecciona una de las opciones disponibles.")

if __name__ == "__main__":
    calculadora_cientifica()