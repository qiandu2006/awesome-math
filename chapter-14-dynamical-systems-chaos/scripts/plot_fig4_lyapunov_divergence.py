"""fig4: 正 Lyapunov 指数导致初值误差指数放大。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig4_lyapunov_divergence.png"

r = 4.0
n = 75
x1 = np.empty(n)
x2 = np.empty(n)
x1[0] = 0.200000
x2[0] = 0.200001
for i in range(n - 1):
    x1[i + 1] = r * x1[i] * (1 - x1[i])
    x2[i + 1] = r * x2[i] * (1 - x2[i])

diff = np.abs(x2 - x1)
diff[diff == 0] = 1e-16

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].plot(x1, color="#1A73E8", lw=2.5, label="轨道 A")
axes[0].plot(x2, color="#D93025", lw=2.0, alpha=0.8, label="轨道 B")
axes[0].set_title("初值几乎相同的两条轨道", fontsize=13, fontweight="bold")
axes[0].set_xlabel("迭代步")
axes[0].set_ylabel("x")
axes[0].legend(frameon=False)
axes[0].grid(alpha=0.25)

axes[1].semilogy(diff, color="#188038", lw=3)
axes[1].set_title("误差在早期近似指数放大", fontsize=13, fontweight="bold")
axes[1].set_xlabel("迭代步")
axes[1].set_ylabel(r"$|x_t-x'_t|$")
axes[1].grid(alpha=0.25, which="both")
axes[1].text(10, 1e-3, r"$|\delta x_t|\approx e^{\lambda t}|\delta x_0|$",
             fontsize=13, color="#202124")

fig.suptitle("混沌：确定规则仍可能放大微小初值误差", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
