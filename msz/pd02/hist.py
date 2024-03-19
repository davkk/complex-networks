import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

file = sys.argv[1]
m = int(sys.argv[2])

edges = np.loadtxt(file).T

base = 2
powers = np.arange(0, np.ceil(np.log2(edges.max())) + 1)
bins_log = np.power(np.full_like(powers, base), powers)

[counts, x] = np.histogram(edges, bins=bins_log)
x = x[:-1]
diffs = np.diff(bins_log)

probability = counts / edges.size / diffs

plt.plot(x, probability, linestyle="", marker=".", label="data points")
plt.plot(x, 2 * m * m / np.power(x, 3), label="$P(k)=2m^2k^{-3}$")
plt.xlabel("$k$")
plt.ylabel("$P(k)$")
plt.xscale("log")
plt.yscale("log")
plt.legend()

plt.tight_layout()
plt.savefig(Path(__file__).with_suffix(".pdf"))

plt.show()
