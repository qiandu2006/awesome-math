"""fig2: 从单纯复形到链群。"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(13, 6))
ax.set_xlim(0, 13)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_aspect('equal')

# triangulated disk-like complex
pts = np.array([[1.0, 1.0], [2.4, 0.9], [3.1, 2.0], [2.0, 3.0], [0.7, 2.35]])
triangles = [(0, 1, 2), (0, 2, 4), (2, 3, 4)]
for tri in triangles:
    ax.add_patch(Polygon(pts[list(tri)], closed=True, facecolor='#E8F0FE', edgecolor='#1A73E8', lw=2))
for i, p in enumerate(pts):
    ax.scatter([p[0]], [p[1]], color='#202124', s=35)
    ax.text(p[0] - 0.08, p[1] + 0.18, f'$v_{i}$', fontsize=10)
ax.text(1.9, 4.0, '单纯复形 K', ha='center', fontsize=14, fontweight='bold', color='#1A73E8')

def box(x, y, text, color):
    patch = FancyBboxPatch((x, y), 2.4, 0.9, boxstyle='round,pad=0.08',
                           facecolor=color, edgecolor='#5F6368', lw=1.5)
    ax.add_patch(patch)
    ax.text(x + 1.2, y + 0.45, text, ha='center', va='center', fontsize=12, fontweight='bold')

box(5.0, 4.1, '$C_2$: 三角形生成', '#DCE9F9')
box(5.0, 2.55, '$C_1$: 边生成', '#E6F4EA')
box(5.0, 1.0, '$C_0$: 顶点生成', '#FFF4D8')

ax.annotate('', xy=(6.2, 3.55), xytext=(6.2, 4.1), arrowprops=dict(arrowstyle='->', lw=2, color='#D93025'))
ax.annotate('', xy=(6.2, 2.0), xytext=(6.2, 2.55), arrowprops=dict(arrowstyle='->', lw=2, color='#D93025'))
ax.text(6.45, 3.25, '$\\partial_2$', fontsize=13, color='#D93025', fontweight='bold')
ax.text(6.45, 1.7, '$\\partial_1$', fontsize=13, color='#D93025', fontweight='bold')

ax.text(9.2, 4.35, '链 = 单纯形的形式线性组合', fontsize=13, fontweight='bold', color='#333333')
ax.text(9.2, 3.55, '$c_2 = a_1\\sigma_1+a_2\\sigma_2+a_3\\sigma_3$', fontsize=12)
ax.text(9.2, 2.75, '$c_1 = b_1e_1+b_2e_2+\\cdots$', fontsize=12)
ax.text(9.2, 1.95, '$c_0 = r_0v_0+r_1v_1+\\cdots$', fontsize=12)
ax.text(6.7, 0.35, '几何对象 → 向量空间 → 线性映射', ha='center', fontsize=13,
        fontweight='bold', color='#5F6368')

plt.tight_layout()
plt.savefig('../images/fig2_simplicial_chain_complex.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig2_simplicial_chain_complex.png saved')
