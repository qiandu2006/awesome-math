"""fig2: 一维固定点与稳定性。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig2_fixed_point_stability.png"

x = np.linspace(-2.4, 2.4, 500)
f = x - x**3
roots = np.array([-1.0, 0.0, 1.0])

fig, ax = plt.subplots(figsize=(9, 5.6))
ax.plot(x, f, color="#1A73E8", lw=3)
ax.axhline(0, color="#202124", lw=1.5)
ax.scatter(roots, np.zeros_like(roots), s=90, color=["#188038", "#D93025", "#188038"], zorder=5)

for start, end in [(-2.0, -1.15), (-0.25, -0.85), (0.25, 0.85), (2.0, 1.15)]:
    ax.annotate("", xy=(end, 0.18), xytext=(start, 0.18),
                arrowprops=dict(arrowstyle="->", lw=2.2, color="#5F6368"))

ax.text(-1.28, -0.42, "稳定", color="#188038", fontsize=12, fontweight="bold")
ax.text(-0.16, -0.42, "不稳定", color="#D93025", fontsize=12, fontweight="bold")
ax.text(0.78, -0.42, "稳定", color="#188038", fontsize=12, fontweight="bold")
ax.set_xlabel("x")
ax.set_ylabel(r"$\dot x = x-x^3$")
ax.set_title("固定点稳定性：附近箭头决定会靠近还是远离", fontsize=15, fontweight="bold")
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
