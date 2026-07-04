"""fig3: Transverse intersection versus tangency."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig3_transversality.png"

x = np.linspace(-1.4, 1.4, 300)
fig, axes = plt.subplots(1, 2, figsize=(9, 4.5), sharex=True, sharey=True)

axes[0].plot(x, 0.35 * x, color="#1A73E8", lw=3)
axes[0].plot(x, -0.45 * x, color="#D93025", lw=3)
axes[0].scatter([0], [0], s=80, color="#202124", zorder=5)
axes[0].set_title("横截相交：稳定", fontsize=14, fontweight="bold")
axes[0].text(0, -1.0, r"$T_pA+T_pB=T_pM$", ha="center", fontsize=12, color="#5F6368")

axes[1].plot(x, x**2, color="#1A73E8", lw=3)
axes[1].plot(x, np.zeros_like(x), color="#D93025", lw=3)
axes[1].scatter([0], [0], s=80, color="#202124", zorder=5)
axes[1].set_title("相切相交：不稳定", fontsize=14, fontweight="bold")
axes[1].text(0, -1.0, "轻微扰动可能改变交点数", ha="center", fontsize=12, color="#5F6368")

for ax in axes:
    ax.axhline(0, color="#DADCE0", lw=0.8)
    ax.axvline(0, color="#DADCE0", lw=0.8)
    ax.set_aspect("equal")
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.2, 1.2)
    ax.axis("off")

fig.suptitle("横截性：一般位置下的交点结构", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
