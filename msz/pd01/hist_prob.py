from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from common import bins_lin, deaths, dx, hist

from msz import set_plot_style

set_plot_style()

[counts, x] = np.histogram(deaths, bins=bins_lin)
probability = counts / deaths.size / dx

hist(plt, x[:-1], probability, label="$P(x)$")
plt.xscale("log")
plt.yscale("log")

plt.xlabel("liczba ofiar")

plt.legend()
plt.tight_layout()
plt.savefig(Path(__file__).with_suffix(".pdf"))
np.savetxt(
    Path(__file__).parent / "DK2.txt",
    np.column_stack((x[:-1], counts)),
)
# plt.show()
