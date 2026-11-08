# Ejercicio 1: Clasificación de un número
# Determina si un número es positivo, negativo o cero.

try:
    numero = float(input("Ingrese un número: "))
    
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")

except ValueError:
    print("Error: debe ingresar un valor numérico.")