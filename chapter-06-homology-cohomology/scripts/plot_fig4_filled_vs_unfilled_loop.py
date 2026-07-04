"""fig4: 填充如何杀死一维洞。"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))
for ax in (ax1, ax2):
    ax.set_aspect('equal')
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.8, 1.8)
    ax.axis('off')

n = 8
theta = np.linspace(0, 2 * np.pi, n, endpoint=False)
outer = np.c_[1.15 * np.cos(theta), 1.15 * np.sin(theta)]
center = np.array([0.0, 0.0])

# unfilled loop
for i in range(n):
    a, b = outer[i], outer[(i + 1) % n]
    ax1.plot([a[0], b[0]], [a[1], b[1]], color='#D93025', lw=3)
for p in outer:
    ax1.scatter([p[0]], [p[1]], color='#202124', s=25)
ax1.add_patch(Circle((0, 0), 0.48, fill=False, edgecolor='#1A73E8', lw=2, linestyle='--'))
ax1.text(0, 0, '没有 2-链\n可填充', ha='center', va='center', fontsize=11, color='#1A73E8', fontweight='bold')
ax1.set_title('未填充：回路代表洞', fontsize=13, fontweight='bold')
ax1.text(0, -1.55, '$H_1\\cong\\mathbb{R}$', ha='center', fontsize=14, fontweight='bold', color='#D93025')

# filled disk triangulated
for i in range(n):
    tri = np.vstack([center, outer[i], outer[(i + 1) % n]])
    ax2.add_patch(Polygon(tri, closed=True, facecolor='#E6F4EA', edgecolor='#137333', lw=1.5, alpha=0.9))
for i in range(n):
    a, b = outer[i], outer[(i + 1) % n]
    ax2.plot([a[0], b[0]], [a[1], b[1]], color='#D93025', lw=3)
for p in outer:
    ax2.scatter([p[0]], [p[1]], color='#202124', s=25)
ax2.scatter([0], [0], color='#202124', s=25)
ax2.text(0, 0, '2-链填住\n外圈回路', ha='center', va='center', fontsize=11, color='#137333', fontweight='bold')
ax2.set_title('填充后：回路成为边界', fontsize=13, fontweight='bold')
ax2.text(0, -1.55, '$H_1=0$', ha='center', fontsize=14, fontweight='bold', color='#137333')

fig.suptitle('同一个闭合回路：是否是洞，取决于能否被更高维对象填住', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig4_filled_vs_unfilled_loop.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig4_filled_vs_unfilled_loop.png saved')
