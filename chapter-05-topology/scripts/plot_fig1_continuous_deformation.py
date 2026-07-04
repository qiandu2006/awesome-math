"""fig1: 连续变形与拓扑等价。"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 3, figsize=(13, 4.8))

t = np.linspace(0, 2 * np.pi, 600)

def draw_torus_like(ax, cx, title, phase):
    r_outer = 1.35 + 0.12 * np.sin(3 * t + phase)
    r_inner = 0.45 + 0.05 * np.cos(4 * t + phase)
    x_outer = cx + r_outer * np.cos(t)
    y_outer = r_outer * np.sin(t)
    x_inner = cx + r_inner * np.cos(t)
    y_inner = r_inner * np.sin(t)
    ax.fill(x_outer, y_outer, '#DCE9F9', ec='#1A73E8', lw=2)
    ax.fill(x_inner, y_inner, 'white', ec='#1A73E8', lw=2)
    ax.set_aspect('equal')
    ax.set_xlim(cx - 1.8, cx + 1.8)
    ax.set_ylim(-1.65, 1.65)
    ax.axis('off')
    ax.set_title(title, fontsize=13, fontweight='bold')
    ax.text(cx, 0.05, r'$\beta_1=1$', ha='center', va='center',
            fontsize=14, fontweight='bold', color='#D93025')

draw_torus_like(axes[0], 0, '甜甜圈形状', 0.0)
draw_torus_like(axes[1], 0, '连续拉伸', 0.9)
draw_torus_like(axes[2], 0, '仍然只有一个洞', 1.8)

for ax in axes:
    ax.text(0, -1.92, '不撕裂，不粘合', ha='center', fontsize=10, color='#555555')

for i in [0, 1]:
    pos1 = axes[i].get_position()
    pos2 = axes[i + 1].get_position()
    arrow = FancyArrowPatch((pos1.x1 + 0.01, (pos1.y0 + pos1.y1) / 2),
                            (pos2.x0 - 0.01, (pos2.y0 + pos2.y1) / 2),
                            transform=fig.transFigure, arrowstyle='->',
                            mutation_scale=18, lw=2, color='#5F6368')
    fig.patches.append(arrow)

fig.suptitle('拓扑等价：形状可变，但洞这类不变量保持不变', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig1_continuous_deformation.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig1_continuous_deformation.png saved')
