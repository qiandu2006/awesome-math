"""fig2: Long-tailed degree distribution on log-log axes."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig2_degree_distribution.png"

k = np.arange(1, 80)
gamma = 2.4
pk = k ** (-gamma)
pk = pk / pk.sum()
rng = np.random.default_rng(11)
observed = pk * np.exp(rng.normal(scale=0.13, size=len(k)))

fig, ax = plt.subplots(figsize=(8.4, 5.4))
ax.loglog(k, observed, "o", color="#1A73E8", markersize=5, alpha=0.78, label="模拟网络")
ax.loglog(k, pk, color="#D93025", lw=2.8, label=r"$P(k)\sim k^{-\gamma}$")
ax.fill_between(k, pk, observed, color="#E8F0FE", alpha=0.45)

ax.annotate("少数 hub\n连接极多", xy=(43, pk[42]), xytext=(22, 0.018),
            arrowprops=dict(arrowstyle="->", lw=1.5, color="#5F6368"),
            fontsize=12, color="#202124")
ax.annotate("多数节点\n连接很少", xy=(3, pk[2]), xytext=(6, 0.18),
            arrowprops=dict(arrowstyle="->", lw=1.5, color="#5F6368"),
            fontsize=12, color="#202124")

ax.set_xlabel("度 k")
ax.set_ylabel("概率 P(k)")
ax.set_title("尺度无关网络：度分布呈长尾", fontsize=16, fontweight="bold")
ax.grid(True, which="both", alpha=0.25)
ax.legend(frameon=False)

plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
