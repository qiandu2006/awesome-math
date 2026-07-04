"""fig1: Statistical manifold of Gaussian distributions."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig1_statistical_manifold.png"

mu = np.linspace(-2, 2, 80)
sigma = np.linspace(0.35, 2.0, 80)
MU, SIG = np.meshgrid(mu, sigma)
Z = np.log(SIG)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(MU, SIG, Z, cmap="viridis", alpha=0.72, linewidth=0, antialiased=True)
points = [(-1.2, 0.55), (0.0, 1.0), (1.1, 1.55)]
for m, s in points:
    ax.scatter([m], [s], [np.log(s)], s=70, color="#D93025")
    ax.text(m, s, np.log(s) + 0.13, rf"$N({m:g},{s:g}^2)$", fontsize=10)
ax.set_xlabel("均值 μ")
ax.set_ylabel("标准差 σ")
ax.set_zlabel("几何高度")
ax.set_title("正态分布族：每个点是一整个概率分布", fontsize=16, fontweight="bold")
ax.view_init(elev=25, azim=-55)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
