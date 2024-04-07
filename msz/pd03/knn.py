from pathlib import Path

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

from msz import set_plot_style

output_dir = Path(__file__).parent / "output"
files = [
    output_dir / "p" / "N=100000_m=1.err",
    output_dir / "p" / "N=100000_m=2.err",
    output_dir / "r" / "N=100000_m=1.err",
    output_dir / "r" / "N=100000_m=2.err",
]
attach = dict(r="random attach.", p="preferential attach.")

set_plot_style()

fig, axs = plt.subplots(nrows=2, ncols=2)
[pref, rand] = axs


def get_params(file: Path):
    parts = file.stem.split("_")
    N = int(parts[0].split("=")[1])
    m = int(parts[1].split("=")[1])
    return N, m


for arg, file in enumerate(files):
    ax = axs[arg // 2, arg % 2]


for idx, file in enumerate(files[:2]):
    ax = pref[idx]
    N, m = get_params(file)
    with open(file) as f:
        adjlist = {
            idx: map(int, line.split())
            for idx, line in enumerate(f.readlines())
        }
        graph = nx.from_dict_of_lists(adjlist)  # type: ignore

    knn = np.array(list(nx.average_neighbor_degree(graph).values()))

    base = 2
    powers = np.arange(0, np.ceil(np.log2(knn.max())))
    x0 = np.sort(knn[knn > 0])[4]
    bins_log = np.power(np.full_like(powers, base), powers) * x0

    [counts, bins] = np.histogram(knn, bins=bins_log)
    bins = bins[:-1]

    ax.plot(bins, counts, "o-")
    # ax.set_xscale("log")
    # ax.set_yscale("log")
    if idx == 0:
        ax.set_ylabel(r"$\left<{k}\right>(k)$")

for idx, file in enumerate(files[2:]):
    ax = rand[idx]
    N, m = get_params(file)
    with open(file) as f:
        adjlist = {
            idx: map(int, line.split())
            for idx, line in enumerate(f.readlines())
        }
        graph = nx.from_dict_of_lists(adjlist)  # type: ignore

    knn = list(nx.average_neighbor_degree(graph).values())

    dx = 1
    bins_lin = np.arange(np.min(knn), np.max(knn) + dx, dx)
    [counts, bins] = np.histogram(knn, bins=bins_lin)
    bins = bins[:-1]

    ax.plot(bins, counts, "o-")
    # ax.set_yscale("log")
    ax.set_xlabel("$k$")
    if idx == 0:
        ax.set_ylabel(r"$\left<{k}\right>(k)$")

for idx, file in enumerate(files):
    ax = axs[idx // 2, idx % 2]
    N, m = get_params(file)

    ax.set_title(f"{attach[file.parent.name]}, ${N=}$, ${m=}$")

fig.suptitle("Average degree distribution")
fig.tight_layout()
# plt.savefig(Path(__file__).with_suffix(".pdf"))
plt.show()
