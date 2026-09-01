import random 

def rolar_dados(lados):
 return random.randint(1,lados)

input("Aperte enter para rolar para o Ataque (d20)")
Ataque=rolar_dados(20)
print(f"resultado do Ataque:{Ataque}")

input("Aperte enter para rolar para o Dano (d8)")
Dano=rolar_dados(8)

print(f"resultado do Dano:{Dano}")

