"""fig1: Smooth deformation from circle to ellipse."""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig1_smooth_deformation.png"
t = np.linspace(0, 2 * np.pi, 400)

fig, ax = plt.subplots(figsize=(9, 4.8))
shapes = [
    (-2.8, 1.0, 1.0, "圆"),
    (0.0, 1.35, 0.85, "光滑变形中"),
    (2.8, 1.75, 0.65, "椭圆"),
]
for x0, a, b, label in shapes:
    x = x0 + a * np.cos(t)
    y = b * np.sin(t)
    ax.plot(x, y, lw=3, color="#1A73E8")
    ax.text(x0, -1.3, label, ha="center", fontsize=13, fontweight="bold")

for start, end in [(-1.65, -0.9), (1.15, 1.9)]:
    ax.add_patch(FancyArrowPatch((start, 0), (end, 0), arrowstyle="->", mutation_scale=18, lw=2, color="#5F6368"))

ax.text(0, 1.55, "没有撕裂、粘合、尖点；光滑类型不变", ha="center", fontsize=13, color="#5F6368")
ax.set_title("微分拓扑关心光滑变形下不变的形状", fontsize=16, fontweight="bold")
ax.set_aspect("equal")
ax.axis("off")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
