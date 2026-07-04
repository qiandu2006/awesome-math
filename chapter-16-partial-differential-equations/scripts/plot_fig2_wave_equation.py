"""fig2: 波方程中扰动传播。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig2_wave_equation.png"

x = np.linspace(-5, 5, 900)
times = [0.0, 0.8, 1.6, 2.4]
colors = ["#202124", "#1A73E8", "#F9AB00", "#D93025"]

def pulse(x):
    return np.exp(-4 * x**2)

fig, ax = plt.subplots(figsize=(9, 5.5))
for t, color in zip(times, colors):
    u = 0.5 * pulse(x - t) + 0.5 * pulse(x + t)
    ax.plot(x, u + 0.22 * t, lw=3, color=color, label=f"t={t}")
ax.text(2.5, 1.03, "向右传播", fontsize=12, color="#D93025")
ax.text(-3.55, 1.03, "向左传播", fontsize=12, color="#D93025")
ax.set_title("波方程：扰动以有限速度传播", fontsize=15, fontweight="bold")
ax.set_xlabel("x")
ax.set_ylabel("位移 u(t,x)（曲线为视觉错开）")
ax.grid(alpha=0.25)
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
