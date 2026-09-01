#DESAFIO 3: RENDIMENTO DO TAXISTA

km_inicial = float(input("Odômetro inicial (km): "))
km_final = float(input("Odômetro final (km): "))
litros = float(input("Litros gastos: "))
recebido = float(input("Valor recebido (R$): "))

if km_final < km_inicial:
    print("Erro: O km final não pode ser menor que o km inicial!")
elif litros <= 0:
    print("Erro: A quantidade de litros deve ser maior que zero!")
else:
    
    media_consumo = (km_final - km_inicial) / litros
    lucro = recebido - (litros * 6.15)

    print("Média do consumo:", media_consumo, "km/L")
    print("Lucro líquido: R$", lucro)