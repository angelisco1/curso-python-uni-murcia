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