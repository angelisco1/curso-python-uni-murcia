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