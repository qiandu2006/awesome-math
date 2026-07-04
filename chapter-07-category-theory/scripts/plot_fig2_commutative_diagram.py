"""fig2: 交换图。"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(8, 7))
ax.set_xlim(0, 8)
ax.set_ylim(0, 7)
ax.axis('off')

nodes = {'A': (2, 5), 'B': (6, 5), 'C': (2, 2), 'D': (6, 2)}
for label, (x, y) in nodes.items():
    ax.add_patch(Circle((x, y), 0.38, facecolor='#FFF4D8', edgecolor='#A05A00', lw=2))
    ax.text(x, y, label, ha='center', va='center', fontsize=15, fontweight='bold')

def arrow(start, end, text, color='#5F6368', offset=(0, 0)):
    x1, y1 = nodes[start]
    x2, y2 = nodes[end]
    arr = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='->',
                          mutation_scale=16, lw=2.2, color=color,
                          shrinkA=28, shrinkB=28)
    ax.add_patch(arr)
    ax.text((x1 + x2) / 2 + offset[0], (y1 + y2) / 2 + offset[1],
            text, fontsize=13, fontweight='bold', color=color, ha='center')

arrow('A', 'B', '$f$', offset=(0, 0.3))
arrow('A', 'C', '$g$', offset=(-0.35, 0))
arrow('B', 'D', '$h$', offset=(0.35, 0))
arrow('C', 'D', '$k$', offset=(0, -0.35))

ax.text(4, 3.5, '$h\\circ f = k\\circ g$', ha='center', va='center',
        fontsize=18, fontweight='bold', color='#D93025')
ax.text(4, 0.8, '同一个起点和终点的不同路径给出同一个态射', ha='center',
        fontsize=13, fontweight='bold', color='#333333')
ax.set_title('交换图：路径相同就是等式', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.savefig('../images/fig2_commutative_diagram.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig2_commutative_diagram.png saved')
