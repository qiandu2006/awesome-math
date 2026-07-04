"""fig1: 从非线性曲面到局部线性切平面。"""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig1_manifold_tangent_plane.png"

fig = plt.figure(figsize=(11, 8))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-2.5, 2.5, 80)
y = np.linspace(-2.5, 2.5, 80)
X, Y = np.meshgrid(x, y)
Z = 0.18 * X**2 - 0.12 * Y**2 + 0.18 * np.sin(1.2 * X)

ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.62, linewidth=0, antialiased=True)

# point and tangent plane
p = np.array([0.8, -0.4])
px, py = p
pz = 0.18 * px**2 - 0.12 * py**2 + 0.18 * np.sin(1.2 * px)
dzdx = 0.36 * px + 0.216 * np.cos(1.2 * px)
dzdy = -0.24 * py

u = np.linspace(-0.9, 0.9, 8)
v = np.linspace(-0.9, 0.9, 8)
U, V = np.meshgrid(u, v)
PX = px + U
PY = py + V
PZ = pz + dzdx * U + dzdy * V
ax.plot_surface(PX, PY, PZ, color='#F4B400', alpha=0.48, linewidth=0)

ax.scatter([px], [py], [pz], color='#D93025', s=70, depthshade=False)

# tangent basis vectors
v1 = np.array([0.95, 0.0, dzdx * 0.95])
v2 = np.array([0.0, 0.85, dzdy * 0.85])
ax.quiver(px, py, pz, v1[0], v1[1], v1[2], color='#D93025', linewidth=2.4, arrow_length_ratio=0.12)
ax.quiver(px, py, pz, v2[0], v2[1], v2[2], color='#D93025', linewidth=2.4, arrow_length_ratio=0.12)

ax.text(px, py, pz + 0.45, 'p 点', color='#D93025', fontsize=12, fontweight='bold')
ax.text(px + 1.1, py - 0.15, pz + 0.35, '切空间 $T_pM$', color='#A05A00', fontsize=12, fontweight='bold')
ax.text(-2.4, 2.0, 1.55, '流形 M：整体弯曲', color='#1E5B4F', fontsize=13, fontweight='bold')
ax.text(-2.4, 2.0, 1.25, '局部看起来像线性空间', color='#555555', fontsize=10)

ax.set_title('微分几何的核心图像：用切空间近似流形', fontsize=15, fontweight='bold', pad=18)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(elev=28, azim=-55)
ax.set_box_aspect((1.3, 1.1, 0.75))
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f'{out.name} saved')
