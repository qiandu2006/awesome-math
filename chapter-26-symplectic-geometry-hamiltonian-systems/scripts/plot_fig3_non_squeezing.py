"""fig3: Conceptual picture of symplectic non-squeezing."""
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig3_non_squeezing.png"

fig, ax = plt.subplots(figsize=(8.8, 5.2))
ax.set_xlim(-3.2, 3.2)
ax.set_ylim(-1.8, 1.8)
ax.axis("off")

ball = patches.Circle((-1.7, 0), 1.0, facecolor="#E8F0FE", edgecolor="#1A73E8", lw=3)
cylinder = patches.Rectangle((1.1, -1.35), 0.95, 2.7, facecolor="#FCE8E6", edgecolor="#D93025", lw=3)
hole = patches.Circle((1.575, 0), 0.47, facecolor="white", edgecolor="#D93025", lw=2, ls="--")
ax.add_patch(ball)
ax.add_patch(cylinder)
ax.add_patch(hole)
ax.annotate("", xy=(0.8, 0), xytext=(-0.55, 0), arrowprops=dict(arrowstyle="->", lw=2.2, color="#5F6368"))
ax.text(-1.7, -1.38, "辛球半径 R", ha="center", fontsize=13, fontweight="bold")
ax.text(1.58, -1.58, "柱体截面半径 r<R", ha="center", fontsize=13, fontweight="bold")
ax.text(0.12, 0.25, "不允许\n辛嵌入", ha="center", fontsize=14, color="#D93025", fontweight="bold")
ax.text(0, 1.45, "非挤压定理：保体积还不够，二维辛截面也受限制", ha="center", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
