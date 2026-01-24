import pandas as pd

df = pd.DataFrame(
    data={
        'Fulano': [8, 10, 4, 8, 6, 10, 8],
        'Beltrano': [10, 2, 0.5, 1, 3, 9.5, 10],
        'Sicrano': [7.5, 8, 7, 8, 8, 8.5, 7]
    },
    index=['Matemática', 'Português', 'Inglês', 'Geografia', 'História', 'Física', 'Química']
)

notas_fulano = df[['Fulano']].copy()
nota_media_fulano = notas_fulano['Fulano'].mean()
notas_fulano['Desvio'] = notas_fulano['Fulano'] - nota_media_fulano
notas_fulano['|Desvio|'] = notas_fulano['Desvio'].abs()
notas_fulano['(Desvio) ^ 2'] = notas_fulano['Desvio'].pow(2)
print(notas_fulano['(Desvio) ^ 2'].sum() / (len(notas_fulano) - 1))

variancia = notas_fulano['Fulano'].var()
print(variancia)