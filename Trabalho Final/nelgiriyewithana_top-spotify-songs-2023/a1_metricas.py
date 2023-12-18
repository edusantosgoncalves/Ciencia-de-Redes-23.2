# ! Importando bibliotecas
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# * Lendo arquivo da rede do git
grafo = nx.read_edgelist(
    r".\nelgiriyewithana_top-spotify-songs-2023\edges.txt",
    delimiter=";",
)

nos = pd.read_csv(r".\nelgiriyewithana_top-spotify-songs-2023\nodes.csv")

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
print(f"Cluster global: {coef_clusterizacao_global}")
print(f"Cluster médio: {coef_clusterizacao_local}")

# ! Plotando distribuição de graus em log
# . Plotando distribuição de graus
distribuicao_graus = nx.degree_histogram(grafo)

# . Criando lista de graus correspondentes aos índices na distribuição
graus = list(range(len(distribuicao_graus)))

# . Plotando a distribuição de graus em um gráfico de pontos
plt.scatter(graus, distribuicao_graus, marker="o")
plt.xscale(
    "log"
)  # . Definindo que o grafico seja plotado em escala logarítmica no eixo x
plt.yscale(
    "log"
)  # . Definindo que o grafico seja plotado em escala logarítmica no eixo y
plt.xlabel("Grau")
plt.ylabel("Contagem")
plt.title("Distribuição de Graus em Escala Logarítmica")
# plt.show()


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
plt.figure()
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
# plt.show()


# * Plotando centralidade de proximidade:
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

# Plotando a rede
plt.figure(figsize=(10, 5))
nx.draw(
    grafo,
)
plt.title("Rede de colaboração de artistas charteados no Spotify (2013)")
plt.show()


# ! Tentando verificar comunidades com todo o grafo
# * Plotando comunidades
comunidades_todo = nx.algorithms.community.girvan_newman(grafo)

# Extraia as comunidades do objeto gerado pelo algoritmo
comunidades_todo = tuple(sorted(c) for c in next(comunidades_todo))

# Crie um dicionário onde as chaves são os nós e os valores são os números das comunidades
comunidades_todo_dict = {
    node: i for i, com in enumerate(comunidades_todo) for node in com
}

# Gere cores diferentes para cada comunidade
cores_todo = [comunidades_todo_dict[node] for node in grafo.nodes()]

# Desenhe o grafo com cores diferentes para cada comunidade
pos = nx.spring_layout(grafo)  # Layout para posicionar os nós
nx.draw(grafo, pos, node_color=cores_todo, with_labels=False)

# Mostre o plot
plt.show()

# ! Verificando comunidades removendo os nós isolados
# Removendo nós isolados
isolados = list(nx.isolates(grafo))
grafo_isolados = grafo.copy()
grafo_isolados.remove_nodes_from(isolados)

# * Plotando comunidades
comunidades_isolados = nx.algorithms.community.girvan_newman(grafo_isolados)

# Extraia as comunidades do objeto gerado pelo algoritmo
comunidades_isolados = tuple(sorted(c) for c in next(comunidades_isolados))

# Crie um dicionário onde as chaves são os nós e os valores são os números das comunidades
comunidades_isolados_dict = {
    node: i for i, com in enumerate(comunidades_isolados) for node in com
}

# Gere cores diferentes para cada comunidade
cores_isolados = [comunidades_isolados_dict[node] for node in grafo_isolados.nodes()]

# Desenhe o grafo com cores diferentes para cada comunidade
pos = nx.spring_layout(grafo_isolados)  # Layout para posicionar os nós
nx.draw(grafo_isolados, pos, node_color=cores_isolados, with_labels=False)

# Mostre o plot
plt.show()


# ! Verificando comunidades com a maior componente conexa
# Obter o maior componente conexo
componentes_conexos = nx.connected_components(grafo)
maior_componente = max(componentes_conexos, key=len)
sub_grafo_maior_componente = grafo.subgraph(maior_componente)

# Identificar comunidades
comunidades = nx.algorithms.community.girvan_newman(sub_grafo_maior_componente)

# * Plotando comunidades
# Extraia as comunidades do objeto gerado pelo algoritmo
comunidades = tuple(sorted(c) for c in next(comunidades))

# Crie um dicionário onde as chaves são os nós e os valores são os números das comunidades
comunidades_dict = {node: i for i, com in enumerate(comunidades) for node in com}

# Gere cores diferentes para cada comunidade
cores = [comunidades_dict[node] for node in sub_grafo_maior_componente.nodes()]

# Desenhe o grafo com cores diferentes para cada comunidade sem Label
pos = nx.spring_layout(sub_grafo_maior_componente)  # Layout para posicionar os nós
nx.draw(sub_grafo_maior_componente, pos, node_color=cores, with_labels=False)

# Mostre o plot
plt.show()

# Desenhe o grafo com cores diferentes para cada comunidade com label
pos = nx.spring_layout(sub_grafo_maior_componente)  # Layout para posicionar os nós
nx.draw(sub_grafo_maior_componente, pos, node_color=cores, with_labels=True)

# Mostre o plot
plt.show()
