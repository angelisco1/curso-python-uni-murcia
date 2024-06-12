# Decoradores

# -> puede hacer cosas
# fn()
# -> puede hacer cosas

# Decorador -> es una función, que devuelve algo (función o clase)
def log(func): # -> func = suma
  def wrapper(*args, **kwargs): # -> args = 1, 2, kwargs = None
    print(f'Acaba de empezar la {func.__name__}')
    resultado = func(*args, **kwargs) # func -> suma o resta
    print(f'Acaba de terminar la {func.__name__}')
    return resultado

  return wrapper

@log
def suma(a, b):
  print('Se está ejecutando la suma')
  return a + b

print(suma(1, 2)) # -> wrapper(1, 2)

@log
def resta(a, b):
  return a - b

print(resta(1, 2))

import time

def temporizador(func):
  def wrapper(*args, **kwargs):
    tiempo_inicial = time.time()
    # print(tiempo_inicial)
    result = func(*args, **kwargs)
    tiempo_final = time.time()
    # print(tiempo_final)
    print(f'La función {func.__name__} ha tardado en ejecutarse {tiempo_final - tiempo_inicial} segundos')
    return result

  return wrapper

@temporizador
def saludar(nombre):
  print(f'Hola {nombre}')
  time.sleep(1)

saludar('Ángel')


def add_metodo_saludar(cls):
  def saludar(self):
    print(f'Hola {self.nombre}')

  cls.saludar = saludar

  return cls


@add_metodo_saludar
class Persona:
  def __init__(self, nombre, apellidos, edad):
    self.nombre = nombre
    self.apellidos = apellidos
    self.edad = edad

p1 = Persona('charly', 'falco', 37)
p1.saludar()


def singleton(cls):
  instancias = {}

  def get_instancia(*args, **kwargs):
    if not cls in instancias:
      instancias[cls] = cls(*args, **kwargs)

    return instancias[cls]

  return get_instancia

@singleton
class CarritoCompra:
  def __init__(self):
    self.carrito = {}

  def add_producto(self, producto_id, cantidad):
    if producto_id in self.carrito:
      self.carrito[producto_id] += cantidad
    else:
      self.carrito[producto_id] = cantidad

  def comprar(self):
    self.carrito = {}

  def __str__(self):
    return f'Carrito: {self.carrito}'


carrito1 = CarritoCompra()
carrito1.add_producto(1, 2)
carrito1.add_producto(3, 4)

carrito2 = CarritoCompra()
carrito2.add_producto(1, 3)
carrito2.add_producto(2, 1)


print(carrito1)
print(carrito2)
# ANTES DEL SINGLETON
# Carrito: {1: 2, 3: 4}
# Carrito: {1: 3, 2: 1}

# DESPUES DEL SINGLETON
# Carrito: {1: 5, 3: 4, 2: 1}
# Carrito: {1: 5, 3: 4, 2: 1}