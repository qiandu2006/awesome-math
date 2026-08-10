"""温度的绝对高低不产生热流；温度梯度才产生热流。"""
import os
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(ROOT / ".mplconfig"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyArrowPatch, Rectangle

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = ROOT / "images" / "heat_flux_gradient.png"
COOL = "#3B82C4"
HOT = "#E45745"
DARK = "#243447"
MUTED = "#667085"

fig = plt.figure(figsize=(11, 6.2), facecolor="white")
grid = fig.add_gridspec(2, 2, height_ratios=[1.05, 1], hspace=0.06, wspace=0.22)
rod_axes = [fig.add_subplot(grid[0, i]) for i in range(2)]
curve_axes = [fig.add_subplot(grid[1, i]) for i in range(2)]

for ax in rod_axes:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis("off")

# 左：温度高但均匀
ax = rod_axes[0]
ax.add_patch(Rectangle((0.7, 1.05), 8.6, 0.9, facecolor="#ECA65B", edgecolor=DARK, lw=1.2))
ax.text(5, 1.5, "处处同温", ha="center", va="center", color="white", fontsize=13, weight="bold")
ax.text(5, 2.55, "温度可以很高，但没有温度差", ha="center", fontsize=13, color=DARK)
ax.text(5, 0.45, r"$u_x=0\quad\Longrightarrow\quad q=0$", ha="center", fontsize=16, color=DARK)

# 右：右热左冷，热流逆着梯度
ax = rod_axes[1]
cmap = LinearSegmentedColormap.from_list("temperature", [COOL, "#F5D76E", HOT])
gradient = np.linspace(0, 1, 500)[None, :]
ax.imshow(gradient, extent=(0.7, 9.3, 1.05, 1.95), origin="lower", aspect="auto", cmap=cmap)
ax.add_patch(Rectangle((0.7, 1.05), 8.6, 0.9, fill=False, edgecolor=DARK, lw=1.2))
ax.text(0.75, 2.18, "冷", ha="left", fontsize=12, color=COOL, weight="bold")
ax.text(9.25, 2.18, "热", ha="right", fontsize=12, color=HOT, weight="bold")
ax.add_patch(FancyArrowPatch((7.4, 0.72), (2.6, 0.72), arrowstyle="-|>", mutation_scale=18,
                             lw=3, color="#7A3E9D"))
ax.text(5, 0.27, r"热流 $q<0$", ha="center", fontsize=13, color="#7A3E9D", weight="bold")
ax.text(5, 2.55, "右边更热：温度沿 x 方向升高", ha="center", fontsize=13, color=DARK)

x = np.linspace(0, 1, 200)

ax = curve_axes[0]
ax.plot(x, np.full_like(x, 0.72), lw=3, color="#ECA65B")
ax.set_title("绝对温度不决定热流", fontsize=12, color=MUTED, pad=7)

ax = curve_axes[1]
ax.plot(x, 0.25 + 0.72 * x, lw=3, color=HOT)
ax.annotate(r"$u_x>0$", xy=(0.62, 0.70), xytext=(0.34, 0.92), fontsize=13, color=HOT,
            arrowprops=dict(arrowstyle="->", color=HOT, lw=1.5))
ax.set_title(r"梯度向右，热流向左：$q=-\lambda u_x$", fontsize=12, color=MUTED, pad=7)

for ax in curve_axes:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.15)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#98A2B3")
    ax.set_xlabel("位置 x")
    ax.set_ylabel("温度 u")
    ax.set_xticks([])
    ax.set_yticks([])

fig.suptitle("热不是被“高温”推动，而是被温度梯度推动", fontsize=17, weight="bold", color=DARK, y=0.98)
fig.text(0.5, 0.015, "负号只表达一件事：热总是从高温一侧流向低温一侧。", ha="center", fontsize=12, color=MUTED)
fig.subplots_adjust(top=0.90, bottom=0.12)
fig.savefig(OUT, dpi=170, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"{OUT.name} saved")
