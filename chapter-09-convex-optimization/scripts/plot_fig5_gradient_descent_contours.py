"""fig5: 梯度下降在凸二次函数上的轨迹。"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

A = np.array([[6.0, 0.0], [0.0, 1.0]])
alpha = 0.22
x = np.array([2.2, 1.8])
pts = [x.copy()]
for _ in range(18):
    grad = A @ x
    x = x - alpha * grad
    pts.append(x.copy())
pts = np.array(pts)

xx = np.linspace(-2.6, 2.6, 250)
yy = np.linspace(-2.2, 2.2, 250)
X, Y = np.meshgrid(xx, yy)
Z = 0.5 * (6 * X**2 + Y**2)

fig, ax = plt.subplots(figsize=(9, 7))
levels = np.geomspace(0.08, 18, 18)
ax.contour(X, Y, Z, levels=levels, cmap='Blues')
ax.plot(pts[:, 0], pts[:, 1], 'o-', color='#D93025', lw=2.2, ms=4)
ax.scatter([0], [0], color='#137333', s=90, marker='*', zorder=5, label='全局最优')
ax.text(0.15, 0.15, '$x^*$', color='#137333', fontsize=13, fontweight='bold')
ax.text(-2.4, 1.85, '条件数大：等高线狭长\n梯度下降会 zig-zag', fontsize=12,
        bbox=dict(boxstyle='round,pad=0.35', fc='white', ec='#5F6368'))
ax.set_aspect('equal')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_title('梯度下降轨迹：凸性给出可证明收敛', fontsize=15, fontweight='bold')
ax.legend()
ax.grid(alpha=0.18)
plt.tight_layout()
plt.savefig('../images/fig5_gradient_descent_contours.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig5_gradient_descent_contours.png saved')
