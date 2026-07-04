"""fig2: 典型集与压缩。"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 6)
ax.axis('off')

# all sequences
ax.add_patch(Rectangle((0.8, 1.0), 4.0, 4.0, facecolor='#F1F3F4', edgecolor='#5F6368', lw=2))
ax.text(2.8, 5.25, '所有长度 n 的序列', ha='center', fontsize=13, fontweight='bold')
ax.text(2.8, 0.55, r'约 $|\mathcal{X}|^n$ 个', ha='center', fontsize=12)

# typical set inside
ax.add_patch(Rectangle((1.7, 1.75), 2.2, 2.5, facecolor='#E8F0FE', edgecolor='#1A73E8', lw=2.5))
ax.text(2.8, 3.15, '典型集', ha='center', fontsize=13, fontweight='bold', color='#1A73E8')
ax.text(2.8, 2.55, r'约 $2^{nH}$ 个', ha='center', fontsize=12, color='#1A73E8')

# code space
ax.add_patch(Rectangle((7.3, 1.75), 3.0, 2.5, facecolor='#E6F4EA', edgecolor='#137333', lw=2.5))
ax.text(8.8, 4.55, '压缩后的编号空间', ha='center', fontsize=13, fontweight='bold', color='#137333')
ax.text(8.8, 3.05, r'$nH$ bits', ha='center', fontsize=16, fontweight='bold', color='#137333')
ax.text(8.8, 2.45, r'可编号 $2^{nH}$ 个典型序列', ha='center', fontsize=11, color='#137333')

arr = FancyArrowPatch((4.05, 3.0), (7.25, 3.0), arrowstyle='->',
                      mutation_scale=18, lw=2.5, color='#D93025')
ax.add_patch(arr)
ax.text(5.65, 3.35, '只编码高概率质量集', ha='center', fontsize=12,
        color='#D93025', fontweight='bold')
ax.text(6, 0.55, '熵给出长序列无损压缩的平均极限', ha='center',
        fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('../images/fig2_typical_set_compression.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig2_typical_set_compression.png saved')
