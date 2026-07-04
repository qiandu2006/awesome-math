"""fig2: 支撑超平面与凸函数。"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-2.2, 2.2, 500)
f = np.exp(0.45 * x) + 0.15 * x**2
x0 = 0.35
f0 = np.exp(0.45 * x0) + 0.15 * x0**2
grad = 0.45 * np.exp(0.45 * x0) + 0.3 * x0
tangent = f0 + grad * (x - x0)

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(x, f, color='#1A73E8', lw=3, label='$f(x)$')
ax.plot(x, tangent, color='#D93025', lw=2.5, linestyle='--', label='支撑线')
ax.scatter([x0], [f0], color='#D93025', s=70, zorder=5)
ax.fill_between(x, tangent, f, where=f >= tangent, color='#E8F0FE', alpha=0.7)
ax.text(-1.9, 2.8, r'$f(y)\geq f(x)+\nabla f(x)^T(y-x)$',
        fontsize=13, fontweight='bold', color='#333333')
ax.text(x0 + 0.15, f0 - 0.35, '切线给出全局下界', fontsize=11, color='#D93025',
        fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('凸函数的切线是全局支撑下界', fontsize=15, fontweight='bold')
ax.legend()
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('../images/fig2_supporting_hyperplane.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig2_supporting_hyperplane.png saved')
