import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\Programacion\Curso de Python\Basic\Archivos\Problemas\Graficos\dispersion.csv")

# Creando el grafico de dispersion
sns.scatterplot(x="Tiempo", y="Dinero", data=df)


# Mostrando el grafico
plt.show()