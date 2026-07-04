"""fig4: Riesz 表示定理——线性泛函的几何图像。

每个连续线性泛函 φ(f) 可以表示为与某个固定元素的内积：φ(f) = ⟨f, g⟩。
左：在 R² 中，每个线性泛函对应一个方向向量（梯度）
右：在函数空间中，积分也可以看作内积
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(13, 5.5))

# --- 左图：R² 中的线性泛函 ---
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_xlim(-3, 3)
ax1.set_ylim(-3, 3)
ax1.set_aspect('equal')
ax1.grid(True, alpha=0.3)
ax1.axhline(y=0, color='gray', linewidth=0.5)
ax1.axvline(x=0, color='gray', linewidth=0.5)

# 一个向量 g = (2, 1)
g = np.array([2.0, 1.0])
ax1.quiver(0, 0, g[0], g[1], angles='xy', scale_units='xy', scale=1,
           color='C3', width=0.03, label='g = (2,1)', zorder=5)

# 泛函 φ(x) = ⟨x, g⟩ 的等高线：2x + y = const
xx_vals = np.linspace(-3, 3, 6)
for c in [-4, -2, 0, 2, 4]:
    x_vals = np.linspace(-3, 3, 100)
    y_vals = c - 2 * x_vals
    mask = (y_vals >= -3) & (y_vals <= 3) & (x_vals >= -3) & (x_vals <= 3)
    ax1.plot(x_vals[mask], y_vals[mask], 'C0', linewidth=0.8, alpha=0.5)

# 几个向量和它们的泛函值
test_vectors = [np.array([1.0, 0.5]), np.array([-0.5, 1.5]), np.array([1.5, -1.0])]
for v in test_vectors:
    phi_v = np.dot(v, g)
    ax1.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1,
               color='gray', width=0.015, alpha=0.7)
    ax1.annotate(f'φ={phi_v:.1f}', xy=(v[0], v[1]), fontsize=9,
                 xytext=(v[0]+0.2, v[1]+0.15), color='gray')

ax1.legend(fontsize=9)
ax1.set_xlabel('x₁')
ax1.set_ylabel('x₂')
ax1.set_title('R² 中的线性泛函 φ(x) = ⟨x, g⟩\n每个泛函 = 一个方向向量 g', fontsize=13)

# --- 右图：从有限维到无穷维 ---
ax2 = fig.add_subplot(1, 2, 2)
x = np.linspace(0, 2*np.pi, 500)

# 泛函的例子：φ(f) = ∫₀^{2π} f(x) sin(3x) dx
# 这就是 f 在第 3 个傅里叶正弦分量上的坐标
g_func = np.sin(3 * x)

# 几个测试函数
def fa(x): return np.sin(3 * x)  # 与 g 对齐 → φ 大
def fb(x): return np.sin(x)      # 与 g 正交 → φ = 0
def fc(x): return 0.3 * np.sin(2*x) + 0.7 * np.sin(3*x)  # 混合

ax2.plot(x, g_func, 'C3', linewidth=2.5, label='g(x)=sin(3x)（表示泛函）')
ax2.plot(x, fa(x), 'C0', linewidth=1.5, label='f₁: φ(f₁)=π（对齐=大值）')
ax2.plot(x, fb(x), 'C1', linewidth=1.5, label='f₂: φ(f₂)=0（正交=零）')
ax2.plot(x, fc(x), 'C2', linewidth=1.5, label='f₃: φ(f₃)=0.7π（部分对齐）')

ax2.set_xlabel('x')
ax2.set_title('L²[0,2π] 中的线性泛函\nφ(f) = ⟨f, g⟩ = ∫ f(x) g(x) dx', fontsize=13)
ax2.legend(fontsize=8, loc='upper right')
ax2.grid(True, alpha=0.3)

fig.suptitle('Riesz 表示定理：Hilbert 空间 ≅ 其对偶空间', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig4_riesz.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig4_riesz.png saved')
