# Arquivo principal do projeto
# Importa funções dos outros módulos e demonstra seu uso

# Importando funções dos submódulos
from projeto.aleatorio import gerar_numero, gerar_array, gerar_matriz
from projeto.algebra import determinante, autovalores, inversa
from projeto.util import maior, menor, soma
import numpy as np  # Biblioteca para operações matemáticas

# Execução principal do programa
if __name__ == "__main__":
    # === Testes do módulo aleatorio.py ===
    print("\n=== Testes aleatorio (numpy.random) ===")
    print(f"Número aleatório: {gerar_numero()}")  # Mostra um número aleatório
    print(f"Array aleatório: {gerar_array(5)}")  # Mostra um array de 5 números
    matriz_random = gerar_matriz(3, 3)           # Cria uma matriz 3x3 aleatória
    print(f"Matriz aleatória:\n{matriz_random}")

    # === Testes do módulo algebra.py ===
    print("\n=== Testes algebra (numpy.linalg) ===")
    print(f"Determinante: {determinante(matriz_random)}")  # Calcula o determinante
    print(f"Autovalores: {autovalores(matriz_random)}")    # Calcula os autovalores
    print(f"Inversa:\n{inversa(matriz_random)}")           # Calcula a inversa

    # === Testes do módulo util.py ===
    print("\n=== Testes util (funções extras) ===")
    lista = [1, 5, 8, 2, 9, 17, 27]  # Lista de exemplo
    print(f"Lista: {lista}")
    print(f"Maior: {maior(lista)}")   # Maior valor da lista
    print(f"Menor: {menor(lista)}")   # Menor valor da lista
    print(f"Soma: {soma(lista)}")     # Soma dos valores da lista
