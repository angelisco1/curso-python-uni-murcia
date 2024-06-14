# Crear un comando con argumentos que permita sacar pantallazos en un de un video en un tiempo dado
# Parametros posicionales:
#   - ruta al video
#   - ruta destino
#   - segundos en los cuales sacar el pantallazo

# python 10-ffmpeg.py videos/video.mp4 screenshots/ 2
# python 10-ffmpeg.py videos/video.mp4 screenshots/ "2, 10"
# python 10-ffmpeg.py videos/video.mp4 screenshots/ "2, 10, 15"


import argparse, subprocess
from datetime import datetime

def genera_frame(source, target, sec):
  tiempo = f'00:00:{sec}'
  timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
  frame = f'{target}/frame-{sec}_{timestamp}.jpeg'
  resultado = subprocess.run(['ffmpeg', '-i', source, '-ss', tiempo, '-vframes', '1', frame, '-y'], capture_output=True, text=True)
  print(resultado.stdout)
  print(resultado.stderr)


if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='Script para sacar frames de un video')
  parser.add_argument('source', help='Ruta al video del cual sacar los frames')
  parser.add_argument('target', help='Ruta al directorio donde guardar los frames obtenidos')
  parser.add_argument('times', help='Texto con los segundos donde queremos sacar los frames. Podemos pasar varios tiempos separandolos por comas. Ej: "2, 4, 8"')

  args = parser.parse_args()

  segundos = args.times.replace(' ', '').split(',')
  for segundo in segundos:
    if int(segundo) <= 9:
      segundo = f'0{segundo}'

    genera_frame(args.source, args.target, segundo)
