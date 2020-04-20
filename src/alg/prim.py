"""
Implementation of the Prim's algorithm to find the minimum spanning tree
(MST) of a graph.
"""

from ..ds.heap import Heap


def prim(G, root=None):
    """
    Find the minimim spanning tree of a graph using Prim's algorithm. If root
    is given, use it as the starting node.

    Args:
        G:      The graph object
        root:   Starting vertex

    Returns: A list of MST edges, where each edge is a 2-tuple of vertices
    """

    # Initialize a priority queue of vertices with all costs as inf
    nodes = Heap([(float("inf"), n) for n in G.nodes])

    # Initiaize parents of all vertices as None
    parent = {n: None for n in G.nodes}

    # If starting vertex is provided, set its priority to 0
    if root:
        nodes[root] = 0

    # Initialize an empty set of MST edges
    mst_edges = set()

    # Loop until the priority queue is empty
    while nodes:

        # Remove the node with minimum cost
        node = nodes.pop()[0]

        # If its parent is not one, add the edge (parent, node) to MST
        if parent[node] is not None:
            mst_edges.add((parent[node], node))

        # Update the costs and parents of its neighbors in the queue
        for neigh, weight in G[node].items():
            if neigh in nodes and weight < nodes[neigh]:
                nodes[neigh] = weight
                parent[neigh] = node

    return mst_edges
