"""fig3: 有向图模型与联合分布分解。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig3_graphical_model_factorization.png"


def node(ax, xy, title, subtitle, color):
    circ = Circle(xy, 0.10, facecolor=color, edgecolor="white", lw=2, zorder=3)
    ax.add_patch(circ)
    ax.text(xy[0], xy[1] + 0.015, title, ha="center", va="center", fontsize=16,
            color="white", fontweight="bold")
    ax.text(xy[0], xy[1] - 0.20, subtitle, ha="center", va="center", fontsize=12,
            color="#202124")


def arrow(ax, start, end):
    dx, dy = end[0] - start[0], end[1] - start[1]
    length = math.hypot(dx, dy)
    ux, uy = dx / length, dy / length
    start = (start[0] + 0.105 * ux, start[1] + 0.105 * uy)
    end = (end[0] - 0.105 * ux, end[1] - 0.105 * uy)
    patch = FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=18,
                            lw=2.5, color="#202124", shrinkA=0, shrinkB=0, zorder=4)
    ax.add_patch(patch)


fig, ax = plt.subplots(figsize=(10, 6))
pos = {
    "R": (0.25, 0.70),
    "S": (0.62, 0.70),
    "W": (0.45, 0.34),
}
node(ax, pos["R"], "R", "下雨", "#1A73E8")
node(ax, pos["S"], "S", "喷淋器", "#F9AB00")
node(ax, pos["W"], "W", "草地湿", "#188038")
arrow(ax, pos["R"], pos["S"])
arrow(ax, pos["R"], pos["W"])
arrow(ax, pos["S"], pos["W"])

ax.text(0.72, 0.46, r"$p(R,S,W)$" + "\n" + r"$=p(R)p(S\mid R)p(W\mid R,S)$",
        fontsize=19, color="#202124", va="center")
ax.text(0.50, 0.08, "图结构把一个联合分布拆成局部条件概率",
        ha="center", fontsize=14, color="#5F6368")
ax.set_title("有向概率图模型：联合分布的局部分解", fontsize=16, fontweight="bold")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
