import pandas as pd
dados = pd.read_csv(r'C:\Users\Lucas Lima\Desktop\ALURA - ANALISE DE DADOS\Base\4-Estatistica com Python\dados.csv')

print(sorted(int(x) for x in dados['Anos de Estudo'].unique()))
print(sorted(int(x) for x in dados['UF'].unique()))
print(sorted(int(x) for x in dados['Sexo'].unique()))
print(sorted(int(x) for x in dados['Cor'].unique()))
print(dados['Idade'].min())
print(dados['Idade'].max())
#print(sorted(dados['UF'].unique()))