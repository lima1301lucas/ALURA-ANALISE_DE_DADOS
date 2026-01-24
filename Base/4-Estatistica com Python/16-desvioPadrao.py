import pandas as pd
import numpy as np

df = pd.DataFrame(
    data={
        'Fulano': [8, 10, 4, 8, 6, 10, 8],
        'Beltrano': [10, 2, 0.5, 1, 3, 9.5, 10],
        'Sicrano': [7.5, 8, 7, 8, 8, 8.5, 7]
    },
    index=['Matemática', 'Português', 'Inglês', 'Geografia', 'História', 'Física', 'Química']
)

notas_fulano = df[['Fulano']].copy()
variancia = notas_fulano['Fulano'].var()
desvio_padrao = np.sqrt(variancia)
print(desvio_padrao)

desvio_padrao_2 = notas_fulano['Fulano'].std()
print(desvio_padrao_2)