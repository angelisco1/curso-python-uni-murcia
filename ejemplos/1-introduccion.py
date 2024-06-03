# Esto es un comentario
hola_mundo = 'Hola mundo'
print(hola_mundo)
print(type(hola_mundo))

# Int
cantidad = 17
print(type(cantidad))

# Float
precio = 19.99
print(type(precio))

# Boolean
# False
disponible = True
print(type(disponible))

es_null = None
print(type(es_null))

# Casting de tipos
precio2 = '3.50'
precio3 = float(precio2)
print(type(precio3))

# precio2 = 'tres con cincuenta'
# precio3 = float(precio2)
# print(type(precio3))

precio4 = str(precio3)
print(type(precio4))

print(2+5j + 1+2j)

print(type(2.0))
print(type(2.))
print(type(2))


print(isinstance(hola_mundo, str))
print(isinstance(hola_mundo, int))
# print(isinstance(es_null, NoneType))


# Asignación múltiple
x = 1
y = 2
x, y = y, x+3


# Formateador de strings
nombre = 'Ángel'
# nombre.encode('utf-8')
edad = 30
print('Hola ' + nombre)
# Antiguo formateador
# print('Hola %s' % nombre)
# print('Hola %s, tengo %d' % (nombre, edad))

# print('Hola {}, tengo {}'.format(nombre, edad))
# print('Hola {1}, tengo {0}'.format(edad, nombre))

# f-strings
print('Hola {nombre}, tengo {edad}')
print(f"Hola {nombre}, tengo {edad}")


# Listas
lista_nums = [1, '2', 3., 4+2j]
print(lista_nums)
print(type(lista_nums))

# Obtener la longitud
print(len(lista_nums))
print(len(nombre))

carrito_compra = []
carrito_compra.append('Alfombrilla de ratón')
carrito_compra.append('Cargador inalambrico')
print(carrito_compra)

ultimo_elem = carrito_compra.pop()
print(ultimo_elem)
print(carrito_compra)

carrito_compra.clear()
print(carrito_compra)

lista_nums = [1, 2, 3, 4, 5, 3, 5]

tres = lista_nums[2]
print(tres)

print(lista_nums.index(4))
print(lista_nums.count(5))


carrito_compra = []
carrito_compra.append('Alfombrilla de ratón')
carrito_compra.append('Cargador inalambrico')

for prod in carrito_compra:
  print(f"El producto {prod} está en el carrito")

for prod in enumerate(carrito_compra):
  print(f"El producto {prod[1]} está en el carrito en la posición {prod[0]+1}")

for i in range(5):
  print(i)

# Tupla
# (0, 'Alfombrilla de ratón')
# (1, 'Cargador inalambrico')


# Unpacking
pos, elem = (0, 'Alfombrilla de ratón')
print(pos, elem)

for pos, nombre in enumerate(carrito_compra):
  print(f"El producto {nombre} está en el carrito en la posición {pos+1}")


muchos_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(muchos_numeros[-2]) # Penultimo elemento: 14

# Slicing
print(muchos_numeros[0:5])
print(muchos_numeros[3:5])
print(muchos_numeros[0:15:2])
print(muchos_numeros[::2])
print(muchos_numeros[::5])
print(muchos_numeros[::-1])

lista_de_2_en_2 = []
for index, elem in enumerate(muchos_numeros):
  if not index % 2:
    lista_de_2_en_2.append(elem)

print(lista_de_2_en_2)


# Placeholder *__
(n1, n2, *resto_elems) = lista_de_2_en_2
print(lista_de_2_en_2)
print(n1)
print(n2)
print(resto_elems)

(n1, *_, n2) = lista_de_2_en_2
print(lista_de_2_en_2)
print(n1)
print(n2)
print(_)


# Añade a la lista los elementos que hay en resto_elems
lista = [1, 2, 3]
lista.extend(resto_elems)
print(lista)

# Elimina el elemento 2
lista.remove(2)
print(lista)



# Sets/Conjuntos
lista_nums = [1, 2, 3, 4, 5, 6, 1, 2, 2, 2, 3, 3, 6]
conjunto1 = set(lista_nums)
print(conjunto1)

conjunto1.add(9)
print(conjunto1)

conjunto1.remove(3)
# conjunto1.remove(7) # Lanza excepción porque no existe el 7
print(conjunto1)

conjunto1.discard(2)
conjunto1.discard(7)
print(conjunto1)

print(conjunto1.union({10, 11, 12}))
print(conjunto1.intersection({1, 5, 12}))
print(conjunto1.difference({1, 5, 12}))
print(conjunto1.symmetric_difference({1, 5, 12}))
