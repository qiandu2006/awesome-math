"""fig5: 平行移动与曲率。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig5_parallel_transport.png"

fig = plt.figure(figsize=(9, 7.2))
ax = fig.add_subplot(111, projection='3d')
ax.set_position([0.02, 0.12, 0.96, 0.82])

theta = np.linspace(0, np.pi, 70)
phi = np.linspace(0, 2 * np.pi, 120)
T, P = np.meshgrid(theta, phi)
X = np.sin(T) * np.cos(P)
Y = np.sin(T) * np.sin(P)
Z = np.cos(T)
ax.plot_surface(X, Y, Z, cmap='Blues', alpha=0.42, linewidth=0)

# spherical triangle: equator point A -> north pole B -> equator point C -> A
A = np.array([1.0, 0.0, 0.0])
B = np.array([0.0, 0.0, 1.0])
C = np.array([0.0, 1.0, 0.0])

s = np.linspace(0, 1, 120)
path1 = np.vstack([np.cos(s * np.pi / 2), np.zeros_like(s), np.sin(s * np.pi / 2)]).T
path2 = np.vstack([np.zeros_like(s), np.sin((1 - s) * np.pi / 2), np.cos((1 - s) * np.pi / 2)]).T
path3 = np.vstack([np.cos((1 - s) * np.pi / 2), np.sin((1 - s) * np.pi / 2), np.zeros_like(s)]).T

for path in [path1, path2, path3]:
    ax.plot(path[:, 0], path[:, 1], path[:, 2], color='#D93025', lw=4)

for point, label in [(A, 'A'), (B, 'B'), (C, 'C')]:
    ax.scatter([point[0]], [point[1]], [point[2]], color='#202124', s=50)
    ax.text(point[0] * 1.12, point[1] * 1.12, point[2] * 1.12, label, fontsize=13,
            fontweight='bold', color='#202124')

# draw initial/final tangent vectors at A to show holonomy
ax.quiver(A[0], A[1], A[2], 0, 0.55, 0, color='#34A853', linewidth=3, arrow_length_ratio=0.18)
ax.text(1.05, 0.58, 0.05, '初始向量', color='#137333', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.72))
ax.quiver(A[0], A[1], A[2], 0, 0, 0.55, color='#F4B400', linewidth=3, arrow_length_ratio=0.18)
ax.text(1.05, 0.05, 0.62, '移动一圈后', color='#A05A00', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.72))

fig.text(0.5, 0.965, '平行移动：不同点切空间之间的比较规则',
         ha='center', va='top', fontsize=15, fontweight='bold')
fig.text(0.5, 0.055,
         '沿闭合路径平行移动一圈，回到起点时方向可能改变；这个方向差就是曲率的可见痕迹',
         ha='center', va='bottom', fontsize=12.2, color='#333333', fontweight='bold')

ax.set_axis_off()
ax.view_init(elev=25, azim=35)
ax.set_box_aspect((1, 1, 1), zoom=1.22)
ax.set_xlim(-1.05, 1.05)
ax.set_ylim(-1.05, 1.05)
ax.set_zlim(-1.05, 1.05)
plt.savefig(out, dpi=150, bbox_inches='tight', pad_inches=0.12)
plt.close()
print(f'{out.name} saved')
