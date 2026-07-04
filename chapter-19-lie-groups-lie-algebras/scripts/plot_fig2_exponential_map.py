"""fig2: 指数映射从切空间到群。"""
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
out = Path(__file__).resolve().parents[1] / "images" / "fig2_exponential_map.png"

t = np.linspace(0, 2*np.pi, 500)
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(np.cos(t), np.sin(t), color="#1A73E8", lw=3)
ax.plot([-2.7, -1.3], [0, 0], color="#D93025", lw=4)
for s in [-2.4, -2.0, -1.6]:
    angle = s + 2.7
    target = (np.cos(angle), np.sin(angle))
    ax.add_patch(FancyArrowPatch((s, 0.0), target, arrowstyle="-|>", mutation_scale=14,
                                 lw=1.8, color="#5F6368", alpha=0.7,
                                 connectionstyle="arc3,rad=0.15"))
ax.text(-2.05, 0.18, "Lie 代数", ha="center", color="#D93025", fontsize=13, fontweight="bold")
ax.text(0, -1.25, "Lie 群", ha="center", color="#1A73E8", fontsize=13, fontweight="bold")
ax.text(-0.55, 0.55, r"$\exp(tA)$", fontsize=14)
ax.set_xlim(-3, 1.4)
ax.set_ylim(-1.4, 1.4)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("指数映射：无穷小生成元产生有限变换", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
