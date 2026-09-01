#1º código

# Informações do Restaurante
print("==========================================")
print("     Bem-vindo ao Japonês Tanoshimi!      ")
print(" Localização: Av. Lúcio Costa - Barra da Tijuca, RJ")
print(" Ambientes climatizados e ao ar livre disponíveis ")
print("==========================================\n")

# Cardápio do restaurante (Código, Nome, Preço)
cardapio = [
    {"codigo": "1", "nome": "sushi", "preco": 35.00},
    {"codigo": "2", "nome": "sashimi", "preco": 40.00},
    {"codigo": "3", "nome": "temaki", "preco": 28.00},
    {"codigo": "4", "nome": "hot roll", "preco": 25.00},
    {"codigo": "5", "nome": "yakisoba", "preco": 32.00}
]
# Loop principal da consulta
rodando = True

while rodando:
    print("--- CONSULTA DE PRATOS ---")
    busca = input("Digite o CÓDIGO ou o NOME do prato (ou 'sair' para encerrar): ").strip().lower()
    
    if busca == "sair":
        print("\nObrigado por utilizar o cardápio do Japonês Tanoshimi! Bom apetite!")
        rodando = False
    else:
        encontrado = False
        
        # Percorre o cardápio procurando pelo código ou pelo nome
        for prato in cardapio:
            if busca == prato["codigo"] or busca == prato["nome"]:
               
                print(f"Código: {prato['codigo']}")
                print(f"Nome: {prato['nome'].capitalize()}")
                print(f"Preço: R$ {prato['preco']:.2f}\n")
                encontrado = True
                break  # Para a busca assim que encontra
        
        if not encontrado:
            print("\nPrato não encontrado. Verifique o nome ou código e tente novamente.\n")



#Como funciona:

#input e lower, permite que o cliente digite o nome em maiúsculas ou minúsculas sem gerar erro na busca

#O comando if busca == prato["codigo"] or busca == prato["nome"] verifica se a entrada do usuário combina com o número ou com o nome do item.

#Loop while, mantém o cardápio ativo para várias consultas até que o usuário digite "sair".
hhhhhhh

