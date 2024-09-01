#crear chatbot
#consulta 1 informacion de inicio de ciclo I 2025
#consulta 2 inicio de incripcion ciclo I 2025
#consulta 3 finaizacion del ciclo 2025

print("Chatbot, informacion del ciclo I 2025")

while True:
    opcion = int(input("Ingrese una opción para obtener mas información "
                       "\n1. Inicio de ciclo I 2025 "
                       "\n2. Inicio de incripción de ciclo I 2025 "
                       "\n3. Finalización de ciclo I 2025 "
                       "\n4. Salir"
                       "\n=>: "))

    if opcion == 1:
        print("El ciclo I 2025 inicia la segunda semana de Enero de 2025")
    elif opcion == 2:
        print("Las incripciones para el ciclo I 2025 comienzan en Diciembre de 2024")
    elif opcion == 3:
        print("La finalizacion del ciclo I 2025 termina en la segunda semana de Junio de 2025")
    elif opcion == 4:
        print("Adios, tenga un exelente dia")
        break
    else:
        print("Opcion invalida")