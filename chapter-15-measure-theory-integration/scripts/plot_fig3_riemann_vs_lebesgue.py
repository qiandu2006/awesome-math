"""fig3: Riemann 与 Lebesgue 积分的切分方式。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig3_riemann_vs_lebesgue.png"

x = np.linspace(0, 1, 500)
f = 0.15 + 0.65 * np.exp(-((x - 0.32) / 0.16) ** 2) + 0.35 * np.exp(-((x - 0.75) / 0.09) ** 2)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(x, f, color="#202124", lw=2.5)
for a in np.linspace(0, 0.9, 10):
    b = a + 0.1
    mid = (a + b) / 2
    height = np.interp(mid, x, f)
    axes[0].add_patch(plt.Rectangle((a, 0), 0.1, height, facecolor="#AECBFA", edgecolor="#1A73E8", alpha=0.65))
axes[0].set_title("Riemann：切横轴", fontsize=14, fontweight="bold")
axes[0].set_xlabel("x")
axes[0].set_ylabel("f(x)")
axes[0].set_xlim(0, 1)
axes[0].set_ylim(0, 1.05)
axes[0].grid(alpha=0.2)

axes[1].plot(x, f, color="#202124", lw=2.5)
levels = np.linspace(0.15, 0.9, 7)
for i in range(len(levels) - 1):
    lo, hi = levels[i], levels[i + 1]
    mask = (f >= lo) & (f < hi)
    axes[1].fill_between(x, lo, hi, where=mask, color=plt.cm.viridis(i / 6), alpha=0.55)
axes[1].set_title("Lebesgue：切函数值", fontsize=14, fontweight="bold")
axes[1].set_xlabel("x")
axes[1].set_ylabel("f(x)")
axes[1].set_xlim(0, 1)
axes[1].set_ylim(0, 1.05)
axes[1].grid(alpha=0.2)

fig.suptitle("两种积分直觉：按位置累加 vs 按函数值分层", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
