"""fig5: 二元对称信道容量。"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

eps = np.linspace(1e-6, 0.5, 700)
H = -eps * np.log2(eps) - (1 - eps) * np.log2(1 - eps)
C = 1 - H

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(eps, C, color='#1A73E8', lw=3)
ax.scatter([0, 0.5], [1, 0], color='#D93025', s=70, zorder=5)
ax.text(0.03, 0.88, '无噪声\n容量 1 bit', fontsize=12, color='#D93025', fontweight='bold')
ax.text(0.37, 0.12, '完全随机\n容量 0', fontsize=12, color='#D93025', fontweight='bold')
ax.set_xlabel('错误概率 ε')
ax.set_ylabel('容量 C bits/use')
ax.set_title('二元对称信道容量：$C=1-H_2(\\epsilon)$', fontsize=15, fontweight='bold')
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('../images/fig5_channel_capacity.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig5_channel_capacity.png saved')
