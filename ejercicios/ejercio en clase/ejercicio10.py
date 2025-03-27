'''
Problema: Crear un diccionario con algunos productos 
y permitir que el usuario agregue un nuevo producto con su precio.
'''

# Crear diccionario con productos y precios
productos = {"Televisor": 700000,"lapto": 1500000,"impresora": 846000}

# Solicitar al usuario un nuevo producto y su precio
nuevo_producto = input("Ingrese el nombre del nuevo producto: ")
precio = float(input(f"Ingrese el precio de {nuevo_producto}: "))

# Agregar el nuevo producto al diccionario
productos[nuevo_producto] = precio

# Mostrar el diccionario actualizado
print("\nLista actualizada de productos y precios:")
for producto, precio in productos.items():
    print(f"{producto}: ${precio:.2f}")

# el carácter “\n” es una secuencia de escape que se utiliza para crear 
# una nueva línea. Se escribe como una barra invertida seguida de la letra “n”. 
