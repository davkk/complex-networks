from pathlib import Path

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

output_dir = Path(__file__).parent / "output"
files = [
    # output_dir / "p" / "N=100000_m=1.err",
    output_dir / "p" / "N=100000_m=2.err",
    # output_dir / "r" / "N=100000_m=1.err",
    # output_dir / "r" / "N=100000_m=2.err",
]
attach = dict(r="random attach.", p="preferential attach.")


def get_params(file: Path):
    parts = file.stem.split("_")
    N = int(parts[0].split("=")[1])
    m = int(parts[1].split("=")[1])
    return N, m


for file in files:
    N, m = get_params(file)
    with open(file) as f:
        adjlist = {
            idx: map(int, line.split())
            for idx, line in enumerate(f.readlines())
        }
        graph = nx.from_dict_of_lists(adjlist)  # type: ignore

    knn = list(nx.average_neighbor_degree(graph).values())
    print(N, m)

    # adjlist = list(nx.to_dict_of_lists(nx.barabasi_albert_graph(N, m)).values())

    # knn = list(nx.average_neighbor_degree(nx.barabasi_albert_graph(N, m)).values())

    # knn = [np.mean(edges) for edges in adjlist]

    counts, bins = np.histogram(knn, bins=50)
    bins = bins[:-1]
    plt.plot(bins, counts, ".")
    plt.show()
    break
