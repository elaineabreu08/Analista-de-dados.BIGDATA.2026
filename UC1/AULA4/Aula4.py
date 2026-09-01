mes = int (input("informe o mes de seu nascimento"))
#VISÃO MATCH CASE:
match mes: 
    
    case 1:
        signo="Aquário"
    case 2:
        signo="Áries"
    case 3:
        signo="Touro"
    case 4:
        signo="Gêmeos"
    case 5:
        signo="Câncer"
    case _:
        signo="Número de mês inválido"

print(f"{signo}.")



    