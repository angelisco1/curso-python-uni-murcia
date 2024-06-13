# file = open('ejemplos/archivos/archivo1.txt', 'r')
# contenido = file.read()
# print(contenido)
# file.close()


with open('ejemplos/archivos/archivo1.txt', 'r') as file:
  contenido = file.read()
  print(contenido)


with open('ejemplos/archivos/archivo2.txt', 'r') as file:
  pw1 = file.readline().strip()
  print(pw1)
  pw2 = file.readline().strip()
  print(pw2)
  pw3 = file.readline().strip()
  print(pw3)


with open('ejemplos/archivos/archivo2.txt', 'r') as file:
  lines = file.readlines()
  for line in lines:
    if line.strip() == 'root':
      print('root se conoce, cambiala')
      break
  else:
    print('root no se conoce, la puedes utilizar')


# r -> solo lectura
# w -> solo escriture
# a -> añade contenido

with open('ejemplos/archivos/archivo3.txt', 'w') as file:
  contenido = 'Hola, que tal?'
  file.write(contenido)
  file.write('\nBien')
  file.write('\nY tu?')


with open('ejemplos/archivos/archivo3.txt', 'w') as file:
  contenido = 'Hola, que tal?'
  file.write(contenido)
  file.write('\nMal')
  file.write('\nY tu?')


with open('ejemplos/archivos/archivo3.txt', 'a') as file:
  contenido = '\nYo bien.\nA ti que te pasa?'
  file.write(contenido)


lista_passwords_filtradas = []
with open('ejemplos/archivos/archivo2.txt') as source, open('ejemplos/archivos/nuevas-contraseñas-filtradas.txt') as source2:
  # lista_passwords_filtradas = map(lambda line: line.strip(), source.readlines())
  lista_passwords_filtradas = [line.strip() for line in source.readlines()]
  print(lista_passwords_filtradas)

  # line = source2.readline():
  # while line:

  #   line = source2.readline()


  while line := source2.readline().strip():
    if line in lista_passwords_filtradas:
      print(f'La contraseña {line} ya está en la lista')
      continue
    lista_passwords_filtradas.append(line)
    print(f'La contraseña {line} se ha añadido a la lista')


  # lista2 = set([*source.readlines(), *source2.readlines()])

print(lista_passwords_filtradas)

with open('ejemplos/archivos/passwords-2024.txt', 'w') as target:
  target.write('\n'.join(lista_passwords_filtradas))
  print('El archivo con las nuevas contraseñas filtradas ya está')
