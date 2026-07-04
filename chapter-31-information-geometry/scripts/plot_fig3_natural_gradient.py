"""fig3: Ordinary gradient versus natural gradient."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig3_natural_gradient.png"

x = np.linspace(-3, 3, 300)
y = np.linspace(-2, 2, 240)
X, Y = np.meshgrid(x, y)
Z = 0.8 * (X - 1.1) ** 2 + 0.18 * (Y + 0.4) ** 2

fig, ax = plt.subplots(figsize=(7.5, 5.8))
ax.contour(X, Y, Z, levels=15, cmap="Blues")
start = np.array([-1.55, 0.95])
ordinary = np.array([1.0, -0.25])
natural = np.array([0.55, -0.9])
ax.arrow(start[0], start[1], ordinary[0], ordinary[1], head_width=0.09, width=0.018, color="#D93025", length_includes_head=True)
ax.arrow(start[0], start[1], natural[0], natural[1], head_width=0.09, width=0.018, color="#188038", length_includes_head=True)
ax.scatter([start[0]], [start[1]], s=70, color="#202124", zorder=3)
ax.text(start[0] + ordinary[0] + 0.1, start[1] + ordinary[1], "普通梯度", color="#D93025", fontsize=12, fontweight="bold")
ax.text(start[0] + natural[0] + 0.08, start[1] + natural[1] - 0.05, "自然梯度", color="#188038", fontsize=12, fontweight="bold")
ax.set_xlabel(r"$\theta_1$")
ax.set_ylabel(r"$\theta_2$")
ax.set_title("自然梯度：按 Fisher 几何校正下降方向", fontsize=16, fontweight="bold")
ax.grid(alpha=0.2)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
