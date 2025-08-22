# ----------------------------------------
# Submódulo responsável por usar numpy.linalg
# para resolver operações de álgebra linear
# ----------------------------------------

import numpy as np

# Calcula o determinante de uma matriz
def determinante(matriz):
    return np.linalg.det(matriz)

# Calcula os autovalores de uma matriz
def autovalores(matriz):
    return np.linalg.eigvals(matriz)

# Calcula a matriz inversa
def inversa(matriz):
    return np.linalg.inv(matriz)
