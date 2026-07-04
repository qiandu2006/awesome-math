"""fig4: 熵、条件熵与互信息。"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(9, 6))
ax.set_aspect('equal')
ax.set_xlim(0, 9)
ax.set_ylim(0, 6)
ax.axis('off')

left = Circle((3.6, 3), 1.75, facecolor='#E8F0FE', edgecolor='#1A73E8', lw=2.5, alpha=0.75)
right = Circle((5.4, 3), 1.75, facecolor='#E6F4EA', edgecolor='#137333', lw=2.5, alpha=0.75)
ax.add_patch(left)
ax.add_patch(right)

ax.text(2.45, 4.55, '$H(X)$', fontsize=15, fontweight='bold', color='#1A73E8')
ax.text(6.15, 4.55, '$H(Y)$', fontsize=15, fontweight='bold', color='#137333')
ax.text(4.5, 3.05, '$I(X;Y)$', ha='center', va='center', fontsize=16,
        fontweight='bold', color='#D93025')
ax.text(3.0, 2.0, '$H(X|Y)$', ha='center', fontsize=13, color='#1A73E8', fontweight='bold')
ax.text(6.0, 2.0, '$H(Y|X)$', ha='center', fontsize=13, color='#137333', fontweight='bold')
ax.text(4.5, 0.7, '互信息 = 两个变量共享的不确定性减少量', ha='center',
        fontsize=14, fontweight='bold')
ax.set_title('互信息：知道一个变量后，另一个变量少了多少不确定性',
             fontsize=15, fontweight='bold')

plt.tight_layout()
plt.savefig('../images/fig4_mutual_information.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig4_mutual_information.png saved')
