"""fig1: 相关、混杂与因果的三种图结构。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig1_correlation_confounding.png"


def draw_node(ax, xy, label, color):
    circle = Circle(xy, 0.11, facecolor=color, edgecolor="white", lw=2, zorder=3)
    ax.add_patch(circle)
    ax.text(*xy, label, ha="center", va="center", color="white", fontsize=15, fontweight="bold")


def draw_arrow(ax, start, end, color="#202124"):
    arr = FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=18,
                          color=color, lw=2.4, shrinkA=18, shrinkB=18)
    ax.add_patch(arr)


fig, axes = plt.subplots(1, 3, figsize=(13, 4.8))
titles = ["真正因果", "反向因果", "共同原因混杂"]
for ax, title in zip(axes, titles):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=14, fontweight="bold")

# X -> Y
draw_node(axes[0], (0.28, 0.55), "X", "#1A73E8")
draw_node(axes[0], (0.72, 0.55), "Y", "#D93025")
draw_arrow(axes[0], (0.39, 0.55), (0.61, 0.55))
axes[0].text(0.50, 0.24, "改变 X 会改变 Y", ha="center", fontsize=12, color="#5F6368")

# Y -> X
draw_node(axes[1], (0.28, 0.55), "X", "#1A73E8")
draw_node(axes[1], (0.72, 0.55), "Y", "#D93025")
draw_arrow(axes[1], (0.61, 0.55), (0.39, 0.55))
axes[1].text(0.50, 0.24, "X 只是结果的信号", ha="center", fontsize=12, color="#5F6368")

# Z -> X, Z -> Y
draw_node(axes[2], (0.25, 0.35), "X", "#1A73E8")
draw_node(axes[2], (0.75, 0.35), "Y", "#D93025")
draw_node(axes[2], (0.50, 0.75), "Z", "#188038")
draw_arrow(axes[2], (0.45, 0.66), (0.31, 0.44))
draw_arrow(axes[2], (0.55, 0.66), (0.69, 0.44))
axes[2].text(0.50, 0.12, "Z 同时推动 X 和 Y", ha="center", fontsize=12, color="#5F6368")

fig.suptitle("同一个相关性，可能来自不同因果结构", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
