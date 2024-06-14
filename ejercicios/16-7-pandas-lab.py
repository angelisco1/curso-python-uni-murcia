import pandas as pd

archivo_apple_store = 'ejemplos/archivos/apple_store.csv'

df_tienda = pd.read_csv(archivo_apple_store)
# print(df_tienda)

# Imprime el número de observaciones de los datos
print(len(df_tienda))

# ¿Cuál es la media de la clasificación/puntuación de las apps?
key = 'user_rating'
print(df_tienda[key].mean())
print(df_tienda.user_rating.mean())

# ¿Cuántas apps tienen una clasificación no inferior a 4?
print(df_tienda[df_tienda['user_rating'] >= 4].shape[0])
print(len(df_tienda[df_tienda['user_rating'] >= 4]))

# ¿Cuántos tipos ("prime_genre") distintos hay?
print(df_tienda['prime_genre'].unique())
print(len(df_tienda['prime_genre'].unique()))

# ¿Cuáles son los 3 géneros principales que tienen la mayor cantidad de aplicaciones?
print(df_tienda['prime_genre'].value_counts().head(3))

# ¿Qué género es más probable que contenga aplicaciones gratuitas?
apps_gratis = df_tienda[df_tienda['price'] == 0]
print(apps_gratis)
print(apps_gratis['prime_genre'].value_counts())


# Ahora puede calcular la proporción de aplicaciones gratuitas en cada género en función de los recuentos de valores que obtuvo en los dos pasos anteriores.
print((apps_gratis['prime_genre'].value_counts() / df_tienda['prime_genre'].value_counts()).sort_values(ascending=False))