"""fig4: 曲率与测地线。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig4_curvature_geodesics.png"

fig = plt.figure(figsize=(12, 6))

# plane
ax1 = fig.add_subplot(121, projection='3d')
u = np.linspace(-2.3, 2.3, 25)
v = np.linspace(-2.3, 2.3, 25)
U, V = np.meshgrid(u, v)
Z = np.zeros_like(U)
ax1.plot_surface(U, V, Z, color='#E8F0FE', edgecolor='#AECBFA', linewidth=0.4, alpha=0.9, shade=False)
ax1.plot([-2, 2], [-1.2, 1.2], [0.04, 0.04], color='#D93025', lw=4)
ax1.text(0, 0.2, 0.2, '平面：直线就是测地线', color='#D93025', fontsize=11, fontweight='bold')
ax1.set_title('零曲率', fontsize=14, fontweight='bold')
ax1.set_axis_off()
ax1.view_init(28, -55)
ax1.set_box_aspect((1, 1, 0.35))

# sphere
ax2 = fig.add_subplot(122, projection='3d')
theta = np.linspace(1e-3, np.pi - 1e-3, 60)
phi = np.linspace(0, 2 * np.pi, 100)
T, P = np.meshgrid(theta, phi)
X = np.sin(T) * np.cos(P)
Y = np.sin(T) * np.sin(P)
Z = np.cos(T)
ax2.plot_surface(X, Y, Z, cmap='Blues', alpha=0.55, linewidth=0, shade=False)

# great circle
s = np.linspace(0, 2 * np.pi, 300)
xg = np.cos(s)
yg = np.sin(s)
zg = np.zeros_like(s)
ax2.plot(xg, yg, zg, color='#D93025', lw=4)

# latitude small circle
lat = 0.55
xs = np.cos(lat) * np.cos(s)
ys = np.cos(lat) * np.sin(s)
zs = np.sin(lat) * np.ones_like(s)
ax2.plot(xs, ys, zs, color='#F4B400', lw=3, linestyle='--')

ax2.text(0.2, -1.15, 0.1, '大圆：球面上的测地线', color='#D93025', fontsize=11, fontweight='bold')
ax2.text(-1.1, 0.1, 0.75, '纬线通常不是测地线', color='#A05A00', fontsize=10, fontweight='bold')
ax2.set_title('正曲率', fontsize=14, fontweight='bold')
ax2.set_axis_off()
ax2.view_init(25, -42)
ax2.set_box_aspect((1, 1, 1))

fig.suptitle('测地线：流形内部的“直线”', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f'{out.name} saved')
