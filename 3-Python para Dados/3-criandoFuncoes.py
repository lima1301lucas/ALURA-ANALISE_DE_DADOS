def media():
    calculo = (10 + 9 + 8) / 3
    print(calculo)

media()


def media2(nota_1, nota_2, nota_3):
    calculo = (nota_1 + nota_2 + nota_3) / 3
    print(calculo)

media2(3, 6, 9)


notas = [8.5, 9.0, 6.0, 10.0]

def media3(lista):
    calculo = sum(lista)/ len(lista)
    print(calculo)

media3(notas)