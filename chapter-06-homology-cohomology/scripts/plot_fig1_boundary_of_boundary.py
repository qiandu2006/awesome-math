"""fig1: 边界的边界为零。"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 3, figsize=(13, 4.6))
for ax in axes:
    ax.set_aspect('equal')
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.5, 1.7)
    ax.axis('off')

# simplex
pts = np.array([[-1.0, -0.6], [1.0, -0.6], [0.0, 1.05]])
axes[0].add_patch(Polygon(pts, closed=True, facecolor='#E8F0FE', edgecolor='#1A73E8', lw=2.5))
for i, p in enumerate(pts):
    axes[0].scatter([p[0]], [p[1]], color='#202124', s=35)
    axes[0].text(p[0] + 0.06, p[1] + 0.06, f'$v_{i}$', fontsize=11)
axes[0].set_title('2-单纯形', fontsize=13, fontweight='bold')
axes[0].text(0, -1.25, r'$[v_0,v_1,v_2]$', ha='center', fontsize=12)

# boundary edges
edges = [(0, 1), (1, 2), (2, 0)]
colors = ['#D93025', '#F4B400', '#34A853']
for (i, j), c in zip(edges, colors):
    a, b = pts[i], pts[j]
    axes[1].plot([a[0], b[0]], [a[1], b[1]], color=c, lw=4)
    mid = (a + b) / 2
    direction = b - a
    direction = direction / np.linalg.norm(direction)
    axes[1].arrow(mid[0] - 0.08 * direction[0], mid[1] - 0.08 * direction[1],
                  0.16 * direction[0], 0.16 * direction[1],
                  head_width=0.09, head_length=0.12, fc=c, ec=c)
axes[1].set_title('一次边界：三条有向边', fontsize=13, fontweight='bold')
axes[1].text(0, -1.25, r'$\partial_2[v_0,v_1,v_2]$', ha='center', fontsize=12)

# boundary of boundary cancellation
for p in pts:
    axes[2].scatter([p[0]], [p[1]], color='#D93025', s=65)
    axes[2].scatter([p[0] + 0.12], [p[1] + 0.02], color='#1A73E8', s=65, marker='x')
axes[2].text(0, 0.1, '顶点两两抵消', ha='center', fontsize=13, fontweight='bold', color='#5F6368')
axes[2].set_title('再取边界：0', fontsize=13, fontweight='bold')
axes[2].text(0, -1.25, r'$\partial_1\partial_2=0$', ha='center', fontsize=12)

for i in [0, 1]:
    pos1 = axes[i].get_position()
    pos2 = axes[i + 1].get_position()
    arr = FancyArrowPatch((pos1.x1 + 0.01, (pos1.y0 + pos1.y1) / 2),
                          (pos2.x0 - 0.01, (pos2.y0 + pos2.y1) / 2),
                          transform=fig.transFigure, arrowstyle='->',
                          mutation_scale=18, lw=2, color='#5F6368')
    fig.patches.append(arr)

fig.suptitle('同调的源头：边界的边界为零', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig1_boundary_of_boundary.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig1_boundary_of_boundary.png saved')
