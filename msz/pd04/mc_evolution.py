from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

from msz import set_plot_style

output_dir = Path(__file__).parent / "output"
set_plot_style()

ps = [0.1, 0.7]

fig, axs = plt.subplots(2, 1, sharex=True)

for p in ps:
    ax = axs[ps.index(p)]

    step, E = np.loadtxt(output_dir / "m" / f"{p}.err").T

    ax.plot(step, E, "o-")

    ax.annotate(
        text="pomiar",
        xy=(step.max(), E.max()),
        xytext=(-20, -60),
        textcoords="offset pixels",
        arrowprops=dict(arrowstyle="->"),
        horizontalalignment="center",
        verticalalignment="bottom",
    )

    ax.set_title(f"Konstrukcja ER, algorytm Metropolis, $N=1000$, ${p=}$")
    ax.set_xlabel("krok MC")
    ax.set_ylabel("liczba krawędzi")

fig.tight_layout()
plt.savefig(Path(__file__).with_suffix(".pdf"))
plt.show()
