"""fig1: 二维动力系统的相图与轨道。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig1_phase_portrait.png"

x = np.linspace(-2.2, 2.2, 24)
y = np.linspace(-2.2, 2.2, 24)
X, Y = np.meshgrid(x, y)
U = Y
V = -0.55 * X + 0.35 * (1 - X**2) * Y
speed = np.sqrt(U**2 + V**2)

fig, ax = plt.subplots(figsize=(8, 7))
ax.streamplot(X, Y, U, V, color=speed, cmap="viridis", linewidth=1.4, density=1.25, arrowsize=1.2)
ax.scatter([0], [0], s=90, color="#D93025", zorder=5)
ax.text(0.10, 0.12, "平衡点", color="#D93025", fontsize=12, fontweight="bold")
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_title("相图：把时间演化看成状态空间中的流", fontsize=15, fontweight="bold")
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_aspect("equal")
ax.grid(alpha=0.2)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
