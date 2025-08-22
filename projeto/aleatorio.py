# ----------------------------------------
# Módulo responsável por gerar números, arrays e matrizes aleatórias
# ----------------------------------------

import numpy as np  # Biblioteca para cálculo numérico

# Gera um número inteiro aleatório entre 0 e 100
def gerar_numero():
    return np.random.randint(0, 100)

# Gera um array de tamanho n com números aleatórios
def gerar_array(n):
    return np.random.randint(0, 100, size=n)

# Gera uma matriz de tamanho linhas x colunas com números aleatórios
def gerar_matriz(linhas, colunas):
    return np.random.randint(0, 100, size=(linhas, colunas))


