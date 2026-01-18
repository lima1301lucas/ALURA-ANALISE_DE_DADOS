#nota = float(input("Digite a nota: "))
#
#def qualitativo(x):
#    return x + 0.5
#
#print(qualitativo(nota))

#nota = float(input("Digite a nota: "))
#qualitativo = lambda x: x + 0.5
#print(qualitativo(nota))

n1 = float(input("Digite a 1a nota: "))
n2 = float(input("Digite a 2a nota: "))
n3 = float(input("Digite a 3a nota: "))

media = lambda x, y, z: (x * 3 + y * 2 + z * 5)/10

print(media(n1, n2, n3))