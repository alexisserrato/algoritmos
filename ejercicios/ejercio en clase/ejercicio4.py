'''
Problema: Escribe un programa que determine si un número ingresado por el 
usuario es par o impar utilizando el operador módulo %.
'''
# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Verificar si el número es par o impar usando el operador módulo
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")


#Usamos la función input()para que el usuario ingrese un número. Como input()devuelve una cadena, utilizamos int()para convertirlo a un número entero.

# Usamos el módulo de operador %para calcular el residuo de la división entre el número ingresado y 2.

# Si el residuo es 0, el número es par.

# Si el residuo es distinto de 0, el número es impar.