# POO

persona1 = {
  'nombre': 'Charly',
  'apellidos': 'Falco'
}


class Persona:
  # atributo de clase
  num_patas = 2

  # Constructor
  def __init__(self, nombre, apellidos, edad):
    # atributos de instancia
    self.nombre = nombre
    self.apellidos = apellidos
    self.edad = edad

  # métodos de instancia
  def get_nombre_completo(self):
    return f'{self.nombre} {self.apellidos}'

  def cumple_años(self):
    self.edad += 1

  def __str__(self):
    return f'{self.nombre} {self.apellidos} tiene {self.edad} años'

  def __repr__(self):
    return f'Persona(nombre={self.nombre}, apellidos={self.apellidos}, edad={self.edad})'



angel = Persona('Ángel', 'Villalba', 33)
charly = Persona('Charly', 'Falco', 33)
mike = Persona('Mike', 'Kozinski', 34)

print(f'{angel.nombre} {angel.apellidos}')
print(angel.get_nombre_completo())
print(charly.get_nombre_completo())
print(mike.get_nombre_completo())

print(angel.edad)
angel.cumple_años()
print(angel.edad)

print(Persona.num_patas)
print(mike.num_patas)

Persona.num_patas = 10
print(mike.num_patas)
print(charly.num_patas)
print(Persona.num_patas)

charly.num_patas = 11
print(mike.num_patas)
print(charly.num_patas)
print(Persona.num_patas)
print(charly.__class__.num_patas)

print(charly.__dict__)
print(angel.__dict__)
print(Persona.__dict__)

print(angel)
print(mike)

lista_personas = [charly, mike, angel]
print(lista_personas)

print(f'-- {Persona.get_nombre_completo(mike)}')

class Calculadora:

  @staticmethod
  def suma(a, b):
    return a + b

  # suma = staticmethod(suma)

  @staticmethod
  def resta(a, b):
    return a - b

print(Calculadora.suma(1, 2))
print(Calculadora.resta(1, 2))

# c = Calculadora()
# print(c.resta(1, 2))


# GETTERS Y SETTERS

class Persona2:

  # Constructor
  def __init__(self, nombre, apellidos, edad, dni = None):
    # atributos de instancia
    self._nombre = nombre
    self._apellidos = apellidos
    self._edad = edad
    self.dni = dni

  # métodos de instancia
  def get_nombre_completo(self):
    return f'{self._nombre} {self._apellidos}'

  def cumple_años(self):
    self._edad += 1

  def get_nombre(self):
    return self._nombre

  def set_nombre(self, nombre):
    self._nombre = nombre

  nombre = property(get_nombre, set_nombre)

  @property
  def apellidos(self):
    return self._apellidos

  @apellidos.setter
  def apellidos(self, apellidos):
    self._apellidos = apellidos

  @property
  def edad(self):
    return self._edad

  @edad.setter
  def edad(self, edad):
    if edad < 18:
      raise ValueError('Edad no permitida')
    self._edad = edad

  def __str__(self):
    return f'{self._nombre} {self._apellidos} tiene {self._edad} años'

  def __repr__(self):
    return f'Persona(nombre={self._nombre}, apellidos={self._apellidos}, edad={self._edad})'

  # ==
  def __eq__(self, persona):
    # return self.nombre == persona.nombre and self.apellidos == persona.apellidos and self.edad == persona.edad
    return self.dni == persona.dni

  # !=
  def __ne__(self, persona):
    return not self.__eq__(persona)

  def __gt__(self, persona):
    return self._edad > persona.edad

  def __lt__(self, persona):
    return self._edad < persona.edad

  def __bool__(self):
    return self.dni != None




angel = Persona2('Ángel', 'Villalba', 32, '0000000T')
print(angel.get_nombre())
print(angel.get_nombre_completo())
angel.set_nombre('Sara')
print(angel.get_nombre())

print(angel.nombre)
angel.nombre = 'Ángel'
print(angel.nombre)

# print(angel.apellidos()) # -> 'Villalba'() -> TypeError: 'str' object is not callable
print(angel.apellidos)
angel.apellidos = 'Villalba Fernández-Paniagua'
print(angel.apellidos)
print(angel.get_nombre_completo())

# print(angel.edad)
# angel.edad = 17 # ValueError: Edad no permitida
# print(angel.edad)

print(angel._nombre)

angel2 = Persona2('Ángel', 'Villalba', 32, '0000000T')
charly = Persona2('Charly', 'Villalba', 32, '0000001Z')

print(angel == angel2)
print(angel == charly)
print(angel != angel2)
print(angel != charly)
charly.edad = 33
print(f'Es mayor? {angel > charly}')
print(f'Es menor? {angel < charly}')

if angel:
  print('Es True')
else:
  print('Es False')

if Persona2('aaa', 'bbb', 123):
  print('Es True')
else:
  print('Es False')


class Contador:
  def __init__(self):
    self.cuenta = 0

  def __call__(self):
    self.cuenta += 1

  def __str__(self):
    return f'La cuenta es: {self.cuenta}'

contador = Contador()
contador()
contador()
contador()
print(contador)


# Herencia
class Leccion:
  def __init__(self, titulo, duracion):
    self.titulo = titulo
    self.duracion = duracion

  def get_punto_temario(self):
    return f'- {self.titulo} ({self.duracion} min)'


class LeccionTexto(Leccion):
  def __init__(self, titulo, duracion, texto):
    super().__init__(titulo, duracion)
    self.texto = texto

  def mostrar_texto(self):
    print(f'Leete el siguiente contenido: {self.texto}')


class LeccionVideo(Leccion):
  def __init__(self, titulo, duracion, src):
    super().__init__(titulo, duracion)
    self.src = src

  def ver_video(self):
    print(f'Entra en {self.src} para ver la lección')

intro_solidity = LeccionTexto('¿Qué es Solidity?', 10, 'Solidity es un lenguaje de programación...')
instalacion_solidity = LeccionVideo('Instar Solidity', 15, 'http://mis-videos-de-solidity.com/instalar.mp4')

print(intro_solidity.get_punto_temario())
print(instalacion_solidity.get_punto_temario())

intro_solidity.mostrar_texto()
instalacion_solidity.ver_video()



from abc import abstractmethod, ABC

class Leccion2(ABC):
  def __init__(self, titulo, duracion):
    self.titulo = titulo
    self.duracion = duracion

  def get_punto_temario(self):
    return f'- {self.titulo} ({self.duracion} min)'

  @abstractmethod
  def mostrar_contenido(self):
    pass


# class Leccion2():
#   def __init__(self, titulo, duracion):
#     self.titulo = titulo
#     self.duracion = duracion

#   def get_punto_temario(self):
#     return f'- {self.titulo} ({self.duracion} min)'

#   def mostrar_contenido(self):
#     raise ValueError('Tienes que implementar esta clase')



class LeccionTexto2(Leccion2):
  def __init__(self, titulo, duracion, texto):
    super().__init__(titulo, duracion)
    self.texto = texto

  def mostrar_contenido(self):
    print(f'Leete el siguiente contenido: {self.texto}')


class LeccionVideo2(Leccion2):
  def __init__(self, titulo, duracion, src):
    super().__init__(titulo, duracion)
    self.src = src

  def mostrar_contenido(self):
    print(f'Entra en {self.src} para ver la lección')


intro_solidity = LeccionTexto2('¿Qué es Solidity?', 10, 'Solidity es un lenguaje de programación...')
instalacion_solidity = LeccionVideo2('Instar Solidity', 15, 'http://mis-videos-de-solidity.com/instalar.mp4')

intro_solidity.mostrar_contenido()
instalacion_solidity.mostrar_contenido()


from dataclasses import dataclass, field
from typing import List

# order=True -> __lt__, __gt__, __le__ y __ge__
# @dataclass(order=True, frozen=True)
@dataclass(order=True)
class Serie:
  num_capitulos: int
  titulo: str
  num_temporadas: int
  finalizada: bool = False
  precuelas: List['Serie'] = field(default_factory=list)
  # precuelas: List[str] = field(default_factory=lambda: ['serie1', 'serie2'])

  actores: List['Persona'] = field(default_factory=list)

  # Ha generador el __init__ automáticamente
  # Ha generador el __str__ automáticamente
  def get_duracion(self):
    return self.num_capitulos * 45

# yellowstone = Serie('Yellowstone', 5, 50)
# s1823 = Serie('1823', 1, 10)
yellowstone = Serie(num_temporadas=5, titulo='Yellowstone', num_capitulos=50)
s1823 = Serie(titulo='1823', num_temporadas=1, num_capitulos=10)
# __gt__ -> ('Yellowstone', 5, 50, False) > ('1823', 10, 110, False)
print(yellowstone)
print(s1823)
print(yellowstone > s1823)

s1823.num_capitulos = s1823.num_capitulos + 10
s1823.num_temporadas = s1823.num_temporadas + 1
print(s1823)
print(s1823.get_duracion())

# yellowstone.precuelas.append(s1823.titulo)
yellowstone.precuelas.append(s1823)
print(yellowstone)
print(yellowstone.precuelas)
