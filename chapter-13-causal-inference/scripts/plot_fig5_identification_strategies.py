"""fig5: 工具变量与前门准则的识别结构。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig5_identification_strategies.png"


def node(ax, xy, label, color):
    circ = Circle(xy, 0.085, facecolor=color, edgecolor="white", lw=2, zorder=3)
    ax.add_patch(circ)
    ax.text(*xy, label, ha="center", va="center", color="white", fontsize=13, fontweight="bold")


def arrow(ax, start, end, color="#202124", dashed=False, curved=0.0):
    arr = FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=17,
                          color=color, lw=2.3, shrinkA=15, shrinkB=15,
                          linestyle="--" if dashed else "-",
                          connectionstyle=f"arc3,rad={curved}")
    ax.add_patch(arr)


fig, axes = plt.subplots(1, 2, figsize=(12, 5))
for ax in axes:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")

# IV
axes[0].set_title("工具变量：外生推动 X", fontsize=14, fontweight="bold")
node(axes[0], (0.18, 0.52), "Z", "#188038")
node(axes[0], (0.48, 0.52), "X", "#1A73E8")
node(axes[0], (0.78, 0.52), "Y", "#D93025")
node(axes[0], (0.62, 0.78), "U", "#9AA0A6")
arrow(axes[0], (0.27, 0.52), (0.39, 0.52))
arrow(axes[0], (0.57, 0.52), (0.69, 0.52))
arrow(axes[0], (0.58, 0.72), (0.51, 0.60), "#9AA0A6")
arrow(axes[0], (0.66, 0.72), (0.75, 0.60), "#9AA0A6")
axes[0].text(0.50, 0.18, "Z 只通过 X 影响 Y\n用 Z 提取 X 的外生变化", ha="center",
             fontsize=12, color="#5F6368")

# Front-door
axes[1].set_title("前门结构：通过中介 M 识别", fontsize=14, fontweight="bold")
node(axes[1], (0.20, 0.52), "X", "#1A73E8")
node(axes[1], (0.50, 0.52), "M", "#F9AB00")
node(axes[1], (0.80, 0.52), "Y", "#D93025")
node(axes[1], (0.50, 0.78), "U", "#9AA0A6")
arrow(axes[1], (0.29, 0.52), (0.41, 0.52))
arrow(axes[1], (0.59, 0.52), (0.71, 0.52))
arrow(axes[1], (0.44, 0.74), (0.26, 0.58), "#9AA0A6", dashed=True)
arrow(axes[1], (0.56, 0.74), (0.74, 0.58), "#9AA0A6", dashed=True)
axes[1].text(0.50, 0.18, "即使 X-Y 有未观测混杂\n仍可借助中介路径识别", ha="center",
             fontsize=12, color="#5F6368")

fig.suptitle("当后门调整不可用时，还可以寻找其他识别结构", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
