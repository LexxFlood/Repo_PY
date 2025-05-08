notas = []

for x in range (2):
    codigo_aluno= input("RM: ")
    nota= float(input("Nota: "))
    total= [codigo_aluno,nota]
    notas.append(total)

print("quantidade de notas")
for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM ", codigo_aluno, "tirou a nota", nota)