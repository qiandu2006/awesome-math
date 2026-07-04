"""fig3: Real distance versus p-adic closeness."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig3_padic_distance.png"

n = np.arange(1, 9)
real_dist = 5 ** n
padic_dist = 5.0 ** (-n)

fig, ax = plt.subplots(figsize=(8.4, 5.2))
ax.semilogy(n, real_dist, "o-", color="#D93025", lw=2.6, label=r"实数距离 $|5^n|$")
ax.semilogy(n, padic_dist, "o-", color="#1A73E8", lw=2.6, label=r"$5$-进距离 $|5^n|_5$")
ax.set_xlabel("n")
ax.set_ylabel("距离尺度")
ax.set_title(r"实数远近与 $p$-进远近的方向相反", fontsize=16, fontweight="bold")
ax.text(2.1, 1e4, "实数里越来越远", color="#D93025", fontsize=12, fontweight="bold")
ax.text(4.4, 2e-5, r"$5$-进里越来越近", color="#1A73E8", fontsize=12, fontweight="bold")
ax.grid(True, which="both", alpha=0.25)
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
