"""fig3: Runge 现象。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig3_runge_interpolation.png"

def f(x):
    return 1 / (1 + 25 * x**2)

x = np.linspace(-1, 1, 1000)
y = f(x)
n = 14
xe = np.linspace(-1, 1, n + 1)
ye = f(xe)
coef_e = np.polyfit(xe, ye, n)
pe = np.polyval(coef_e, x)

k = np.arange(n + 1)
xc = np.cos((2 * k + 1) * np.pi / (2 * (n + 1)))
yc = f(xc)
coef_c = np.polyfit(xc, yc, n)
pc = np.polyval(coef_c, x)

fig, ax = plt.subplots(figsize=(9, 5.5))
ax.plot(x, y, color="#202124", lw=3, label="真实函数")
ax.plot(x, pe, color="#D93025", lw=2.5, label="等距节点插值")
ax.plot(x, pc, color="#1A73E8", lw=2.5, label="Chebyshev 节点插值")
ax.scatter(xe, ye, color="#D93025", s=24, alpha=0.8)
ax.set_ylim(-0.6, 1.25)
ax.set_title("Runge 现象：高次等距插值在边界附近振荡", fontsize=15, fontweight="bold")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(alpha=0.25)
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
