notas = {"1o Trimestre": 8.5, "2o Trimestre": 9.5, "3o Trimestre": 7}
soma = 0

for nota in notas.values():
    soma += nota

#print(soma)

somatorio = sum(notas.values())
qtde_notas = len(notas)
media = somatorio / qtde_notas
print(round(media, 1))