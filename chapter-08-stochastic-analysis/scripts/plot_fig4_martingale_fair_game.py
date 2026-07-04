"""fig4: 鞅——条件期望保持当前值。"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

rng = np.random.default_rng(123)
n_steps = 10
n_paths = 1200
steps = rng.choice([-1, 1], size=(n_paths, n_steps))
paths = np.c_[np.zeros(n_paths), np.cumsum(steps, axis=1)]

s = 5
current_value = 1
selected = paths[:, s] == current_value
future = paths[selected]
t = np.arange(n_steps + 1)

fig, ax = plt.subplots(figsize=(10, 6))
for path in future[:80]:
    ax.plot(t, path, color='#1A73E8', alpha=0.12, lw=1)
mean_future = future.mean(axis=0)
ax.plot(t, mean_future, color='#D93025', lw=3, label='条件平均路径')
ax.axvline(s, color='#5F6368', linestyle='--')
ax.axhline(current_value, color='#137333', linestyle='--', label='$M_s$')
ax.scatter([s], [current_value], color='#137333', s=70, zorder=5)

ax.set_xlabel('时间')
ax.set_ylabel('财富/位置')
ax.set_title(r'鞅直觉：已知 $M_s$ 后，未来条件期望仍是 $M_s$', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('../images/fig4_martingale_fair_game.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig4_martingale_fair_game.png saved')
