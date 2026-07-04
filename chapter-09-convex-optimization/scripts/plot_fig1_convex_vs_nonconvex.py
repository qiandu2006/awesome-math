"""fig1: 凸优化与非凸优化的地形差异。"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-3, 3, 600)
convex = 0.35 * (x - 0.3) ** 2 + 0.2
nonconvex = 0.12 * x**4 - 0.7 * x**2 + 0.25 * x + 1.8

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.2))

ax1.plot(x, convex, color='#1A73E8', lw=3)
ax1.scatter([0.3], [0.2], color='#D93025', s=70, zorder=5)
ax1.set_title('凸：一个盆地', fontsize=13, fontweight='bold')
ax1.text(0.3, 0.55, '局部最优\n= 全局最优', ha='center', fontsize=11,
         color='#D93025', fontweight='bold')
ax1.grid(alpha=0.25)

ax2.plot(x, nonconvex, color='#5F6368', lw=3)
mins = [-1.85, 1.65]
for m in mins:
    y = 0.12 * m**4 - 0.7 * m**2 + 0.25 * m + 1.8
    ax2.scatter([m], [y], color='#D93025', s=70, zorder=5)
ax2.text(-1.85, 0.15, '局部最优', ha='center', fontsize=11, color='#D93025', fontweight='bold')
ax2.text(1.65, 0.45, '另一个谷底', ha='center', fontsize=11, color='#D93025', fontweight='bold')
ax2.set_title('非凸：多个谷底', fontsize=13, fontweight='bold')
ax2.grid(alpha=0.25)

for ax in (ax1, ax2):
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

fig.suptitle('凸性把局部信息变成全局保证', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig1_convex_vs_nonconvex.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig1_convex_vs_nonconvex.png saved')
