"""fig5: 收敛阶的 log-log 图。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig5_convergence_order.png"

h = 2.0 ** (-np.arange(2, 10))
err1 = 0.8 * h
err2 = 0.35 * h**2
err4 = 0.08 * h**4

fig, ax = plt.subplots(figsize=(8, 6))
ax.loglog(h, err1, "o-", lw=3, color="#D93025", label="一阶方法 O(h)")
ax.loglog(h, err2, "o-", lw=3, color="#1A73E8", label="二阶方法 O(h²)")
ax.loglog(h, err4, "o-", lw=3, color="#188038", label="四阶方法 O(h⁴)")
ax.invert_xaxis()
ax.set_xlabel("网格尺度 h")
ax.set_ylabel("误差")
ax.set_title("收敛阶：网格变细时误差按幂律下降", fontsize=15, fontweight="bold")
ax.grid(alpha=0.25, which="both")
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
