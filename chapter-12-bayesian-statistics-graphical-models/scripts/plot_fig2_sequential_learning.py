"""fig2: 序贯贝叶斯学习中后验逐渐收缩。"""
import math
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig2_sequential_learning.png"


def beta_pdf(x, a, b):
    log_norm = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    return np.exp(log_norm + (a - 1) * np.log(x) + (b - 1) * np.log(1 - x))


theta = np.linspace(1e-4, 1 - 1e-4, 900)
true_theta = 0.7
snapshots = [(0, 0, "先验"), (4, 1, "5 次观测"), (18, 7, "25 次观测"), (71, 29, "100 次观测")]
colors = ["#5F6368", "#F9AB00", "#1A73E8", "#D93025"]

fig, ax = plt.subplots(figsize=(9, 6))
for (h, t, label), color in zip(snapshots, colors):
    a, b = 1 + h, 1 + t
    ax.plot(theta, beta_pdf(theta, a, b), lw=3, color=color, label=f"{label}: Beta({a},{b})")

ax.axvline(true_theta, color="#188038", ls="--", lw=2)
ax.text(true_theta + 0.015, 8.0, "真实 θ=0.7", color="#188038", fontsize=12, fontweight="bold")
ax.text(0.20, 5.5, "数据越多\n后验越集中", fontsize=13, color="#202124")
ax.set_xlabel("θ")
ax.set_ylabel("后验密度")
ax.set_title("序贯学习：后验成为下一次更新的先验", fontsize=15, fontweight="bold")
ax.set_xlim(0, 1)
ax.grid(alpha=0.25)
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
