"""fig1: 随机过程的多条样本路径。"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

rng = np.random.default_rng(42)
T = 1.0
n = 500
dt = T / n
t = np.linspace(0, T, n + 1)

fig, ax = plt.subplots(figsize=(11, 6))
for i in range(8):
    increments = np.sqrt(dt) * rng.normal(size=n)
    path = np.r_[0, np.cumsum(increments)]
    ax.plot(t, path, lw=1.8, alpha=0.85)

ax.axhline(0, color='#5F6368', lw=1, alpha=0.5)
ax.set_xlabel('时间 t')
ax.set_ylabel('$X_t(\\omega)$')
ax.set_title('同一个随机过程，不同 $\\omega$ 给出不同样本路径', fontsize=15, fontweight='bold')
ax.text(0.02, 0.95, '固定 t：随机变量\n固定 ω：一条路径', transform=ax.transAxes,
        fontsize=12, va='top', bbox=dict(boxstyle='round,pad=0.35', fc='white', ec='#5F6368'))
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('../images/fig1_sample_paths.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig1_sample_paths.png saved')
