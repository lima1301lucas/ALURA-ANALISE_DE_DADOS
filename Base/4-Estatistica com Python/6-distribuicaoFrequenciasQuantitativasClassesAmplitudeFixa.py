import pandas as pd
import numpy as np

dados = pd.read_csv(r'C:\Users\Lucas Lima\Desktop\ALURA - ANALISE DE DADOS\Base\4-Estatistica com Python\dados.csv')

n = dados.shape[0]

k = 1 + (10 / 3) * np.log10(n)
k = int(k.round(0))

frequencia = pd.value_counts(pd.cut(x = dados.Renda, bins = 17, include_lowest = True), sort = False)
percentual = pd.value_counts(pd.cut(x = dados.Renda, bins = 17, include_lowest = True), sort = False, normalize = True) * 100

dist_freq_quantitativa_amplitude_fixa = pd.DataFrame({'Frequencia': frequencia, 'Porcentagem': percentual})
print(dist_freq_quantitativa_amplitude_fixa)