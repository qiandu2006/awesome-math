"""fig5: 弱解把导数转移到测试函数上。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig5_weak_solution.png"

x = np.linspace(-2, 2, 900)
u = np.where(x < 0, 1.0, 0.25)
phi = np.exp(-4 * (x - 0.25) ** 2)
dphi = -8 * (x - 0.25) * phi

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].plot(x, u, color="#D93025", lw=3)
axes[0].plot(x, phi, color="#1A73E8", lw=2.5)
axes[0].fill_between(x, 0, phi, color="#AECBFA", alpha=0.4)
axes[0].set_title("不光滑解 u 与光滑测试函数 φ", fontsize=13, fontweight="bold")
axes[0].legend(["跳跃函数 u", "测试函数 φ"], frameon=False)
axes[0].grid(alpha=0.25)

axes[1].plot(x, dphi, color="#188038", lw=3)
axes[1].axhline(0, color="#202124", lw=1)
axes[1].set_title("分部积分：导数落到 φ 上", fontsize=13, fontweight="bold")
axes[1].text(-1.65, 1.15, r"$\int u\,\partial_x\varphi$", fontsize=16, color="#202124")
axes[1].grid(alpha=0.25)

for ax in axes:
    ax.set_xlabel("x")

fig.suptitle("弱解：不要求 u 逐点可导，而要求积分恒等式成立", fontsize=16, fontweight="bold", y=1.03)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
