"""fig5: de Rham 上同调——闭形式不一定恰当。"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.set_xlim(-2.4, 2.4)
ax.set_ylim(-2.4, 2.4)
ax.axis('off')

# punctured plane
ax.add_patch(Circle((0, 0), 2.15, facecolor='#E8F0FE', edgecolor='#1A73E8', lw=2, alpha=0.55))
ax.add_patch(Circle((0, 0), 0.28, facecolor='white', edgecolor='#D93025', lw=2.5))
ax.text(0, 0, '洞', ha='center', va='center', fontsize=11, color='#D93025', fontweight='bold')

# vector field for angular form
grid = np.linspace(-1.8, 1.8, 13)
X, Y = np.meshgrid(grid, grid)
R2 = X**2 + Y**2
mask = R2 > 0.22
U = np.zeros_like(X)
V = np.zeros_like(Y)
U[mask] = -Y[mask] / R2[mask]
V[mask] = X[mask] / R2[mask]
norm = np.sqrt(U**2 + V**2)
norm[norm == 0] = 1
U = U / norm
V = V / norm
ax.quiver(X[mask], Y[mask], U[mask], V[mask], color='#1A73E8', alpha=0.75,
          width=0.004, scale=22)

# unit circle integration path
t = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(t), np.sin(t), color='#D93025', lw=3)
ax.arrow(1, 0, -0.02, 0.16, head_width=0.12, head_length=0.16,
         fc='#D93025', ec='#D93025', length_includes_head=True)

ax.text(0, 2.25, r'$\omega=\frac{-y\,dx+x\,dy}{x^2+y^2}$', ha='center',
        fontsize=15, fontweight='bold')
ax.text(0, -2.1, r'$d\omega=0$，但 $\int_{S^1}\omega=2\pi$，所以 $\omega$ 不是全局 $df$',
        ha='center', fontsize=12.5, fontweight='bold', color='#333333')
ax.set_title('闭形式不一定恰当：洞阻止全局势函数存在', fontsize=15, fontweight='bold')

plt.tight_layout()
plt.savefig('../images/fig5_derham_cohomology.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig5_derham_cohomology.png saved')
