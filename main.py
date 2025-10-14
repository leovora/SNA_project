import networkx as nx
import matplotlib.pyplot as plt

#G = nx.read_pajek("Strike.paj")
G = nx.read_gml("Dolphins.txt")
G = nx.Graph(G)

# Controlla i nodi e gli archi
print(G.nodes(data=True))
print(G.edges(data=True))

# Numero di nodi e archi
print(f"Nodi: {G.number_of_nodes()}, Archi: {G.number_of_edges()}")

# Calcolo centralità
centrality = nx.degree_centrality(G)
print(centrality)

# Visualizzazione semplice
nx.draw(G, with_labels=True, node_size=500)
plt.show()