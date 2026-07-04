"""fig2: 开集与邻域。"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

for ax in (ax1, ax2):
    ax.set_aspect('equal')
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.0, 2.0)
    ax.axis('off')

# open disk
disk = Circle((0, 0), 1.25, facecolor='#E8F0FE', edgecolor='#1A73E8', lw=2, linestyle='--')
ax1.add_patch(disk)
points = [(-0.45, 0.35), (0.55, -0.2), (0.95, 0.45)]
for p in points:
    ax1.scatter([p[0]], [p[1]], color='#D93025', s=55, zorder=5)
    small = Circle(p, 0.28, facecolor='#FCE8E6', edgecolor='#D93025', alpha=0.65, lw=1.5)
    ax1.add_patch(small)
ax1.text(0, 1.55, '开集：每个点周围\n还能放进一个小邻域', ha='center',
         fontsize=12, fontweight='bold', color='#1A73E8')

# closed square with boundary point
rect = Rectangle((-1.2, -1.2), 2.4, 2.4, facecolor='#E6F4EA', edgecolor='#137333', lw=2)
ax2.add_patch(rect)
boundary = (1.2, 0.35)
ax2.scatter([boundary[0]], [boundary[1]], color='#D93025', s=65, zorder=5)
circle = Circle(boundary, 0.42, facecolor='#FCE8E6', edgecolor='#D93025', alpha=0.55, lw=1.5)
ax2.add_patch(circle)
ax2.text(0, 1.62, '边界点：任何小邻域\n都会伸到集合外面', ha='center',
         fontsize=12, fontweight='bold', color='#137333')
ax2.text(1.25, -1.55, '这说明它不是开集', ha='right', fontsize=11, color='#D93025')

fig.suptitle('开集把“靠近”变成一种结构，而不必先指定距离公式', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig2_open_sets_neighborhoods.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig2_open_sets_neighborhoods.png saved')
