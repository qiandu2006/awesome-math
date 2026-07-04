"""fig1: 测度统一长度、面积和概率。"""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig1_measure_unifies_size.png"

fig, axes = plt.subplots(1, 3, figsize=(13, 4.5))
for ax in axes:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")

axes[0].plot([0.12, 0.88], [0.5, 0.5], color="#202124", lw=3)
axes[0].plot([0.28, 0.68], [0.5, 0.5], color="#1A73E8", lw=8, solid_capstyle="round")
axes[0].text(0.48, 0.62, "长度", ha="center", fontsize=14, fontweight="bold", color="#1A73E8")
axes[0].text(0.50, 0.25, r"$\mu([a,b])=b-a$", ha="center", fontsize=13, color="#5F6368")

axes[1].add_patch(Rectangle((0.18, 0.20), 0.62, 0.55, facecolor="#E8F0FE", edgecolor="#1A73E8", lw=2))
axes[1].add_patch(Circle((0.50, 0.48), 0.18, facecolor="#1A73E8", alpha=0.55, edgecolor="none"))
axes[1].text(0.50, 0.82, "面积", ha="center", fontsize=14, fontweight="bold", color="#1A73E8")
axes[1].text(0.50, 0.08, r"$\mu(A)$ 给区域大小", ha="center", fontsize=13, color="#5F6368")

bars = [0.18, 0.32, 0.14, 0.24]
xs = np.arange(len(bars))
axes[2].bar(xs, bars, color=["#1A73E8", "#188038", "#F9AB00", "#D93025"])
axes[2].set_xlim(-0.7, 3.7)
axes[2].set_ylim(0, 0.42)
axes[2].axis("on")
axes[2].spines[["top", "right"]].set_visible(False)
axes[2].set_xticks(xs, ["a", "b", "c", "d"])
axes[2].set_yticks([])
axes[2].set_title("概率", fontsize=14, fontweight="bold", color="#1A73E8")
axes[2].text(1.5, -0.12, r"$P(A)$ 给事件大小", ha="center", fontsize=13,
             color="#5F6368", transform=axes[2].transData)

fig.suptitle("测度：给集合赋予大小的统一语言", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
