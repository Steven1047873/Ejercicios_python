# Ejercicio 4: Tabla de multiplicar con ciclo while
 
try:
    numero = float(input("Ingrese el número para generar su tabla: "))
    contador = 1
 
    print(f"\nTabla de multiplicar del {numero:g}")
 
    while contador <= 10:
        resultado = numero * contador
        print(f"{numero:g} x {contador} = {resultado:g}")
        contador += 1
 
except ValueError:
    print("Error: debe ingresar un valor numérico.")
