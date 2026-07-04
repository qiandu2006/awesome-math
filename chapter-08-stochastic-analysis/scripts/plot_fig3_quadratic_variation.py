"""fig3: 二次变差——布朗运动和光滑路径的差别。"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

rng = np.random.default_rng(10)
T = 1.0
n_max = 2**15
dt = T / n_max
increments = np.sqrt(dt) * rng.normal(size=n_max)
B = np.r_[0, np.cumsum(increments)]
t_full = np.linspace(0, T, n_max + 1)
smooth = np.sin(2 * np.pi * t_full)

levels = np.arange(4, 15)
ns = 2**levels
qv_b = []
qv_s = []
for n in ns:
    step = n_max // n
    b_sub = B[::step]
    s_sub = smooth[::step]
    qv_b.append(np.sum(np.diff(b_sub) ** 2))
    qv_s.append(np.sum(np.diff(s_sub) ** 2))

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(ns, qv_b, 'o-', color='#1A73E8', lw=2, label='布朗运动')
ax.plot(ns, qv_s, 'o-', color='#D93025', lw=2, label='光滑路径 $\\sin(2\\pi t)$')
ax.axhline(T, color='#1A73E8', linestyle='--', alpha=0.7, label='$T=1$')
ax.set_xscale('log', base=2)
ax.set_xlabel('分割区间数 n')
ax.set_ylabel(r'$\sum_i (\Delta X_i)^2$')
ax.set_title('二次变差：光滑路径趋于 0，布朗运动趋于 T', fontsize=15, fontweight='bold')
ax.legend()
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('../images/fig3_quadratic_variation.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig3_quadratic_variation.png saved')
