"""fig2: 时域与频域——同一信号的两种表示。

左侧：时域中两个正弦波和噪声叠加而成的信号。
右侧：通过傅里叶变换得到的频谱，清晰地揭示出两个主频率。
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

rng = np.random.default_rng(42)
fs = 500  # 采样率
t = np.linspace(0, 2.0, int(fs * 2.0), endpoint=False)

# 构造信号：5Hz 主成分 + 20Hz 次成分 + 噪声
signal = (1.2 * np.sin(2 * np.pi * 5 * t)
          + 0.6 * np.sin(2 * np.pi * 20 * t)
          + 0.3 * rng.normal(0, 1, len(t)))

# 频谱
n = len(t)
freqs = np.fft.fftfreq(n, d=1 / fs)[:n // 2]
spectrum = np.abs(np.fft.fft(signal))[:n // 2] / n * 2

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

# 左：时域
ax1.plot(t, signal, linewidth=0.6, color='C0')
ax1.set_xlabel('时间 t (秒)')
ax1.set_ylabel('幅度')
ax1.set_title('时域：看起来杂乱无章', fontsize=13)
ax1.grid(True, alpha=0.3)
# 示意肉眼难以分辨周期
ax1.annotate('你能看出\n几个周期成分？', xy=(1.3, 1.2), fontsize=10,
             color='gray', ha='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.7))

# 右：频域
ax2.stem(freqs, spectrum, linefmt='C1-', markerfmt='C1o', basefmt='gray')
ax2.set_xlabel('频率 (Hz)')
ax2.set_ylabel('幅度')
ax2.set_title('频域：两个主频率一目了然', fontsize=13)
ax2.set_xlim(0, 30)
ax2.grid(True, alpha=0.3)
# 标注两个峰值
ax2.annotate('5 Hz', xy=(5, 1.2), xytext=(8, 1.3), fontsize=10,
             arrowprops=dict(arrowstyle='->', color='C3'), color='C3')
ax2.annotate('20 Hz', xy=(20, 0.6), xytext=(23, 0.8), fontsize=10,
             arrowprops=dict(arrowstyle='->', color='C3'), color='C3')

fig.suptitle('同一信号的两个视角', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig2_two_domains.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig2_two_domains.png saved')
