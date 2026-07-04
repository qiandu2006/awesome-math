"""fig3: 切向量作为曲线速度。"""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig3_tangent_vectors.png"

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_aspect('equal')
ax.set_xlim(-3.3, 3.3)
ax.set_ylim(-2.5, 2.8)
ax.axis('off')

# ellipse manifold
t = np.linspace(0, 2 * np.pi, 500)
x = 2.5 * np.cos(t)
y = 1.4 * np.sin(t)
ax.plot(x, y, color='#1A73E8', lw=3)
ax.text(-2.9, 1.85, '流形 M 上的曲线', fontsize=14, color='#1A73E8', fontweight='bold')

# point and tangent
t0 = 0.75
p = np.array([2.5 * np.cos(t0), 1.4 * np.sin(t0)])
vel = np.array([-2.5 * np.sin(t0), 1.4 * np.cos(t0)])
vel = vel / np.linalg.norm(vel)

ax.scatter([p[0]], [p[1]], color='#D93025', s=80, zorder=5)
ax.text(p[0] + 0.12, p[1] + 0.15, '$p=\\gamma(0)$', fontsize=13, color='#D93025', fontweight='bold')

# tangent line
line_s = np.linspace(-1.4, 1.4, 2)
line = p[:, None] + vel[:, None] * line_s
ax.plot(line[0], line[1], color='#F4B400', lw=5, alpha=0.7, solid_capstyle='round')

# velocity arrow
ax.arrow(p[0], p[1], vel[0] * 1.0, vel[1] * 1.0, head_width=0.14, head_length=0.22,
         fc='#D93025', ec='#D93025', lw=2.2, length_includes_head=True)
ax.text(p[0] + vel[0] * 1.18, p[1] + vel[1] * 1.18, "$\\gamma'(0) \\in T_pM$",
        fontsize=13, color='#D93025', fontweight='bold')

# nearby curve parameter marks
for dt, label in [(-0.28, '$t<0$'), (0.28, '$t>0$')]:
    q = np.array([2.5 * np.cos(t0 + dt), 1.4 * np.sin(t0 + dt)])
    ax.scatter([q[0]], [q[1]], color='#1A73E8', s=40)
    ax.text(q[0] - 0.25, q[1] + 0.17, label, fontsize=11, color='#1A73E8')

ax.text(0, -2.15,
        '切向量的本质：不是外部空间随便画的箭头，而是曲线穿过 p 时的速度',
        ha='center', fontsize=13, fontweight='bold', color='#333333')

plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f'{out.name} saved')
