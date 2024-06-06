# [item for item in items]
nums = [1, 2, 3, 4, 5, 6]

# map
doble_nums = [num * 2 for num in nums]
print(doble_nums)

# filter
doble_nums_entre_3_y_9 = [num * 2 for num in nums if num * 2 > 3 and num * 2 < 9]
print(doble_nums_entre_3_y_9)

doble_nums_entre_3_y_9 = [num for num in doble_nums if num > 3 and num < 9]
print(doble_nums_entre_3_y_9)

# lista = []
# for num in doble_nums:
#   if num > 3 and num < 9:
#     lista.append(num)


titulos = [
  'game of thrones',
  'the walking dead',
  'yellowstone'
]

titulos_titlecased = [titulo.title() for titulo in titulos]
print(titulos_titlecased)



# [item for item in items for item1 in items1 ... for item_n in items_n]
combinados = []
nums = [1, 2, 3]
letras = ['a', 'b', 'c']

for n in nums:
  for l in letras:
    combinados.append((n, l))

print(combinados)

combinados2 = [(l, n) for l in letras for n in nums]
print(combinados2)

combinados3 = []
for n in nums:
  for l in letras:
    if l != 'b':
      combinados3.append((n, l))

print(combinados3)

combinados4 = [(n, l) for n in nums for l in letras if l != 'b']
print(combinados4)


combinados5 = []
for n in nums:
  if n != 1:
    for l in letras:
      combinados5.append((n, l))

print(combinados5)

combinados6 = [(n, l) for n in nums if n != 1 for l in letras]
print(combinados6)



# Dict comprehensions
# {clave: valor for item in items}

sugus = {
  'piña': 'azul',
  'fresa': 'rojo',
  'limón': 'amarillo',
  'naranja': 'naranja',
}

sugus_al_reves = {}

for sabor, color in sugus.items():
  sugus_al_reves[color] = sabor

print(sugus_al_reves)

sugus_al_reves_2 = {color: sabor for sabor, color in sugus.items()}
print(sugus_al_reves_2)


frase = 'Winter is coming'

num_letras_palabras = {palabra: len(palabra) for palabra in frase.split(' ')}
print(num_letras_palabras)

mensaje = 'Eres muy tonto y me voy'
palabras_malsonantes = ['tonto']

lista_palabras_corregidas = [palabra if not palabra in palabras_malsonantes else '*' * len(palabra) for palabra in mensaje.split(' ')]

mensaje_corregido = ' '.join(lista_palabras_corregidas)

print(mensaje_corregido)

dict1 = {
  'a': [1, 2, 3],
  'b': 2,
  3: {
    'r': 'str'
  }
}
print(dict1)


# Set comprehension
# {valor for item in items}

set1 = set((1, 2))
print(set1)
print(type(set1))

set2 = {3, 4}
print(set2)
print(type(set2))

def triple(n):
  return n * 3

conjunto_triple_nums = {triple(num) for num in nums}
print(conjunto_triple_nums)