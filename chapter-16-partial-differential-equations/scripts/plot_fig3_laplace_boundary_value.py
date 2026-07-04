"""fig3: Laplace 边值问题中边界决定内部平衡。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig3_laplace_boundary_value.png"

n = 80
u = np.zeros((n, n))
u[-1, :] = 1.0
u[0, :] = 0.0
u[:, 0] = np.linspace(0, 1, n)
u[:, -1] = np.linspace(0, 1, n)

for _ in range(2500):
    u[1:-1, 1:-1] = 0.25 * (u[2:, 1:-1] + u[:-2, 1:-1] + u[1:-1, 2:] + u[1:-1, :-2])

fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(u, origin="lower", cmap="viridis", extent=[0, 1, 0, 1])
ax.contour(np.linspace(0, 1, n), np.linspace(0, 1, n), u, levels=9, colors="white", linewidths=0.7, alpha=0.7)
ax.text(0.5, 1.04, "边界温度高", ha="center", fontsize=12, color="#202124")
ax.text(0.5, -0.09, "边界温度低", ha="center", fontsize=12, color="#202124")
ax.set_title("Laplace 方程：边界条件决定内部平衡", fontsize=15, fontweight="bold")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="u")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
