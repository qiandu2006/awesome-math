"""fig4: 自然变换。"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(9, 7))
ax.set_xlim(0, 9)
ax.set_ylim(0, 7)
ax.axis('off')

nodes = {
    'F(A)': (2.2, 5.2),
    'F(B)': (6.6, 5.2),
    'G(A)': (2.2, 2.0),
    'G(B)': (6.6, 2.0),
}

for label, (x, y) in nodes.items():
    color = '#1A73E8' if label.startswith('F') else '#137333'
    ax.add_patch(Circle((x, y), 0.42, facecolor='white', edgecolor=color, lw=2))
    ax.text(x, y, label, ha='center', va='center', fontsize=12, fontweight='bold')

def arrow(a, b, label, color='#5F6368', offset=(0, 0)):
    p1, p2 = nodes[a], nodes[b]
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle='->', mutation_scale=16,
                                 lw=2.2, color=color, shrinkA=30, shrinkB=30))
    ax.text((p1[0] + p2[0]) / 2 + offset[0], (p1[1] + p2[1]) / 2 + offset[1],
            label, fontsize=13, fontweight='bold', color=color, ha='center')

arrow('F(A)', 'F(B)', '$F(f)$', '#1A73E8', (0, 0.3))
arrow('G(A)', 'G(B)', '$G(f)$', '#137333', (0, -0.35))
arrow('F(A)', 'G(A)', '$\\eta_A$', '#D93025', (-0.45, 0))
arrow('F(B)', 'G(B)', '$\\eta_B$', '#D93025', (0.45, 0))

ax.text(4.4, 3.6, '$G(f)\\circ\\eta_A = \\eta_B\\circ F(f)$',
        ha='center', fontsize=16, fontweight='bold', color='#5F6368')
ax.text(4.4, 0.75, '自然性：先变对象再用 G，或先用 F 再变对象，结果一致',
        ha='center', fontsize=12.5, fontweight='bold', color='#333333')
ax.set_title('自然变换：函子之间与所有态射相容的映射', fontsize=15, fontweight='bold')

plt.tight_layout()
plt.savefig('../images/fig4_natural_transformation.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig4_natural_transformation.png saved')
