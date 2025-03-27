'''
tipos de datos
<class 'int'>: identifica que la variable es un entero
<class 'float'>:identifica que la variable es un decimal
<class 'str'>:identifica que la variable es una cadena de texto
<class 'boot'>: identifica que la variable es un valor true o false(boolean)
'''

X=True #True y  son palabras reservadas del lenguaje
print(type(X))

carro="this is Alexis'"
modelo='1992'
print(carro + modelo) #El simbolo + permite concatenar textos en python


'''

TIPOS DE ESTRUCTURAS DE DATOS Y METODOS
1. Conjuntos +
2. Tuplas ++
3. Listas +++
4. Diccionarios +++
'''

#uSO DE CONJUNTOS

'''Los sets o conjuntos son estructuras especiales que nos ayudan a almacenera un grupo 
de elementos. Cuando el orden de los elementos no es relevante podemos utilizar sets
en Python.
además esta estructura no permite elementos duplicados

Cómo se define: {, , , , }

'''

set1={"a","b",'c','d'}
# print(type(set1))

#métodos para el tratamientos de conjuntos
set1.union()
# Unión de conjuntos
set2={"e",'f',"g"}
# print(set1.union(set2))

set3={"a","b","c","d","d"}
# print(set3)
set4=set3.union(set1)
# print(set4)


#Interseccion
set5={"f","w","a","b"}
# print(set5.intersection(set1))
# set5.remove("w")
# print(set5)

# set4.add("r")
# print(set4)

set6={"alexis",5,True}
set7={"alexis",5,True, "daniel"}
# print(set6.issuperset(set7))# false
# print(set7.issuperset(set6))# True


# print(set6.issubset(set7))#true
# print(set7.issubset(set6))#false


'''
Uso de Tuplas
Son estructuras de datos rigidas, que no permiten muchos métodos
se usan cuando queremos resguardar la información (inmutable)
como se define:(, , , , , )
<class ''>
'''

tupla1=(1,1,1,1,1,2,3,4,5)
print(type(tupla1))

#Métodos
#count
conteo=tupla1.count(1)
# print(conteo)

#index
indice=tupla1.index(5)

'''PYTHON ES UN LENGUAJE INDEXADO EN CERO
Siempre la estructura de datos tiene
el indice 0, en otras palabras, la posición inicial siempre es 0
indice <==> posición
'''

'''USO DE LISTAS
LA LISTA EN PYTHON SON UNA ESTRUCTURAS DE DATOS QUE ALMACENAN
ELEMENTOS DE MANERA ORDENADAS Y MUTABLES.
SON UN TIPO DE DATO NATIVO DEL LENGUAJE DE PROGRAMACIÓN PYTHON.
COMO SE DEFINEN: [, , , , , ]
<class 'list'>
'''
lista1=[8,9,7,5,4,10]
print(type(lista1))

lista2=[["jhon", "alejandro", "lewin"],["isabel", "juan", "daniel"]]
# print(type(lista2))#<class'list'>

#métodos
# print(lista1.count(14))

print("------")
#INVESTIGACIÓN
#reverse
lista1 = [8, 9, 7, 5, 4, 10]
lista1.reverse()  # Modifica lista1 en su lugar
print("Salida del método reverse ")
print(lista1)  # Ahora lista1 está invertida
# 
#Salida del método reverse
#[10, 4, 5, 7, 9, 8]
lista1 = [8, 9, 7, 5, 4, 10]
listad= list(reversed(lista1))  # Convierte el iterador en una lista nueva
print("esta es la lista d", listad)


#sort
lista2  = [8, 9, 7, 5, 4, 10]
lista2.sort() #en orden ascendente es por defecto
print("salida del método sort")
print(lista2)
#salida del método sort
#[4, 5, 7, 8, 9, 10]
lista2.sort(reverse=True)
listac=lista2.sort(reverse=True)
print("salida del método sort con reverse True")
print(lista2)

#salida del método sort con reverse True -->orden descendente
#[10, 9, 8, 7, 5, 4]
lista2.sort()

#FIRMA DEL MÉTODO SORT
#list.sort(*, key: None = None, reverse: bool = False) -> None
'''
* → Indica que los parámetros después de este deben pasarse por nombre 
(es decir, key= y reverse= deben especificarse explícitamente).

key: None = None → Parámetro opcional que permite definir una función personalizada 
para ordenar los elementos.

reverse: bool = False → Si es True, ordena en orden descendente; si es False,
ordena en ascendente (por defecto).

-> None → Indica que el método no devuelve nada (None), 
sino que modifica la lista en su lugar (in-place).
'''

'''
Si quieres guardar la lista ordenada en otra variable sin modificar la original,
NO uses .sort() porque modifica la lista en su lugar y devuelve None.
En su lugar, usa la función sorted().

lista2 = [8, 9, 7, 5, 4, 10]

lista_ordenada = sorted(lista2)  # Crea una nueva lista ordenada
print("Lista original:", lista2)  # [8, 9, 7, 5, 4, 10]
print("Lista ordenada:", lista_ordenada)  # [4, 5, 7, 8, 9, 10]

Otra opción es:
lista2.sort()
lista_ordenada = lista2.copy()  # Guarda una copia de la lista ordenada
print("Lista ordenada:", lista_ordenada)  # [4, 5, 7, 8, 9, 10]

'''
#reverse
# print(lista1.reverse())

#append

# lista1.append("20")
# print(lista1)

# listab=lista1.sort()


# lista1.remove(7)
# print(lista1)

#como acceder a los elmentos de la lista
lista2=[["jhon", "alejandro", "lewin"],["isabel", "juan", "daniel"]]

print(lista2[0][1])