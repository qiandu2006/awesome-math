"""fig4: Markov blanket 屏蔽远处变量。"""
import math
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig4_markov_blanket.png"


def draw_node(ax, name, xy, color, radius=0.075):
    circ = Circle(xy, radius, facecolor=color, edgecolor="white", lw=2, zorder=3)
    ax.add_patch(circ)
    ax.text(xy[0], xy[1], name, ha="center", va="center", color="white",
            fontsize=13, fontweight="bold")


def draw_arrow(ax, start, end, color="#202124", alpha=1.0):
    dx, dy = end[0] - start[0], end[1] - start[1]
    length = math.hypot(dx, dy)
    ux, uy = dx / length, dy / length
    start = (start[0] + 0.075 * ux, start[1] + 0.075 * uy)
    end = (end[0] - 0.075 * ux, end[1] - 0.075 * uy)
    patch = FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=20,
                            lw=2, color=color, alpha=alpha, shrinkA=0, shrinkB=0, zorder=4)
    ax.add_patch(patch)


fig, ax = plt.subplots(figsize=(9, 6))
target = (0.50, 0.50)
parents = {"P1": (0.32, 0.75), "P2": (0.58, 0.78)}
children = {"C1": (0.36, 0.26), "C2": (0.66, 0.28)}
cosp = {"Q1": (0.17, 0.42), "Q2": (0.82, 0.47)}
far = {"A": (0.10, 0.83), "B": (0.91, 0.82), "D": (0.10, 0.14), "E": (0.90, 0.12)}

blanket_color = "#1A73E8"
target_color = "#D93025"
far_color = "#9AA0A6"

for name, xy in far.items():
    draw_node(ax, name, xy, far_color, 0.06)

for name, xy in parents.items():
    draw_node(ax, name, xy, blanket_color)
    draw_arrow(ax, xy, target)

for name, xy in children.items():
    draw_node(ax, name, xy, blanket_color)
    draw_arrow(ax, target, xy)

for name, xy in cosp.items():
    draw_node(ax, name, xy, blanket_color)

draw_arrow(ax, cosp["Q1"], children["C1"])
draw_arrow(ax, cosp["Q2"], children["C2"])
draw_arrow(ax, far["A"], parents["P1"], far_color, 0.55)
draw_arrow(ax, far["B"], parents["P2"], far_color, 0.55)
draw_arrow(ax, children["C1"], far["D"], far_color, 0.55)
draw_arrow(ax, children["C2"], far["E"], far_color, 0.55)

draw_node(ax, "X", target, target_color, 0.09)
ax.text(0.50, 0.91, "蓝色节点构成 X 的 Markov blanket", ha="center",
        fontsize=14, color=blanket_color, fontweight="bold")
ax.text(0.50, 0.06, "给定 blanket 后，远处灰色节点不再额外影响 X",
        ha="center", fontsize=13, color="#5F6368")
ax.set_title("Markov blanket：局部条件独立的屏障", fontsize=16, fontweight="bold")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
