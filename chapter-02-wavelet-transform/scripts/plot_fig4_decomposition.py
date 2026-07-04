"""fig4: 离散小波变换的多分辨率分解。

展示信号如何通过级联滤波器组被分解为：
- 近似系数（低频，粗尺度）
- 细节系数（高频，细尺度）

左：原始信号
右：三层小波分解（A3 + D3 + D2 + D1）
"""
import numpy as np
import matplotlib.pyplot as plt
import pywt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

rng = np.random.default_rng(42)

# 生成一个复杂信号
t = np.linspace(0, 1, 1024)
signal = (np.sin(2 * np.pi * 5 * t)                    # 5Hz 低频
          + 0.5 * np.sin(2 * np.pi * 50 * t)           # 50Hz 中频
          + 0.3 * np.sin(2 * np.pi * 200 * t)          # 200Hz 高频
          + 0.2 * rng.normal(0, 1, len(t)))            # 噪声

# 做 3 层小波分解
coeffs = pywt.wavedec(signal, 'db4', level=4)
# coeffs = [cA4, cD4, cD3, cD2, cD1]

# 重建各级分量
# 我们将每个系数集单独重建回原始长度
reconstructions = []
for i, c in enumerate(coeffs):
    coeff_list = [np.zeros_like(c) if j != i else c for j, c in enumerate(coeffs)]
    rec = pywt.waverec(coeff_list, 'db4')
    # 截断到原始长度
    rec = rec[:len(signal)]
    reconstructions.append(rec)

fig, axes = plt.subplots(2, 1, figsize=(12, 8))

# 上图：原始信号
ax = axes[0]
ax.plot(t[:512], signal[:512], 'k', linewidth=0.6)
ax.set_title('原始信号', fontsize=13)
ax.set_xlabel('t')
ax.set_ylabel('幅度')
ax.grid(True, alpha=0.3)

# 下图：各级分解
ax = axes[1]
# 从粗到细排列：A4 最底，D4, D3, D2, D1 往上
colors = ['C0', 'C1', 'C2', 'C3', 'C4']
labels = ['A4 (近似)', 'D4 (细节 level 4)', 'D3 (细节 level 3)',
          'D2 (细节 level 2)', 'D1 (细节 level 1)']
offsets = [0, 2.5, 5, 7.5, 10]

for rec, offset, color, label in zip(reconstructions, offsets, colors, labels):
    ax.plot(t[:512], rec[:512] + offset, color, linewidth=0.7, label=label)
    # 标零线
    ax.axhline(y=offset, color='gray', linewidth=0.3, alpha=0.5)

ax.set_title('多分辨率分解（各级分量）', fontsize=13)
ax.set_xlabel('t')
ax.set_yticks([])
ax.legend(fontsize=8, loc='upper right', ncol=2)
ax.grid(True, alpha=0.2, axis='x')

fig.suptitle('离散小波变换：级联分解', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig4_dwt_decomposition.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig4_dwt_decomposition.png saved')
