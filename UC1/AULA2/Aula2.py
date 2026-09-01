#LÓGICAS CONDICIONAIS 

# x=15
# y=20
# print("x é maior que y?",x>y)
# print("x é igual a y?",x==y)
# resposta=x>y
# print(resposta)
# print(type(resposta))


# cnh = True
# bebidinha = False
   
# posso_dirigir = cnh and bebidinha
# print(posso_dirigir)

# cnh = True
# bebidinha = False
   
# posso_dirigir = cnh and not bebidinha
# print(posso_dirigir)

# busaum = False
# trenzin = False

# Venho_para_aula = busaum or trenzin

# print(Venho_para_aula)

#3

# locomocao = "moto"
# choveu = True

# if choveu and locomocao == "moto":
#     resultado = "Tô todo molhado:("


# locomocao = "celtinha"
# choveu = True

# if choveu and locomocao == "moto":
#     resultado = "Tô todo molhado:("
# else:
#     resultado = "Tô seco:)"


# print(resultado)


# locomocao = "celtinha"
# choveu = True

# if choveu and locomocao == "moto":
#     resultado = "Tô todo molhado:("
# elif not choveu and locomocao=='moto':
#         resultado = "Tô seco:)"
# else:
#     resultado = "Tô seco:)"


# print(resultado)


locomocao = input("diga qual é a sua locomocao:")
choveu = True

if choveu and locomocao == "moto":
    resultado = "Tô todo molhado:("
elif not choveu and locomocao=='moto':
        resultado = "Tô seco:)"
else:
    resultado = "Tô seco:)"


print(resultado)
