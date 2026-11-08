# Ejercicio 2: Cálculo y clasificación del IMC
# IMC = peso (kg) / altura (m) ** 2

try:
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))

    if peso <= 0 or altura <= 0:
        print("Error: el peso y la altura deben ser mayores que cero.")
    else:
        imc = peso / (altura ** 2)
        print(f"Su IMC es: {imc:.2f}")

        if imc < 18.5:
            print("Clasificación: bajo peso.")
        elif imc < 25:
            print("Clasificación: peso normal.")
        elif imc < 30:
            print("Clasificación: sobrepeso.")
        else:
            print("Clasificación: obesidad.")

except ValueError:
    print("Error: ingrese valores numéricos válidos.")