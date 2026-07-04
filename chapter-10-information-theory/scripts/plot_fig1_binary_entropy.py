"""fig1: 二元熵函数。"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

p = np.linspace(1e-6, 1 - 1e-6, 800)
H = -p * np.log2(p) - (1 - p) * np.log2(1 - p)

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(p, H, color='#1A73E8', lw=3)
ax.scatter([0.5], [1.0], color='#D93025', s=70, zorder=5)
ax.text(0.5, 0.86, '最大不确定性\n1 bit', ha='center', fontsize=12,
        color='#D93025', fontweight='bold')
ax.text(0.08, 0.12, '几乎确定\n熵接近 0', ha='center', fontsize=11, color='#5F6368')
ax.text(0.92, 0.12, '几乎确定\n熵接近 0', ha='center', fontsize=11, color='#5F6368')
ax.set_xlabel('p')
ax.set_ylabel('$H_2(p)$ bits')
ax.set_title('二元熵：不确定性在 p=1/2 时最大', fontsize=15, fontweight='bold')
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('../images/fig1_binary_entropy.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig1_binary_entropy.png saved')
