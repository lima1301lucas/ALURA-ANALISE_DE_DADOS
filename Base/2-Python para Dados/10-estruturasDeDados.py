#lista = ["Lucas Lima",  9.5, 10.0, 9.0, True]
#print(lista)
#print(lista[0])
#print(lista[1])
#print(lista[2])
#print(lista[3])
#print(lista[4])
#print(lista[-1])

#for elemento in lista:
#   print(elemento)

#print(len(lista))
#print(lista[1:4])
#
#media = float((lista[1] + lista[2] + lista[3])/3)
#lista.append(media)

dicionario = {
    'chave_1': 1,
    'chave_2': 2
}

cadastro = {
    'matricula': 2000168933,
    'dia_cadastro': 25,
    'mes_cadastro': 10,
    'turma': '2E'
}

print(cadastro['matricula'])
cadastro['turma'] = '2G'
cadastro['modalidade'] = 'EAD'
cadastro.pop('turma')


for chaves in cadastro.keys():
    print(cadastro[chaves])

for valores in cadastro.values():
    print(valores)

for chaves, valores  in cadastro.items():
    print(chaves, valores)