import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\Programacion\Curso de Python\Basic\Archivos\Problemas\Graficos\Bigotes.csv")

# Creando el grafico de bigotes
sns.boxenplot(x="Categoria", y="Valor", data=df)


# Mostrando el grafico
plt.show()