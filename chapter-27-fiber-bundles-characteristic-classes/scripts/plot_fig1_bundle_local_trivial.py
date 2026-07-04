"""fig1: Fiber bundle as local product patches."""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig1_bundle_local_trivial.png"

t = np.linspace(0, 2 * np.pi, 300)
base_x = 3 * np.cos(t)
base_y = 0.55 * np.sin(t)

fig, ax = plt.subplots(figsize=(9, 5.4))
ax.plot(base_x, base_y, color="#202124", lw=2.2)
for idx, ti in enumerate(np.linspace(0.15, 2 * np.pi - 0.15, 18)):
    x = 3 * np.cos(ti)
    y = 0.55 * np.sin(ti)
    height = 0.9 + 0.25 * np.sin(2 * ti)
    ax.plot([x, x], [y, y + height], color="#1A73E8", lw=1.7, alpha=0.82)
    ax.scatter([x], [y], color="#202124", s=18)
ax.axvspan(-2.8, -0.7, color="#E8F0FE", alpha=0.6)
ax.axvspan(0.65, 2.8, color="#FCE8E6", alpha=0.45)
ax.text(-1.75, 1.55, r"$U_i\times F$", ha="center", fontsize=14, color="#1A73E8", fontweight="bold")
ax.text(1.75, 1.55, r"$U_j\times F$", ha="center", fontsize=14, color="#D93025", fontweight="bold")
ax.text(0, -1.0, "底空间 M", ha="center", fontsize=13, fontweight="bold")
ax.set_title("纤维丛：局部像乘积，全局由粘合决定", fontsize=16, fontweight="bold")
ax.set_xlim(-3.6, 3.6)
ax.set_ylim(-1.35, 2.05)
ax.axis("off")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
