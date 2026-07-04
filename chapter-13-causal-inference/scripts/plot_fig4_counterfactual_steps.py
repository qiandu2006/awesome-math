"""fig4: 反事实推理的三步：溯因、行动、预测。"""
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig4_counterfactual_steps.png"


def box(ax, xy, title, body, color):
    patch = FancyBboxPatch((xy[0] - 0.16, xy[1] - 0.18), 0.32, 0.36,
                           boxstyle="round,pad=0.02,rounding_size=0.025",
                           facecolor=color, edgecolor="white", lw=2)
    ax.add_patch(patch)
    ax.text(xy[0], xy[1] + 0.075, title, ha="center", va="center",
            fontsize=15, color="white", fontweight="bold")
    ax.text(xy[0], xy[1] - 0.055, body, ha="center", va="center",
            fontsize=11.5, color="white")


def arrow(ax, start, end):
    arr = FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=18,
                          color="#202124", lw=2.5, shrinkA=10, shrinkB=10)
    ax.add_patch(arr)


fig, ax = plt.subplots(figsize=(10, 4.8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

box(ax, (0.20, 0.55), "溯因", "用已发生事实\n推断 U", "#1A73E8")
box(ax, (0.50, 0.55), "行动", "替换方程\n执行 do(X=x')", "#D93025")
box(ax, (0.80, 0.55), "预测", "在新模型中\n计算 Y'", "#188038")
arrow(ax, (0.36, 0.55), (0.44, 0.55))
arrow(ax, (0.66, 0.55), (0.74, 0.55))
ax.text(0.50, 0.17, "反事实不是重新抽一个人，而是在同一个外生背景下改写机制",
        ha="center", fontsize=13, color="#5F6368")
ax.set_title("反事实推理：同一个世界背景下的另一个可能结果", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
