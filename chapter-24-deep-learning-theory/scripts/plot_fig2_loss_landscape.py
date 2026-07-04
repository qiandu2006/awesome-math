"""fig2: Sharp and flat minima in a stylized loss landscape."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig2_loss_landscape.png"

x = np.linspace(-4.5, 4.5, 600)
flat = 0.23 + 0.045 * (x + 2.0) ** 2 + 0.008 * (x + 2.0) ** 4
sharp = 0.22 + 1.55 * (x - 2.1) ** 2
baseline = 1.55 + 0.16 * np.sin(2.4 * x) + 0.04 * (x ** 2)
loss = np.minimum(np.minimum(flat, sharp), baseline)

fig, ax = plt.subplots(figsize=(8.8, 5.2))
ax.plot(x, loss, color="#202124", lw=2.8)
ax.fill_between(x, loss, 2.35, color="#E8F0FE", alpha=0.7)

flat_x = -2.0
sharp_x = 2.1
flat_y = np.interp(flat_x, x, loss)
sharp_y = np.interp(sharp_x, x, loss)
ax.scatter([flat_x, sharp_x], [flat_y, sharp_y], s=90, color=["#1A73E8", "#D93025"], zorder=3)
ax.annotate("平坦极小值\n扰动后损失变化小", xy=(flat_x, flat_y), xytext=(-3.95, 1.1),
            arrowprops=dict(arrowstyle="->", lw=1.6, color="#1A73E8"),
            fontsize=12, color="#1A73E8", fontweight="bold")
ax.annotate("尖锐极小值\n对参数扰动敏感", xy=(sharp_x, sharp_y), xytext=(1.2, 1.55),
            arrowprops=dict(arrowstyle="->", lw=1.6, color="#D93025"),
            fontsize=12, color="#D93025", fontweight="bold")

ax.set_xlabel("参数方向的二维切片")
ax.set_ylabel("训练损失")
ax.set_ylim(0.1, 2.25)
ax.set_title("非凸损失景观：训练找到的是低损失区域", fontsize=16, fontweight="bold")
ax.grid(alpha=0.22)

plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
