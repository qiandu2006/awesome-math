"""fig5: 同调与 Betti 数。"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 4, figsize=(14, 4.8))
names = ['圆盘 $D^2$', '圆 $S^1$', '球面 $S^2$', '环面 $T^2$']
betti = [r'$(1,0,0)$', r'$(1,1,0)$', r'$(1,0,1)$', r'$(1,2,1)$']

for ax, name, b in zip(axes, names, betti):
    ax.set_aspect('equal')
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.8, 1.8)
    ax.axis('off')
    ax.set_title(name, fontsize=12.5, fontweight='bold')
    ax.text(0, -1.55, r'$(\beta_0,\beta_1,\beta_2)=$' + b, ha='center', fontsize=10.5)

# disk
axes[0].add_patch(Circle((0, 0), 1.0, facecolor='#E6F4EA', edgecolor='#137333', lw=2))
axes[0].text(0, 0, '无洞', ha='center', va='center', fontsize=11, color='#137333', fontweight='bold')

# circle
axes[1].add_patch(Circle((0, 0), 1.0, fill=False, edgecolor='#D93025', lw=4))
axes[1].text(0, 0, '1 个\n一维洞', ha='center', va='center', fontsize=11, color='#D93025', fontweight='bold')

# sphere as shaded disk boundary
theta = np.linspace(0, 2 * np.pi, 300)
axes[2].add_patch(Circle((0, 0), 1.0, facecolor='#E8F0FE', edgecolor='#1A73E8', lw=2, alpha=0.9))
axes[2].plot(np.cos(theta), 0.28 * np.sin(theta), color='#1A73E8', lw=1.5, alpha=0.7)
axes[2].text(0, 0.05, '1 个\n二维空腔', ha='center', va='center', fontsize=11,
             color='#1A73E8', fontweight='bold')

# torus schematic
t = np.linspace(0, 2 * np.pi, 500)
outer = 1.15
inner = 0.42
axes[3].fill(outer * np.cos(t), outer * np.sin(t), '#FFF4D8', ec='#A05A00', lw=2)
axes[3].fill(inner * np.cos(t), inner * np.sin(t), 'white', ec='#A05A00', lw=2)
axes[3].plot(0.78 * np.cos(t), 0.78 * np.sin(t), color='#D93025', lw=2.2)
axes[3].plot([0, 0], [-1.12, 1.12], color='#1A73E8', lw=2.2)
axes[3].text(0, 0, '2 个\n一维洞', ha='center', va='center', fontsize=10.5,
             color='#A05A00', fontweight='bold')

fig.suptitle('同调用 Betti 数记录各维度的洞', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig6_homology_holes.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig6_homology_holes.png saved')
