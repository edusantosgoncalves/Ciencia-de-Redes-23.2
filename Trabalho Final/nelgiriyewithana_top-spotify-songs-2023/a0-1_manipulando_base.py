import pandas as pd
import networkx as nx
from itertools import combinations as cb

# * Leia o arquivo CSV original
df = pd.read_csv(
    r".\nelgiriyewithana_top-spotify-songs-2023\spotify-2023.csv",
    encoding="1252",
)
df_nos = pd.DataFrame(
    {
        "track": [],
        "artist": [],
    }
)
df_arestas = pd.DataFrame({"artist_1": [], "artist_2": [], "track_name": []})

grafo = nx.Graph()


for index, row in df.iterrows():
    track_name = row["track_name"]
    artistas_split = row["artist(s)_name"].split(", ")
    artistas_split = [artista.strip() for artista in artistas_split]

    if len(artistas_split) == 1:
        if not grafo.has_node(artistas_split[0]):
            grafo.add_node(artistas_split[0])
        continue

    artista_tuple = list(cb(artistas_split, 2))
    artista_tuple = [
        artista for artista in artista_tuple if artista[0] != artista[1]
    ]  # Limpando relações de artistas com si mesmos
    if len(artista_tuple) > 0:
        grafo.add_edges_from(artista_tuple)  # , label=track_name)

# * Exportando nos
# Convertendo lista de nos num dataframe
df = pd.DataFrame(grafo.nodes)

# Exportando o dataframe em csv
df.to_csv(r".\nelgiriyewithana_top-spotify-songs-2023\nodes.csv", index=False)

# * Exportando lista de arestas
nx.write_edgelist(
    grafo, r".\nelgiriyewithana_top-spotify-songs-2023\edges.txt", delimiter=";"
)
