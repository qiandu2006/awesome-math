"""fig2: 布朗运动连续但不可微。"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

rng = np.random.default_rng(7)
T = 1.0
n = 4000
dt = T / n
t = np.linspace(0, T, n + 1)
B = np.r_[0, np.cumsum(np.sqrt(dt) * rng.normal(size=n))]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))
ax1.plot(t, B, color='#1A73E8', lw=1.4)
ax1.set_title('整体看：路径连续', fontsize=13, fontweight='bold')
ax1.set_xlabel('t')
ax1.set_ylabel('$B_t$')
ax1.grid(alpha=0.25)

start, end = 0.44, 0.50
mask = (t >= start) & (t <= end)
ax2.plot(t[mask], B[mask], color='#D93025', lw=1.4)
ax2.set_title('局部放大：仍然粗糙', fontsize=13, fontweight='bold')
ax2.set_xlabel('t')
ax2.grid(alpha=0.25)

for ax in (ax1, ax2):
    ax.text(0.03, 0.08, r'典型增量 $|\Delta B|\sim\sqrt{\Delta t}$',
            transform=ax.transAxes, fontsize=11,
            bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#5F6368'))

fig.suptitle('布朗路径没有跳跃，但没有稳定切线', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig2_brownian_nowhere_differentiable.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig2_brownian_nowhere_differentiable.png saved')
