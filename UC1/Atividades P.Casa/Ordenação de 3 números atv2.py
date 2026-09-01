#DESAFIO 1: ORDENAÇÃO DE 3 NÚMEROS

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a > b:
    a, b = b, a  

if b > c:
    b, c = c, b  

if a > b:
    a, b = b, a  

print(f"Ordem crescente: {a}, {b}, {c}")


#


