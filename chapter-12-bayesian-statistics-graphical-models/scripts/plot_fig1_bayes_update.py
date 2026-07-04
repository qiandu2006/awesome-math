"""fig1: 贝叶斯更新中的先验、似然与后验。"""
import math
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig1_bayes_update.png"


def beta_pdf(x, a, b):
    log_norm = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    return np.exp(log_norm + (a - 1) * np.log(x) + (b - 1) * np.log(1 - x))


theta = np.linspace(1e-4, 1 - 1e-4, 900)
prior = beta_pdf(theta, 2, 2)
h, t = 7, 3
likelihood = theta ** h * (1 - theta) ** t
likelihood = likelihood / np.trapezoid(likelihood, theta)
posterior = beta_pdf(theta, 2 + h, 2 + t)

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(theta, prior, lw=3, color="#5F6368", label="先验 Beta(2,2)")
ax.plot(theta, likelihood, lw=3, color="#F9AB00", label="似然：7 正 3 反")
ax.plot(theta, posterior, lw=3, color="#1A73E8", label="后验 Beta(9,5)")
ax.axvline(h / (h + t), color="#D93025", ls="--", lw=2)
ax.text(0.71, 3.7, "样本频率 0.7", color="#D93025", fontsize=12, fontweight="bold")
ax.text(0.42, 1.25, "后验 = 先验 × 证据\n再归一化", fontsize=13, color="#202124")
ax.set_xlabel("硬币正面概率 θ")
ax.set_ylabel("密度")
ax.set_title("贝叶斯更新：旧信念遇到新证据", fontsize=15, fontweight="bold")
ax.set_xlim(0, 1)
ax.grid(alpha=0.25)
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
