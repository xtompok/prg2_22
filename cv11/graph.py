import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(1)
G.add_node(2)
G.add_edge(1,2,weight=1)
G.add_edge(2,3,weight=30)

#print(nx.info(G))
print(f"Vrcholu: {len(G.nodes)}")
print(f"Hran: {len(G.edges)}")

print(G.edges[(1,2)]['weight'])

nx.draw(G,with_labels=True)
plt.show()
