# Programación funcional

# map: transformar una lista en otra lista
clicks_de_usuarios_al_min = [142, 130, 135, 150]

def transforma_clicks_a_texto(item):
  index, num = item
  return f'El usuario {index + 1} ha hecho {num} clicks en 1 minuto'

lista_clicks_por_min_texto = map(transforma_clicks_a_texto, enumerate(clicks_de_usuarios_al_min))
print(lista_clicks_por_min_texto)
print(list(lista_clicks_por_min_texto))

# El iterador ya se ha consumido y por eso muestra []
print(list(lista_clicks_por_min_texto))


lista_clicks_por_min_texto = list(map(transforma_clicks_a_texto, enumerate(clicks_de_usuarios_al_min)))
print(lista_clicks_por_min_texto)
print(lista_clicks_por_min_texto)
print(lista_clicks_por_min_texto)


titulos = [
  'game of thrones',
  'the walking dead',
  'yellowstone'
]

def titlecase(titulo):
  return titulo.title()

print(list(map(titlecase, titulos)))


# filter -> filtra un iterable y obtenemos un iterador con los valores que cumplen una condición
nums = [1, 2, 3, 4, 5, 6]

def es_par(num):
  return num % 2 == 0

nums_pares = list(filter(es_par, nums))
print(nums_pares)


# sorted -> ordenar
import random

nums_aleatorios = random.sample(range(100), 15)
print(sorted(nums_aleatorios))
print(sorted(nums_aleatorios, reverse=True))
print(sorted(nums_aleatorios)[::-1])

print(sorted(list(filter(es_par, clicks_de_usuarios_al_min))))

usuarios = [
  { 'nombre': 'Charly', 'edad': 38 },
  { 'nombre': 'Paco', 'edad': 36 },
  { 'nombre': 'Sara', 'edad': 37 },
  { 'nombre': 'Eva', 'edad': 34 },
]

def get_edad(usuario):
  return usuario['edad']

print(sorted(usuarios, key=get_edad))

def get_nombre(usuario):
  return usuario['nombre']

print(list(map(get_nombre, sorted(usuarios, key=get_edad))))




stock_productos = [100, 120, 119, 180]
ventas_productos = [140, 10, 229, 90]
ids_productos = ['a', 'b', 'c', 'd']

lista_stock_ventas_productos = list(zip(stock_productos, ventas_productos))
print(lista_stock_ventas_productos)

print(lista_stock_ventas_productos, list(zip()))

print(list(zip(ids_productos, list(zip(stock_productos, ventas_productos)))))

stock_ventas_productos = dict(zip(ids_productos, lista_stock_ventas_productos))
print(stock_ventas_productos)

print(stock_ventas_productos['c'][1])


# Funciones lambdas: funciones anónimas
# lambda x, y, z: x + y * z

# def titlecase(titulo):
#   return titulo.title()
print(list(map(lambda titulo: titulo.title(), titulos)))


nums = [1, 2, 3, 4, 5, 6]
# def es_par(num):
#   return num % 2 == 0

nums_pares = list(filter(lambda n: n % 2 == 0, nums))
print(nums_pares)

# nums_pares = [n for n in nums if (lambda num: num % 2 == 0)()]

print(list(map(lambda u: u['nombre'], sorted(usuarios, key=lambda u: u['edad']))))


# ITERTOOLS
import itertools

stock_productos = [100, 120, 119, 180, 225]
ventas_productos = [140, 10, 229, 90]
ids_productos = ['a', 'b', 'c', 'd', 'e']

lista_stock_ventas_productos = list(zip(stock_productos, ventas_productos))
print(lista_stock_ventas_productos)

lista_stock_ventas_productos = list(itertools.zip_longest(stock_productos, ventas_productos))
print(lista_stock_ventas_productos)

lista_stock_ventas_productos = list(itertools.zip_longest(stock_productos, ventas_productos, fillvalue=0))
print(lista_stock_ventas_productos)


letras = 'one'
longitud_contraseña = 3

print(list(itertools.product(letras, repeat=longitud_contraseña)))


import functools

print(functools.reduce(lambda x, y: x + y, ventas_productos))
print(functools.reduce(lambda x, y: x + y, ventas_productos, 10))


usuarios = [
  { 'nombre': 'Charly', 'edad': 38 },
  { 'nombre': 'Paco', 'edad': 36 },
  { 'nombre': 'Sara', 'edad': 37 },
  { 'nombre': 'Eva', 'edad': 34 },
]