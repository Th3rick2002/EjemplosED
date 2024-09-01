temperaturas = []

print("Por favor ingrese 10 temperaturas")

for i in range(10):
    temperaturas.append(float(input(f"Temperatura {i + 1}: ")))

promedio = sum(temperaturas)/len(temperaturas)
print(f"El promediode las temperaturas es: {promedio:.2f}")

