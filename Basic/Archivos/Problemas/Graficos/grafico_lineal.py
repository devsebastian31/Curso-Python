import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\Programacion\Curso de Python\Basic\Archivos\Problemas\Graficos\pedos.csv")

# Creando el grafico lineal
sns.lineplot(x="Fecha", y="Pedos", data=df)

# Creando un punto en el momento de mas pedos xd
plt.plot("01-09",17,"o")

# Mostrando el grafico
plt.show()