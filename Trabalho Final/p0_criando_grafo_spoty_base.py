# ! Importando bibliotecas
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# . Lendo arquivo da rede do git
nos = pd.read_csv(
    r"E:\UNIRIO\23.2\CR\Trabalho Final\jfreyberg_spotify-artist-feature-collaboration-network\nodes.csv"
)
arestas = pd.read_csv(
    r"E:\UNIRIO\23.2\CR\Trabalho Final\jfreyberg_spotify-artist-feature-collaboration-network\edges.csv"
)

# . Instanciando grafo (não-direcionado)
grafo = nx.Graph()

# . Iterando pelos nós do csv e adicionando-os no grafo
for i in range(len(nos)):
    # . Adicionando nó no grafo junto a atributo de nome
    grafo.add_node(
        nos.spotify_id[i],
        **{
            "spotify_id": nos.spotify_id[i],
            "name": nos.name[i],
            "followers": nos.followers[i],
            "popularity": nos.popularity[i],
            "genres": nos.genres[i],
            "chart_hits": nos.chart_hits[i],
        },
    )

# . Iterando pelas aresta do csv e adicionando-as no grafo
for i in range(len(arestas)):
    # . Adicionando aresta entre nós
    grafo.add_edge((arestas.id_0[i]), (arestas.id_1[i]))

# . Obtendo métricas da rede
num_nos = grafo.number_of_nodes()
num_arestas = grafo.number_of_edges()

print(f"Num nos: {num_nos}")
print(f"Num arestas: {num_arestas}")

# * Obtendo densidade
densidade = nx.density(
    grafo
)  # Rede muito esparsa, muitos nós com poucas ou sem conexões
print(f"Densidade: {densidade}")

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

# * Plotando centralidade de grau:
centralidade_grau = dict(
    sorted(centralidade_grau.items(), key=lambda item: item[1], reverse=True)
)
# Selecione os 15 nós com a maior centralidade de grau
top_15_nos_centralidade_grau = {
    key: centralidade_grau[key] for key in list(centralidade_grau)[:15]
}

# Extraia os valores de centralidade desses 15 nós
valores_centralidade_grau = [
    top_15_nos_centralidade_grau[node] for node in top_15_nos_centralidade_grau
]

# Plote um gráfico de barras da centralidade de grau
plt.figure(figsize=(10, 5))
plt.bar(top_15_nos_centralidade_grau.keys(), valores_centralidade_grau)
plt.xlabel("Nós")
plt.ylabel("Coeficiente de centralidade de Grau")
plt.title("Centralidade de Grau")
plt.xticks(
    range(len(top_15_nos_centralidade_grau.keys())),
    top_15_nos_centralidade_grau.keys(),
    size="small",
)
# plt.show()

# * Plotando centralidade de betweness:
centralidade_betweness = dict(
    sorted(centralidade_betweness.items(), key=lambda item: item[1], reverse=True)
)
# Selecione os 15 nós com a maior centralidade
top_15_nos_centralidade_betweness = {
    key: centralidade_betweness[key] for key in list(centralidade_betweness)[:15]
}

# Extraia os valores de centralidade desses 15 nós
valores_centralidade_betweness = [
    top_15_nos_centralidade_betweness[node]
    for node in top_15_nos_centralidade_betweness
]
# Plote um gráfico de barras da centralidade de betweness
plt.figure(figsize=(10, 5))
plt.bar(top_15_nos_centralidade_betweness.keys(), valores_centralidade_betweness)
plt.xlabel("Nós")
plt.ylabel("Coeficiente de centralidade de Betweness")
plt.title("Centralidade de Betweness")
plt.xticks(
    range(len(top_15_nos_centralidade_betweness.keys())),
    top_15_nos_centralidade_betweness.keys(),
    size="small",
)


# * Plotando centralidade de betweness:
centralidade_proximidade = dict(
    sorted(centralidade_proximidade.items(), key=lambda item: item[1], reverse=True)
)
# Selecione os 15 nós com a maior centralidade
top_15_nos_centralidade_proximidade = {
    key: centralidade_proximidade[key] for key in list(centralidade_proximidade)[:15]
}

# Extraia os valores de centralidade desses 15 nós
valores_centralidade_proximidade = [
    top_15_nos_centralidade_proximidade[node]
    for node in top_15_nos_centralidade_proximidade
]
# Plote um gráfico de barras da centralidade de betweness
plt.figure(figsize=(10, 5))
plt.bar(top_15_nos_centralidade_proximidade.keys(), valores_centralidade_proximidade)
plt.xlabel("Nós")
plt.ylabel("Coeficiente de centralidade de proximidade")
plt.title("Centralidade de proximidade")
plt.xticks(
    range(len(top_15_nos_centralidade_proximidade.keys())),
    top_15_nos_centralidade_proximidade.keys(),
    size="small",
)
plt.show()
"""
plt.figure(figsize=(10, 5))
# pos = nx.spring_layout(grafo)  # Position the nodes using a spring layout
nx.draw(
    grafo,
    # pos,
    # with_labels=True,
)
plt.title("Rede de colaboração de artistas charteados no Spotify (2013)")
plt.show()"""
