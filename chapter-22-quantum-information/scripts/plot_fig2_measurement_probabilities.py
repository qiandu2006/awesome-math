"""fig2: Measurement probabilities in different bases."""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig2_measurement_probabilities.png"

theta = 0.62 * np.pi
phi = 0.28 * np.pi
alpha = np.cos(theta / 2)
beta = np.exp(1j * phi) * np.sin(theta / 2)
psi = np.array([alpha, beta], dtype=complex)

z_basis = [np.array([1, 0], dtype=complex), np.array([0, 1], dtype=complex)]
x_basis = [
    np.array([1, 1], dtype=complex) / np.sqrt(2),
    np.array([1, -1], dtype=complex) / np.sqrt(2),
]

z_probs = [abs(np.vdot(v, psi)) ** 2 for v in z_basis]
x_probs = [abs(np.vdot(v, psi)) ** 2 for v in x_basis]

fig, axes = plt.subplots(1, 2, figsize=(9, 4.8), sharey=True)
panels = [
    (axes[0], z_probs, [r"$|0\rangle$", r"$|1\rangle$"], "Z 基测量"),
    (axes[1], x_probs, [r"$|+\rangle$", r"$|-\rangle$"], "X 基测量"),
]
colors = ["#1A73E8", "#D93025"]

for ax, probs, labels, title in panels:
    bars = ax.bar(labels, probs, color=colors, alpha=0.88, width=0.56)
    for bar, prob in zip(bars, probs):
        ax.text(bar.get_x() + bar.get_width() / 2, prob + 0.025, f"{prob:.2f}", ha="center", fontsize=12)
    ax.set_ylim(0, 1.05)
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.grid(axis="y", alpha=0.25)
    ax.set_ylabel("概率")

fig.suptitle("同一个量子态，在不同测量基下给出不同概率", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
