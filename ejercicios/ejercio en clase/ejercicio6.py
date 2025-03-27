'''
Problema: Solicitar al usuario 5 números enteros, almacenarlos en una lista y luego mostrar:

    La lista original.

    La lista en orden inverso.

    La suma de los números.
'''

# texto = "ingresa 5 numeros enteros"

# user1 = input("ingrese numero")
# user2 = input("ingrese numero")
# user3 = input("ingrese numero")
# user4 = input("ingrese numero")
# user5 = input("ingrese numero")


# # Mostrar la lista original
# print(f"Lista original: {user1, user2,user3 , user4, user5}")

# # Mostrar la lista en orden inverso
# print(f"Lista en orden inverso: {user1 , user2 ,user3 , user4 , user5 [-1]}")

# # Calcular y mostrar la suma de los números
# suma = sum(user1 + user2 + user3 + user4 + user5)
# print(f"La suma de los números es: {suma}")

# Solicitar 5 números enteros al usuario y almacenarlos en una lista
numeros = []
for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Mostrar la lista original
print(f"Lista original: {numeros}")

# Mostrar la lista en orden inverso
print(f"Lista en orden inverso: {numeros[::-1]}")

# Calcular y mostrar la suma de los números
suma = sum(numeros)
print(f"La suma de los números es: {suma}")
