"""
Implementation of Graph data structure and various graph functions.
"""

import random

import networkx as nx


class Graph:
    """
    Undirected graph data structure. It maintains a list of nodes and edges.
    """

    def __init__(self, nodes=None, edges=None):
        """
        Initialize the graph with given nodes and edges. Graph is stored
        internally as adjacency lists.
        """
        self.graph = {}
        if nodes:
            self.add_nodes(nodes)
        if edges:
            self.add_edges(edges)

    def __repr__(self):
        return repr(self.graph)

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, node):
        return self.graph[node]

    def add_node(self, node):
        """
        Add a node to the graph.
        """
        if node not in self.graph:
            self.graph[node] = {}

    def add_nodes(self, nodes):
        """
        Add multiple nodes to the graph.
        """
        for node in nodes:
            self.add_node(node)

    def add_edge(self, a, b, weight=1):
        """
        Add an edge to the graph.
        """
        assert a != b  # no self-loops allowed
        self.add_nodes([a, b])
        self.graph[a][b] = self.graph[b][a] = weight

    def add_edges(self, edges):
        """
        Add multiple edges to the graph.
        """
        for edge in edges:
            self.add_edge(*edge)

    @property
    def nodes(self):
        """
        Return the list of nodes as a python set.
        """
        return set(self.graph.keys())

    @property
    def edges(self):
        """
        Return the list of edges as a python set of 3-tuples (from, to, weight).
        """
        E = set()
        for a, adj in self.graph.items():
            for b, w in adj.items():
                if a < b:
                    E.add((a, b, w))
                else:
                    E.add((b, a, w))
        return E

    def depth_first_traversal(self, node, f=None, visited=None):
        """
        Depth-first traversal with the given start node.

        Args:
            node:       Starting node
            f:          Function to execute for every visited node
            visited:    Set of visited nodes (will be initialized empty if
                        not given)
        """
        if visited is None:
            visited = set()
        visited.add(node)
        if f:
            f(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.depth_first_traversal(neighbor, f=f, visited=visited)

    def breadth_first_traversal(self, node, f=None, visited=None):
        """
        Breadth-first traversal with the given start node.

        Args:
            node:       Starting node
            f:          Function to execute for every visited node
            visited:    Set of visited nodes (will be initialized empty if
                        not given)
        """
        visited = set() if visited is None else visited
        queue = []
        queue.append(node)
        visited.add(node)
        while queue:  # O(V)
            node = queue.pop(0)
            if f:
                f(node)
            for neighbor in self.graph[node]:  # O(E)
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def is_connected(self):
        """
        Returns true if the graph is connected.
        """
        if not self.graph:
            return True
        visited = set()
        root = list(self.graph.keys())[0]
        self.breadth_first_traversal(root, visited=visited)
        return len(visited) == len(self.graph)

    @classmethod
    def from_nx(cls, graph):
        """
        Convert graph from networkx format.
        """
        G = cls()
        G.add_nodes(graph.nodes)
        G.add_edges([(u, v, data.get("weight", 1))
                     for u, v, data in graph.edges(data=True)])
        return G

    def to_nx(self):
        """
        Convert graph to networkx format.
        """
        G = nx.Graph()
        G.add_nodes_from(self.nodes)
        G.add_weighted_edges_from(self.edges)
        return G

    def to_file(self, filename):
        """
        Save the graph as edge-list in a text file.
        """
        with open(filename, "w") as f:
            for u, v, w in self.edges:
                f.write(f"{u} {v} {w}\n")

    @classmethod
    def from_file(cls, filename):
        """
        Read the graph from a file.
        """
        with open(filename, "r") as f:
            G = cls()
            for line in f.readlines():
                u, v, w = line.split()
                w = int(w)
                G.add_edge(u, v, w)
            return G


def generate_random_connected_graph(n, p=None):
    """
    Generates a random graph with given number of edges and edge probability.

    Args:
        n:  Number of vertices
        p:  Probability of edge existing between any pair of vertices

    Returns a graph object.
    """
    probs = [0.01, 0.05, 0.1, 0.2, 0.3, 0.4]
    if p is not None:
        probs = [p]
    for p in probs:
        G = nx.erdos_renyi_graph(n=n, p=p)
        if nx.is_connected(G):
            for _u, _v, d in G.edges(data=True):
                d["weight"] = random.randint(1, 15)
            return Graph.from_nx(G)
