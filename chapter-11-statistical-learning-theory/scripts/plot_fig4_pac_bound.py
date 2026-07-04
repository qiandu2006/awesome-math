"""fig4: PAC 泛化界随样本量下降。"""
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig4_pac_bound.png"

n = np.arange(20, 2001)
delta = 0.05
sizes = [10, 1_000, 1_000_000]
colors = ["#188038", "#1A73E8", "#D93025"]

fig, ax = plt.subplots(figsize=(9, 6))
for size, color in zip(sizes, colors):
    bound = np.sqrt((np.log(size) + np.log(1 / delta)) / (2 * n))
    label = f"|F| = {size:g}"
    ax.plot(n, bound, lw=3, color=color, label=label)

ax.text(1180, 0.08, "样本量增加\n复杂度惩罚下降", fontsize=12, color="#5F6368")
ax.set_xlabel("样本量 n")
ax.set_ylabel("泛化界中的复杂度项")
ax.set_title("PAC 界：更多样本让经验风险更可信", fontsize=15, fontweight="bold")
ax.set_ylim(0, 0.45)
ax.grid(alpha=0.25)
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
