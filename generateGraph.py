import random
import networkx as nx
import matplotlib.pyplot as plt

def generate(n):

    # Create a 100x100 adjacency matrix initialized with 0s
    graph = [[0] * n for _ in range(n)]

    # Define edge probability (e.g., 20% chance of an edge existing between two nodes)
    edge_probability = 0.2

    # Populate the adjacency matrix with random weights
    for i in range(n):
        for j in range(i + 1, n):  # Ensure j > i to avoid self-loops and duplicate edges
            if random.random() < edge_probability:
                # Random weight between 1 and 10
                weight = random.randint(1, 10)
                graph[i][j] = weight
                graph[j][i] = weight  # Since this is an undirected graph

    return graph


def visualize_graph(graph):
    G = nx.Graph()

    # Add nodes
    num_nodes = len(graph)
    G.add_nodes_from(range(num_nodes))

    # Add edges based on the adjacency matrix
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):  # Only consider upper triangular matrix to avoid duplicates
            if graph[i][j] != 0:  # If there is an edge
                G.add_edge(i, j, weight=graph[i][j])

    # Get edge weights for visualization
    edges = G.edges(data=True)
    edge_weights = [edge[2]['weight'] for edge in edges]

    # Draw the graph
    plt.figure(figsize=(8, 8))
    pos = nx.spring_layout(G, seed=42)  # Spring layout for better visualization

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='skyblue')

    # Draw edges with thickness based on weights
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=1)

    # Draw edge labels (weights)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): f'{w["weight"]}' for i, j, w in edges})

    # Draw node labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

    plt.title('Graph Visualization from Adjacency Matrix')
    plt.show()