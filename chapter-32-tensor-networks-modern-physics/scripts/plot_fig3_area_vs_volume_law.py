"""fig3: Area law versus volume law entanglement scaling."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig3_area_vs_volume_law.png"

L = np.arange(1, 60)
area = 1.2 * np.log1p(L) ** 0.35 + 0.4
volume = 0.065 * L + 0.35

fig, ax = plt.subplots(figsize=(8.4, 5.2))
ax.plot(L, area, color="#1A73E8", lw=3, label="面积律：纠缠增长慢")
ax.plot(L, volume, color="#D93025", lw=3, label="体积律：纠缠随规模增长")
ax.fill_between(L, area, volume, where=volume > area, color="#FCE8E6", alpha=0.45)
ax.set_xlabel("子系统大小")
ax.set_ylabel("纠缠熵")
ax.set_title("张量网络是否有效，取决于纠缠增长规律", fontsize=16, fontweight="bold")
ax.text(34, area[33] + 0.2, "可压缩", color="#1A73E8", fontsize=12, fontweight="bold")
ax.text(37, volume[36] + 0.25, "难压缩", color="#D93025", fontsize=12, fontweight="bold")
ax.grid(alpha=0.25)
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
