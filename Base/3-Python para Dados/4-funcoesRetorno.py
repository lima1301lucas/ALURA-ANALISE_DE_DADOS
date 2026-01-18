notas = [8.5, 9.0, 6.0, 5.0]

def boletim(lista):
    media = sum(lista)/ len(lista)

    if media >= 6:
        situacao = "Aprovado"
    else: 
        situacao = "Reprovado"
    
    return (media, situacao)

resultado = boletim(notas)
media, situacao = boletim(notas)
print(resultado)
print(media)
print(situacao)