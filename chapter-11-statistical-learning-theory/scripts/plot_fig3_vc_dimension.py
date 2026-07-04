"""fig3: VC 维与打散。"""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig3_vc_dimension.png"

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# One-dimensional threshold cannot realize the pattern 1, 0 on two ordered points.
ax = axes[0]
ax.axhline(0, color="#5F6368", lw=2)
points = np.array([0.30, 0.70])
labels = np.array([1, 0])
colors = np.where(labels == 1, "#1A73E8", "#D93025")
ax.scatter(points, np.zeros_like(points), s=180, c=colors, edgecolor="white", linewidth=1.8, zorder=3)
ax.axvline(0.50, color="#202124", lw=2, ls="--")
ax.text(0.50, 0.18, "阈值 t", ha="center", fontsize=12, fontweight="bold")
ax.text(0.30, -0.20, "1", ha="center", fontsize=13, color="#1A73E8", fontweight="bold")
ax.text(0.70, -0.20, "0", ha="center", fontsize=13, color="#D93025", fontweight="bold")
ax.text(0.50, -0.40, "单阈值无法实现 1,0 模式", ha="center", fontsize=12, color="#5F6368")
ax.set_xlim(0, 1)
ax.set_ylim(-0.55, 0.45)
ax.set_yticks([])
ax.set_title("一维阈值：不能打散 2 个点", fontsize=13, fontweight="bold")
ax.grid(axis="x", alpha=0.18)

# A line in the plane shatters three points in general position.
ax = axes[1]
tri = np.array([[0.22, 0.25], [0.78, 0.28], [0.52, 0.78]])
patterns = [
    ([1, 1, 1], None),
    ([1, 0, 0], (0.38, 0.95, -0.07)),
    ([0, 1, 0], (-0.38, 0.95, 0.18)),
    ([0, 0, 1], (0.0, -1.0, 0.52)),
]
offsets = [(0, 0), (1.15, 0), (0, -1.05), (1.15, -1.05)]

for pattern, line in patterns:
    ox, oy = offsets.pop(0)
    pts = tri + np.array([ox, oy])
    c = ["#1A73E8" if v == 1 else "#D93025" for v in pattern]
    ax.scatter(pts[:, 0], pts[:, 1], s=95, c=c, edgecolor="white", linewidth=1.4, zorder=3)
    if line is not None:
        a, b, c0 = line
        xx = np.linspace(ox + 0.10, ox + 0.95, 80)
        yy = -(a * (xx - ox) + c0) / b + oy
        ax.plot(xx, yy, color="#202124", lw=2)

ax.text(1.03, -0.58, "二维直线可实现 3 点的所有标记模式", ha="center", fontsize=12, color="#5F6368")
ax.set_xlim(0.05, 2.08)
ax.set_ylim(-1.00, 0.95)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("二维线性分类器：可打散 3 个点", fontsize=13, fontweight="bold")
for spine in ax.spines.values():
    spine.set_visible(False)

plt.suptitle("VC 维：模型族能制造多少标记模式", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
