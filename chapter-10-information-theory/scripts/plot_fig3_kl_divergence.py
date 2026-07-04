"""fig3: KL 散度——用错模型的额外代价。"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-4, 5, 900)
def normal_pdf(x, mu, sigma):
    return 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

p = normal_pdf(x, 0.0, 1.0)
q = normal_pdf(x, 1.1, 1.35)
dx = x[1] - x[0]
kl_pq = np.sum(p * np.log2((p + 1e-15) / (q + 1e-15))) * dx
kl_qp = np.sum(q * np.log2((q + 1e-15) / (p + 1e-15))) * dx

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, p, color='#1A73E8', lw=3, label='真实分布 p')
ax.plot(x, q, color='#D93025', lw=3, label='模型分布 q')
ax.fill_between(x, p, q, where=p > q, color='#E8F0FE', alpha=0.8)
ax.fill_between(x, p, q, where=q >= p, color='#FCE8E6', alpha=0.6)
ax.text(-3.6, 0.34, f'$D_{{KL}}(p\\|q)\\approx {kl_pq:.2f}$ bits\n'
                    f'$D_{{KL}}(q\\|p)\\approx {kl_qp:.2f}$ bits',
        fontsize=12, bbox=dict(boxstyle='round,pad=0.35', fc='white', ec='#5F6368'))
ax.text(1.7, 0.21, '不对称：\n方向不同，代价不同', fontsize=11, color='#5F6368')
ax.set_xlabel('x')
ax.set_ylabel('density')
ax.set_title('KL 散度：真实分布 p 与模型 q 的编码代价差', fontsize=15, fontweight='bold')
ax.legend()
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('../images/fig3_kl_divergence.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig3_kl_divergence.png saved')
