import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv(r'C:\Users\Lucas Lima\Desktop\ALURA - ANALISE DE DADOS\Base\4-Estatistica com Python\dados.csv')

ax = sns.boxplot(x = 'Altura', y = 'Sexo', data = dados, orient = 'h')
ax.figure.set_size_inches(12,4)
ax.set_title('Altura', fontsize = 14)
ax.set_xlabel('Metros', fontsize=14)
plt.show()