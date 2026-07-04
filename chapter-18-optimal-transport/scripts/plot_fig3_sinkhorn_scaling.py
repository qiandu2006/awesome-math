"""fig3: Sinkhorn 交替缩放行列边缘。"""
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
out = Path(__file__).resolve().parents[1] / "images" / "fig3_sinkhorn_scaling.png"

rng = np.random.default_rng(4)
K = rng.random((8, 8)) ** 2
mu = np.linspace(1, 2, 8); mu = mu / mu.sum()
nu = np.linspace(2, 1, 8); nu = nu / nu.sum()
u = np.ones(8)
v = np.ones(8)
plans = []
for _ in range(4):
    u = mu / (K @ v)
    v = nu / (K.T @ u)
    plans.append(np.diag(u) @ K @ np.diag(v))

fig, axes = plt.subplots(1, 4, figsize=(13, 3.6))
for i, ax in enumerate(axes):
    im = ax.imshow(plans[i], cmap="Blues")
    ax.set_title(f"迭代 {i+1}", fontsize=12, fontweight="bold")
    ax.set_xticks([])
    ax.set_yticks([])
fig.suptitle("Sinkhorn 迭代：交替调整行边缘和列边缘", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
