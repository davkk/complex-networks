from pathlib import Path

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
from common import bins_lin, deaths, hist

from msz import set_plot_style

set_plot_style()

[counts, x] = np.histogram(deaths, bins=bins_lin)

gs = gridspec.GridSpec(nrows=4, ncols=4)
fig = plt.figure()

ax1 = plt.subplot(gs[:2, :2])
hist(ax1, x[:-1], counts, label="$N(x)$")
ax1.set_title("liniowy")
ax1.set_xlabel("liczba ofiar")
ax1.legend()

ax2 = plt.subplot(gs[:2, 2:])
hist(ax2, x[:-1], counts, label="$N(x)$")
ax2.set_yscale("log")
ax2.set_xlabel("liczba ofiar")
ax2.set_title("lin-log")
ax2.legend()

ax3 = plt.subplot(gs[2:4, 1:3])
hist(ax3, x[:-1], counts, label="$N(x)$")
ax3.set_xscale("log")
ax3.set_yscale("log")
ax3.set_xlabel("liczba ofiar")
ax3.set_title("log-log")
ax3.legend()

fig.tight_layout()
plt.savefig(Path(__file__).with_suffix(".pdf"))
np.savetxt(
    Path(__file__).parent / "DK1.txt",
    np.column_stack((x[:-1], counts)),
)
# plt.show()
