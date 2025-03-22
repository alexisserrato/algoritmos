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