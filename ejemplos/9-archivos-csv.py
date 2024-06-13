import csv

ruta_apple_store_csv = 'ejemplos/archivos/apple_store.csv'

with open(ruta_apple_store_csv) as csvfile:
  csv_reader = csv.reader(csvfile)
  # print(type(csv_reader))
  for index, fila in enumerate(csv_reader):
    if index == 5:
      break
    print(fila)


with open(ruta_apple_store_csv) as csvfile:
  # Cuidado que esto devuelve un Iterador y si lo volvemos a leer, ya no leeriamos nada porque los datos se han consumido con el primer for
  csv_reader = csv.DictReader(csvfile)
  for index, fila in enumerate(csv_reader):
    if index == 5:
      break
    print(fila)




lista_ofertas_trabajo = [
    {
        "id": 1,
        "titulo": "Desarrollador Full Stack",
        "tecnologias": ["Python", "Django", "JavaScript", "React"],
        "salario": 50000,
        "lugar": "Madrid, España",
        "empresa": "Tech Solutions SL"
    },
    {
        "id": 2,
        "titulo": "Ingeniero de DevOps",
        "tecnologias": ["AWS", "Docker", "Kubernetes", "Terraform"],
        "salario": 55000,
        "lugar": "Ciudad de México, México",
        "empresa": "Cloud Innovators MX"
    },
    {
        "id": 3,
        "titulo": "Desarrollador Backend",
        "tecnologias": ["Java", "Spring Boot", "MySQL", "Kafka"],
        "salario": 65000,
        "lugar": "Buenos Aires, Argentina",
        "empresa": "DataCorp SA"
    },
    {
        "id": 4,
        "titulo": "Desarrollador Frontend",
        "tecnologias": ["HTML", "CSS", "JavaScript", "Vue.js"],
        "salario": 45000,
        "lugar": "Barcelona, España",
        "empresa": "Web Creations"
    },
    {
        "id": 5,
        "titulo": "Ingeniero de Datos",
        "tecnologias": ["Python", "SQL", "Hadoop", "Spark"],
        "salario": 70000,
        "lugar": "Bogotá, Colombia",
        "empresa": "Data Solutions Ltda"
    },
    {
        "id": 6,
        "titulo": "Analista de Seguridad",
        "tecnologias": ["Cybersecurity", "Python", "Linux", "SIEM"],
        "salario": 60000,
        "lugar": "Lisboa, Portugal",
        "empresa": "SecureIT"
    },
    {
        "id": 7,
        "titulo": "Desarrollador Móvil",
        "tecnologias": ["Kotlin", "Java", "Android", "REST APIs"],
        "salario": 55000,
        "lugar": "Santiago, Chile",
        "empresa": "AppDev Chile"
    },
    {
        "id": 8,
        "titulo": "Ingeniero de Machine Learning",
        "tecnologias": ["Python", "TensorFlow", "Pandas", "scikit-learn"],
        "salario": 75000,
        "lugar": "Berlín, Alemania",
        "empresa": "AI Innovations GmbH"
    },
    {
        "id": 9,
        "titulo": "Desarrollador de Software",
        "tecnologias": ["C#", ".NET", "SQL Server", "Azure"],
        "salario": 65000,
        "lugar": "Lima, Perú",
        "empresa": "SoftTech Peru"
    },
    {
        "id": 10,
        "titulo": "Administrador de Sistemas",
        "tecnologias": ["Linux", "Windows Server", "Bash", "Powershell"],
        "salario": 50000,
        "lugar": "Dublín, Irlanda",
        "empresa": "IT Services Ireland"
    }
]

ruta_archivo_ofertas_trabajo = 'ejemplos/archivos/ofertas_trabajo.csv'
ruta_archivo_ofertas_trabajo2 = 'ejemplos/archivos/ofertas_trabajo-2.csv'

with open(ruta_archivo_ofertas_trabajo, 'w') as file:
  csv_writer = csv.writer(file)

  csv_writer.writerow(['id', 'titulo', 'tecnologias', 'salario', 'lugar', 'empresa'])
  # csv_writer.writerow(lista_ofertas_trabajo[0].keys())

  for oferta in lista_ofertas_trabajo:
    tupla_oferta_row = (oferta['id'], oferta['titulo'], ', '.join(oferta['tecnologias']), oferta['salario'], oferta['lugar'], oferta['empresa'])
    csv_writer.writerow(tupla_oferta_row)


with open(ruta_archivo_ofertas_trabajo2, 'w') as file:
  csv_writer = csv.DictWriter(file, fieldnames=lista_ofertas_trabajo[0].keys())

  csv_writer.writeheader()
  for oferta in lista_ofertas_trabajo:
    csv_writer.writerow(oferta)




ruta_archivo_ofertas_trabajo_pc = 'ejemplos/archivos/ofertas_trabajo_pc.csv'
with open(ruta_archivo_ofertas_trabajo_pc) as csvfile:
  csv_reader = csv.reader(csvfile, delimiter=';')
  for fila in csv_reader:
    print(fila)