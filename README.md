# Projeto linguagem Python e NumPy

Este projeto tem como objetivo demonstrar a combinação de estruturas básicas da linguagem Python com funcionalidades da biblioteca NumPy, iremos abordar os submódulos numpy.linalg e numpy.random.

# Linguagem utlizada
Python 3.13.5

# Biblioteca utlizada 
Numpy

# Autora  
**Nome:** Kaline de Almeida Felipe  
**Disciplina/Curso:** (Introdução aos Softwares Estatísticos/ Estatística)  
**Data:** 22 de Agosto de 2025 

# Estrutura das pastas

projeto/                # Pasta principal do projeto
│
├── projeto/            # Pacote com os módulos
│   ├── __init__.py     # Inicializa o pacote
│   ├── aleatorio.py    # Funções com números aleatórios (numpy.random)
│   ├── algebra.py      Funções de álgebra (numpy.linalg)

│   └── util.py         # Função maior()
│
├── main.py             # Arquivo principal
└── README.md           # Documentação


# Estruturas básicas do Python

Listas: [1, 2, 3]
Dicionários: {"nome": "Aline", "idade": 35}
Laços: for, while
Funções: def soma(a, b): return a+b
Condicionais: if, else

# Funcionalidades do NumPy

- Criar arrays/matrizes: np.array([1,2,3])
- Operações matemáticas eficientes: np.mean(arr), np.dot(A,B)
- Submódulos:
  - numpy.linalg → coisas de álgebra linear (autovalores, resolver sistema, inversa de matriz etc.)
  - numpy.random → gerar números aleatórios (simulações, amostras, matrizes aleatórias etc.)

# Exemplos na prática

Dessa forma, iremos demostrar o uso combinado de estruturas básicas da linguagem Python e funcionalidades do NumPy. Por meio de exemplos práticos nos submódulo solicitado (numpy.linalg e numpy.random) no qual estão implementados no arquivo `main.py`.

# Instalação e execução

Para executar o projeto no computador, seguimos os passos abaixo:

1. **Clonar o repositório:**

   ```bash
   git clone https://github.com/KalineFelipe/Phyton-Numpy-Projeto.git
   cd Phyton-Numpy-Projeto

      Esse é o local onde pode ser encontrado o repositório no GitHub.

2. **Criar e ativar um ambiente virtual:**

python -m venv venv

- Ativar no Windows
venv\Scripts\activate

- Ativar no Linux/Mac
source venv/bin/activate

3. **Instalar dependências:**

Como estamos utilizando apenas o NumPy, basta apenas instalá-lo:
pip install numpy

4. **Executar o projeto:**

Rode o arquivo principal:
python main.py

# Conclusão

Este projeto foi desenvolvido com o objetivo de praticar e aplicar conceitos da linguagem Python em conjunto com a biblioteca NumPy. Como processo de avaliação da segunda nota da disciplina.
Foram implementadas funções para manipulação de matrizes, operações algébricas e geração de números aleatórios, demonstrando como o NumPy pode simplificar cálculos e otimizar o desenvolvimento.



