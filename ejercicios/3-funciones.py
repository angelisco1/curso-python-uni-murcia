# Ejercicio 1
def comparar_num(num):
  # print('Mayor que 5' if num > 5 else 'Menor o igual que 5')
  print('Mayor que 5' if num > 5 else 'Menor que 5' if num < 5 else 'Igual que 5')

# if num > 5:
# else:
#   if num < 5:
#   else:

comparar_num(5)
comparar_num(1)
comparar_num(7)


# Ejercicio 2
def sumatorio_de_n(n):
  suma = 0

  for n in range(1, n + 1):
    suma += n

  return suma


print(sumatorio_de_n(3))
print(sumatorio_de_n(5))



# Ejercicio 3
def sumatorio_tope(tope):
  suma = 0
  i = 1

  while suma + i <= tope:
    suma += i
    i += 1

  return suma


print(sumatorio_tope(6))
print(sumatorio_tope(7))


# Ejercicio 7
import calendar, locale, datetime

# calendar -> date, time, ...

def get_nombre_dia_hoy():
  locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

  hoy = datetime.date.today()
  print(hoy)

  num_dia = hoy.isoweekday()
  print(num_dia)

  dias_semana = list(calendar.day_name)
  print(dias_semana)

  return dias_semana[num_dia - 1]


print(get_nombre_dia_hoy())

def get_currency(precio, lang='es_ES.UTF-8'):
  locale.setlocale(locale.LC_ALL, lang)

  return locale.currency(precio)

print(get_currency(1025.89))
print(get_currency(1025.89, 'en_US.UTF-8'))



# Ejercicio 8
def suma(*args):
  suma = 0
  for n in args:
    suma += n

  return suma


print(suma(1, 2, 3, 4))
print(suma(10, 5, 8, 20, 2))