filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

matriz = []

for i in range(filas):
    filas = []
    for j in range(columnas):
        valor = float(input(f"Elemento[{ i + 1 }][{ j + 1 }]: "))
        filas.append(valor)
        matriz.append(filas)

print("La matriz ingresada es:")
for fila in matriz:
    print(fila)