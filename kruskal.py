#!/usr/bin/env python3

import sys

from src.alg.kruskal import kruskal
from src.ds.graph import Graph


def abort(msg, code=1):
    print(msg, file=sys.stderr)
    sys.exit(code)


def main():
    # check for arguments
    if len(sys.argv) != 2:
        abort(f"Usage: {sys.argv[0]} <graph-file>")

    # load the graph
    try:
        G = Graph.from_file(sys.argv[1])
    except Exception:
        abort("Error reading graph file")

    # run the algorithm
    mst = kruskal(G)

    # display the result MST edges
    for (u, v) in mst:
        print(u, v)


if __name__ == "__main__":
    main()
