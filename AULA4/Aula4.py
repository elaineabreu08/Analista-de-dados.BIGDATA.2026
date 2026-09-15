
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


dados = np.array([12,15,17,20,22,25,28,30,35,40])
print(dados)

#calcular quartis
q1 = np.percentile(dados,25)
q2 = np.percentile(dados,50)
q3 = np.percentile(dados,75)

#exibir os resultados




