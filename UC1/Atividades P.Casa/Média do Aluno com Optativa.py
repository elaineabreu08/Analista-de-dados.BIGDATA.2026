
nota1 = float(input("Digite a nota da 1ª avaliação: "))
nota2 = float(input("Digite a nota da 2ª avaliação: "))
optativa = float(input("Digite a nota da optativa (ou -1 se não fez): "))

if optativa != -1:
    if nota1 < nota2 and optativa > nota1:
        nota1 = optativa
    elif nota2 <= nota1 and optativa > nota2:
        nota2 = optativa

media = (nota1 + nota2) / 2

print("\nMédia final:", media)

if media >= 6.0:
    print("Situação: APROVADO")
elif media >= 3.0:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: REPROVADO")