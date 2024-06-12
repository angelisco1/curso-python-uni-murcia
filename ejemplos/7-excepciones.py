# Excepciones

# AttributeError
# IndexError
# ZeroDivisionError
# FileNotFoundError
# ValueError
# TypeError


def get_elemento(lista, pos):
  try:
    return lista[pos]
  except IndexError:
    return f'La lista {lista} no tiene un elemento en la posicion {pos}'

print(get_elemento([1, 2, 3], 1))
print(get_elemento([1, 2, 3], 9))


def divide(n1, n2):
  try:
    int_n1 = int(n1)
    int_n2 = int(n2)
    return int_n1 / int_n2
  except ZeroDivisionError:
    return f'No se pueden realizar divisiones con 0'
  except TypeError:
    return f'No se puede dividir el {type(n1)} ({n1}) con el {type(n2)} ({n2})'
  except ValueError:
    return f'No puedes convertir a int el {n2} porque es una letra'

print(divide(6, 3))
print(divide(6, 0))
print(divide(6, '1'))
print(divide(6, 'a'))


def verifica_numero_positivo(num):
  if num < 0:
    raise ValueError(f'El valor pasado no es válido, tiene que ser positivo: {num}')
  return True

try:
  verifica_numero_positivo(-2)
except ValueError as e:
  print(e)



class Triangulo:

  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def __setattr__(self, attr_name, attr_value):
    if attr_value <= 0:
      raise Exception(f'El atributo {attr_name} no puede ser menor o igual a 0')
    self.__dict__[attr_name] = attr_value

  def area(self):
    return (self.base * self.altura) / 2

t1 = None
try:
  # t1 = Triangulo(2, -1)
  t1 = Triangulo(2, 1)
except Exception as e:
  print(e)
else:
  print('Por aquí pasa solo si va bien')
  print(t1.area())
finally:
  print('Por aquí pasa tanto si va bien como si va mal')


# print(t1.__dict__)


class APIError(Exception):
  def __init__(self, status_code, message):
    self.status_code = status_code
    self.status_text = APIError.get_status_text(status_code)
    self.message = message
    super().__init__(f'Error {self.status_code} ({self.status_text}): {self.message}')

  @staticmethod
  def get_status_text(status_code):
    status_texts = {
      400: 'Bad Request',
      401: 'Unauthorized',
      403: 'Forbidden',
      404: 'Not Found',
    }
    return status_texts[status_code]


def login(username, password):
  if username == 'admin' and password == 'admin':
    return f'Token: 12341234'
  else:
    raise APIError(400, 'Las credenciales no son correctas')

try:
  print(login('admin', 'pepito'))
except APIError as e:
  print(e)


import jwt

token1_correcto = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6ImFuZ2VsIiwiaWF0IjoxNTE2MjM5MDIyLCJyb2wiOiJhZG1pbiJ9.6xELhqS5Thm0On5Yk5EvtnIOKtrmwAlDXn2mzCD4Ybg'
token2_free = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6ImFuZ2VsIiwiaWF0IjoxNTE2MjM5MDIyLCJyb2wiOiJmcmVlIn0.rhAVFMupZl8yyB-XT6ku8kAMS6wpI_o3oBS8qtLJ0CI'
secreto = '1234'


def crear_informe(titulo, contenido, token):

  if not token:
    raise APIError(401, 'No estás autenticado')

  payload = None
  try:
    payload = jwt.decode(token, secreto, algorithms=['HS256'])
  except Exception:
    raise APIError(400, 'El token que nos has enviado, no es correcto')

  autor, rol = payload.get('name'), payload.get('rol')

  if not rol in ['premium', 'admin']:
    raise APIError(403, 'No tienes permiso para crear el informe')

  missing_fields = []
  if not titulo:
    missing_fields.append('titulo')
  if not contenido:
    missing_fields.append('contenido')

  if missing_fields:
    raise APIError(400, f'Te faltan los campos del informe: {', '.join(missing_fields)}')

  print(f'El usuario {autor} ha creado el informe {titulo}: {contenido}')


try:
  crear_informe('Informe 1', 'Contenido 1', token2_free)
  # crear_informe('Informe 1', 'Contenido 1', token1_correcto)
  # crear_informe('Informe 1', 'Contenido 1', None)
  # crear_informe('Informe 1', None, 'angel')
  # crear_informe(None, None, 'angel')
except APIError as e:
  print(e)
else:
  # Guardar en la BBDD el informe