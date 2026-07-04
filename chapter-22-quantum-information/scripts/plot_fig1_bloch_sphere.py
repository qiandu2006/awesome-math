"""fig1: Bloch sphere for a single qubit."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig1_bloch_sphere.png"

theta = np.linspace(0, np.pi, 48)
phi = np.linspace(0, 2 * np.pi, 96)
theta_grid, phi_grid = np.meshgrid(theta, phi)
x = np.sin(theta_grid) * np.cos(phi_grid)
y = np.sin(theta_grid) * np.sin(phi_grid)
z = np.cos(theta_grid)

state_theta = 0.72 * np.pi
state_phi = 0.32 * np.pi
sx = np.sin(state_theta) * np.cos(state_phi)
sy = np.sin(state_theta) * np.sin(state_phi)
sz = np.cos(state_theta)

fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(x, y, z, color="#E8F0FE", edgecolor="#DADCE0", linewidth=0.25, alpha=0.35, shade=False)

circle = np.linspace(0, 2 * np.pi, 300)
ax.plot(np.cos(circle), np.sin(circle), 0, color="#5F6368", lw=1.5, alpha=0.7)
ax.plot(np.cos(circle), np.zeros_like(circle), np.sin(circle), color="#9AA0A6", lw=1.0, alpha=0.55)
ax.plot(np.zeros_like(circle), np.cos(circle), np.sin(circle), color="#9AA0A6", lw=1.0, alpha=0.55)

ax.quiver(0, 0, 0, 1.15, 0, 0, color="#D93025", arrow_length_ratio=0.08, lw=2)
ax.quiver(0, 0, 0, 0, 1.15, 0, color="#188038", arrow_length_ratio=0.08, lw=2)
ax.quiver(0, 0, 0, 0, 0, 1.15, color="#1A73E8", arrow_length_ratio=0.08, lw=2)
ax.quiver(0, 0, 0, sx, sy, sz, color="#F9AB00", arrow_length_ratio=0.1, lw=4)

ax.text(1.25, 0, 0, "X", color="#D93025", fontsize=13, fontweight="bold")
ax.text(0, 1.25, 0, "Y", color="#188038", fontsize=13, fontweight="bold")
ax.text(0, 0, 1.25, r"$|0\rangle$", color="#1A73E8", fontsize=13, fontweight="bold")
ax.text(0, 0, -1.27, r"$|1\rangle$", color="#5F6368", fontsize=13, fontweight="bold")
ax.text(sx * 1.15, sy * 1.15, sz * 1.02, r"$|\psi\rangle$", color="#B06000", fontsize=14, fontweight="bold")

ax.set_xlim(-1.25, 1.25)
ax.set_ylim(-1.25, 1.25)
ax.set_zlim(-1.45, 1.3)
ax.set_box_aspect((1, 1, 1))
ax.set_axis_off()
ax.view_init(elev=24, azim=36)
ax.set_title("Bloch 球：qubit 的状态是球面上的方向", fontsize=16, fontweight="bold", pad=18)

plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
