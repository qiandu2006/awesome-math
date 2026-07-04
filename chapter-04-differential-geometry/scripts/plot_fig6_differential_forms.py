"""fig6: 微分形式是适合积分的几何对象。"""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig6_differential_forms.png"

fig, axes = plt.subplots(1, 3, figsize=(14, 4.8))
for ax in axes:
    ax.set_aspect('equal')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.8, 1.8)
    ax.axis('off')

# 0-form: scalar function
x = np.linspace(-2, 2, 120)
y = np.linspace(-1.8, 1.8, 120)
X, Y = np.meshgrid(x, y)
Z = np.exp(-((X + 0.4) ** 2 + (Y - 0.2) ** 2)) + 0.45 * np.exp(-((X - 0.9) ** 2 + (Y + 0.5) ** 2) / 0.5)
axes[0].contourf(X, Y, Z, levels=12, cmap='Blues', alpha=0.88)
axes[0].contour(X, Y, Z, levels=7, colors='#1A73E8', linewidths=0.8, alpha=0.7)
axes[0].set_title('0-形式：函数', fontsize=13, fontweight='bold')
axes[0].text(0, -1.55, r'$f(p)$ 给每个点一个数', ha='center', fontsize=10.5)

# 1-form: integrate along path
for c in np.linspace(-2.2, 2.2, 10):
    axes[1].plot([c - 1.2, c + 1.2], [-1.8, 1.8], color='#AECBFA', lw=1)
t = np.linspace(0, 1, 160)
px = -1.45 + 2.9 * t
py = -0.8 + 0.75 * np.sin(1.3 * np.pi * t)
axes[1].plot(px, py, color='#D93025', lw=3)
axes[1].scatter([px[0], px[-1]], [py[0], py[-1]], color='#D93025', s=45)
for idx in [35, 80, 125]:
    axes[1].arrow(px[idx], py[idx], 0.25, 0.18, head_width=0.08, head_length=0.11,
                  fc='#D93025', ec='#D93025')
axes[1].set_title('1-形式：沿曲线积分', fontsize=13, fontweight='bold')
axes[1].text(0, -1.55, r'$\int_\gamma \omega$ 测量路径穿过的“层”', ha='center', fontsize=10.5)

# 2-form: integrate over oriented region
theta = np.linspace(0, 2 * np.pi, 200)
region_x = 1.25 * np.cos(theta) + 0.18 * np.sin(3 * theta)
region_y = 0.95 * np.sin(theta)
axes[2].fill(region_x, region_y, color='#FFF4D8', ec='#A05A00', lw=2, alpha=0.9)
for cx in np.linspace(-0.8, 0.8, 4):
    for cy in np.linspace(-0.45, 0.45, 3):
        axes[2].add_patch(Circle((cx, cy), 0.08, facecolor='#F4B400', edgecolor='none', alpha=0.8))
axes[2].arrow(1.1, 0.0, -0.08, 0.42, head_width=0.08, head_length=0.11,
              fc='#A05A00', ec='#A05A00')
axes[2].set_title('2-形式：在区域上积分', fontsize=13, fontweight='bold')
axes[2].text(0, -1.55, r'$\int_S \eta$ 测量有向面积/通量', ha='center', fontsize=10.5)

fig.suptitle('微分形式按维度匹配积分对象：点、路径、区域', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f'{out.name} saved')
