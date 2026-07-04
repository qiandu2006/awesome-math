"""fig4: 三个收敛定理的直觉位置。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig4_convergence_theorems.png"

x = np.linspace(0, 1, 500)
fig, axes = plt.subplots(1, 3, figsize=(14, 4.6), sharey=True)

for n, color in zip([2, 4, 8, 16], ["#AECBFA", "#78A8F8", "#1A73E8", "#174EA6"]):
    f = 1 - np.exp(-n * x)
    axes[0].plot(x, f, color=color, lw=2)
axes[0].set_title("单调收敛\n从下逼近", fontsize=13, fontweight="bold")

for n, color in zip([2, 4, 8, 16], ["#FAD2CF", "#F28B82", "#D93025", "#A50E0E"]):
    f = np.exp(-((x - 0.5) * n) ** 2)
    axes[1].plot(x, f, color=color, lw=2)
axes[1].set_title("Fatou 引理\n保留下界", fontsize=13, fontweight="bold")

g = 0.95 * np.ones_like(x)
axes[2].fill_between(x, -g, g, color="#E6F4EA", alpha=0.9, label="可积上界 g")
for n, color in zip([2, 4, 8, 16], ["#B7E1CD", "#81C995", "#188038", "#0B5724"]):
    f = np.sin(2 * np.pi * x) * np.exp(-n * (x - 0.5) ** 2) / 2
    axes[2].plot(x, f, color=color, lw=2)
axes[2].set_title("控制收敛\n被同一上界夹住", fontsize=13, fontweight="bold")

for ax in axes:
    ax.set_xlim(0, 1)
    ax.set_ylim(-1.05, 1.05)
    ax.set_xlabel("x")
    ax.grid(alpha=0.2)
axes[0].set_ylabel("$f_n(x)$")

fig.suptitle("积分与极限能否交换，取决于收敛结构", fontsize=16, fontweight="bold", y=1.05)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
