"""用峰、直线和谷解释 u_xx 如何决定当地温度升降。"""
import os
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(ROOT / ".mplconfig"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = ROOT / "images" / "curvature_temperature_change.png"
DARK = "#243447"
RED = "#E45745"
BLUE = "#3B82C4"
GREEN = "#219653"

x = np.linspace(-1.25, 1.25, 500)
curves = [1.18 - 0.55 * x**2, 0.72 + 0.28 * x, 0.48 + 0.55 * x**2]
titles = ["局部峰值：热量向外流", "线性温度：流入等于流出", "局部谷值：热量向内流"]
signs = [r"$u_{xx}<0\;\Rightarrow\;u_t<0$（降温）",
         r"$u_{xx}=0\;\Rightarrow\;u_t=0$（暂时不变）",
         r"$u_{xx}>0\;\Rightarrow\;u_t>0$（升温）"]
colors = [RED, GREEN, BLUE]

fig, axes = plt.subplots(1, 3, figsize=(12, 4.8), facecolor="white")
for i, (ax, y, title, sign, color) in enumerate(zip(axes, curves, titles, signs, colors)):
    ax.plot(x, y, color=color, lw=3)
    ax.axvspan(-0.22, 0.22, color="#98A2B3", alpha=0.14)
    ax.plot([0], [np.interp(0, x, y)], "o", ms=7, color=color, zorder=5)
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(0.15, 1.42)
    ax.set_title(title, fontsize=12.3, color=DARK, pad=10, weight="bold")
    ax.text(0.5, -0.20, sign, transform=ax.transAxes, ha="center", fontsize=11.5, color=color)
    ax.set_xlabel("位置 x")
    ax.grid(alpha=0.16)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#98A2B3")
    ax.set_xticks([])
    ax.set_yticks([])

    arrow_y = 0.30
    if i == 0:  # 从中心向两边
        arrows = [((-0.05, arrow_y), (-0.80, arrow_y)), ((0.05, arrow_y), (0.80, arrow_y))]
    elif i == 1:  # 等量穿过
        arrows = [((0.65, arrow_y), (-0.65, arrow_y))]
    else:  # 从两边向中心
        arrows = [((-0.80, arrow_y), (-0.05, arrow_y)), ((0.80, arrow_y), (0.05, arrow_y))]
    for start, end in arrows:
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=15,
                                     lw=2.3, color=color))

axes[0].set_ylabel("温度 u")
fig.suptitle("二阶导数在比较左右热流：当地究竟是“入多出少”还是“入少出多”？", fontsize=16.5,
             weight="bold", color=DARK, y=0.99)
fig.subplots_adjust(top=0.82, bottom=0.23, wspace=0.20)
fig.savefig(OUT, dpi=170, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"{OUT.name} saved")
