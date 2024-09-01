temperaturas = []

print("Por favor ingrese 10 temperaturas")

for i in range(10):
    temperaturas.append(float(input(f"Temperatura {i + 1}: ")))

promedio = sum(temperaturas)/len(temperaturas)
print(f"El promediode las temperaturas es: {promedio:.2f}")

while True:
    opcion = input("¿Ver alguna temperatura especifica? (si/no): ").strip().lower()
    if opcion == "si":
        posicion = int(input("Ingrese la posicion que desea ver (1-10: "))
        if 1 <= posicion <= 10:
            print(f"Latemperatura en la pocision {posicion} es: {temperaturas[posicion-1]:.2f}")
        else:
            print("Pocicion fuera de rango")
    elif opcion == "no":
        print("Cierre del programa")
        break
    else:
        print("Por favr ingresa si o no")