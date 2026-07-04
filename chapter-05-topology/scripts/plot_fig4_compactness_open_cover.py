"""fig4: 紧性——从开覆盖中选出有限子覆盖。"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))
for ax in (ax1, ax2):
    ax.set_aspect('equal')
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.55, 1.75)
    ax.axis('off')

t = np.linspace(0, 2 * np.pi, 400)
disk_x, disk_y = np.cos(t), np.sin(t)

centers = [(-0.7, 0.25), (-0.15, 0.55), (0.55, 0.2), (0.1, -0.35),
           (-0.85, -0.45), (0.85, -0.35), (0.0, 0.05)]
radii = [0.75, 0.65, 0.72, 0.78, 0.55, 0.55, 0.62]
colors = ['#DCE9F9', '#E6F4EA', '#FFF4D8', '#FCE8E6', '#E8EAED', '#E0F2F1', '#F3E8FD']

for (cx, cy), r, c in zip(centers, radii, colors):
    ax1.add_patch(Circle((cx, cy), r, facecolor=c, edgecolor='#5F6368', lw=1.2, alpha=0.62))
ax1.plot(disk_x, disk_y, color='#202124', lw=2)
ax1.set_title('开覆盖：很多开集盖住空间', fontsize=13, fontweight='bold')
ax1.text(0, -1.35, '可以是无限多个开集', ha='center', fontsize=11, color='#5F6368')

selected = [0, 2, 3, 4]
for idx in selected:
    (cx, cy), r, c = centers[idx], radii[idx], colors[idx]
    ax2.add_patch(Circle((cx, cy), r, facecolor=c, edgecolor='#D93025', lw=2.3, alpha=0.68))
ax2.plot(disk_x, disk_y, color='#202124', lw=2)
ax2.set_title('紧性：可挑出有限子覆盖', fontsize=13, fontweight='bold')
ax2.text(0, -1.35, '有限个仍然盖住整个空间', ha='center', fontsize=11,
         color='#D93025', fontweight='bold')

fig.suptitle('紧性 = 无限覆盖问题能被有限数据控制', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig4_compactness_open_cover.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig4_compactness_open_cover.png saved')
