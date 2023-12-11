# Importando biblitecas
import pandas as pd
import numpy as np


# Lendo os arquivos
df1nos = pd.read_csv("./nodes.csv")
df2nos = pd.read_csv("./nodes.csv")
df1arestas = pd.read_csv("./edges.csv")

# Mantendo somente coluna id e name
df1nos = df1nos[["spotify_id", "name"]]
df2nos = df2nos[["spotify_id", "name"]]

# Trocando as colunas id_0 e id_1 do edges para a coluna "name" contido em nodes
dfarestas = pd.merge(
    df1arestas, df1nos, how="inner", left_on="id_0", right_on="spotify_id"
)

dfarestas = dfarestas.rename(columns={"name": "name_0"})

dfarestas = pd.merge(
    dfarestas, df2nos, how="inner", left_on="id_1", right_on="spotify_id"
)

dfarestas = dfarestas.rename(columns={"name": "name_1"})

# Removendo colunas desnecessárias
dfarestas = dfarestas[["name_0", "name_1"]]

# Exportando o dataframe em csv
dfarestas.to_csv("./edges_by_node_name.csv", index=False)
