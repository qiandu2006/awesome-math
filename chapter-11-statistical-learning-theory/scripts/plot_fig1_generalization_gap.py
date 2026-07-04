"""fig1: 模型复杂度与泛化误差。"""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig1_generalization_gap.png"

x = np.linspace(0, 1, 500)
train = 0.48 * np.exp(-3.2 * x) + 0.035
test = 0.20 + 0.42 * (x - 0.42) ** 2 + 0.30 * np.maximum(x - 0.55, 0) ** 2
gap = test - train

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(x, train, lw=3, color="#1A73E8", label="训练误差")
ax.plot(x, test, lw=3, color="#D93025", label="测试误差")
ax.fill_between(x, train, test, where=gap > 0, color="#FCE8E6", alpha=0.9, label="泛化差距")

best = x[np.argmin(test)]
ax.axvline(best, color="#188038", ls="--", lw=2)
ax.text(best + 0.015, 0.52, "合适复杂度", color="#188038", fontsize=12, fontweight="bold")
ax.text(0.10, 0.48, "欠拟合\n偏差大", ha="center", fontsize=12, color="#5F6368")
ax.text(0.82, 0.54, "过拟合\n方差大", ha="center", fontsize=12, color="#5F6368")

ax.set_xlabel("模型复杂度")
ax.set_ylabel("误差")
ax.set_title("泛化问题：训练误差下降不等于测试误差下降", fontsize=15, fontweight="bold")
ax.set_xlim(0, 1)
ax.set_ylim(0, 0.75)
ax.grid(alpha=0.25)
ax.legend(frameon=False, loc="upper center", ncol=3)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
