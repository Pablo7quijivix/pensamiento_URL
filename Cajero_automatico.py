#Terminar ejercicio de cajero autmatico a más tardar mañana por la mañana o si mucho 
#Tengo hasta media noche del dia de mañana (Jueves 19 de marzo)

saldo_inicial = 3000
saldo_actual = saldo_inicial
intentos_fallidos = 0

while True:
    try:
        monto_retiro = int(input("Ingrese monto a retirar (0 para salir): "))

        if monto_retiro == 0:
            print("Adiós.")
            break

        if monto_retiro > saldo_actual:
            print("Saldo insuficiente.")
            intentos_fallidos += 1
            print(f"Intentos restantes: {3 - intentos_fallidos}")

            if intentos_fallidos >= 3:
                print("Demasiados intentos fallidos. Adiós.")
                break
        else:
            saldo_actual -= monto_retiro
            print("Retiro exitoso.")
            print(f"Nuevo saldo: {saldo_actual}")
            intentos_fallidos = 0  # Reiniciar intentos fallidos si el retiro es exitoso

            if saldo_actual == 0:
                print("Saldo agotado. Adiós.")
                break

    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")