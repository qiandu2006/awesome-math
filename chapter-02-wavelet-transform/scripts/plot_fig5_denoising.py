"""fig5: 小波降噪——一个关键应用。

对含噪信号做 DWT → 阈值处理小波系数（剔除噪声）→ 逆变换重建。
展示原始纯净信号、含噪信号、降噪后的信号三者对比。
"""
import numpy as np
import matplotlib.pyplot as plt
import pywt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

rng = np.random.default_rng(42)

# 生成带突变和振荡的纯净信号
t = np.linspace(0, 1, 1024)
clean = (np.sin(2 * np.pi * 10 * t)
         + 0.3 * np.sin(2 * np.pi * 60 * t)
         + 0.8 * np.exp(-((t - 0.3) / 0.03)**2)   # 尖峰
         - 0.5 * np.exp(-((t - 0.7) / 0.02)**2))  # 另一个尖峰

# 加噪声
noise_level = 0.3
noisy = clean + noise_level * rng.normal(0, 1, len(t))

# 小波降噪：软阈值
coeffs = pywt.wavedec(noisy, 'db4', level=5)
# 通用阈值（Donoho-Johnstone）
sigma = noise_level
threshold = sigma * np.sqrt(2 * np.log(len(t)))

# 对细节系数做软阈值处理（保留近似系数不动）
coeffs_thresh = [coeffs[0]]  # cA5 不变
for c in coeffs[1:]:
    coeffs_thresh.append(pywt.threshold(c, threshold, mode='soft'))

denoised = pywt.waverec(coeffs_thresh, 'db4')
denoised = denoised[:len(t)]

fig, axes = plt.subplots(3, 1, figsize=(12, 9))

ax = axes[0]
ax.plot(t, clean, 'C0', linewidth=0.8)
ax.set_title('原始纯净信号', fontsize=13)
ax.set_ylabel('幅度')
ax.grid(True, alpha=0.3)
ax.set_ylim(-2, 2.5)

ax = axes[1]
ax.plot(t, noisy, 'C3', linewidth=0.5, alpha=0.8)
ax.set_title(f'含噪信号（σ={noise_level}）', fontsize=13)
ax.set_ylabel('幅度')
ax.grid(True, alpha=0.3)
ax.set_ylim(-2, 2.5)

ax = axes[2]
ax.plot(t, clean, 'gray', linewidth=0.6, alpha=0.4, label='原始')
ax.plot(t, denoised, 'C0', linewidth=1.0, label='降噪后')
ax.set_title('小波降噪结果', fontsize=13)
ax.set_xlabel('t')
ax.set_ylabel('幅度')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_ylim(-2, 2.5)

fig.suptitle('小波降噪：阈值 + 逆变换', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig5_denoising.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig5_denoising.png saved')
