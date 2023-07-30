import networkx as nx
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

from dijkstra import Graph

plt.ion()

# Generate random vertices
n_vertices = random.randint(4, 7)
vertices = [v for v in range(n_vertices)]

# Create graph
original = nx.complete_graph(vertices)
for u, v in original.edges():
    weight = random.randint(1, 10)
    original[u][v]['weight'] = weight

result = nx.Graph()
result.add_nodes_from(vertices)

# Generate random node positions
pos = {v: (random.uniform(0, 10), random.uniform(0, 10)) for v in vertices}

# Running Dijkstra's algorithm
g = Graph(n_vertices)

for u, v in original.edges():
    w = original[u][v]['weight']
    g.addEdge(u, v, w)

resulting_edges = g.Dijkstra(0)

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

def update(frame):
    u, v, w = resulting_edges[frame]
    result.add_edge(u, v, weight=w)

    ax1.clear()
    ax2.clear()

    nx.draw_networkx(original, ax=ax1, pos=pos, with_labels=True, node_color='lightgreen', node_size=500, font_size=10)
    
    edge_labels = {(u, v): f"{original[u][v]['weight']:.2f}" for u, v in original.edges()}
    nx.draw_networkx_edge_labels(original, pos=pos, edge_labels=edge_labels, ax=ax1, font_size=8)
    
    ax1.set_title('Original', weight='bold')

    nx.draw_networkx(result, ax=ax2, pos=pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10)
    nx.draw_networkx_edges(result, pos=pos, edge_color="tab:red")
    
    edge_labels = {(u, v): f"{original[u][v]['weight']:.2f}" for u, v in result.edges()}
    nx.draw_networkx_edge_labels(result, pos=pos, edge_labels=edge_labels, ax=ax2, font_size=8)
    
    ax2.set_title('Shortest Paths (Dijkstra\'s Algorithm)', weight='bold')

    plt.pause(1)

ani = FuncAnimation(fig, update, frames=len(resulting_edges), repeat=False)

plt.ioff()
plt.show()