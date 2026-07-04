"""fig2: Regular value preimage as a smooth submanifold."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig2_regular_value.png"

x = np.linspace(-1.8, 1.8, 400)
y = np.linspace(-1.8, 1.8, 400)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig, ax = plt.subplots(figsize=(7, 6))
levels = [0.25, 0.64, 1.0, 1.44, 2.25]
cs = ax.contour(X, Y, Z, levels=levels, colors="#BDC1C6", linewidths=1.2)
ax.clabel(cs, fmt=lambda v: f"{v:g}", fontsize=9)
ax.contour(X, Y, Z, levels=[1.0], colors="#D93025", linewidths=3.4)
ax.text(0, -1.32, r"$F^{-1}(1)$", color="#D93025", fontsize=15, ha="center", fontweight="bold")
ax.arrow(0.7, 0.714, 0.42, 0.42, width=0.01, head_width=0.08, color="#1A73E8", length_includes_head=True)
ax.text(1.05, 1.18, r"$\nabla F\ne0$", color="#1A73E8", fontsize=13, fontweight="bold")
ax.set_title(r"正则值逆像：$F(x,y)=x^2+y^2$ 的水平集", fontsize=16, fontweight="bold")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_aspect("equal")
ax.grid(alpha=0.18)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
