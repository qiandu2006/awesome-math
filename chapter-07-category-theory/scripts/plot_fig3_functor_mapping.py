"""fig3: 函子把对象和态射一起搬运。"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 6)
ax.axis('off')

left_box = FancyBboxPatch((0.7, 0.8), 4.2, 4.4, boxstyle='round,pad=0.12',
                          facecolor='#E8F0FE', edgecolor='#1A73E8', lw=2)
right_box = FancyBboxPatch((7.1, 0.8), 4.2, 4.4, boxstyle='round,pad=0.12',
                           facecolor='#E6F4EA', edgecolor='#137333', lw=2)
ax.add_patch(left_box)
ax.add_patch(right_box)
ax.text(2.8, 5.45, '范畴 $\\mathcal{C}$', ha='center', fontsize=14, fontweight='bold', color='#1A73E8')
ax.text(9.2, 5.45, '范畴 $\\mathcal{D}$', ha='center', fontsize=14, fontweight='bold', color='#137333')

left_nodes = {'A': (1.8, 3.8), 'B': (3.8, 2.2)}
right_nodes = {'F(A)': (8.1, 3.8), 'F(B)': (10.0, 2.2)}

for label, (x, y) in left_nodes.items():
    ax.add_patch(Circle((x, y), 0.32, facecolor='white', edgecolor='#1A73E8', lw=2))
    ax.text(x, y, label, ha='center', va='center', fontsize=12, fontweight='bold')
for label, (x, y) in right_nodes.items():
    ax.add_patch(Circle((x, y), 0.38, facecolor='white', edgecolor='#137333', lw=2))
    ax.text(x, y, label, ha='center', va='center', fontsize=11, fontweight='bold')

def arr(p1, p2, label, color):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle='->', mutation_scale=16,
                                 lw=2, color=color, shrinkA=22, shrinkB=22))
    ax.text((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 + 0.28,
            label, fontsize=12, fontweight='bold', color=color, ha='center')

arr(left_nodes['A'], left_nodes['B'], '$f$', '#1A73E8')
arr(right_nodes['F(A)'], right_nodes['F(B)'], '$F(f)$', '#137333')
arr((4.9, 3.2), (7.1, 3.2), '$F$', '#D93025')

ax.text(6, 0.35, '$F(g\\circ f)=F(g)\\circ F(f)$，函子保留组合关系',
        ha='center', fontsize=13, fontweight='bold', color='#333333')
ax.set_title('函子：范畴之间的结构保持映射', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.savefig('../images/fig3_functor_mapping.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig3_functor_mapping.png saved')
