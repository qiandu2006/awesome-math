"""fig3: Scaling law as a power-law relation."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig3_scaling_law.png"

rng = np.random.default_rng(23)
compute = np.logspace(0, 5, 70)
alpha = 0.18
irreducible = 1.05
loss = 3.8 * compute ** (-alpha) + irreducible
observed = loss * np.exp(rng.normal(scale=0.025, size=len(loss)))

fig, ax = plt.subplots(figsize=(8.6, 5.4))
ax.loglog(compute, observed, "o", color="#1A73E8", markersize=5, alpha=0.75, label="实验观测")
ax.loglog(compute, loss, color="#D93025", lw=3, label=r"$L(C)=AC^{-\alpha}+L_\infty$")
ax.axhline(irreducible, color="#5F6368", lw=1.5, ls="--", alpha=0.8)
ax.text(1.2, irreducible * 1.06, "不可约损失", fontsize=11, color="#5F6368")

ax.annotate("资源增加带来稳定但递减的收益", xy=(1.8e3, np.interp(1.8e3, compute, loss)),
            xytext=(65, 2.35),
            arrowprops=dict(arrowstyle="->", lw=1.5, color="#5F6368"),
            fontsize=12)

ax.set_xlabel("计算量 / 数据量 / 模型规模")
ax.set_ylabel("验证损失")
ax.set_title("缩放律：性能随规模呈幂律改善", fontsize=16, fontweight="bold")
ax.grid(True, which="both", alpha=0.25)
ax.legend(frameon=False)

plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
