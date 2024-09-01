Datos_Basicos = {
    'Nombres': 'Juan Carlos',
    'Apellidos': 'Pérez Garcia',
    'DUI': '01025487-9',
    'Fecha_Nacimiento': '23/07/1980',
    'Lugar_Nacimiento': 'Soya City',
    'Nacionalidad': 'Salvadoreño',
    'Estado_Civil': 'Complicado'
}

print("\nDetalles del Diccionario")
print("=============================")

print(f"Claves del Diccionario: {Datos_Basicos.keys()}")
print(f"Valores del diccionario: {Datos_Basicos.values()}")
print(f"Elementos del diccionario: {Datos_Basicos.items()}")

#Ejemplo practico de los diccionarios
print("Inscripcion del curso")
print("=============================")

print("Datos del participante")
print("==============================")

print(f"DUI: {Datos_Basicos['DUI']}")
print(f"Nombre completo: {Datos_Basicos['Nombres']} {Datos_Basicos['Apellidos']}")