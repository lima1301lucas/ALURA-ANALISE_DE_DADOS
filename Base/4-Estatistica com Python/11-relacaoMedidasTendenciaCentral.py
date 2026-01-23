import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv(r'C:\Users\Lucas Lima\Desktop\ALURA - ANALISE DE DADOS\Base\4-Estatistica com Python\dados.csv')

ax = sns.displot(dados.query('Renda < 20000').Renda)
ax.figure.set_size_inches(12, 6)

moda = dados.Renda.mode()[0]
mediana = dados.Renda.median()
media = dados.Renda.mean()

print(moda)
print(mediana)
print(media)
plt.show()