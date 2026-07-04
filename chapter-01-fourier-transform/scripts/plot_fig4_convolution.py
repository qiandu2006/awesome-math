"""fig4: 卷积定理——傅里叶变换最核心的性质。

展示两个信号的卷积在频域中变成了简单的乘法。
上排：两个方波信号及其卷积结果
下排：各自频谱的乘积（= 卷积的频谱）
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

rng = np.random.default_rng(42)
t = np.linspace(-5, 5, 500)
dt = t[1] - t[0]

# 两个矩形脉冲
def rect(x, center, width):
    return np.where(np.abs(x - center) < width / 2, 1.0, 0.0)

f = rect(t, 1.0, 2.0)
g = rect(t, -1.0, 1.5)

# 卷积
conv = convolve(f, g, mode='same') * dt
t_conv = t

# 频谱
n = len(t)
freqs = np.fft.fftfreq(n, d=dt)
F = np.abs(np.fft.fft(f))
G = np.abs(np.fft.fft(g))
FG = np.abs(np.fft.fft(conv))

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 上排：信号
ax = axes[0, 0]
ax.plot(t, f, 'C0', linewidth=1.5, label='f(t)')
ax.plot(t, g, 'C1', linewidth=1.5, label='g(t)')
ax.set_title('原始信号 f 和 g', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlabel('t')

ax = axes[0, 1]
ax.plot(t_conv, conv, 'C2', linewidth=1.5, label='(f * g)(t)')
ax.set_title('卷积 f * g（时域逐点滑动乘加）', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlabel('t')

# 下排：频谱
freq_mask = (freqs >= 0) & (freqs <= 10)
ax = axes[1, 0]
ax.plot(freqs[freq_mask], F[freq_mask], 'C0', linewidth=1.5, label='|F(ω)|')
ax.plot(freqs[freq_mask], G[freq_mask], 'C1', linewidth=1.5, label='|G(ω)|')
ax.set_title('频谱 |F| 和 |G|', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlabel('ω')
# 乘法示意
ax.annotate('×', xy=(6, 0.5 * np.max(np.maximum(F[freq_mask], G[freq_mask]))),
            fontsize=20, ha='center', color='gray')

ax = axes[1, 1]
ax.plot(freqs[freq_mask], FG[freq_mask], 'C3', linewidth=1.5, label='|F·G| (乘积)')
ax.set_title('卷积的频谱 = F(ω)·G(ω)', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlabel('ω')

fig.suptitle('卷积定理：时域卷积 ⇌ 频域乘积', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig4_convolution.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig4_convolution.png saved')
