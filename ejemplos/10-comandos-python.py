print('Hola mundo!')


# Ejecutar otros scripts o apps
import subprocess

subprocess.run(['echo', 'Hola mundo!'])
# ERRORES QUE DAN POR SEGURIDAD
# subprocess.run('echo Hola mundo!')
# subprocess.run(['echo Hola mundo!'])


# python3 10-comandos.py 'ejemplos; rm -rf /'
# ls 'ejemplos; rm -rf /'
# 'ls ejemplos; rm -rf /'

subprocess.run(['ls', '-l', 'ejemplos'])

resultado = subprocess.run(['ls', 'ejemplos'])
print(resultado)

resultado = subprocess.run(['ls', 'ejemplos'], capture_output=True, text=True)
print(resultado.stdout)

resultado = subprocess.run(['ls', 'ejemplos-no-existe'], capture_output=True, text=True)
print(resultado.stdout)
print(resultado.stderr)



ruta_video = 'ejemplos/archivos/videos/video1.mp4'
destino = 'ejemplos/archivos/screenshots/screenshot-1.png'
tiempo = '00:00:04'
resultado = subprocess.run(['ffmpeg', '-i', ruta_video, '-ss', tiempo, '-vframes', '1', destino, '-y'], capture_output=True, text=True)
print(resultado.stdout)
print(resultado.stderr)



proceso = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = proceso.communicate()
print(f'out-> {stdout}')
print(f'err-> {stderr}')

proceso = subprocess.Popen(['ls', '-l', 'no-existe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = proceso.communicate()
print(f'out-> {stdout}')
print(f'err-> {stderr}')



lista_correos = [
  'angel@abc.es',
  'sara@hooli.com',
  'andres@tesla.com',
  'paco@abc.com',
  'sandra@def.com',
  'maria@tesla.com',
]

proceso = subprocess.Popen(['grep', '@tesla.com'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

stdout, stderr = proceso.communicate(input='\n'.join(lista_correos))
print(stdout)



proceso1 = subprocess.Popen(['ls', 'ejemplos/archivos/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
proceso2 = subprocess.Popen(['grep', '.csv'], stdin=proceso1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

stdout, stderr = proceso2.communicate()
print(f'out: {stdout}')



import argparse

parser = argparse.ArgumentParser(description='Todavia no sabemos que hace esto')

parser.add_argument('nombre', help='El nombre de la persona a la que saludar')
parser.add_argument('apellidos', help='Los apellidos de la persona a la que saludar')
parser.add_argument('-e', '--email', help='El correo al que enviar el saludo')


args = parser.parse_args()
print(args)

if args.email:
  print(f'Enviando email a {args.email}: Hola {args.nombre} {args.apellidos}')
else:
  print(f'Hola {args.nombre} {args.apellidos}')


import sys
print(sys.argv)