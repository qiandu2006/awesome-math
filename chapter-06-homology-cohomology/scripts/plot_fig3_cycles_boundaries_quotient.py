"""fig3: 同调是闭合链除以边界链。"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(9, 7))
ax.set_aspect('equal')
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-2.6, 2.8)
ax.axis('off')

# big cycle space
big = Circle((0, 0), 2.15, facecolor='#E8F0FE', edgecolor='#1A73E8', lw=2.5, alpha=0.9)
small = Circle((-0.65, -0.2), 0.95, facecolor='#FCE8E6', edgecolor='#D93025', lw=2.5, alpha=0.95)
ax.add_patch(big)
ax.add_patch(small)

ax.text(0.35, 1.65, '$Z_k=\\ker\\partial_k$', fontsize=15, fontweight='bold', color='#1A73E8')
ax.text(0.35, 1.35, '闭合链', fontsize=12, color='#1A73E8')
ax.text(-1.4, -0.25, '$B_k=\\operatorname{im}\\partial_{k+1}$', fontsize=12,
        fontweight='bold', color='#D93025', ha='center')
ax.text(-1.35, -0.55, '边界链', fontsize=11, color='#D93025', ha='center')

ax.arrow(1.6, -0.1, 1.25, 0, head_width=0.14, head_length=0.2,
         fc='#5F6368', ec='#5F6368', lw=2, length_includes_head=True)
ax.text(2.25, 0.18, '取商', ha='center', fontsize=12, fontweight='bold', color='#5F6368')

ax.add_patch(Circle((3.15, 0), 0.45, facecolor='#E6F4EA', edgecolor='#137333', lw=2))
ax.text(3.15, 0, '$H_k$', ha='center', va='center', fontsize=14, fontweight='bold', color='#137333')

ax.text(0, -2.25, '$H_k = Z_k/B_k$: 把已经被填住的边界当作 0，剩下的就是洞',
        ha='center', fontsize=13, fontweight='bold', color='#333333')
ax.set_title('同调的商空间图像', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.savefig('../images/fig3_cycles_boundaries_quotient.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig3_cycles_boundaries_quotient.png saved')
