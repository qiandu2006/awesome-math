"""fig1: 方波的傅里叶级数逼近——核心思想的视觉锚点。

一个方波用 1, 2, 3, 10 项正弦波叠加来逼近。
展示"任意周期函数都可以分解为正弦波的叠加"这一核心洞察。
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-np.pi, np.pi, 2000)
# 方波
square = np.where(np.sin(x) >= 0, 1.0, -1.0)

def fourier_approx(x, n_terms):
    """用前 n_terms 个奇次谐波逼近方波。"""
    result = np.zeros_like(x)
    for k in range(1, n_terms + 1):
        n = 2 * k - 1  # 1, 3, 5, 7, ...
        result += (4 / (np.pi * n)) * np.sin(n * x)
    return result

fig, axes = plt.subplots(2, 2, figsize=(12, 9))
axes = axes.ravel()
term_counts = [1, 2, 3, 10]

for ax, n in zip(axes, term_counts):
    approx = fourier_approx(x, n)
    ax.plot(x, square, 'k-', linewidth=0.8, alpha=0.4, label='方波')
    ax.plot(x, approx, 'C0', linewidth=1.8, label=f'{n}项逼近')
    ax.fill_between(x, square, approx, alpha=0.15, color='C0')
    ax.set_ylim(-1.5, 1.5)
    ax.set_title(f'{n} 项正弦波叠加', fontsize=13)
    ax.legend(fontsize=9, loc='upper right')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.grid(True, alpha=0.3)
    # 标记 Gibbs 现象的位置（仅最后一张）
    if n == max(term_counts):
        ax.annotate('Gibbs 现象\n(跳变点处过冲)', xy=(np.pi / 2, 1.0),
                    xytext=(1.5, 1.3), fontsize=9,
                    arrowprops=dict(arrowstyle='->', color='gray'),
                    color='gray')

fig.suptitle('用正弦波"拼"出一个方波', fontsize=15, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig('../images/fig1_square_wave.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig1_square_wave.png saved')
