from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

from msz import set_plot_style

output_dir = Path(__file__).parent / "output"
set_plot_style()


def k_trad(*, p: float):
    with open(output_dir / "t" / str(p)) as file:
        lines = file.readlines()
    return [len(line.split()) for line in lines]


def k_metr(*, p: float):
    with open(output_dir / "m" / str(p)) as file:
        lines = file.readlines()
    return [sum(map(int, line.split())) for line in lines]


def hist(*, ax, data):
    dx = 4

    bins_lin = np.arange(np.min(data), np.max(data) + dx, dx)
    [counts, bins] = np.histogram(data, bins=bins_lin)
    bins = bins[:-1]

    ax.plot(bins, counts, "o-")


fig, axs = plt.subplots(nrows=2, ncols=2)
[trad, metr] = axs

[left, right] = trad
hist(ax=left, data=k_trad(p=0.1))
left.set_title("tradycyjnie, $p=0.1$")
hist(ax=right, data=k_trad(p=0.7))
right.set_title("tradycyjnie, $p=0.7$")

[left, right] = metr
hist(ax=left, data=k_metr(p=0.1))
left.set_title("Metropolis, $10^7$ kroków, $p=0.1$")
hist(ax=right, data=k_metr(p=0.7))
right.set_title("Metropolis, $10^7$ kroków, $p=0.7$")

left.set_xlabel("$k$")
right.set_xlabel("$k$")

fig.suptitle("Porównanie algorytmów konstruowania ER, $N=1000$")
fig.tight_layout()
plt.savefig(Path(__file__).with_suffix(".pdf"))
plt.show()
