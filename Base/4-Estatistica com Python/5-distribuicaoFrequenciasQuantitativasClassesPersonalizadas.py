import pandas as pd
dados = pd.read_csv(r'C:\Users\Lucas Lima\Desktop\ALURA - ANALISE DE DADOS\Base\4-Estatistica com Python\dados.csv')

#dados.Renda.min()
#dados.Renda.max()

classes = [0, 1576, 3152, 7880, 15760, 200000]
labels = ['E', 'D', 'C', 'B', 'A']

classes = pd.cut(x = dados.Renda, bins = classes, labels = labels, include_lowest = True)
frequencia = pd.value_counts(classes)
percentual = pd.value_counts(classes, normalize= True) * 100

dist_freq_quantitativa_personalizadas = pd.DataFrame({'Frequencia': frequencia, 'Porcentagem': percentual})
print(dist_freq_quantitativa_personalizadas)