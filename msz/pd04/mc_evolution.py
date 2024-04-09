from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

from msz import set_plot_style

output_dir = Path(__file__).parent / "output"
set_plot_style()

step, E = np.loadtxt(output_dir / "m" / "0.7.err").T

plt.plot(step, E, "o-")

plt.annotate(
    text="pomiar",
    xy=(step.max(), E.max()),
    xytext=(-20, -60),
    textcoords="offset pixels",
    arrowprops=dict(arrowstyle="->"),
    horizontalalignment="center",
    verticalalignment="bottom",
)

plt.title("Konstrukcja ER, algorytm Metropolis, $N=1000$, $p=0.7$")
plt.xlabel("krok MC")
plt.ylabel("liczba krawędzi")

plt.savefig(Path(__file__).with_suffix(".pdf"))
plt.show()
