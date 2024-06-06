# Ejercicio 1: Palindromo

# Dada una lista de palabras o frases aleatorias, escribir una función que devuelva una list comprehension para quedarnos solo con las palabras de esa lista que sean palíndromos.
#
# - Pista: Revisa el uso combinado de las funciones join y split para eliminar espacios.
# - Pista: ¿Habrá alguna función en Python para pasar cadenas a minúsculas?
# - Pista: La indexación de iterables en Python es muy potente. Puedes usar la sintáxis [start:end:step] para obtener un subiterable a partir de otro. Investiga qué pasa si omites uno o varios de los 3 parámetros, o usas números negativos para el step. Por ejemplo, ¿qué obtienes al ejecutar "me llamo jorge"[1:7:1]?, ¿y "me llamo jorge"[7::-1]?
#
# Aquí tienes el código de pruebas

lista = [
  "Añora la Roña", # -> ['Añora', 'la', 'roña'] -> 'Añoralaroña'
  "Como que moc",
  "Anita lava la tina",
  "Eva ya hay ave",
  "Yo no maldigo mi suerte porque minero naci"
]

lista_palindromos = [frase for frase in lista if ''.join(frase.split(' ')).lower() == ''.join(frase.split(' '))[::-1].lower()]
print(lista_palindromos)

lista_palindromos = [frase for frase in lista if frase.replace(' ', '').lower() == frase.replace(' ', '')[::-1].lower()]
print(lista_palindromos)

def get_frase_limpia(frase):
  return ''.join(caracter.lower() for caracter in frase if caracter.isalpha())

lista_palindromos = [frase for frase in lista if get_frase_limpia(frase) == get_frase_limpia(frase)[::-1]]
print(lista_palindromos)


resultado = [
  "Añora la Roña",
  "Anita lava la tina",
  "Eva ya hay ave",
]


# Ejercicio 2: Conversor de grados
# Convierte una lista de grados fahrenheit a kelvin o celsius
grados_f = [70, 67, 65, 68, 73, 79, 77, 83]

grados_c = [round((grado - 32) * 5 / 9, 2) for grado in grados_f]
print(grados_c)
grados_k = [round((grado - 32) * 5 / 9 + 273.15, 2) for grado in grados_f]
print(grados_k)
