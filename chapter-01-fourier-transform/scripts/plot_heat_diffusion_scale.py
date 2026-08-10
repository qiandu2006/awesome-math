"""热核随时间变宽，展示典型扩散距离 sqrt(alpha t)。"""
import os
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(ROOT / ".mplconfig"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = ROOT / "images" / "heat_diffusion_scale.png"
DARK = "#243447"
COLORS = ["#E45745", "#F2A541", "#3B82C4"]
TIMES = [0.2, 0.8, 1.8]

x = np.linspace(-5, 5, 1200)
fig, axes = plt.subplots(1, 3, figsize=(12, 4.5), sharex=True, sharey=True, facecolor="white")

for ax, t, color in zip(axes, TIMES, COLORS):
    width = np.sqrt(t)  # alpha = 1
    u = np.exp(-(x**2) / (4 * t)) / np.sqrt(4 * np.pi * t)
    ax.plot(x, u, color=color, lw=3)
    ax.fill_between(x, 0, u, color=color, alpha=0.12)
    ax.axvspan(-width, width, color=color, alpha=0.12)
    y_marker = 0.10
    ax.annotate("", xy=(-width, y_marker), xytext=(width, y_marker),
                arrowprops=dict(arrowstyle="|-|", color=color, lw=2))
    ax.text(0, y_marker + 0.045, r"$2\sqrt{\alpha t}$", ha="center", fontsize=12, color=color, weight="bold")
    ax.set_title(fr"$t={t}$", fontsize=14, color=DARK)
    ax.set_xlabel("位置 x")
    ax.grid(alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#98A2B3")
    ax.set_xticks([-4, -2, 0, 2, 4])

axes[0].set_ylabel("温度 u（总热量保持不变）")
fig.suptitle(r"同一份热量越摊越开：影响距离按 $\sqrt{\alpha t}$ 增长", fontsize=17,
             weight="bold", color=DARK, y=0.99)
fig.text(0.5, 0.015, r"因此，要抹平长度尺度 $L$ 上的温差，时间量级是 $t\sim L^2/\alpha$。",
         ha="center", fontsize=12, color="#667085")
fig.subplots_adjust(top=0.84, bottom=0.18, wspace=0.12)
fig.savefig(OUT, dpi=170, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"{OUT.name} saved")
