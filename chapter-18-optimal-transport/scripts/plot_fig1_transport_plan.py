"""fig1: 从一个分布搬运到另一个分布。"""
import os
from pathlib import Path
import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
out = Path(__file__).resolve().parents[1] / "images" / "fig1_transport_plan.png"

x = np.linspace(-4, 4, 500)
p = np.exp(-(x + 1.3) ** 2 / 0.7)
q = 0.65 * np.exp(-(x - 1.1) ** 2 / 0.9) + 0.45 * np.exp(-(x - 2.2) ** 2 / 0.35)
p /= np.trapezoid(p, x)
q /= np.trapezoid(q, x)

fig, ax = plt.subplots(figsize=(9, 5.5))
ax.plot(x, p, color="#1A73E8", lw=3, label="源分布 μ")
ax.plot(x, q, color="#D93025", lw=3, label="目标分布 ν")
for a, b, h in [(-1.7, 0.8, 0.28), (-1.1, 1.5, 0.22), (-0.5, 2.4, 0.16)]:
    ax.add_patch(FancyArrowPatch((a, h), (b, h), arrowstyle="-|>", mutation_scale=18,
                                 lw=2.2, color="#5F6368", alpha=0.75,
                                 connectionstyle="arc3,rad=0.18"))
ax.set_title("最优传输：把源分布的质量搬到目标分布", fontsize=15, fontweight="bold")
ax.set_xlabel("x")
ax.set_ylabel("密度")
ax.grid(alpha=0.25)
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
