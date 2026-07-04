"""fig2: Area preservation under a linear symplectic shear."""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig2_area_preservation.png"

square = np.array([[-0.6, -0.6], [0.6, -0.6], [0.6, 0.6], [-0.6, 0.6]])
A = np.array([[1.0, 1.0], [0.0, 1.0]])
sheared = square @ A.T

fig, ax = plt.subplots(figsize=(8.5, 4.8))
left = square + np.array([-2.2, 0])
right = sheared + np.array([2.2, 0])
ax.add_patch(Polygon(left, closed=True, facecolor="#E8F0FE", edgecolor="#1A73E8", lw=2.5))
ax.add_patch(Polygon(right, closed=True, facecolor="#FCE8E6", edgecolor="#D93025", lw=2.5))
ax.add_patch(FancyArrowPatch((-1.1, 0), (1.1, 0), arrowstyle="->", mutation_scale=18, lw=2, color="#5F6368"))
ax.text(-2.2, -1.15, "初始小面积元", ha="center", fontsize=13, fontweight="bold")
ax.text(2.2, -1.15, "Hamilton 流后\n面积仍相同", ha="center", fontsize=13, fontweight="bold")
ax.text(0, 0.35, r"$\varphi_t^*\omega=\omega$", ha="center", fontsize=17, color="#5F6368")
ax.set_title("Liouville 定理：相空间面积不会被压缩或膨胀", fontsize=16, fontweight="bold")
ax.set_xlim(-3.3, 3.3)
ax.set_ylim(-1.6, 1.6)
ax.set_aspect("equal")
ax.axis("off")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
