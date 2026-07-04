"""fig5: Rademacher 复杂度与拟合随机符号。"""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig5_rademacher_complexity.png"
rng = np.random.default_rng(11)

x = np.linspace(0, 1, 26)
sigma = rng.choice([-1, 1], size=x.size)
grid = np.linspace(0, 1, 500)

coef_low = np.polyfit(x, sigma, 1)
coef_high = np.polyfit(x, sigma, 18)
pred_low = np.polyval(coef_low, grid)
pred_high = np.polyval(coef_high, grid)

fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
for ax, pred, title, color in [
    (axes[0], pred_low, "低复杂度函数族：难以追踪随机符号", "#188038"),
    (axes[1], pred_high, "高复杂度函数族：可以追踪随机符号", "#D93025"),
]:
    ax.axhline(0, color="#5F6368", lw=1)
    ax.scatter(x, sigma, c=np.where(sigma > 0, "#1A73E8", "#D93025"), s=70,
               edgecolor="white", linewidth=1.2, zorder=3)
    ax.plot(grid, pred, color=color, lw=3)
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.set_xlabel("x")
    ax.set_xlim(-0.03, 1.03)
    ax.set_ylim(-1.8, 1.8)
    ax.grid(alpha=0.22)

axes[0].set_ylabel("随机标签 σ")
plt.suptitle("Rademacher 复杂度：拟合纯噪声的能力", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
