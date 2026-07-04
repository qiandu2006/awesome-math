"""fig1: 单位圆作为 Lie 群。"""
import os
from pathlib import Path
import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
out = Path(__file__).resolve().parents[1] / "images" / "fig1_circle_group.png"

t = np.linspace(0, 2*np.pi, 500)
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(np.cos(t), np.sin(t), color="#1A73E8", lw=3)
theta = 0.75
p = np.array([np.cos(theta), np.sin(theta)])
q = np.array([1.0, 0.0])
ax.scatter([q[0], p[0]], [q[1], p[1]], color=["#D93025", "#188038"], s=80, zorder=5)
ax.arrow(1, 0, 0, 0.45, head_width=0.06, head_length=0.08, fc="#D93025", ec="#D93025")
ax.text(1.06, 0.28, r"$T_eS^1$", color="#D93025", fontsize=13, fontweight="bold")
ax.text(p[0]+0.08, p[1]+0.05, r"$e^{i\theta}$", fontsize=13, color="#188038")
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("单位圆：既是流形，也是乘法群", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
