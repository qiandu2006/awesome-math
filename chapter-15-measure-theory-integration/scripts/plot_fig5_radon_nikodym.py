"""fig5: Radon-Nikodym 导数作为测度密度。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig5_radon_nikodym.png"

x = np.linspace(-4, 4, 700)
base = np.ones_like(x) / 8
density = 0.65 * np.exp(-0.5 * ((x + 1.0) / 0.7) ** 2) / (0.7 * np.sqrt(2 * np.pi))
density += 0.35 * np.exp(-0.5 * ((x - 1.4) / 0.9) ** 2) / (0.9 * np.sqrt(2 * np.pi))

fig, ax = plt.subplots(figsize=(9, 5.5))
ax.fill_between(x, 0, base, color="#E8EAED", alpha=0.9, label=r"参考测度 $\mu$ 的均匀背景")
ax.plot(x, density, color="#1A73E8", lw=3, label=r"$d\nu/d\mu$")
ax.fill_between(x, 0, density, where=(x > -1.6) & (x < 0.2), color="#AECBFA", alpha=0.65)
ax.text(-0.7, 0.25, r"$\nu(A)=\int_A \frac{d\nu}{d\mu}\,d\mu$", fontsize=15,
        color="#202124", ha="center")
ax.set_xlabel("x")
ax.set_ylabel("密度")
ax.set_title("Radon-Nikodym 导数：一个测度相对另一个测度的密度", fontsize=15, fontweight="bold")
ax.grid(alpha=0.25)
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
