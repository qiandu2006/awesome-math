"""fig3: 连通性与路径连通。"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 3, figsize=(14, 4.8))
titles = ['不连通：两块', '路径连通：能画路径', '连通但路径不连通']

for ax, title in zip(axes, titles):
    ax.set_aspect('equal')
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-1.8, 1.8)
    ax.axis('off')
    ax.set_title(title, fontsize=12.5, fontweight='bold')

# disconnected
axes[0].add_patch(Circle((-0.75, 0), 0.65, facecolor='#E8F0FE', edgecolor='#1A73E8', lw=2))
axes[0].add_patch(Circle((0.85, 0), 0.55, facecolor='#FCE8E6', edgecolor='#D93025', lw=2))
axes[0].text(0, -1.35, r'$\beta_0=2$', ha='center', fontsize=13, fontweight='bold')

# path connected blob
t = np.linspace(0, 2 * np.pi, 400)
r = 1.0 + 0.15 * np.sin(4 * t)
x = r * np.cos(t)
y = 0.75 * r * np.sin(t)
axes[1].fill(x, y, '#E6F4EA', ec='#137333', lw=2)
s = np.linspace(0, 1, 120)
px = -0.7 + 1.35 * s
py = 0.35 * np.sin(np.pi * s)
axes[1].plot(px, py, color='#D93025', lw=3)
axes[1].scatter([-0.7, 0.65], [0, 0], color='#D93025', s=45)
axes[1].text(0, -1.35, '任意两点可由路径连接', ha='center', fontsize=11)

# topologist sine curve impression
axes[2].set_xlim(-0.7, 1.65)
axes[2].set_ylim(-1.35, 1.35)
x = np.linspace(0.035, 1.55, 2600)
y = np.sin(1 / x)
axes[2].plot(x, y, color='#1A73E8', lw=1.25)
axes[2].plot([0, 0], [-1, 1], color='#1A73E8', lw=3.2)
axes[2].scatter([0, 1.48], [0.82, np.sin(1 / 1.48)], color='#D93025', s=50, zorder=5)
axes[2].annotate('极限竖线\n粘在闭包里', xy=(0, 0.75), xytext=(-0.55, 0.95),
                 arrowprops=dict(arrowstyle='->', color='#5F6368', lw=1.5),
                 fontsize=10, ha='center', color='#5F6368')
axes[2].annotate('没有路径能从曲线\n穿到竖线上的点', xy=(0.06, -0.5), xytext=(0.85, -1.12),
                 arrowprops=dict(arrowstyle='->', color='#D93025', lw=1.5),
                 fontsize=10, ha='center', color='#D93025', fontweight='bold')
axes[2].text(0.55, 1.18, r'$\{(x,\sin(1/x))\}\cup\{0\}\times[-1,1]$',
             ha='center', fontsize=8.5, color='#333333')

fig.suptitle('“连在一起”在拓扑里有不同强度', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig3_connectedness.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig3_connectedness.png saved')
