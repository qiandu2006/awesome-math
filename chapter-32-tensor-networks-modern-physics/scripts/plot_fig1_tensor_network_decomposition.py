"""fig1: High-order tensor decomposed into a tensor network."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig1_tensor_network_decomposition.png"

fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis("off")

ax.add_patch(patches.FancyBboxPatch((0.8, 1.55), 2.0, 1.8, boxstyle="round,pad=0.05,rounding_size=0.08",
                                    facecolor="#E8F0FE", edgecolor="#1A73E8", lw=2))
ax.text(1.8, 2.65, "高阶张量", ha="center", fontsize=14, fontweight="bold")
ax.text(1.8, 2.1, r"$T_{i_1\dots i_n}$", ha="center", fontsize=15, color="#1A73E8")
ax.annotate("", xy=(4.0, 2.45), xytext=(3.0, 2.45), arrowprops=dict(arrowstyle="->", lw=2.2, color="#5F6368"))
ax.text(3.5, 2.75, "分解", ha="center", fontsize=11, color="#5F6368")

coords = [(5.0, 2.8), (6.2, 2.0), (7.4, 2.8), (8.6, 2.0)]
for i, (x, y) in enumerate(coords):
    ax.add_patch(patches.Circle((x, y), 0.36, facecolor="#FCE8E6", edgecolor="#D93025", lw=2))
    ax.text(x, y, f"A{i+1}", ha="center", va="center", fontsize=11, fontweight="bold")
for (x1, y1), (x2, y2) in zip(coords[:-1], coords[1:]):
    ax.plot([x1, x2], [y1, y2], color="#5F6368", lw=2)
for x, y in coords:
    ax.plot([x, x], [y, y + 0.75], color="#1A73E8", lw=1.8)
ax.text(6.8, 0.9, "内部边求和；外部边保留物理指标", ha="center", fontsize=12, color="#5F6368")
ax.set_title("张量网络：用小张量和连接图表示大张量", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
