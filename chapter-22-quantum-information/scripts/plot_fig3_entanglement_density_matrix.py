"""fig3: Density matrix of a Bell state."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig3_entanglement_density_matrix.png"

psi = np.array([1, 0, 0, 1], dtype=float) / np.sqrt(2)
rho = np.outer(psi, psi)
labels = [r"$|00\rangle$", r"$|01\rangle$", r"$|10\rangle$", r"$|11\rangle$"]

fig, ax = plt.subplots(figsize=(7.2, 6.2))
im = ax.imshow(rho, cmap="Blues", vmin=0, vmax=0.55)

for i in range(4):
    for j in range(4):
        value = rho[i, j]
        color = "white" if value > 0.35 else "#202124"
        ax.text(j, i, f"{value:.1f}", ha="center", va="center", fontsize=13, color=color, fontweight="bold")

ax.set_xticks(range(4))
ax.set_yticks(range(4))
ax.set_xticklabels(labels)
ax.set_yticklabels(labels)
ax.set_xlabel("列状态")
ax.set_ylabel("行状态")
ax.set_title(r"Bell 态 $|\Phi^+\rangle$ 的密度矩阵", fontsize=16, fontweight="bold")
ax.text(1.5, 4.55, "对角项给出概率；非对角项保留相干与纠缠信息", ha="center", fontsize=12, color="#5F6368")

cbar = fig.colorbar(im, ax=ax, shrink=0.78)
cbar.set_label("矩阵元素")

plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
