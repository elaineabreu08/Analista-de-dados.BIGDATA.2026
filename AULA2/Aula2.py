import pandas as pd
import numpy as np


#LOC
#ILOC
#QUERY

filmes = {

'título': ["Lagoa Azul","Agente secreto","Gênio indomável","A freira","Brinquedo assasino","Top gum"],
    'categoria': ["Romance","Ação","Drama","Terror","Comédia","Aventura"],
    'ano':["1980","2025","1997","2022","1995","1986"],
'faturamento':[6.5,4,5.5,8,8,9]
}
indice =['A','B','C','D','E','F']

tabela_filmes = pd.DataFrame(filmes,index=indice)
print(tabela_filmes)
#print(type(tabela_filmes))
#print(tabela_filmes)
#print(type(tabela_filmes))

#print(tabela_filmes.iloc[-1])
#print('-'*20)
print(tabela_filmes.loc['B'])
print('-'*20)

print(tabela_filmes.iloc[1:3])
print(tabela_filmes.loc['B':'E'])
#print(tabela_filmes.query['titulo'!="Agente secreto"!])
consulta1= tabela_filmes.query("faturamento ==5.5")
print(consulta1)


#<> <= >= == ! = and or not in




