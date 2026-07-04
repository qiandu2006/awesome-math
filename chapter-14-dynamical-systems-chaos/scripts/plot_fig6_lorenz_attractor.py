"""fig6: Lorenz 奇异吸引子。"""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig6_lorenz_attractor.png"

sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0
dt = 0.006
n = 12000
pts = np.empty((n, 3))
pts[0] = [0.1, 1.0, 1.05]


def f(p):
    x, y, z = p
    return np.array([sigma * (y - x), x * (rho - z) - y, x * y - beta * z])


for i in range(n - 1):
    p = pts[i]
    k1 = f(p)
    k2 = f(p + 0.5 * dt * k1)
    k3 = f(p + 0.5 * dt * k2)
    k4 = f(p + dt * k3)
    pts[i + 1] = p + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6

pts = pts[1000:]

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")
colors = np.linspace(0, 1, len(pts))
ax.plot(pts[:, 0], pts[:, 1], pts[:, 2], lw=0.55, color="#1A73E8", alpha=0.72)
ax.set_title("Lorenz 奇异吸引子：有界但不周期的长期行为", fontsize=15, fontweight="bold")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(elev=25, azim=-58)
ax.set_box_aspect((1, 1, 0.8))
plt.tight_layout()
plt.savefig(out, dpi=160, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
