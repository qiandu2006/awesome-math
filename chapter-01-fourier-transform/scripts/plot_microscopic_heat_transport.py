"""用平均自由程说明截面两侧携带的能量信息为何形成净热流。"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(ROOT / ".mplconfig"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = ROOT / "images" / "microscopic_heat_transport.png"
COOL = "#3B82C4"
HOT = "#E45745"
DARK = "#243447"
PURPLE = "#7A3E9D"

fig, ax = plt.subplots(figsize=(11, 5.4), facecolor="white")
ax.set_xlim(-5.8, 5.8)
ax.set_ylim(-2.0, 3.1)
ax.axis("off")

# 棒的左右两侧：右热左冷
ax.add_patch(Rectangle((-5.3, -0.85), 5.3, 2.15, facecolor="#DDEEFF", edgecolor="none"))
ax.add_patch(Rectangle((0, -0.85), 5.3, 2.15, facecolor="#FBE2DC", edgecolor="none"))
ax.add_patch(Rectangle((-5.3, -0.85), 10.6, 2.15, fill=False, edgecolor=DARK, lw=1.3))
ax.axvline(0, ymin=0.225, ymax=0.755, color=DARK, lw=2.2)

# 粒子/声子示意，右侧颜色更热
left_points = [(-4.3, 0.65), (-3.5, -0.20), (-2.6, 0.83), (-1.6, 0.05), (-0.9, 0.73)]
right_points = [(0.8, 0.08), (1.6, 0.83), (2.5, -0.25), (3.4, 0.63), (4.4, -0.05)]
for px, py in left_points:
    ax.add_patch(Circle((px, py), 0.10, facecolor=COOL, edgecolor="white", lw=0.7))
for px, py in right_points:
    ax.add_patch(Circle((px, py), 0.13, facecolor=HOT, edgecolor="white", lw=0.7))

# 两个方向都有运动，但从热侧来的能量通量更大
ax.add_patch(FancyArrowPatch((-2.8, 0.35), (1.0, 0.35), arrowstyle="-|>", mutation_scale=15,
                             lw=2.0, color=COOL, connectionstyle="arc3,rad=-0.12"))
ax.text(-1.0, 0.82, "向右穿过：携带较少能量", ha="center", fontsize=11, color=COOL)
ax.add_patch(FancyArrowPatch((2.9, -0.02), (-1.0, -0.02), arrowstyle="-|>", mutation_scale=18,
                             lw=3.4, color=HOT, connectionstyle="arc3,rad=-0.12"))
ax.text(1.0, -0.62, "向左穿过：携带较多能量", ha="center", fontsize=11, color=HOT, weight="bold")

ax.text(-3.1, 1.62, r"来自 $x-\ell$ 的信息", ha="center", fontsize=13, color=COOL, weight="bold")
ax.text(3.1, 1.62, r"来自 $x+\ell$ 的信息", ha="center", fontsize=13, color=HOT, weight="bold")
ax.text(-3.1, 1.25, r"温度 $u(x-\ell)$", ha="center", fontsize=12, color=DARK)
ax.text(3.1, 1.25, r"温度 $u(x+\ell)$", ha="center", fontsize=12, color=DARK)
ax.text(0, 1.62, "截面 x", ha="center", fontsize=12, color=DARK, weight="bold")

# 平均自由程标尺
for center, sign in [(-1.55, -1), (1.55, 1)]:
    ax.annotate("", xy=(0, -1.25), xytext=(2 * center, -1.25),
                arrowprops=dict(arrowstyle="|-|", color="#667085", lw=1.3))
    ax.text(center, -1.55, r"平均自由程 $\ell$", ha="center", fontsize=10.5, color="#667085")

# 净输运
ax.add_patch(FancyArrowPatch((2.2, 2.35), (-2.2, 2.35), arrowstyle="-|>", mutation_scale=20,
                             lw=3.6, color=PURPLE))
ax.text(0, 2.63, "净能量输运：热 → 冷", ha="center", fontsize=14, color=PURPLE, weight="bold")

fig.suptitle("微观直觉：两边都有随机运动，但携带的平均能量不同", fontsize=17, weight="bold", color=DARK, y=0.98)
fig.text(0.5, 0.025, r"净差 $\propto u(x-\ell)-u(x+\ell)\approx-2\ell u_x(x)$", ha="center", fontsize=15, color=DARK)
fig.subplots_adjust(top=0.88, bottom=0.15)
fig.savefig(OUT, dpi=170, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"{OUT.name} saved")
