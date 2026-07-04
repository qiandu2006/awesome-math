"""fig1: 傅里叶基底 vs 小波基底——小波变换的核心动机。

傅里叶基底是无限延伸的正弦波，没有时间定位能力。
小波基底是局部化的"小波浪"，在时间和频率上都有紧支撑。
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

t_long = np.linspace(-4, 4, 2000)
t_short = np.linspace(-4, 4, 2000)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 左上：傅里叶基底——无限延伸的正弦波
ax = axes[0, 0]
for k, c in [(1, 'C0'), (2, 'C1'), (4, 'C2')]:
    ax.plot(t_long, np.sin(k * np.pi * t_long), c, linewidth=1.2, alpha=0.8,
            label=f'sin({k}πt)')
ax.set_title('傅里叶基底（无限延伸）', fontsize=13)
ax.set_xlim(-4, 4)
ax.set_ylim(-1.5, 1.8)
ax.legend(fontsize=9, loc='upper right')
ax.set_xlabel('t')
ax.grid(True, alpha=0.3)

# 右上：小波基底——局部化在不同位置
ax = axes[0, 1]
# 生成一个类似 Ricker (Mexican hat) 的小波
def ricker(t, sigma=1.0):
    t = np.asarray(t)
    a = (1 - (t / sigma)**2) * np.exp(-t**2 / (2 * sigma**2))
    return a

shifts = [-2, 0, 2]
colors = ['C0', 'C1', 'C2']
for s, c in zip(shifts, colors):
    ax.plot(t_short, ricker(t_short - s, sigma=0.6), c, linewidth=1.8,
            label=f'ψ(t {"+" if s < 0 else "-"}{abs(s) if s != 0 else ""})' if s != 0 else 'ψ(t)')
ax.set_title('小波基底（局部化）', fontsize=13)
ax.set_xlim(-4, 4)
ax.set_ylim(-1.5, 1.8)
ax.legend(fontsize=9, loc='upper right')
ax.set_xlabel('t')
ax.grid(True, alpha=0.3)

# 左下：傅里叶变换结果——只有频率信息，没有时间信息
ax = axes[1, 0]
t_sig = np.linspace(0, 8, 1000)
signal = np.where(t_sig < 4, np.sin(2 * np.pi * 1 * t_sig), np.sin(2 * np.pi * 3 * t_sig))
ax.plot(t_sig, signal, 'C0', linewidth=0.8)
ax.set_title('信号：频率在 t=4 处突变', fontsize=13)
ax.set_xlabel('t')
ax.set_ylabel('f(t)')
ax.grid(True, alpha=0.3)
ax.annotate('1 Hz', xy=(2, 0.5), fontsize=11, color='C3', ha='center')
ax.annotate('3 Hz', xy=(6, 0.5), fontsize=11, color='C3', ha='center')
ax.axvline(x=4, color='gray', linestyle='--', alpha=0.5)

# 右下：频谱——能看到两个频率但不知道何时
ax = axes[1, 1]
freqs = np.fft.rfftfreq(len(t_sig), d=t_sig[1]-t_sig[0])
spectrum = np.abs(np.fft.rfft(signal))
ax.plot(freqs, spectrum, 'C1', linewidth=1.5)
ax.set_xlim(0, 10)
ax.set_xlabel('频率 (Hz)')
ax.set_ylabel('幅度')
ax.set_title('傅里叶频谱：有 1Hz 和 3Hz\n但无法分辨"先后"', fontsize=13)
ax.grid(True, alpha=0.3)
ax.annotate('1 Hz', xy=(1, np.max(spectrum[:len(spectrum)//4])), xytext=(2.5, np.max(spectrum)*0.85),
            fontsize=10, arrowprops=dict(arrowstyle='->', color='C3'), color='C3')
ax.annotate('3 Hz', xy=(3, np.max(spectrum[len(spectrum)//4:2*len(spectrum)//4])),
            xytext=(5, np.max(spectrum)*0.7), fontsize=10,
            arrowprops=dict(arrowstyle='->', color='C3'), color='C3')

fig.suptitle('傅里叶 vs 小波：时间局部化的缺失', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig1_fourier_vs_wavelet_basis.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig1_fourier_vs_wavelet_basis.png saved')
