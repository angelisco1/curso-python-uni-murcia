import pandas as pd


# Series -> equivale a una lista
# DataFrames -> equivale a una matriz

# Etiquetados

s1 = pd.Series([1, 2, 3, 4, 5])
print(s1)

print(s1[3])

s2 = pd.Series(range(10))
print(s2)


datos = {
  'id': ['a', 'b', 'c', 'd'],
  'venta': [140, 10, 229, 90],
  'stock': [100, 120, 119, 180],
}
df1 = pd.DataFrame(datos)
print(df1)


datos_empresas = [
  ['E-Corp', 'elliot@ecorp.com', 'Unlimited 100'],
  ['Hooli', 'belson@hooli.com', 'Unlimited 100'],
  ['Los pollos hermanos', 'fring@hermanos.com', 'Premium'],
]

tabla_empresas_clientes = pd.DataFrame(datos_empresas, columns=['Empresa', 'Contacto', 'Plan'])
print(tabla_empresas_clientes)

print(tabla_empresas_clientes['Empresa'])


print(type(tabla_empresas_clientes['Empresa']))
print(type(tabla_empresas_clientes))


# Obtener varias columnas
print(tabla_empresas_clientes[['Empresa', 'Plan']])


print(tabla_empresas_clientes['Empresa'][1])

datos = {
  'id': ['a', 'b', 'c', 'd'],
  'venta': [140, 10, 229, 90],
  'stock': [100, 120, 119, 180],
}
datos = {
  'a': [140, 100],
  'b': [10, 120],
  'c': [229, 119],
  'd': [90, 180],
}
df_datos_productos = pd.DataFrame.from_dict(datos)
print(df_datos_productos)

df_datos_productos = pd.DataFrame.from_dict(datos, orient='index', columns=['Ventas', 'Stock'])
print(df_datos_productos)


print(df_datos_productos['Ventas']['b'])
print(df_datos_productos['Ventas'][2]) # warning

# loc (busca por el indice) y iloc (busca por el indice original que sería como la posición)
print(df_datos_productos['Ventas'].loc['c'])
print(df_datos_productos['Ventas'].iloc[2])


print(df_datos_productos['b':'c']['Stock'])
print(df_datos_productos['b':'d':2]['Stock'])



print(f'Total stock: {df_datos_productos['Stock'].sum()}')

df_datos_productos['Precio'] = [3, 7, 7, 24]
print(df_datos_productos)

mas_caro = df_datos_productos['Precio'].max()
print(mas_caro)

media_precios = df_datos_productos['Precio'].mean()
print(media_precios)

# .var(), .std(), .mode(), .median()
print(df_datos_productos['Precio'].mode())


archivo_apple_store = 'ejemplos/archivos/apple_store.csv'

df_tienda = pd.read_csv(archivo_apple_store)
print(df_tienda)


print(df_tienda.head())
print(df_tienda.tail())


ultimas_apps_con_categoria_rating= df_tienda.tail()[['track_name', 'user_rating', 'prime_genre']]
print(ultimas_apps_con_categoria_rating)

ultimos_juegos = ultimas_apps_con_categoria_rating[ultimas_apps_con_categoria_rating['prime_genre'] == 'Games']
print(ultimos_juegos)

print(ultimos_juegos[ultimos_juegos['user_rating'] > 4.6])



ultimas_apps = ultimas_apps_con_categoria_rating
print(ultimas_apps[(ultimas_apps['prime_genre'] == 'Games') & (ultimas_apps['user_rating'] > 4.6)])
print(ultimas_apps.query('prime_genre == "Games" and user_rating > 4.6'))



ultimas_apps.to_csv('ejemplos/archivos/ultimas_apps_de_apple_store.csv')
ultimas_apps.to_csv('ejemplos/archivos/ultimas_apps_de_apple_store2.csv', sep=';')
ultimas_apps.to_csv('ejemplos/archivos/ultimas_apps_de_apple_store3.csv', index=False)
ultimas_apps.to_csv('ejemplos/archivos/ultimas_apps_de_apple_store4.csv', index=False, header=['App Name', 'Rating', 'Category'])

ultimas_apps.to_csv('ejemplos/archivos/ultimas_apps_de_apple_store5.csv', index=False, columns=['track_name', 'user_rating'], header=['App Name', 'Rating'])