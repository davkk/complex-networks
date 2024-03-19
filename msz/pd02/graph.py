import sys

import matplotlib.pyplot as plt
import networkx as nx

file = sys.argv[1]

with open(file) as f:
    edgelist = []
    idx = 0
    while line := f.readline():
        for edge in map(int, line.split()):
            edgelist.append((idx, edge))
        idx += 1

    graph = nx.from_edgelist(edgelist)
    d = dict(nx.degree(graph))
    nx.draw(
        graph,
        nodelist=d.keys(),
        node_size=[v * 100 for v in d.values()],
    )
    plt.show()
