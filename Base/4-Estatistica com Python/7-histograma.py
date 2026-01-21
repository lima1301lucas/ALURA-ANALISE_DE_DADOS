import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv(r'C:\Users\Lucas Lima\Desktop\ALURA - ANALISE DE DADOS\Base\4-Estatistica com Python\dados.csv')
dados.Altura.hist(bins=50, figsize=(12, 6))
plt.show()

#ax = sns.displot(dados.Altura, kde = True)
#ax.figure.set_size_inches(12,6)
#ax.set_titles('Distribuição de Frequências - Altura', fontsize = 18)
#ax.set_xlabels('Metros', fontsize = 14)
#
#plt.show()