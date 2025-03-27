'''
Problema: Escribe un programa que verifique si una palabra ingresada por el usuario está 
en la siguiente frase:
"Python es un lenguaje de programación poderoso".
'''


texto = "Python es un lenguaje de programación poderoso"

palabra = input("ingrese su palabra")

veri = palabra in texto

print(veri)