'''Problema: Solicitar al usuario dos conjuntos de números y luego mostrar:

    La unión de ambos conjuntos.

    La intersección de ambos conjuntos'''
    
   
def obtener_conjunto(mensaje):
   return set(map(int, input(mensaje).split()))

# Solicitar los dos conjuntos al usuario
conjunto1 = obtener_conjunto("Ingrese los números del primer conjunto separados por espacios: ")
conjunto2 = obtener_conjunto("Ingrese los números del segundo conjunto separados por espacios: ")

# Calcular la unión e intersección
union = conjunto1 | conjunto2
interseccion = conjunto1 & conjunto2

# Mostrar resultados
print(f"Unión: {union}")
print(f"Intersección: {interseccion}")