import pandas as pd

# Cambiar el tipo de dato de una columna
df = pd.read_csv("D:/Programacion/Curso de Python/Basic/Archivos/CSV/datos.csv")

# Convertir los datos de una columna a string
df["Edad"] = df["Edad"].astype(str)

# Mostrar el tipo de dato de la columna edad
# print(type(df["Edad"]))

# Remplazando los datos Medellín por Quito
df["Ciudad"].replace("Medellín","Quito",inplace=True)

# Mostrando la columna Ciudad 
# print(df["Ciudad"])

# Eliminando las filas con datos vacios
df = df.dropna()
print(df)

# Eliminado columnas con datos faltantes
df = df.dropna(axis=1) # El paremetro 0 es filas y el 1 es columnas


# Eliminado filas repetidas
df = df.drop_duplicates()

# Creando un CSV con el dataframe resultante (limpio)
df.to_csv("D:/Programacion/Curso de Python/Basic/Archivos/CSV/datos_limpios.csv",index=False)