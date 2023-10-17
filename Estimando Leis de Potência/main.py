# ! Importando bibliotecas
import networkx as nx
from scipy.stats import linregress
import numpy as np
import matplotlib.pyplot as plot
import scipy.linalg as la
import scipy.special as sp


# . Instanciando grafo (não-direcionado)
grafo = nx.read_edgelist(
    r"E:\UNIRIO\23.2\CR\Estimando Leis de Potência\bases-livro\collaboration.edgelist.txt"
)

# . Obtendo distribuicao graus
freq_graus = nx.degree_histogram(grafo)

# . Criando lista de graus correspondentes aos índices na distribuição
graus = list(range(len(freq_graus)))

# . Plotando a distribuição de graus em um gráfico de pontos - c log
plot.scatter(graus, freq_graus, marker="o")
plot.xscale(
    "log"
)  # . Definindo que o grafico seja plotado em escala logarítmica no eixo x
plot.yscale(
    "log"
)  # . Definindo que o grafico seja plotado em escala logarítmica no eixo y
plot.xlabel("Grau")
plot.ylabel("Contagem")
plot.title("Distribuição de Graus em Escala Logarítmica")
plot.show()

# . Plotando a distribuição de graus em um gráfico de pontos - sem log
plot.scatter(graus, freq_graus, marker="o")
plot.xlabel("Grau")
plot.ylabel("Contagem")
plot.title("Distribuição de Graus em Escala Logarítmica")
plot.show()


# ! 1. Plote em escala normal e escala log-log a distribuição de grau da rede (desprezando vértices de grau 0). Qual delas é mais adequada para estimar o valor de γ? Por quê?
# . A distribuição de graus em log é mais adequada pois permite visualizar melhor a distribuição de graus em grandes redes. Em redes pequenas, a distribuição de graus pode ser plotada sem logaritmo e ainda ser legível. No entanto, em redes grandes, a distribuição de graus tende a ser muito dispersa, o que pode dificultar a visualização de padrões.

# ! 2. De posse desse plot, estime superficialmente o valor de γ interpolando os dados por uma linha reta. Qual é a inclinação da linha reta que você traçou? A partir desta inclinação, qual é o valor estimado de γ?

# . Cateto A -> ampl eixo contagem -> 3200 - 1 = 3199
# . Cateto B -> ampl eixo grau -> 61 - 2 = 59
hipotenusa = np.hypot(3199, 59)  # . sqrt(Cateto a ^ 2 + Cateto B ^ 2)
print(f"Hipotenusa: {hipotenusa}")
seno_angulo = 3199 / hipotenusa  # . Cateto Oposto = A / hipotenusa
print(f"Seno do ângulo: {seno_angulo}")
gamma = np.arcsin(seno_angulo)
print(f"Valor estimado de gamma = {gamma}")

# ! 3. Repita os itens 1 e 2, mas utilizando a distribuição de grau cumulativa (lembrete: na distribuição cumulativa de uma variável aleatória X, o eixo y contém P[X ≥ x] em vez de P[X = x]). Qual é a inclinação da linha reta traçada nesse caso? Qual é o valor estimado de γ?

# . Obtendo frequencia de graus
degree_sequence = [d for n, d in grafo.degree()]
degree_counts = dict(zip(*np.unique(degree_sequence, return_counts=True)))

# . Transformando os dados em logaritmos naturais
degrees = list(degree_counts.keys())
probabilities = [count / len(degree_sequence) for count in degree_counts.values()]
ln_degrees = np.log(degrees)
ln_probabilities = np.log(probabilities)

# . Fazendo regressão linear
slope, intercept, r_value, p_value, std_err = linregress(ln_degrees, ln_probabilities)
gamma = -slope
print("Índice de Lei de Potência (gamma):", gamma)

# . Plotando a distribuição de graus em um gráfico de pontos - c log e reta
plot.scatter(ln_degrees, ln_probabilities, label="Dados")
plot.plot(
    ln_degrees, intercept + slope * ln_degrees, color="red", label="Regressão Linear"
)
plot.xlabel("ln(k)")
plot.ylabel("ln(P(k))")
plot.legend()
plot.show()
