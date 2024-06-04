dbs = [0, 1, 0, 0, 0, 0, 1, 0, 1, 23, 31, 0, 1, 1, 0, 0, 0, 1, 1, 0, 20, 1, 1, 15, 1, 0, 0, 0, 40, 15, 0, 0]

mayores_de_10 = []

for index, db in enumerate(dbs):
  if db > 10:
    mayores_de_10.append(db)
    print(f'DB: {db}, Indice: {index}, Tiempo: {index * 5}s')

print(mayores_de_10)


tuplas_mayores_de_10 = []

for index, db in enumerate(dbs):
  if db > 10:
    tupla = (index, db)
    tuplas_mayores_de_10.append(tupla)

print(tuplas_mayores_de_10)

# print(tuple([1, 2, 3]))
# list() -> []
# tuple() -> ()
# dict() -> {}

# mi_lista = [1, 2, 3]
# mi_lista[1] = 0
# print(mi_lista)

long_lista = len(dbs)
for index, db in enumerate(dbs):
  if db > 10:
    if index+1 < long_lista and dbs[index+1] > 10:
      print('Alarm!')

for index, db in enumerate(dbs):
  if db > 10:
    dbs[index] = 2

print(dbs)