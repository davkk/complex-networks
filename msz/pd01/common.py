import numpy as np


def hist(ax, *args, **kwargs):
    ax.plot(*args, linestyle="", marker=".", **kwargs)


names, deaths = np.genfromtxt("./data/wars.txt", delimiter="\t", dtype=str).T
names = names[1:]
deaths = deaths[1:].astype(int)

dx = deaths.min()
bins_lin = range(deaths.min(), deaths.max() + dx, dx)

base = 2
powers = np.arange(0, np.ceil(np.log2(deaths.max() / deaths.min())) + 1)
bins_log = np.power(np.full_like(powers, base), powers) * deaths.min()
