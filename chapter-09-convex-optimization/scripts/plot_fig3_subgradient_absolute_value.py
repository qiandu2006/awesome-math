"""fig3: |x| 在尖点处的次梯度。"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-2.5, 2.5, 500)
f = np.abs(x)
slopes = [-1.0, -0.45, 0.0, 0.55, 1.0]

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(x, f, color='#1A73E8', lw=3, label='$|x|$')
for m in slopes:
    ax.plot(x, m * x, lw=1.8, linestyle='--', alpha=0.9,
            label=f'斜率 {m:g}' if m in [-1, 0, 1] else None)
ax.scatter([0], [0], color='#D93025', s=75, zorder=5)
ax.text(0.15, 0.25, r'$\partial |0|=[-1,1]$', fontsize=14,
        color='#D93025', fontweight='bold')
ax.text(-2.25, 2.25, '尖点没有唯一梯度\n但有一整族支撑线', fontsize=12,
        bbox=dict(boxstyle='round,pad=0.35', fc='white', ec='#5F6368'))
ax.set_ylim(-1.1, 2.8)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('次梯度：不可微点仍有一阶几何', fontsize=15, fontweight='bold')
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('../images/fig3_subgradient_absolute_value.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig3_subgradient_absolute_value.png saved')
