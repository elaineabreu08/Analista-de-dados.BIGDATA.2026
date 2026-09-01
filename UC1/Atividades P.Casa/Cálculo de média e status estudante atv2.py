#DESAFIO 2: CÁLCULO DE MÉDIA E STATUS DO ESTUDANTE 

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

media = (n1 + n2 + n3 + n4) / 4

if media > 7:
    print("Aprovado!")
elif media >= 5:
    print("Recuperação!")
else:
    print("Reprovado!")


    