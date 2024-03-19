from pathlib import Path

import networkx as nx
from matplotlib import pyplot as plt

from msz import set_plot_style

output_dir = Path(__file__).parent / "output"
files = [
    output_dir / "p" / "N=100_m=1.err",
    output_dir / "p" / "N=100_m=2.err",
    output_dir / "r" / "N=100_m=1.err",
    output_dir / "r" / "N=100_m=2.err",
]
attach = dict(r="random attach.", p="preferential attach.")

set_plot_style()

fig, axs = plt.subplots(nrows=2, ncols=2)

for arg, file in enumerate(files):
    ax = axs[arg // 2, arg % 2]
    with open(file) as f:
        adjlist = {
            idx: map(int, line.split())
            for idx, line in enumerate(f.readlines())
        }
        graph = nx.from_dict_of_lists(adjlist)  # type: ignore
        degs = dict(nx.degree(graph))

        nx.draw(
            graph,
            nodelist=degs.keys(),
            node_size=[v * 50 for v in degs.values()],
            ax=ax,
            pos=nx.kamada_kawai_layout(graph),
            edgecolors="black",
        )

        parts = file.stem.split("_")
        N = int(parts[0].split("=")[1])
        m = int(parts[1].split("=")[1])
        ax.set_title(f"{attach[file.parent.name]}, ${N=}$, ${m=}$")


fig.suptitle("Generated BA graphs")
fig.tight_layout()
plt.savefig(Path(__file__).with_suffix(".pdf"))
plt.show()
