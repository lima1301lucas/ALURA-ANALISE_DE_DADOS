import pandas as pd

df = pd.DataFrame(data = {
    'Fulano': [8, 10, 4, 8, 6, 10, 8, 5],
    'Beltrano': [10, 2, 0.5, 1, 3, 9.5, 10, 4],
    'Sicrano': [7.5, 8, 7, 8, 8, 8.5, 7, 10]},
    index = ['Matemática', 'Português', 'Inglês', 'Geografia', 'História', 'Física', 'Química', 'Ciencias'])

df.rename_axis('Matérias', axis = 'columns', inplace = True)

#exemplo ímpar
notas_mediana = df.Fulano.sort_values()
notas_mediana = notas_mediana.reset_index()
n = notas_mediana.shape[0]
n = (n + 1) / 2

#print(notas_mediana.loc[n - 1])
#print(notas_mediana.median())

#exemplo par
notas_mediana = df.Beltrano.sort_values().reset_index(drop=True)
n = notas_mediana.shape[0]

pos1 = n // 2 - 1
pos2 = n // 2
mediana_par = (notas_mediana.loc[pos1] + notas_mediana.loc[pos2]) / 2

print(mediana_par)
print(notas_mediana.median())