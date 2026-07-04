"""fig2: Cylinder versus Mobius strip conceptual comparison."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig2_mobius_twist.png"

theta = np.linspace(0, 2 * np.pi, 180)
v = np.linspace(-0.22, 0.22, 8)
T, V = np.meshgrid(theta, v)

def strip(center_x, twist=False):
    phase = T / 2 if twist else 0
    x = center_x + (1 + V * np.cos(phase)) * np.cos(T)
    y = (1 + V * np.cos(phase)) * np.sin(T)
    z = V * np.sin(phase)
    return x, y, z

fig = plt.figure(figsize=(10, 4.8))
for i, (center, title, twist) in enumerate([(-1.6, "圆柱：全局乘积", False), (1.6, "Möbius 带：绕一圈翻转", True)]):
    ax = fig.add_subplot(1, 2, i + 1, projection="3d")
    x, y, z = strip(0, twist)
    ax.plot_surface(x, y, z, color="#E8F0FE" if not twist else "#FCE8E6", edgecolor="#9AA0A6", linewidth=0.35, alpha=0.85)
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_axis_off()
    ax.set_box_aspect((1, 1, 0.45))
    ax.view_init(elev=23, azim=35)

fig.suptitle("局部看起来相同，全局粘合可以不同", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
