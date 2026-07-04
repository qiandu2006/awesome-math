"""fig2: 条件数把单位圆拉成狭长椭圆。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig2_condition_number.png"

t = np.linspace(0, 2 * np.pi, 400)
circle = np.vstack([np.cos(t), np.sin(t)])
A_good = np.array([[1.3, 0.2], [0.1, 0.9]])
A_bad = np.array([[2.5, 1.1], [1.1, 0.55]])
ell_good = A_good @ circle
ell_bad = A_bad @ circle

fig, axes = plt.subplots(1, 2, figsize=(11, 5))
for ax, ell, title, cond in [
    (axes[0], ell_good, "良态问题", np.linalg.cond(A_good)),
    (axes[1], ell_bad, "病态问题", np.linalg.cond(A_bad)),
]:
    ax.plot(circle[0], circle[1], color="#9AA0A6", lw=2, ls="--", label="单位圆")
    ax.plot(ell[0], ell[1], color="#1A73E8", lw=3, label="矩阵作用后")
    ax.set_aspect("equal")
    ax.grid(alpha=0.25)
    ax.set_title(f"{title}: κ≈{cond:.1f}", fontsize=13, fontweight="bold")
    ax.legend(frameon=False)
    ax.set_xlim(-3.0, 3.0)
    ax.set_ylim(-2.0, 2.0)
fig.suptitle("条件数：几何越狭长，反问题越敏感", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
