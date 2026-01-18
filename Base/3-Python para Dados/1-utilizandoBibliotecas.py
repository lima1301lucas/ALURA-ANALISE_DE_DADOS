import matplotlib.pyplot as plt

estudantes = ["Lucas", "João", "Maria", "José"]
notas = [10.0, 8.5, 7.0, 9.5]

plt.bar(x = estudantes, height = notas)
plt.show()