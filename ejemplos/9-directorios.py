import os, datetime

initial_path = os.getcwd()
print(initial_path)


with os.scandir('ejemplos/archivos/') as files:
  for file in files:
    # print(dir(file))
    print(f'{file.name} - {initial_path}/{file.path} - {'Archivo' if file.is_file() else 'Carpeta'}')

with os.scandir('ejemplos/archivos/carpeta-prueab/') as files:
  nombre_carpeta = f'carpeta-{datetime.date.today()}'
  if not nombre_carpeta in [file.name for file in files]:
    os.mkdir(f'ejemplos/archivos/carpeta-prueab/carpeta-{datetime.date.today()}')
    print('He creado la carpeta')
  else:
    print('No he creado la carpeta')