import numpy as np

lista = [1, 2, 3]
print(lista)

mi_array = np.array(lista)
print(mi_array)
print(type(mi_array))
print(f'Size: {mi_array.size}')

mi_matriz = np.array([lista, lista[::-1]])
print(mi_matriz)
print(type(mi_matriz))
print(f'Size: {mi_matriz.size}')


print(mi_array.shape)
print(mi_matriz.shape)


matriz_ceros = np.zeros((3, 3))
print(matriz_ceros)
array_ceros = np.zeros((4,))
print(array_ceros)

matriz_unos = np.ones((3, 3))
print(matriz_unos)
array_unos = np.ones((4,))
print(array_unos)


# range(0, 10)

array_nums = np.arange(0, 10)
print(array_nums)

array_nums = np.arange(2, 15, 3)
print(array_nums)


nums_1 = np.linspace(0, 12, 5, dtype='float32')
print(nums_1)

print(mi_array.dtype)
print(nums_1.dtype)

nums_2 = np.linspace(0, 3, 8)
print(nums_2)


# [n * 2 for n in range(10)]
nums_1_por_2 = nums_1 * 2
print(nums_1_por_2)

nums_1_mas_2 = nums_1 + 2
print(nums_1_mas_2)

suma_dos_arrays = nums_1_por_2 + nums_1_mas_2
print(suma_dos_arrays)

print(matriz_unos * 4)



print(f'Suma total de los elementos del array: {np.sum(suma_dos_arrays)}')

nums_aleatorios = np.random.rand(10)
print(nums_aleatorios)
print(np.min(nums_aleatorios))
print(np.max(nums_aleatorios))



print(f'La media es: {nums_2.mean()}')
# print(f'La moda es: {nums_2.mode()}')

a1 = np.array([1, 2, 3])
a2 = np.array([[0], [4], [1]])
a3 = a1 + a2
print(a3)
# [1, 2, 3] + [0
#             4
#             1]

print(array_nums)
mascara = array_nums > 7
print(mascara)
mayores_de_7 = array_nums[mascara]
print(mayores_de_7)

otro_array = array_nums[[1, 2, 4]]
print(otro_array)


m_32 = np.ones((3, 2))
m_23 = m_32.reshape((2, 3))
print(m_32)
print(m_23)

print(np.identity(3))
print(np.diag([1, 2, 3]))

matriz_10 = np.array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])

print(matriz_10.T)
print(matriz_10.T.flatten())


print(np.dot(matriz_10, a3))