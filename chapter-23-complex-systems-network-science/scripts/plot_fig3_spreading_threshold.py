"""fig3: Spreading thresholds under different network heterogeneity."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig3_spreading_threshold.png"

beta = np.linspace(0, 1.0, 300)

def outbreak(x, threshold, steepness):
    return 1 / (1 + np.exp(-steepness * (x - threshold)))

homogeneous = outbreak(beta, 0.55, 18)
heterogeneous = outbreak(beta, 0.28, 16)

fig, ax = plt.subplots(figsize=(8.6, 5.4))
ax.plot(beta, homogeneous, color="#1A73E8", lw=3, label="均匀网络")
ax.plot(beta, heterogeneous, color="#D93025", lw=3, label="含 hub 的异质网络")
ax.axvline(0.55, color="#1A73E8", lw=1.5, ls="--", alpha=0.65)
ax.axvline(0.28, color="#D93025", lw=1.5, ls="--", alpha=0.65)
ax.fill_between(beta, heterogeneous, homogeneous, where=homogeneous > heterogeneous, color="#FCE8E6", alpha=0.55)

ax.text(0.22, 0.12, "hub 降低传播阈值", color="#D93025", fontsize=12, fontweight="bold")
ax.text(0.58, 0.44, "连接更均匀时\n需要更高感染率", color="#1A73E8", fontsize=12)
ax.set_xlabel("传播强度")
ax.set_ylabel("最终受影响比例")
ax.set_ylim(-0.02, 1.04)
ax.set_title("传播是否爆发，取决于规则和网络结构", fontsize=16, fontweight="bold")
ax.grid(alpha=0.25)
ax.legend(frameon=False, loc="lower right")

plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
