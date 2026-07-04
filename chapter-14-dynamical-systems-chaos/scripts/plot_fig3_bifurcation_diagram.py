"""fig3: pitchfork 分岔图。"""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig3_bifurcation_diagram.png"

mu_neg = np.linspace(-1.5, 0, 200)
mu_pos = np.linspace(0, 1.5, 300)

fig, ax = plt.subplots(figsize=(8.5, 6))
ax.plot(mu_neg, np.zeros_like(mu_neg), color="#188038", lw=3, label="稳定固定点")
ax.plot(mu_pos, np.zeros_like(mu_pos), color="#D93025", lw=3, ls="--", label="不稳定固定点")
ax.plot(mu_pos, np.sqrt(mu_pos), color="#188038", lw=3)
ax.plot(mu_pos, -np.sqrt(mu_pos), color="#188038", lw=3)
ax.axvline(0, color="#5F6368", lw=1.5)
ax.scatter([0], [0], color="#202124", s=55, zorder=5)
ax.text(0.08, 0.18, "临界参数\n结构改变", fontsize=12, color="#202124")
ax.set_xlabel(r"参数 $\mu$")
ax.set_ylabel("长期平衡 $x^*$")
ax.set_title(r"分岔：$\dot x=\mu x-x^3$ 的长期结构随参数改变", fontsize=15, fontweight="bold")
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.4, 1.4)
ax.grid(alpha=0.25)
ax.legend(frameon=False, loc="upper left")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
