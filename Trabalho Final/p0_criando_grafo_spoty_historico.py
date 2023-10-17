# ! Importando bibliotecas
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plot

# . Lendo arquivo da rede do git
nos = pd.read_csv("./jfreyberg_spotify-artist-feature-collaboration-network/nodes.csv")
arestas = pd.read_csv(
    "./jfreyberg_spotify-artist-feature-collaboration-network/edges.csv"
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
