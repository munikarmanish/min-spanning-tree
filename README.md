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
run.py                      # run the algorithm on an input graph file
README.md                   # this file
report.pdf                  # project report
requirements.txt            # third-party python packages used
```

Command-line Usage
------------------

Make sure you have `python3` with `matplotlib` and `networkx`.

To run the MST algorithm on a graph:

    $ ./run.py graphs/small.graph

It will print the list of MST edges.

> Note: Graph files are simple text files containing list of edges (one per
> line). Each line contains 3 elements: source node, destination node,
> weight. See sample graphs in `graphs/` folder for examples.

For other functionalities (such as visualizing the graph), see:
`./run.py -h`.

Author
------

Manish Munikar<br>
UTA ID: 1001826846<br>
manish.munikar@mavs.uta.edu
