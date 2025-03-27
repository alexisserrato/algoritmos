'''
Problema: Crear un diccionario con las calificaciones de 3 estudiantes 
y permitir que el usuario consulte la calificación de uno de ellos.
'''

# Crear diccionario con calificaciones
calificaciones = {
    "Ana": 85,
    "Juan": 90,
    "Luis": 78
}

# Solicitar nombre del estudiante
nombre = input("Ingrese el nombre del estudiante para consultar su calificación: ")

# Mostrar la calificación si el estudiante existe
if nombre in calificaciones:
    print(f"La calificación de {nombre} es {calificaciones[nombre]}")
else:
    print("Estudiante no encontrado.")
