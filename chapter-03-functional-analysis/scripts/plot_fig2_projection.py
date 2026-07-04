"""fig2: 正交投影——泛函分析的核心几何图像。

左：R³ 中向量投影到二维子空间，余量垂直于子空间
右：函数空间中 f(x) 投影到正弦波张成的子空间（= 傅里叶级数的前几项）
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(13, 5.5))

# --- 左图：R³ 中的正交投影 ---
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# 一个子空间（平面）：由 (1,0,0) 和 (0,1,0) 张成
xx, yy = np.meshgrid(np.linspace(-0.5, 2, 10), np.linspace(-1, 1.5, 10))
zz = np.zeros_like(xx)
ax1.plot_surface(xx, yy, zz, alpha=0.2, color='C0')

# 原点
ax1.scatter([0], [0], [0], color='k', s=30)

# 一个向量 v 和它的投影
v = np.array([1.5, 0.8, 1.2])
proj = np.array([1.5, 0.8, 0.0])  # 投影到 xy 平面
residual = v - proj  # [0, 0, 1.2]

# 画 v
ax1.quiver(0, 0, 0, v[0], v[1], v[2], color='C3', linewidth=2.5,
           arrow_length_ratio=0.1, label='f (向量/函数)')

# 画投影
ax1.quiver(0, 0, 0, proj[0], proj[1], proj[2], color='C0', linewidth=2.5,
           arrow_length_ratio=0.1, label='Pf (投影/逼近)')

# 画残差
ax1.quiver(proj[0], proj[1], proj[2], residual[0], residual[1], residual[2],
           color='C2', linewidth=2.5, arrow_length_ratio=0.1,
           label='f − Pf (误差)')

# 画虚线连接 v 到投影
ax1.plot([v[0], proj[0]], [v[1], proj[1]], [v[2], proj[2]],
         '--', color='gray', linewidth=0.8)

# 直角标记
ax1.text(1.7, 0.8, 0.6, '⟂', fontsize=16, color='C2')
ax1.text(0, 0, 1.3, '⟨f−Pf, Pf⟩=0', fontsize=9, color='C2')

ax1.set_xlabel('e₁')
ax1.set_ylabel('e₂')
ax1.set_zlabel('e₃')
ax1.set_title('R³ 中的正交投影', fontsize=13)
ax1.legend(fontsize=9, loc='upper left')
ax1.view_init(elev=20, azim=-60)

# --- 右图：函数空间中的正交投影 ---
ax2 = fig.add_subplot(1, 2, 2)

x = np.linspace(0, 2*np.pi, 1000)
# 目标函数：一个三角波
f = np.zeros_like(x)
for i, xi in enumerate(x):
    if xi < np.pi:
        f[i] = xi / np.pi
    else:
        f[i] = (2*np.pi - xi) / np.pi

# 傅里叶逼近：直接用正弦级数（奇函数部分需要调整，这里用余弦近似）
def fourier_approx(x, n):
    result = np.ones_like(x) * 0.5  # a0/2
    for k in range(1, n + 1):
        n_term = 2*k - 1  # 1, 3, 5, ...
        result += (4 / (np.pi**2 * n_term**2)) * np.cos(n_term * x)
    return result

approx1 = fourier_approx(x, 1)
approx3 = fourier_approx(x, 3)
approx10 = fourier_approx(x, 10)

ax2.plot(x, f, 'C3', linewidth=2, label='f (目标函数)', alpha=0.7)
ax2.plot(x, approx1, 'gray', linewidth=1, alpha=0.5, label='1项逼近')
ax2.plot(x, approx3, 'C0', linewidth=1.2, alpha=0.7, label='3项逼近')
ax2.plot(x, approx10, 'C0', linewidth=2, label='10项逼近（≈ 投影）')

# 标注残差区域
ax2.fill_between(x[:400], f[:400], approx10[:400], alpha=0.12, color='C2')
ax2.annotate('残差（正交于\n逼近子空间）', xy=(0.8, 0.75), fontsize=9,
             color='C2', ha='center')

ax2.set_xlabel('x')
ax2.set_ylabel('f(x)')
ax2.set_title('L²[0,2π] 中的正交投影\n（傅里叶级数 = 投影到正弦基底张成的子空间）', fontsize=13)
ax2.legend(fontsize=8, loc='upper right')
ax2.grid(True, alpha=0.3)

fig.suptitle('正交投影：有限维 → 无穷维', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig2_orthogonal_projection.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig2_orthogonal_projection.png saved')
