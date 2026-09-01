#for i in range(10):
    #print (i)

#for i in range(1,10):
    #print (i) 

#while:
# somador = int(input("registros:"))
# controle = 0

# while controle<=30:
#     controle=controle+somador
#     somador = int(input("registros:"))

# print("oficina lotada")



#FOR



for i in range(5):
    try:
        # i representa o número atual da repetição (0, 1, 2...)
        print(f"Número {i + 1} de 5:")
        num = float(input("Digite um número: "))
 
        dobro = num * 2
        triplo = num * 3
        quádruplo = num * 4
 
        print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
 
    except ValueError:
        print("Entrada inválida. Tente novamente.")


        

acertou = 0
while acertou < 5:
    print(f"Número {acertou + 1} de 5:") 
    num = float(input("Digite um número: ")) 
        
    dobro = num * 2 
    triplo = num * 3 
    quádruplo = num * 4 
        
    print(f"  Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
    acertou+=1 



