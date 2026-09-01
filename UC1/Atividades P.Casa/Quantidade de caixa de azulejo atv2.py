#DESAFIO 2: QUANTIDADE DE CAIXAS DE AZULEJO

comp = float(input("Comprimento (m): "))
larg = float(input("Largura (m): "))
alt = float(input("Altura (m): "))

area = 2 * (comp + larg) * alt
caixas = area / 1.5

if caixas % 1 != 0:
    caixas = int(caixas) + 1

print("Caixas necessárias:", int(caixas))


