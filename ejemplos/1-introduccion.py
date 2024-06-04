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

# carrito_compra.clear()
fn_clear = carrito_compra.clear
fn_clear()
print(f'CLEAR: {carrito_compra}')

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


# Diccionarios
persona = {
  'nombre': 'Charly',
  'apellido': 'Falco'
}

print(f'Hola, me llamo {persona["nombre"]} {persona["apellido"]}')
# print(f'Hola, me llamo {persona['nombre']} {persona['apellido']}')

print(f'Las claves del dict son {persona.keys()}')
print(f'Los valores del dict son {persona.values()}')
print(f'Los pares del dict son {persona.items()}')

if 'nombre' in persona.keys():
  print('Hacemos algo con el nombre')


persona['email'] = 'cfalco@gmail.com'

print(persona)

print(len(persona))


color = 'red'
if color == 'green' or color == 'red':
  print('El color está en la lista')

if color in ['green', 'red']:
  print('El color está en la lista')


for item in persona:
  print(item)

for item in persona.values():
  print(item)

for item in persona.items():
  print(f'{item[0]} = {item[1]}')

for key, value in persona.items():
  print(f'{key} = {value}')

# print(persona['password']) # KeyError: 'password'
print(persona.get('password')) # None
print(persona.get('password', '12345')) # '12345'



# CONDICIONALES
pais = 'eeuu'
edad = 20

if pais == 'eeuu':
  print('Estás en EEUU')
  if edad >= 18 and edad < 21:
    print('Puedes conducir, puedes tener un arma, pero no puedes beber alcohol')
  elif edad >= 21:
    print('Puedes conducir, puedes tener un arma y puedes beber alcohol')
  else:
    print('No puedes conducir, ni tener un arma, ni beber alcohol')
else:
  print('No estás en EEUU')

usuario_logueado = None

# if usuario_logueado == None:
if not usuario_logueado:
  print('No hay ningún usuario logueado...')


# BUCLES

# for i=0;i<5;i++
i = 0
while i < 5:
  print(i)
  i += 1


i = 0
num_buscado = 7
while i < 5:
  if i == num_buscado:
    break
  print(i)
  i += 1
else:
  print('No se ha pasado por el número buscado')


lista_usuarios = [
  persona,
  { 'nombre': 'Mike', 'apellido': 'Kozinski', 'email': 'mike@gmail.com', 'password': '1234' },
  { 'nombre': 'Sara', 'apellido': 'Connor', 'email': 's.connor@gmail.com', 'password': '1234' },
]
usuario_buscado = None
email_buscado = 'mike@gmail.com'
# email_buscado = 'mike@gmail.es'

for usuario in lista_usuarios:
  if usuario['email'] == email_buscado:
    usuario_buscado = usuario
    break
  print(usuario)

if usuario_buscado:
  print('Hemos encontrado el usuario')
else:
  print('No hemos encontrado ningún usuario con los datos de búsqueda usados.')

for usuario in lista_usuarios:
  if usuario['email'] == email_buscado:
    usuario_buscado = usuario
    print('Hemos encontrado el usuario')
    break
  print(usuario)
else:
  print('No hemos encontrado ningún usuario con los datos de búsqueda usados.')