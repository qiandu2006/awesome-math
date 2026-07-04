"""fig2: STFT vs CWT 的时频分辨率对比。

STFT 使用固定窗口 → 时频分辨率处处相同（固定的 Heisenberg 矩形）。
CWT 使用尺度变化的窗口 → 高频时时间分辨率好，低频时频率分辨率好。
这对应了时频平面上的"自适应剖分"。
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

# --- 左图：STFT 固定分辨率 ---
ax1.set_xlim(0, 8)
ax1.set_ylim(0, 8)
ax1.set_xlabel('时间 t', fontsize=12)
ax1.set_ylabel('频率 ω', fontsize=12)
ax1.set_title('STFT：固定时频分辨率', fontsize=13)

# 画均匀的矩形网格
for i in range(8):
    for j in range(8):
        rect = Rectangle((i, j), 1, 1, linewidth=0.8, edgecolor='C0',
                         facecolor='C0', alpha=0.15)
        ax1.add_patch(rect)

# 标注一个矩形的大小
ax1.annotate('', xy=(1.5, 0.2), xytext=(2.5, 0.2),
             arrowprops=dict(arrowstyle='<->', color='C3', lw=1.5))
ax1.text(2, 0.05, 'Δt（固定）', ha='center', fontsize=9, color='C3')

ax1.annotate('', xy=(0.2, 1.5), xytext=(0.2, 2.5),
             arrowprops=dict(arrowstyle='<->', color='C3', lw=1.5))
ax1.text(0.4, 2, 'Δω\n（固定）', ha='center', fontsize=9, color='C3')

# --- 右图：CWT 自适应分辨率 ---
ax2.set_xlim(0, 8)
ax2.set_ylim(0, 9)
ax2.set_xlabel('时间 t', fontsize=12)
ax2.set_ylabel('尺度 (1/频率)', fontsize=12)
ax2.set_title('CWT：自适应时频分辨率', fontsize=13)

# 画变高度的矩形：低频（小尺度指示）→ 矮宽，高频 → 窄高
# 使用对数间隔的尺度
y_positions = [0.5, 1.5, 2.8, 4.5, 6.5]
heights = [0.3, 0.5, 0.8, 1.4, 2.5]
alphas = [0.35, 0.30, 0.25, 0.20, 0.15]

for y, h, a in zip(y_positions, heights, alphas):
    # 宽度与高度成反比（高频=窄时间窗口，低频=宽时间窗口）
    # heights 较大 = 低频 = 频率分辨率好、时间分辨率差 → 矩形的宽度大
    # heights 较小 = 高频 = 时间分辨率好、频率分辨率差 → 矩形的宽度小
    n_rects = int(8 / (h * 0.9))
    rect_width = 8 / n_rects
    for k in range(n_rects):
        rect = Rectangle((k * rect_width, y), rect_width * 0.95, h * 0.9,
                         linewidth=0.6, edgecolor='C1',
                         facecolor='C1', alpha=a)
        ax2.add_patch(rect)

# 标注说明
ax2.annotate('高频：窄时窗\n     + 宽频窗', xy=(7, 1.2), fontsize=9, color='C1')
ax2.annotate('低频：宽时窗\n     + 窄频窗', xy=(7, 7.5), fontsize=9, color='C1')

fig.suptitle('时频平面的剖分：STFT vs CWT', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig2_stft_vs_cwt_tiling.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig2_stft_vs_cwt_tiling.png saved')
