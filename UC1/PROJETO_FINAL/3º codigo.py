#3º Código

# Cabeçalho com dados do restaurante
print("=== JAPONÊS TANOSHIMI ===")
print("Av. Lúcio Costa - Barra da Tijuca, RJ\n")

# Listas com os pratos e preços
codigos = ["1", "2", "3", "4"]
nomes = ["sushi", "sashimi", "temaki", "yakisoba"]
precos = [35.00, 40.00, 28.00, 32.00]

rodando = True

# Loop principal da consulta
while rodando:
    print("--- CONSULTA DE PRATOS ---")
    busca = input("Digite o CÓDIGO ou NOME do prato (ou 'sair' para encerrar): ").lower()
    
    if busca == "sair":
        print("\nObrigado por utilizar o cardápio do Japonês Tanoshimi! Bom apetite!")
        rodando = False
    elif busca in codigos:
        posicao = codigos.index(busca)
        print(f"Prato: {nomes[posicao].capitalize()} | Preço: R$ {precos[posicao]:.2f}\n")
    elif busca in nomes:
        posicao = nomes.index(busca)
        print(f"Código: {codigos[posicao]} | Preço: R$ {precos[posicao]:.2f}\n")
    else:
        print("Prato não encontrado!\n")