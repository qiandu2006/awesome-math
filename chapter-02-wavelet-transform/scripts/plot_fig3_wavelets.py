"""fig3: 三个经典母小波。

- Morlet 小波：复指数乘以高斯包络，与傅里叶联系最紧密
- 墨西哥帽小波：高斯函数的二阶导数，形状像草帽
- Daubechies db4 小波：紧支撑正交小波，离散小波变换的主力
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

# --- Morlet ---
t = np.linspace(-4, 4, 1000)
f0 = 1.0
sigma = 0.8
morlet_real = np.exp(-t**2 / (2 * sigma**2)) * np.cos(2 * np.pi * f0 * t)
morlet_imag = np.exp(-t**2 / (2 * sigma**2)) * np.sin(2 * np.pi * f0 * t)
envelope = np.exp(-t**2 / (2 * sigma**2))

ax = axes[0]
ax.plot(t, morlet_real, 'C0', linewidth=1.5, label='实部')
ax.plot(t, morlet_imag, 'C1', linewidth=1.2, alpha=0.7, label='虚部')
ax.plot(t, envelope, 'gray', linewidth=0.8, linestyle='--', alpha=0.5)
ax.plot(t, -envelope, 'gray', linewidth=0.8, linestyle='--', alpha=0.5)
ax.set_title('Morlet 小波', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlabel('t')
ax.set_ylim(-1.2, 1.2)

# --- Mexican Hat (Ricker) ---
t = np.linspace(-4, 4, 1000)
sigma = 0.7
mex_hat = (2 / (np.sqrt(3 * sigma) * np.pi**0.25)) * \
          (1 - (t / sigma)**2) * np.exp(-t**2 / (2 * sigma**2))

ax = axes[1]
ax.plot(t, mex_hat, 'C2', linewidth=1.8)
ax.fill_between(t, 0, mex_hat, alpha=0.15, color='C2')
ax.set_title('墨西哥帽小波\n(Ricker)', fontsize=13)
ax.grid(True, alpha=0.3)
ax.set_xlabel('t')
ax.set_ylim(-0.6, 1.2)

# --- Daubechies db4 ---
# 使用级联算法（cascade algorithm）生成近似
import pywt

wavelet = pywt.Wavelet('db4')
# 获取 scaling function 在 resolution=8 时的近似
phi, psi, x = wavelet.wavefun(level=6)

ax = axes[2]
ax.plot(x, psi, 'C3', linewidth=1.5)
ax.fill_between(x, 0, psi, alpha=0.15, color='C3')
ax.set_title('Daubechies db4 小波', fontsize=13)
ax.grid(True, alpha=0.3)
ax.set_xlabel('t')
ax.set_ylim(np.min(psi)*1.2, np.max(psi)*1.2)

fig.suptitle('三种经典母小波 ψ(t)', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig3_mother_wavelets.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig3_mother_wavelets.png saved')
