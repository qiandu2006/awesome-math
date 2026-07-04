"""fig5: Logistic 映射分岔图。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig5_logistic_bifurcation.png"

r_values = np.linspace(2.5, 4.0, 1600)
xs = np.full_like(r_values, 0.37)
rs_plot = []
xs_plot = []

for i in range(1200):
    xs = r_values * xs * (1 - xs)
    if i >= 900:
        rs_plot.append(r_values.copy())
        xs_plot.append(xs.copy())

R = np.concatenate(rs_plot)
X = np.concatenate(xs_plot)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(R, X, ",", color="#202124", alpha=0.32)
ax.axvline(3.0, color="#1A73E8", lw=1.5, ls="--")
ax.axvline(3.57, color="#D93025", lw=1.5, ls="--")
ax.text(2.72, 0.86, "固定点", color="#1A73E8", fontsize=12, fontweight="bold")
ax.text(3.13, 0.92, "周期倍化", color="#5F6368", fontsize=12, fontweight="bold")
ax.text(3.66, 0.18, "混沌区间", color="#D93025", fontsize=12, fontweight="bold")
ax.set_xlabel("增长参数 r")
ax.set_ylabel("长期取值 x")
ax.set_title(r"Logistic 映射：$x_{t+1}=r x_t(1-x_t)$ 的分岔图", fontsize=15, fontweight="bold")
ax.set_xlim(2.5, 4.0)
ax.set_ylim(0, 1)
ax.grid(alpha=0.2)
plt.tight_layout()
plt.savefig(out, dpi=170, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
