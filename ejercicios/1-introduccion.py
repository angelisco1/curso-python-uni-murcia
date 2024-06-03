# Dada una lista de numeros, crea otra lista que tenga los numeros en posiciones pares, multiplicados a su vez por la posición original.
# [1, 2, 3] -> [1, 3] -> resultado: [0, 6]

# if not index % 2:
lista = [1, 2, 3]
resultado = []
for index, num in enumerate(lista):
  if not index % 2:
    resultado.append(num*index)

print(resultado)


# Si no pedimos que se multiplique por la posición original, esta solución serviría
# lista = [1, 2, 3, 4, 5]
# resultado2= []
# for i, valor in enumerate(lista[::2]):
#   resultado2.append(valor * i)

# print(resultado2)