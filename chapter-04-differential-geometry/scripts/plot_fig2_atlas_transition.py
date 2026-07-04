"""fig2: 图册与坐标变换。"""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig2_atlas_transition.png"

fig, ax = plt.subplots(figsize=(13, 7))
ax.set_xlim(0, 13)
ax.set_ylim(0, 7)
ax.axis('off')

# manifold as a wavy closed curve
t = np.linspace(0, 2 * np.pi, 500)
r = 1.25 + 0.18 * np.sin(3 * t) + 0.08 * np.cos(5 * t)
x = 2.3 + r * np.cos(t)
y = 3.5 + 0.72 * r * np.sin(t)
ax.fill(x, y, color='#DCE9F9', alpha=0.95, ec='#3569A8', lw=2)
ax.text(2.3, 5.1, '流形 M', ha='center', fontsize=14, fontweight='bold', color='#1F4D7A')

# two overlapping chart domains
c1 = Circle((2.0, 3.55), 0.85, color='#FBBC04', alpha=0.35, ec='#A05A00', lw=2)
c2 = Circle((2.65, 3.3), 0.85, color='#34A853', alpha=0.30, ec='#137333', lw=2)
ax.add_patch(c1)
ax.add_patch(c2)
ax.text(1.45, 2.45, '$U_\\alpha$', fontsize=13, color='#A05A00', fontweight='bold')
ax.text(3.1, 2.25, '$U_\\beta$', fontsize=13, color='#137333', fontweight='bold')

# coordinate planes
rect1 = Rectangle((5.0, 4.0), 2.5, 1.8, facecolor='#FFF4D8', edgecolor='#A05A00', lw=2)
rect2 = Rectangle((9.6, 1.2), 2.5, 1.8, facecolor='#E4F6EA', edgecolor='#137333', lw=2)
ax.add_patch(rect1)
ax.add_patch(rect2)
ax.text(6.25, 5.95, '$\\varphi_\\alpha(U_\\alpha) \\subset \\mathbb{R}^n$', ha='center',
        fontsize=12, color='#A05A00', fontweight='bold')
ax.text(10.85, 3.15, '$\\varphi_\\beta(U_\\beta) \\subset \\mathbb{R}^n$', ha='center',
        fontsize=12, color='#137333', fontweight='bold')

# grids inside coordinate rectangles
for gx in np.linspace(5.2, 7.3, 5):
    ax.plot([gx, gx], [4.15, 5.65], color='#C7A45C', lw=0.6, alpha=0.6)
for gy in np.linspace(4.15, 5.65, 4):
    ax.plot([5.15, 7.35], [gy, gy], color='#C7A45C', lw=0.6, alpha=0.6)
for gx in np.linspace(9.8, 11.9, 5):
    ax.plot([gx, gx], [1.35, 2.85], color='#74B989', lw=0.6, alpha=0.6)
for gy in np.linspace(1.35, 2.85, 4):
    ax.plot([9.75, 11.95], [gy, gy], color='#74B989', lw=0.6, alpha=0.6)

def arrow(start, end, text, color):
    arr = FancyArrowPatch(start, end, arrowstyle='->', mutation_scale=16, lw=2, color=color)
    ax.add_patch(arr)
    mid = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
    ax.text(mid[0], mid[1] + 0.18, text, color=color, fontsize=12, ha='center', fontweight='bold')

arrow((3.25, 4.25), (5.0, 5.0), '$\\varphi_\\alpha$', '#A05A00')
arrow((3.25, 2.95), (9.6, 2.1), '$\\varphi_\\beta$', '#137333')
arrow((7.55, 4.2), (9.55, 2.8), '$\\varphi_\\beta \\circ \\varphi_\\alpha^{-1}$', '#5F6368')

ax.text(6.5, 0.55, '流形没有唯一坐标；关键是重叠区域上的坐标变换必须光滑', ha='center',
        fontsize=13, fontweight='bold', color='#333333')

plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f'{out.name} saved')
