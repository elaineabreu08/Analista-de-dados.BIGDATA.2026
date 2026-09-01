ANO_ATUAL = 2026


for i in range(1, 13):
    print(f"\n--- Candidato {i} ---")
    
    
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    idade = ANO_ATUAL - ano_nascimento
    
    
    if idade < 18:
        print(f"Candidato tem {idade} anos. Menores de 18 anos não podem participar.")
        continue  
    
    
    print(f"Candidato aprovado na triagem ({idade} anos). Prosseguindo com o cadastro:")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")
    
    print("-> Cadastro realizado com sucesso!")