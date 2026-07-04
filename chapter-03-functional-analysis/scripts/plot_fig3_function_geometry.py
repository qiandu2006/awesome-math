"""fig3: 函数空间几何——将函数视为空间中的点。

左：两个函数 f 和 g 之间的 L² 距离（填充区域 = 距离²的积分）
右：三个函数的"点图"——相互正交或接近正交的函数
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

rng = np.random.default_rng(42)

# --- 左：L² 距离的几何意义 ---
x = np.linspace(0, 1, 500)
f = 0.5 + 0.4 * np.sin(2 * np.pi * 3 * x)
g = 0.5 + 0.2 * np.sin(2 * np.pi * 1 * x + 0.5) + 0.1 * rng.normal(0, 1, len(x))

ax1.plot(x, f, 'C0', linewidth=1.8, label='f')
ax1.plot(x, g, 'C1', linewidth=1.8, label='g')
ax1.fill_between(x, f, g, alpha=0.25, color='C2',
                 label=f'∥f−g∥² = ∫(f−g)²dx ≈ {np.trapz((f-g)**2, x):.3f}')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.set_title('L² 距离：∥f − g∥² = ∫|f(x)−g(x)|² dx', fontsize=13)
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)

# --- 右：函数在空间中的"点"表示 ---
# 用前三个傅里叶系数将函数映射到 3D 坐标
def fc(func, n=3):
    """计算一个函数的前 n 个傅里叶余弦系数作为坐标"""
    coeffs = []
    for k in range(n):
        c = 2 * np.trapz(func(x) * np.cos(np.pi * k * x), x)
        coeffs.append(c)
    return np.array(coeffs)

# 定义几个函数
def f1(x): return np.sin(np.pi * x)
def f2(x): return np.sin(2 * np.pi * x)
def f3(x): return np.sin(3 * np.pi * x)
def f4(x): return np.exp(x) - 1
def f5(x): return x * (1 - x)

funcs = [f1, f2, f3, f4, f5]
names = ['sin(πx)', 'sin(2πx)', 'sin(3πx)', 'eˣ−1', 'x(1−x)']
colors = ['C0', 'C1', 'C2', 'C3', 'C4']

ax2_3d = fig.add_subplot(1, 2, 2, projection='3d')

for func, name, c in zip(funcs, names, colors):
    v = fc(func)
    ax2_3d.scatter(*v, color=c, s=80, label=name, zorder=5)
    ax2_3d.quiver(0, 0, 0, v[0], v[1], v[2], color=c, linewidth=1.5,
                  arrow_length_ratio=0.1, alpha=0.6)

# 标出正交关系
ax2_3d.text(0.5, 0, 0.6, '正弦函数\n≈ 正交', fontsize=8, color='C0')
ax2_3d.text(0.1, 0.8, 0, '⟂', fontsize=14, color='gray')

ax2_3d.set_xlabel('c₀')
ax2_3d.set_ylabel('c₁')
ax2_3d.set_zlabel('c₂')
ax2_3d.set_title('每个函数 = 空间中的一个"点"\n（用傅里叶系数坐标表示）', fontsize=13)
ax2_3d.legend(fontsize=8, loc='upper right')

fig.suptitle('函数空间的几何直觉', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('../images/fig3_function_geometry.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig3_function_geometry.png saved')
