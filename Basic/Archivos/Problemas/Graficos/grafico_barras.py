import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\Programacion\Curso de Python\Basic\Archivos\Problemas\Graficos\cofla_ingresos.csv")

# Creando el grafico de barras
sns.barplot(x="Fuente", y="Ingresos", data=df)

# Suma todos los datos del valor numerico
total_ingresos = df["Ingresos"].sum()

# Mostrar el total
print(f"El total: {total_ingresos}")

# Mostrando el grafico
plt.show()