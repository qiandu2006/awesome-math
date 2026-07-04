"""fig2: 条件化与干预的图操作差别。"""
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig2_observation_vs_intervention.png"


def node(ax, xy, label, color):
    circ = Circle(xy, 0.09, facecolor=color, edgecolor="white", lw=2, zorder=3)
    ax.add_patch(circ)
    ax.text(*xy, label, ha="center", va="center", color="white", fontsize=14, fontweight="bold")


def arrow(ax, start, end, color="#202124", dashed=False):
    arr = FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=18,
                          color=color, lw=2.4, shrinkA=16, shrinkB=16,
                          linestyle="--" if dashed else "-")
    ax.add_patch(arr)


fig, axes = plt.subplots(1, 2, figsize=(11, 5))
for ax in axes:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")

for ax, title in zip(axes, ["观察：条件化在 X=x", "干预：do(X=x)"]):
    ax.set_title(title, fontsize=14, fontweight="bold")
    node(ax, (0.50, 0.78), "Z", "#188038")
    node(ax, (0.30, 0.38), "X", "#1A73E8")
    node(ax, (0.72, 0.38), "Y", "#D93025")
    arrow(ax, (0.45, 0.70), (0.34, 0.47))
    arrow(ax, (0.55, 0.70), (0.68, 0.47))
    arrow(ax, (0.40, 0.38), (0.62, 0.38))

axes[0].text(0.30, 0.18, "筛选自然发生的 X=x\nZ 的信息仍在 X 中", ha="center",
             fontsize=12, color="#5F6368")

# cover incoming arrow to X in intervention panel with a cut mark
axes[1].plot([0.36, 0.45], [0.56, 0.61], color="white", lw=8, solid_capstyle="round", zorder=4)
axes[1].plot([0.36, 0.45], [0.56, 0.61], color="#D93025", lw=3, zorder=5)
axes[1].plot([0.36, 0.45], [0.61, 0.56], color="#D93025", lw=3, zorder=5)
axes[1].text(0.30, 0.18, "剪断 Z→X\n把 X 的机制替换为常数", ha="center",
             fontsize=12, color="#5F6368")

fig.suptitle("条件化是在筛选世界；干预是在改造世界", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
