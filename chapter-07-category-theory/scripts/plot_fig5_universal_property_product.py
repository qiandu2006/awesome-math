"""fig5: 乘积的泛性质。"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(9, 7))
ax.set_xlim(0, 9)
ax.set_ylim(0, 7)
ax.axis('off')

nodes = {
    'X': (4.5, 5.8),
    'P=A×B': (4.5, 3.4),
    'A': (2.0, 1.4),
    'B': (7.0, 1.4),
}

for label, (x, y) in nodes.items():
    color = '#D93025' if label == 'P=A×B' else '#1A73E8'
    ax.add_patch(Circle((x, y), 0.48, facecolor='white', edgecolor=color, lw=2.2))
    ax.text(x, y, label, ha='center', va='center', fontsize=12, fontweight='bold', color=color)

def arrow(a, b, label, color='#5F6368', style='solid', offset=(0, 0)):
    p1, p2 = nodes[a], nodes[b]
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle='->', mutation_scale=16,
                                 lw=2.2, color=color, linestyle=style,
                                 shrinkA=34, shrinkB=34))
    ax.text((p1[0] + p2[0]) / 2 + offset[0], (p1[1] + p2[1]) / 2 + offset[1],
            label, fontsize=13, fontweight='bold', color=color, ha='center')

arrow('P=A×B', 'A', '$\\pi_A$', '#D93025', offset=(-0.25, -0.1))
arrow('P=A×B', 'B', '$\\pi_B$', '#D93025', offset=(0.25, -0.1))
arrow('X', 'A', '$f$', '#1A73E8', style='dashed', offset=(-0.45, 0.2))
arrow('X', 'B', '$g$', '#1A73E8', style='dashed', offset=(0.45, 0.2))
arrow('X', 'P=A×B', '$\\exists!\\,u$', '#137333', offset=(0.55, 0))

ax.text(4.5, 0.45, '$\\pi_A\\circ u=f,\\quad \\pi_B\\circ u=g$',
        ha='center', fontsize=15, fontweight='bold', color='#333333')
ax.set_title('乘积的泛性质：由映射关系定义对象', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.savefig('../images/fig5_universal_property_product.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig5_universal_property_product.png saved')
