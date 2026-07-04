"""fig5: 变分推断用简单分布近似复杂后验。"""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig5_variational_inference.png"


def gaussian_density(x, y, mean, cov):
    pos = np.stack([x - mean[0], y - mean[1]], axis=-1)
    inv = np.linalg.inv(cov)
    quad = np.einsum("...i,ij,...j->...", pos, inv, pos)
    det = np.linalg.det(cov)
    return np.exp(-0.5 * quad) / (2 * np.pi * np.sqrt(det))


grid = np.linspace(-3.2, 3.2, 260)
xx, yy = np.meshgrid(grid, grid)

posterior = gaussian_density(xx, yy, np.array([0.0, 0.0]), np.array([[1.4, 1.05], [1.05, 1.1]]))
mean_field = gaussian_density(xx, yy, np.array([0.0, 0.0]), np.array([[1.0, 0.0], [0.0, 0.75]]))

fig, ax = plt.subplots(figsize=(8, 7))
levels_p = np.linspace(posterior.max() * 0.08, posterior.max() * 0.85, 7)
levels_q = np.linspace(mean_field.max() * 0.08, mean_field.max() * 0.85, 7)
ax.contour(xx, yy, posterior, levels=levels_p, colors="#1A73E8", linewidths=2.5)
ax.contour(xx, yy, mean_field, levels=levels_q, colors="#D93025", linewidths=2.2, linestyles="--")
ax.text(-2.9, 2.65, "真实后验 p(z|x)\n相关结构倾斜", color="#1A73E8",
        fontsize=13, fontweight="bold")
ax.text(1.00, -2.75, "平均场 q(z)\n轴对齐近似", color="#D93025",
        fontsize=13, fontweight="bold")
ax.annotate("选择简单分布族\n换取可计算优化", xy=(0.85, 0.55), xytext=(1.55, 1.65),
            arrowprops=dict(arrowstyle="->", lw=2, color="#202124"),
            fontsize=12, color="#202124")
ax.set_xlabel("$z_1$")
ax.set_ylabel("$z_2$")
ax.set_title("变分推断：用可优化的 q 近似真实后验", fontsize=15, fontweight="bold")
ax.set_aspect("equal")
ax.grid(alpha=0.2)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
