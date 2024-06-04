def funcion1():
  pass


def suma(a, b):
  return a + b


print(suma(1, 2))


def saludar(nombre='Mundo'):
  print(f'Hola {nombre}')


saludar('Charly')
saludar('Ángel')
saludar()


def add_to_list(item, lista=[]):
  lista.append(item)
  return lista


# lista1 = []
# lista1 = add_to_list(1, lista1)
# lista1 = add_to_list(2, lista1)
# print(lista1)


lista1 = add_to_list(1)
lista1 = add_to_list(2)
print(lista1)


def add_to_list2(item, lista=None):
  if not lista:
    lista = []
  lista.append(item)
  return lista


lista1 = add_to_list2(1)
print(lista1)
lista1 = add_to_list2(2)
print(lista1)


# *args y **kwargs
def muestra_num_loteria(sorteo, *args, **kwargs):
  print(args)
  print(kwargs)
  # nums_como_str2 = []
  # for n in args:
  #   nums_como_str2.append(str(n))
  nums_como_str = map(str, args)
  if sorteo == 'Euromillón':
    print(f'El número que has comprado para el sorteo {sorteo} es: {", ".join(nums_como_str)} y las estrellas son: {kwargs["e1"]}, {kwargs["e2"]}')
  else:
    print(f'El número que has comprado para el sorteo {sorteo} es: {", ".join(nums_como_str)}')


muestra_num_loteria('Bonoloto', 1, 2, 3, 4, 5)
muestra_num_loteria('Primitiva', 1, 2, 3, 4, 5, 6, 7, 8)
muestra_num_loteria('Euromillón', 1, 2, 3, 4, 5, 6, e1=2, e2=5)


nums = [1, 2, 3, 4, 5, 6, 7, 8]
n1, n2, *resto = nums
print(n1, n2)
print(resto)

*resto, n1, n2 = nums
print(n1, n2)
print(resto)

n1, *resto, n2 = nums
print(n1, n2)
print(resto)


lista_nueva = [nums]
print(lista_nueva)


producto = {
  'stock': 248,
  'ventas': 13
}

conjunto = {1, 2, 20}
tupla = (21, 32, -20)
lista_nueva = [*nums, 10, 11, 12, *conjunto, *tupla, *producto.values()]
print(lista_nueva)


persona = {
  'nombre': 'Charly',
  'apellido': 'Falco',
  'email': 'charly@gmail.com'
}

credenciales = {
  'email': 'cfalco@gmail.com',
  'password': '1234qwerty'
}

datos_usuario = {**persona, **credenciales}
print(datos_usuario)
