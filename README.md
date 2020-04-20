Minimum Spanning Tree
=====================

Minimum spanning tree (MST) of a weighted, connected and undirected graph is
the subgraph that is still connected and has the minimum possible total edge
weight. Minimum spanning trees have many useful applications. It is most
helpful in designing networks with minimum cost; network can be anything from
telecommunication cable networks, electrical grid networks, water supply
networks, computer networks, transportation networks, etc. For theoretical
discussion and analysis, see `report.pdf`.

This project implements two most popular MST algorithms: Kruskal's and Prim's
algorithms.

Project Structure
-----------------

```sh
graphs                      # sample input graphs
src/                        # main source tree
    alg/                    # algorithms
        kruskal.py          # Kruskal's algorithm implementation
        prim.py             # Prim's algorithm implementation
    ds/                     # data structures
        disjointset.py      # disjoint set implementation
        graph.py            # graph implementation
        heap.py             # heap implementation
    viz.py                  # visualization helper functions
kruskal.py                  # command-line tool to run Kruskal's algorithm
prim.py                     # command-lien tool to run Prim's algorithm
README.md                   # this file
report.pdf                  # project report
requirements.txt            # third-party python packages used
```

Command-line Usage
------------------

To run the MST algorithm on a graph:

- Kruskal's algorithm

      python3 kruskal.py graphs/small.graph

- Prim's algorithm

      python3 prim.py graphs/small.graph

Both commands will print the list of MST edges.

> Note: Graph files are simple text files containing list of edges (one per
> line). Each line contains 3 elements: source node, destination node,
> weight. See sample graphs in `graphs/` folder for examples.

Author
------

Manish Munikar<br>
UTA ID: 1001826846<br>
manish.munikar@mavs.uta.edu
