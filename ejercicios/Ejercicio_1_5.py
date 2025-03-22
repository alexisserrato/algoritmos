#ejercicio 1.5
'''Escriba un programa que realice la comprobación
de la división. Recuerde:
Divisor * Cociente + Residuo = Dividendo
Tome como entrada dos números, realice la
división entre ellos y entregue al usuario un texto
descriptivo con la comprobación de la división.'''

divide=10/52
print(10/2)
print(float(10/2))
dividendo=int(input("ingrese el primer numero"))
divisor=int(input("ingrese el segundo numero"))
#calculos
cociente=dividendo/divisor
residuo=dividendo%divisor
print(f"la comprobación de la division es {divisor} por {cociente} más {residuo} es igual {dividendo}")

