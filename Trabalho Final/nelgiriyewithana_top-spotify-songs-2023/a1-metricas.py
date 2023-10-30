# ! Importando bibliotecas
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

# * Lendo arquivo da rede do git
grafo = nx.read_edgelist(
    r"E:\UNIRIO\23.2\CR\Trabalho Final\nelgiriyewithana_top-spotify-songs-2023\edges2.csv",
    delimiter=";",
)

nos = pd.read_csv(
    r"E:\UNIRIO\23.2\CR\Trabalho Final\nelgiriyewithana_top-spotify-songs-2023\nodes.csv"
)

for index, row in nos.iterrows():
    artista = row["0"]
    if not grafo.has_node(artista):
        grafo.add_node(artista)


# * Obtendo métricas da rede
num_nos = grafo.number_of_nodes()
num_arestas = grafo.number_of_edges()

print(f"Num nos: {num_nos}")
print(f"Num arestas: {num_arestas}")

# * Obtendo densidade
densidade = nx.density(
    grafo
)  # Rede muito esparsa, muitos nós com poucas ou sem conexões
print(f"Densidade: {densidade}")

"""
# ! mostrando grafo
nx.draw(grafo)
"""

# * Obtendo centralidade
centralidade_grau = nx.degree_centrality(
    grafo
)  # . Artistas com mais colaborações com outros artistas
centralidade_betweness = nx.betweenness_centrality(
    grafo
)  # . Artistas que desempenham um papel crucial na conexão de diferentes partes da rede (importância de um artista na rede como intermediário em colaborações entre outros artistas)
centralidade_proximidade = nx.closeness_centrality(
    grafo
)  # . Artistas mais próximos a todos os outros artistas na rede (o artista que chega com o menor caminho para qualquer outro nó)

# * Obter coef. clusterização global e local (o quanto de panelinha tem, se é num todo ou em pequenas panelinhas)
coef_clusterizacao_local = nx.average_clustering(grafo)
coef_clusterizacao_global = nx.transitivity(grafo)

# * Grau medio
graus = []
for node in grafo.nodes:
    graus.append(nx.degree(grafo, node))

grau_medio = np.mean(graus)

print(f"Grau médio: {grau_medio}")
print(f"Densidade: {densidade}")
print(f"Cluster global: {coef_clusterizacao_global}")
print(f"Cluster médio: {coef_clusterizacao_local}")
print(f"Coeficiente de centralidade de grau: {centralidade_grau}")
print(f"Coeficiente de centralidade de proximidade: {centralidade_proximidade}")
print(f"Coeficiente de centralidade de betweeness: {centralidade_betweness}")
