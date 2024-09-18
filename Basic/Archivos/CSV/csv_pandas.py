import pandas as pd

# archivo = pd.read_csv("D:/Programacion/Curso de Python/Basic/Archivos/CSV/datos.csv")
# print(archivo)


# Mostrar por columnas

# names=["name","lastname","age"] sirve para el encabezado
df = pd.read_csv("D:/Programacion/Curso de Python/Basic/Archivos/CSV/datos.csv",names=["name","age","city"])

nombres = df["name"] # Mostramos solo la columna name (el Nombre)


# Ordenando el dataframe por edad
df_ordenado_ascendente = df.sort_values("age")


# Ordenandolo forma descendente
df_ordenado_descendiente = df.sort_values("age", ascending=False) # Ordena de mayor a menor


# Concatenando 2 dataframes
df1 = pd.read_csv("D:/Programacion/Curso de Python/Basic/Archivos/CSV/datos.csv")
df2 = pd.read_csv("D:/Programacion/Curso de Python/Basic/Archivos/CSV/datos.csv")

df_concatenando = pd.concat([df1, df2])


# Acceder a las primeras 3 filas con head()
primera_filas = df.head(3)

# Accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)


# Accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape


# Obteniendo data estadistica del dataframe
df_info = df.describe()


# Accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2, "age"] # 30

# Accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2,2] # Bogotá

# Accediendo a todos las filas de una columna
apellidos = df.iloc[:,2] # Los : va acceder a todos los datos, primero es la fila y luego la columna

# Convierta la columna "edad" a valores numéricos, forzando los errores a NaN
df["age"] = pd.to_numeric(df["age"], errors="coerce")

# Accediendo a todas las filas con edad mayor que 30
mayor_que_30 = df.loc[df["age"]>30,:]

print(mayor_que_30)



# Metodo slicing sirve para acceder desde un principio hasta un final
cadena = "0123456789"
print(cadena[2:5]) # Comienza en el 2 y termina en el 4