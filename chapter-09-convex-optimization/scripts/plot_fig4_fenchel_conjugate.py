"""fig4: Fenchel 共轭与对偶下界。"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-2.2, 2.8, 500)
f = 0.5 * x**2 + 0.35
y = 1.1
x_star = y
f_star = 0.5 * y**2 + 0.35
intercept = x_star * y - f_star
line = y * x - (0.5 * y**2 - 0.35)

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(x, f, color='#1A73E8', lw=3, label='$f(x)$')
ax.plot(x, line, color='#D93025', lw=2.5, linestyle='--', label='斜率为 y 的支撑线')
ax.scatter([x_star], [f_star], color='#D93025', s=70, zorder=5)
ax.annotate('', xy=(x_star, y * x_star), xytext=(x_star, f_star),
            arrowprops=dict(arrowstyle='<->', color='#137333', lw=2))
ax.text(x_star + 0.12, (y * x_star + f_star) / 2,
        r'$f^*(y)$', color='#137333', fontsize=13, fontweight='bold')
ax.text(-2.0, 3.8, r'$f^*(y)=\sup_x\{\langle y,x\rangle-f(x)\}$',
        fontsize=13, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('value')
ax.set_title('Fenchel 共轭：从斜率空间看函数', fontsize=15, fontweight='bold')
ax.legend()
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('../images/fig4_fenchel_conjugate.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig4_fenchel_conjugate.png saved')
