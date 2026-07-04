"""fig1: 范畴中的对象与态射。"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

nodes = {
    'A': (2, 3.8),
    'B': (5, 4.2),
    'C': (7.7, 2.3),
}

for label, (x, y) in nodes.items():
    ax.add_patch(Circle((x, y), 0.42, facecolor='#E8F0FE', edgecolor='#1A73E8', lw=2))
    ax.text(x, y, label, ha='center', va='center', fontsize=16, fontweight='bold', color='#1A73E8')

def arrow(a, b, label, rad=0.0, color='#5F6368'):
    x1, y1 = nodes[a]
    x2, y2 = nodes[b]
    arr = FancyArrowPatch((x1 + 0.4, y1), (x2 - 0.4, y2),
                          connectionstyle=f'arc3,rad={rad}',
                          arrowstyle='->', mutation_scale=16, lw=2, color=color)
    ax.add_patch(arr)
    ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.35, label, fontsize=13,
            fontweight='bold', color=color, ha='center')

arrow('A', 'B', '$f$')
arrow('B', 'C', '$g$')
arrow('A', 'C', '$g\\circ f$', rad=-0.18, color='#D93025')

# identity loops
for label, (x, y) in nodes.items():
    loop = FancyArrowPatch((x - 0.1, y + 0.42), (x + 0.1, y + 0.42),
                           connectionstyle='arc3,rad=1.8',
                           arrowstyle='->', mutation_scale=12, lw=1.8, color='#137333')
    ax.add_patch(loop)
    ax.text(x, y + 0.9, f'$id_{label}$', fontsize=11, color='#137333', ha='center')

ax.text(5, 0.75, '范畴 = 对象 + 态射 + 可结合的组合 + 单位态射', ha='center',
        fontsize=14, fontweight='bold', color='#333333')
ax.set_title('从对象转向对象之间的箭头', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.savefig('../images/fig1_category_objects_morphisms.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig1_category_objects_morphisms.png saved')
