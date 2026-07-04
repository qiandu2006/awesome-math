"""fig2: 偏差-方差权衡。"""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig2_bias_variance.png"
rng = np.random.default_rng(7)

x = np.linspace(0, 1, 300)
truth = np.sin(2 * np.pi * x) + 0.35 * np.sin(6 * np.pi * x)

fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

for ax, degree, title in [
    (axes[0], 2, "低复杂度：偏差大，方差小"),
    (axes[1], 13, "高复杂度：偏差小，方差大"),
]:
    preds = []
    for _ in range(22):
        xs = np.sort(rng.uniform(0, 1, 24))
        ys = np.sin(2 * np.pi * xs) + 0.35 * np.sin(6 * np.pi * xs) + rng.normal(0, 0.22, xs.size)
        coef = np.polyfit(xs, ys, degree)
        pred = np.polyval(coef, x)
        preds.append(pred)
        ax.plot(x, pred, color="#9AA0A6", lw=1, alpha=0.35)

    mean_pred = np.mean(preds, axis=0)
    ax.plot(x, truth, color="#202124", lw=3, label="真实函数")
    ax.plot(x, mean_pred, color="#1A73E8", lw=3, label="平均预测")
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.set_xlabel("x")
    ax.set_ylim(-1.8, 1.8)
    ax.grid(alpha=0.22)

axes[0].set_ylabel("y")
axes[0].legend(frameon=False, loc="lower left")
plt.suptitle("偏差-方差：平均偏离与样本敏感性", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
