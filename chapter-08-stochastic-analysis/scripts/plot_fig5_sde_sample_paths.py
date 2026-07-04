"""fig5: 随机微分方程的样本路径——Ornstein-Uhlenbeck 过程。"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

rng = np.random.default_rng(2024)
T = 4.0
n = 1000
dt = T / n
t = np.linspace(0, T, n + 1)
theta = 1.4
sigma = 0.65
x0 = 1.6

fig, ax = plt.subplots(figsize=(11, 6))
for i in range(8):
    x = np.empty(n + 1)
    x[0] = x0
    dB = np.sqrt(dt) * rng.normal(size=n)
    for k in range(n):
        x[k + 1] = x[k] + (-theta * x[k]) * dt + sigma * dB[k]
    ax.plot(t, x, lw=1.7, alpha=0.85)

ax.axhline(0, color='#202124', lw=1.2, linestyle='--', alpha=0.7)
ax.set_xlabel('时间 t')
ax.set_ylabel('$X_t$')
ax.set_title(r'Ornstein-Uhlenbeck SDE：$dX_t=-\theta X_tdt+\sigma dB_t$', fontsize=15, fontweight='bold')
ax.text(0.03, 0.92, '漂移把路径拉回 0\n噪声不断扰动', transform=ax.transAxes,
        fontsize=12, va='top', bbox=dict(boxstyle='round,pad=0.35', fc='white', ec='#5F6368'))
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('../images/fig5_sde_sample_paths.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig5_sde_sample_paths.png saved')
