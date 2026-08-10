"""一维金属棒微元的流入、流出与内能增加。"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(ROOT / ".mplconfig"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = ROOT / "images" / "heat_control_volume.png"
DARK = "#243447"
BLUE = "#2F80ED"
ORANGE = "#F2994A"
GREEN = "#219653"

fig, ax = plt.subplots(figsize=(11, 5.2), facecolor="white")
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-2.0, 3.0)
ax.axis("off")

# 整根棒与被截取的小段
ax.add_patch(Rectangle((0.3, 0.15), 9.4, 1.35, facecolor="#EEF2F6", edgecolor=DARK, lw=1.2))
x_left, x_right = 3.4, 6.7
ax.add_patch(Rectangle((x_left, 0.15), x_right - x_left, 1.35,
                       facecolor="#FFF0D5", edgecolor=ORANGE, lw=2.2))
ax.plot([x_left, x_left], [0.0, 1.66], color=ORANGE, lw=2)
ax.plot([x_right, x_right], [0.0, 1.66], color=ORANGE, lw=2)
ax.text((x_left + x_right) / 2, 0.84, "控制体（小棒段）", ha="center", va="center",
        fontsize=14, color=DARK, weight="bold")

# q 定义为沿 +x，因此两端箭头都向右；相减来自一入一出
ax.add_patch(FancyArrowPatch((1.45, 1.92), (x_left - 0.03, 1.92), arrowstyle="-|>", mutation_scale=19,
                             lw=3.2, color=BLUE))
ax.text(2.25, 2.28, r"流入功率 $S q(x,t)$", ha="center", fontsize=13, color=BLUE, weight="bold")
ax.add_patch(FancyArrowPatch((x_right + 0.03, 1.92), (9.0, 1.92), arrowstyle="-|>", mutation_scale=19,
                             lw=3.2, color=GREEN))
ax.text(8.05, 2.28, r"流出功率 $S q(x+\Delta x,t)$", ha="center", fontsize=13, color=GREEN, weight="bold")

# 正方向与区间宽度
ax.add_patch(FancyArrowPatch((0.8, -0.32), (2.3, -0.32), arrowstyle="-|>", mutation_scale=13,
                             lw=1.5, color="#667085"))
ax.text(1.52, -0.63, "x 正方向", ha="center", fontsize=10.5, color="#667085")
ax.annotate("", xy=(x_left, -0.50), xytext=(x_right, -0.50),
            arrowprops=dict(arrowstyle="|-|", lw=1.5, color=ORANGE))
ax.text((x_left + x_right) / 2, -0.86, r"长度 $\Delta x$，体积 $S\Delta x$", ha="center", fontsize=12, color=ORANGE)
ax.text(x_left, -0.05, r"$x$", ha="center", va="top", fontsize=12, color=DARK)
ax.text(x_right, -0.05, r"$x+\Delta x$", ha="center", va="top", fontsize=12, color=DARK)

# 守恒的核心等式
ax.text(5.05, -1.55,
        r"$\rho cS\Delta x\,u_t$" + "   =   " + r"$S q(x,t)$" + "   −   " + r"$S q(x+\Delta x,t)$",
        ha="center", fontsize=16, color=DARK,
        bbox=dict(boxstyle="round,pad=0.55", facecolor="white", edgecolor="#D0D5DD"))
ax.text(2.78, -1.93, "内能增加率", ha="center", fontsize=10.5, color=ORANGE)
ax.text(7.15, -1.93, "流入 − 流出", ha="center", fontsize=10.5, color="#667085")

fig.suptitle("能量守恒只做一本账：小段内的增加 = 左端流入 − 右端流出", fontsize=17,
             weight="bold", color=DARK, y=0.98)
fig.subplots_adjust(top=0.86, bottom=0.09)
fig.savefig(OUT, dpi=170, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"{OUT.name} saved")
