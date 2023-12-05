# Getting Started matplotlib

# Importação das bibliotecas
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#definição de funções

def quadratica(x):
    return x*x

# Atribuição de variáveis 
x = np.linspace(-10,10, 200)
y = quadratica(x)

# Processamento de dados
fig, ax = plt.subplots()
ax. plot(x,y)

#Saída de dados
plt.show()