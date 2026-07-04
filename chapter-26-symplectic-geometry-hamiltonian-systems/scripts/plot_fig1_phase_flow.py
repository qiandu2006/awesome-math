"""fig1: Hamiltonian phase flow of harmonic oscillator."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig1_phase_flow.png"

q = np.linspace(-2.2, 2.2, 25)
p = np.linspace(-2.2, 2.2, 25)
Q, P = np.meshgrid(q, p)
U = P
V = -Q
speed = np.sqrt(U**2 + V**2)

fig, ax = plt.subplots(figsize=(7, 6))
ax.streamplot(Q, P, U, V, color=speed, cmap="viridis", density=1.2, linewidth=1.2, arrowsize=1.2)
levels = [0.5, 1.0, 1.5, 2.0]
t = np.linspace(0, 2 * np.pi, 400)
for r in levels:
    ax.plot(r * np.cos(t), r * np.sin(t), color="#202124", lw=1.0, alpha=0.45)
ax.set_xlabel("位置 q")
ax.set_ylabel("动量 p")
ax.set_title("谐振子的 Hamilton 流：沿能量曲线旋转", fontsize=16, fontweight="bold")
ax.set_aspect("equal")
ax.grid(alpha=0.2)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
