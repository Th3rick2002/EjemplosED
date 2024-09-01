filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

matriz = [["A" for _ in range(columnas)] for _ in range(filas)]

print("La matriz resultante es: ")
for fila in matriz:
    print(fila)