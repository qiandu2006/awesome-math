"""fig2: Wasserstein 距离看见质量移动。"""
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
out = Path(__file__).resolve().parents[1] / "images" / "fig2_wasserstein_vs_kl.png"

x = np.linspace(-5, 5, 800)
fig, ax = plt.subplots(figsize=(9, 5.5))
for shift, color in [(0, "#1A73E8"), (1.2, "#D93025")]:
    y = np.exp(-0.5 * (x - shift) ** 2) / np.sqrt(2 * np.pi)
    ax.plot(x, y, lw=3, color=color, label=f"均值 {shift}")
ax.annotate("Wasserstein 看到整体位移", xy=(0.2, 0.24), xytext=(1.45, 0.33),
            arrowprops=dict(arrowstyle="->", lw=2), fontsize=13)
ax.set_title("Wasserstein 距离：分布差异可以是几何位移", fontsize=15, fontweight="bold")
ax.set_xlabel("x")
ax.set_ylabel("密度")
ax.grid(alpha=0.25)
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
