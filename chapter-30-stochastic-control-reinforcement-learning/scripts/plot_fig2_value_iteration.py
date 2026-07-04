"""fig2: Value iteration convergence."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig2_value_iteration.png"

iters = np.arange(0, 36)
error = np.exp(-iters / 7.0)
value = 1 - error

fig, axes = plt.subplots(1, 2, figsize=(9, 4.5))
axes[0].plot(iters, value, color="#1A73E8", lw=3)
axes[0].set_title("价值估计逐步上升", fontsize=13, fontweight="bold")
axes[0].set_xlabel("Bellman 更新次数")
axes[0].set_ylabel("V_k(s)")
axes[0].grid(alpha=0.25)

axes[1].semilogy(iters, error, color="#D93025", lw=3)
axes[1].set_title("误差几何收敛", fontsize=13, fontweight="bold")
axes[1].set_xlabel("Bellman 更新次数")
axes[1].set_ylabel(r"$\|V_k-V^*\|$")
axes[1].grid(True, which="both", alpha=0.25)

fig.suptitle("Bellman 更新：用递归逼近最优价值函数", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
