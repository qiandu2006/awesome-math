"""fig1: 热方程扩散会抹平尖峰。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig1_heat_equation_diffusion.png"

x = np.linspace(-4, 4, 800)
times = [0.08, 0.25, 0.70, 1.50]
colors = ["#D93025", "#F9AB00", "#1A73E8", "#188038"]

fig, ax = plt.subplots(figsize=(9, 5.5))
for t, color in zip(times, colors):
    u = np.exp(-x**2 / (4 * t)) / np.sqrt(4 * np.pi * t)
    ax.plot(x, u, lw=3, color=color, label=f"t={t}")
ax.set_title("热方程：局部尖峰随时间扩散并变平", fontsize=15, fontweight="bold")
ax.set_xlabel("x")
ax.set_ylabel("u(t,x)")
ax.grid(alpha=0.25)
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
