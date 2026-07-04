"""fig2: KL divergence locally approximated by a quadratic."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig2_kl_local_metric.png"

d = np.linspace(-1.5, 1.5, 300)
kl = 0.5 * d**2 + 0.18 * d**3 + 0.08 * d**4
quad = 0.5 * d**2

fig, ax = plt.subplots(figsize=(8.2, 5.2))
ax.plot(d, kl, color="#1A73E8", lw=3, label="KL 散度")
ax.plot(d, quad, color="#D93025", lw=2.5, ls="--", label="二阶 Fisher 近似")
ax.axvspan(-0.45, 0.45, color="#E6F4EA", alpha=0.55, label="局部区域")
ax.set_xlabel(r"参数扰动 $d\theta$")
ax.set_ylabel("散度")
ax.set_title("KL 的局部二阶项给出 Fisher 度量", fontsize=16, fontweight="bold")
ax.grid(alpha=0.25)
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
