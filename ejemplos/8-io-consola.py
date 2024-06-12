from getpass import getpass

nombre = input('- Nombre: ')
email = input('- Email: ')
password = getpass('- Password: ')
edad = int(input('- Edad: '))

print(type(edad))

print(f"""
  Usuario: {nombre}
  Edad: {edad}
  Email: {email}
  Password: {password}
""")