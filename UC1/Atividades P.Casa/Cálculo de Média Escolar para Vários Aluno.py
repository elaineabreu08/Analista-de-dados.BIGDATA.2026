for i in range(1, 11):
    print(f"\n--- Estudante {i} ---")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2
    print(f"Média: {media:.1f}")

    if media >= 7.0:
        print("Status: Aprovado")
    elif media >= 5.0:
        print("Status: Recuperação")
    else:
        print("Status: Reprovado")
        