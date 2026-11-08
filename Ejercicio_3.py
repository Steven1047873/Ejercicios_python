# Ejercicio 3: Cálculo del factorial con ciclo for
# El factorial de n es el producto de los enteros desde 1 hasta n.
# Por definición, 0! = 1.

try:
    numero = int(input("Ingrese un número entero no negativo: "))

    if numero < 0:
        print("Error: el factorial no está definido para números negativos.")
    else:
        factorial = 1

        for i in range(1, numero + 1):
            factorial *= i

        print(f"El factorial de {numero} es: {factorial}")

except ValueError:
    print("Error: debe ingresar un número entero.")
