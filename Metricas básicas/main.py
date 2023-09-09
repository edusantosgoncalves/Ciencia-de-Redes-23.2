# ! Importando bibliotecas
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plot

# . Lendo arquivo da rede do git
nos = pd.read_csv("./rede_git/musae_git_target.csv")
arestas = pd.read_csv("./rede_git/musae_git_edges.csv")

# . Instanciando grafo (não-direcionado)
grafo = nx.Graph()

# . Iterando pelos nós do csv e adicionando-os no grafo
for i in range(len(nos)):
    # . Adicionando nó no grafo junto a atributo de nome
    grafo.add_node(i, **{"name": nos.name[i]})

# . Iterando pelas aresta do csv e adicionando-as no grafo
for i in range(len(arestas)):
    # . Adicionando aresta entre nós
    grafo.add_edge(int(arestas.id_1[i]), int(arestas.id_2[i]))

# . Obtendo métricas da rede
num_nos = grafo.number_of_nodes()
num_arestas = grafo.number_of_edges()
print(f"Número de nós: {num_nos}")
print(f"Número de arestas: {num_arestas}")
print(f"Densidade: {nx.density(grafo):.4f}")

# . Obtendo grau médio do grafo
graus = dict(
    nx.degree(grafo)
)  # . Como o degree retorna array de tuplas (nó, grau), converto-os para dicionários key-value no formato nó: grau

graus = list(
    graus.values()
)  # . Convertendo o dicionario para um array só com os graus dos nós

grau_medio = 2 * num_arestas / num_nos
print(f"Grau médio: {grau_medio:.4f}")

# . Voltando a outras métricas
print(f"Quantidade de componentes conexas: {nx.number_connected_components(grafo)}")

componentes_conexas = nx.connected_components(grafo)
maior_componente_conexa = max(componentes_conexas, key=len)
qtd_nos_maior_componente_conexa = len(maior_componente_conexa)
print(
    f"Quantidade de nós na maior componente conexa: {qtd_nos_maior_componente_conexa}"
)

# . Obtendo tamanho componentes isoladas
tamanhos_componentes_isoladas = [
    len(componente) for componente in list(nx.isolates(grafo))
]

# . Obtendo o tamanho médio das componentes isoladas
tamanho_medio_componentes_isoladas = 0

if len(tamanhos_componentes_isoladas) > 0:
    tamanho_medio_componentes_isoladas = sum(tamanhos_componentes_isoladas) / len(
        tamanhos_componentes_isoladas
    )
else:
    tamanho_medio_componentes_isoladas = "não possui componente isolada!"

print(f"Tamanho médio de componentes isoladas: {tamanho_medio_componentes_isoladas}")


# . Coeficiente de clusterização
print(f"Coeficiente de clusterização do Grafo: {nx.average_clustering(grafo):.4f}")

# . Plotando distribuição de graus
distribuicao_graus = nx.degree_histogram(grafo)

# . Criando lista de graus correspondentes aos índices na distribuição
graus = list(range(len(distribuicao_graus)))

# . Plotando a distribuição de graus em um gráfico de pontos
plot.scatter(graus, distribuicao_graus, marker="o")
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
