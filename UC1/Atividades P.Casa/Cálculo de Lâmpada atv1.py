#DESAFIO 1: CÁLCULO DE LÂMPADAS

potencia = float(input("Potência da lâmpada (W): "))
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))

area = largura * comprimento
watts_necessarios = area * 3
lampadas = watts_necessarios / potencia

if lampadas < 1:
    lampadas = 1
else:
    lampadas = int(lampadas)

print("Lâmpadas necessárias:", lampadas)

