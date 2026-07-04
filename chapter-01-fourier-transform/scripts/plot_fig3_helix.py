"""fig3: 缠绕机——傅里叶变换的几何直觉。

将信号缠绕在单位圆上，以不同频率旋转。
当缠绕频率与信号频率匹配时，质心会偏离原点——这就是频谱峰值的位置。
这个视角来自 3Blue1Brown 关于傅里叶变换的视频。
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

rng = np.random.default_rng(42)
t = np.linspace(0, 10 * np.pi, 600)
signal = np.sin(3 * t)  # 频率 = 3

fig, axes = plt.subplots(2, 3, figsize=(12, 8))

test_freqs = [1.5, 2.5, 3.0, 3.5, 4.5, 6.0]
test_freqs = [(1.5, '偏离匹配'), (2.5, '接近匹配'), (3.0, '精确匹配 ω=3'),
              (3.5, '稍过匹配'), (4.5, '偏离较多'), (6.0, '倍频 ω=6')]

for ax, (w, label) in zip(axes.ravel(), test_freqs):
    # 缠绕：以角速度 w 旋转
    winding = signal * np.exp(1j * w * t)  # f(t) * e^{-iwt} 的复共轭视角
    # 计算质心
    centroid = np.mean(winding)

    ax.plot(winding.real, winding.imag, linewidth=0.3, color='C0', alpha=0.7)
    ax.plot(centroid.real, centroid.imag, 'o', color='C3', markersize=8, zorder=5)
    ax.plot([0, centroid.real], [0, centroid.imag], '--', color='C3',
            linewidth=1.5, alpha=0.7)
    ax.axhline(y=0, color='gray', linewidth=0.4)
    ax.axvline(x=0, color='gray', linewidth=0.4)
    ax.set_aspect('equal')
    ax.set_title(label, fontsize=11)
    ax.set_xlabel('Re')
    ax.set_ylabel('Im')
    # 以原点为中心的坐标范围
    lim = max(1.2, np.max(np.abs(winding)) * 1.1)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

fig.suptitle('缠绕图像：匹配的频率让质心"走偏"', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig3_helix.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig3_helix.png saved')
