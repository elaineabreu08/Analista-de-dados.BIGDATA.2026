while True:
    codigo = int(input("Digite o código (ou 0 para encerrar): "))
    
    if codigo == 0:
        print("Programa finalizado.")
        break  
        
    if codigo == 1:
        print("Procedência: Sul")
    elif codigo == 2:
        print("Procedência: Norte")
    elif codigo == 3:
        print("Procedência: Leste")
    elif codigo == 4:
        print("Procedência: Oeste")
    elif codigo in (5, 6):
        print("Procedência: Nordeste")
    elif codigo in (7, 8, 9):
        print("Procedência: Sudeste")
    elif codigo == 10:
        print("Procedência: Centro-Oeste")
    elif codigo == 11:
        print("Procedência: Noroeste")
    else:
        print("Procedência: Importado")