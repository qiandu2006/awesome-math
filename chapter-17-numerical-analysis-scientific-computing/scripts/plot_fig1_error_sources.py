"""fig1: 数值计算中的误差来源。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig1_error_sources.png"

fig, ax = plt.subplots(figsize=(12, 4.8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

labels = [
    ("真实系统", "建模误差", "#5F6368"),
    ("数学模型", "离散误差", "#1A73E8"),
    ("离散问题", "算法误差", "#F9AB00"),
    ("迭代算法", "舍入误差", "#D93025"),
    ("计算结果", "", "#188038"),
]
xpos = [0.10, 0.30, 0.50, 0.70, 0.90]
for x, (title, err, color) in zip(xpos, labels):
    box = FancyBboxPatch((x - 0.075, 0.45), 0.15, 0.18,
                         boxstyle="round,pad=0.02,rounding_size=0.02",
                         facecolor=color, edgecolor="white", lw=2)
    ax.add_patch(box)
    ax.text(x, 0.54, title, ha="center", va="center", color="white", fontsize=13, fontweight="bold")
for i in range(4):
    ax.add_patch(FancyArrowPatch((xpos[i] + 0.08, 0.54), (xpos[i + 1] - 0.08, 0.54),
                                 arrowstyle="-|>", mutation_scale=18, lw=2.5, color="#202124"))
    ax.text((xpos[i] + xpos[i + 1]) / 2, 0.70, labels[i][1], ha="center", fontsize=12, color="#202124")

ax.text(0.5, 0.22, "数值分析的目标不是消灭误差，而是让误差可理解、可控制、可估计",
        ha="center", fontsize=13, color="#5F6368")
ax.set_title("从真实系统到计算结果，每一步都会引入误差", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
