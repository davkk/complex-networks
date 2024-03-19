from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

from msz import set_plot_style

output_dir = Path(__file__).parent / "output"
files = [
    output_dir / "p" / "N=100000_m=1",
    output_dir / "p" / "N=100000_m=2",
    output_dir / "r" / "N=100000_m=1",
    output_dir / "r" / "N=100000_m=2",
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


for idx, file in enumerate(files[:2]):
    ax = pref[idx]
    N, m = get_params(file)
    edges = np.loadtxt(file).T

    base = 2
    powers = np.arange(0, np.ceil(np.log2(edges.max())))
    x0 = edges[edges > 0].min()
    bins_log = np.power(np.full_like(powers, base), powers) * x0

    [counts, x] = np.histogram(edges, bins=bins_log)
    x = x[:-1]
    diffs = np.diff(bins_log)

    probability = counts / edges.size / diffs

    ax.plot(x, probability, "o", label="data points")
    ax.plot(x, 2 * m * m / np.power(x, 3), label="$P(k)=2m^2k^{-3}$", c="gray")
    ax.set_xscale("log")
    ax.set_yscale("log")
    if idx == 0:
        ax.set_ylabel("$P(k)$")

for idx, file in enumerate(files[2:]):
    ax = rand[idx]
    N, m = get_params(file)
    edges = np.loadtxt(file).T

    dx = edges.min()
    bins_lin = np.arange(edges.min(), edges.max() + dx, dx)
    [counts, x] = np.histogram(edges, bins=bins_lin)
    x = x[:-1]
    probability = counts / edges.size / dx

    ax.plot(x, probability, "o", label="data points")
    ax.set_yscale("log")
    ax.set_xlabel("$k$")
    if idx == 0:
        ax.set_ylabel("$P(k)$")

for idx, file in enumerate(files):
    ax = axs[idx // 2, idx % 2]
    N, m = get_params(file)

    ax.set_title(f"{attach[file.parent.name]}, ${N=}$, ${m=}$")
    ax.legend()

fig.suptitle("Comparison of different attachment methods")
fig.tight_layout()
plt.savefig(Path(__file__).with_suffix(".pdf"))
plt.show()
