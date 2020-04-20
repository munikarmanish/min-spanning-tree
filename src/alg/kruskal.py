"""
Kruskal's algorithm for minimum spanning tree.
"""

from ..ds import DisjointSet
from ..ds.heap import build_min_heap, min_heap_pop


def kruskal(G):
    """
    Find the minimim spanning tree of the given graph using Kruskal's algorithm.
    """
    # Initialize empty spanning tree (set of edges)
    mst_edges = set()

    # Create a disjoint set with all vertices as separate subsets
    ds = DisjointSet(G.nodes)

    # Create a heap of edges
    edges = [(w, (u, v)) for u, v, w in G.edges]
    build_min_heap(edges)

    # Loop until we have enough edges in the spanning tree
    N = len(G.nodes)    # number of vertices
    while len(mst_edges) < N-1:

        # Pick the edge with the smallest weight
        (u, v) = min_heap_pop(edges)[1]

        # Check if the edge creates a cycle. If not, merge the subsets
        # of u and v and add this edge to MST.
        u_root, v_root = ds.find(u), ds.find(v)
        if u_root != v_root:
            mst_edges.add((u, v))
            ds.union(u_root, v_root)

    return mst_edges
