import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv(r'C:\Users\Lucas Lima\Desktop\ALURA - ANALISE DE DADOS\Base\4-Estatistica com Python\dados.csv')
quartis = dados.Renda.quantile([0.25, 0.5, 0.75])
#print(quartis)

decis = dados.Renda.quantile([i / 10 for i in range(1, 10)])
#print(decis)

percentis = dados.Renda.quantile([i / 100 for i in range(1, 100)])
#print(percentis)

ax = sns.displot(dados.Idade, kind='hist', cumulative=True)
ax.figure.set_size_inches(14,6)
ax.set_titles('Distribuição de frequêcia acumulada', fontsize = 18)
ax.set_ylabels('Acumulado', fontsize=14)
ax.set_xlabels('Anos', fontsize=14)
plt.show()