#impar_1 = 3
#impar_2 = 5
#impar_3 = 13
#impar_4 = 27


#impares = []
#print(type(impares))
#impares = [3,5,13,27]
#print(impares[0])

# lista_01 = [
#     12,
#     "pedro",
#     12.53343,
#     "[{_{^^{}}}",
#     False,
#     0,[2,4,6,8]
#     ]


# print(lista_01[1],lista_01[2],lista_01[4],lista_01[6][2])


#condicionais:

# lista_02 = ["Márcia"]

# if "Márcia" in lista_02:
#     print(lista_02)
# else:
#     print("Márcia não está presente na lista.")

#looping

# partcipantes = ["Isaque","Luana","Fernanda","Bianca","Ana Paula"]

# #for participante in partcipantes:
# #    print(participante)

# partic_2 = "Hugo"
# partcipantes.append(partic_2) 
# partcipantes.insert(2,partic_2)
# partcipantes.remove(partcipantes[1])
# partcipantes.pop(1)
# partcipantes.reverse("hugo")
# partcipantes.count("hugo")
# partcipantes.index()
# partcipantes.clear()



# print(partcipantes)


#Tuplas:

# partcipantes = ["Isaque","Luana","Fernanda","Bianca","Ana Paula"]
# print(partcipantes)
# print(partcipantes,type(partcipantes))
#participante_02=


#Sets:

numeros_pares = {
    202,
    203,
    204,
    205,
    219,
    291,
    292,
    202
}
#print(numeros_pares,type(numeros_pares))

numeros_pares={111,111,112,291,291,205}
print(numeros_pares.intersection(numeros_pares))

numeros_pares.remove(205)
print(numeros_pares)

#Dict (dicioário)

produtos = {
    "maçã":5.99,
    "laranja":4.79
}
#print(produtos,(type(produtos)))

print(produtos.items())
print(produtos.keys())
print(produtos.values())
print(produtos.get("laranja"))
produtos2 = produtos.copy()
print(produtos2)
#produtos.update()
produtos2["maçã"]=7.99
print(produtos2)
###
achadinhos = {}
print(type(achadinhos))
achadinhos["capinha celular"]=12.99
print(achadinhos)





























