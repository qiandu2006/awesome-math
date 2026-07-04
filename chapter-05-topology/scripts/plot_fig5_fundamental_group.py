"""fig4: 基本群与不可收缩回路。"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))
for ax in (ax1, ax2):
    ax.set_aspect('equal')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.axis('off')

# disk
ax1.add_patch(Circle((0, 0), 1.35, facecolor='#E6F4EA', edgecolor='#137333', lw=2))
for r, alpha in [(1.0, 0.9), (0.65, 0.7), (0.28, 0.5)]:
    ax1.add_patch(Circle((0, 0), r, fill=False, edgecolor='#D93025', lw=2, alpha=alpha))
ax1.scatter([0], [0], color='#D93025', s=45)
ax1.set_title('圆盘：闭合路径可收缩', fontsize=13, fontweight='bold')
ax1.text(0, -1.65, r'$\pi_1(D^2)=0$', ha='center', fontsize=14, fontweight='bold', color='#137333')

# annulus
ax2.add_patch(Circle((0, 0), 1.35, facecolor='#E8F0FE', edgecolor='#1A73E8', lw=2))
ax2.add_patch(Circle((0, 0), 0.55, facecolor='white', edgecolor='#1A73E8', lw=2))
theta = np.linspace(0, 2 * np.pi, 300)
ax2.plot(0.95 * np.cos(theta), 0.95 * np.sin(theta), color='#D93025', lw=3)
ax2.arrow(0.95, 0, -0.02, 0.18, head_width=0.12, head_length=0.16,
          fc='#D93025', ec='#D93025', length_includes_head=True)
ax2.set_title('圆环：绕洞路径不能收缩', fontsize=13, fontweight='bold')
ax2.text(0, -1.65, r'$\pi_1(S^1)\cong\mathbb{Z}$', ha='center', fontsize=14,
         fontweight='bold', color='#1A73E8')

fig.suptitle('基本群记录闭合路径的绕洞方式', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig5_fundamental_group.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig5_fundamental_group.png saved')
