"""fig4: 非线性守恒律中曲线变陡形成激波。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig4_conservation_shock.png"

x0 = np.linspace(-2.5, 2.5, 800)
u0 = 1.0 + 0.55 * np.exp(-x0**2)
times = [0.0, 0.55, 1.0, 1.35]
colors = ["#202124", "#1A73E8", "#F9AB00", "#D93025"]

fig, ax = plt.subplots(figsize=(9, 5.5))
for t, color in zip(times, colors):
    x = x0 + u0 * t
    order = np.argsort(x)
    ax.plot(x[order], u0[order], color=color, lw=3, label=f"t={t}")
ax.text(2.15, 1.42, "高处传播更快\n曲线逐渐变陡", fontsize=12, color="#D93025")
ax.set_title("非线性守恒律：不同高度速度不同，可能形成激波", fontsize=15, fontweight="bold")
ax.set_xlabel("x")
ax.set_ylabel("u")
ax.set_xlim(-2.5, 4.2)
ax.grid(alpha=0.25)
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
