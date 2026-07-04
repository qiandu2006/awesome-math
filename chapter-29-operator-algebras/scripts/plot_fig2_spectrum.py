"""fig2: Point spectrum and continuous spectrum."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig2_spectrum.png"

fig, axes = plt.subplots(1, 2, figsize=(9, 4.5), sharey=True)
eig = np.array([-2, -0.8, 0.4, 1.7])
axes[0].axhline(0, color="#5F6368", lw=1.5)
axes[0].scatter(eig, np.zeros_like(eig), s=120, color="#1A73E8", zorder=3)
for e in eig:
    axes[0].text(e, 0.12, f"{e:g}", ha="center", fontsize=10)
axes[0].set_title("有限维矩阵：离散特征值", fontsize=13, fontweight="bold")

x = np.linspace(-2, 2, 400)
axes[1].axhline(0, color="#5F6368", lw=1.5)
axes[1].plot(x, np.zeros_like(x), color="#D93025", lw=8, solid_capstyle="round")
axes[1].text(0, 0.16, "连续谱区间", ha="center", fontsize=12, color="#D93025", fontweight="bold")
axes[1].set_title("无限维算子：可能有连续谱", fontsize=13, fontweight="bold")

for ax in axes:
    ax.set_xlim(-2.7, 2.7)
    ax.set_ylim(-0.5, 0.6)
    ax.set_yticks([])
    ax.set_xlabel("谱参数 λ")
    ax.grid(axis="x", alpha=0.2)

fig.suptitle("谱：可逆性失败的位置", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
