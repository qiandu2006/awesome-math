"""fig4: 显式 Euler 稳定性限制。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig4_euler_stability.png"

lam = -8.0
t = np.linspace(0, 1.5, 400)
exact = np.exp(lam * t)
steps = [0.08, 0.18, 0.32]
colors = ["#188038", "#F9AB00", "#D93025"]

fig, ax = plt.subplots(figsize=(9, 5.5))
ax.plot(t, exact, color="#202124", lw=3, label="真实解")
for h, color in zip(steps, colors):
    n = int(1.5 / h)
    ts = np.arange(n + 1) * h
    ys = (1 + h * lam) ** np.arange(n + 1)
    ax.plot(ts, ys, marker="o", lw=2.5, color=color, label=f"Euler h={h}")
ax.axhline(0, color="#5F6368", lw=1)
ax.set_ylim(-2.2, 2.2)
ax.set_title(r"显式 Euler：步长太大会让衰减方程数值爆炸", fontsize=15, fontweight="bold")
ax.set_xlabel("t")
ax.set_ylabel("y")
ax.grid(alpha=0.25)
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
