import networkx as nx
import matplotlib.pyplot as plt

# Crear grafo original con los promedios como pesos
edges = [
    ('Alan', 'Giovanni', (3.2 + 1.27) / 2),     # 2.24
    ('Andres', 'Marlene', (3.12 + 2.29) / 2),   # 2.71
    ('Alan', 'Marlene', (3.38 + 2.8) / 2),      # 3.09
    ('Marlene', 'Giovanni', (7.5 + 1.01) / 2),  # 4.26
    ('Andres', 'Giovanni', (8.5 + 1.02) / 2),   # 4.76
    ('Alan', 'Andres', (2.5 + 12.1) / 2),       # 7.3
]

G = nx.Graph()
G.add_weighted_edges_from(edges)

# Calcular el Árbol de Expansión Mínima (MST)
mst = nx.minimum_spanning_tree(G, algorithm='kruskal')

# Dibujar el grafo original en gris
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{d["weight"]:.2f}' for u, v, d in G.edges(data=True)})

# Dibujar el MST en rojo encima
nx.draw_networkx_edges(mst, pos, edge_color='red', width=3)

plt.title("Árbol de Expansión Mínima (Kruskal) sobre el Grafo Original")
plt.axis('off')
plt.show()