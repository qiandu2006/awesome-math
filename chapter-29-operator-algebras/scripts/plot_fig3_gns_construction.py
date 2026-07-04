"""fig3: GNS construction flow."""
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig3_gns_construction.png"

fig, ax = plt.subplots(figsize=(9.5, 5.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis("off")

steps = [
    (1.4, "代数 A", "可观测量", "#E8F0FE"),
    (3.8, "状态 φ", "期望值", "#FEF7E0"),
    (6.2, r"$H_\varphi$", "Hilbert 空间", "#E6F4EA"),
    (8.6, r"$\pi_\varphi(A)$", "算子表示", "#FCE8E6"),
]
for x, title, body, color in steps:
    ax.add_patch(patches.FancyBboxPatch((x - 0.85, 1.65), 1.7, 1.65,
                                        boxstyle="round,pad=0.04,rounding_size=0.08",
                                        facecolor=color, edgecolor="#BDC1C6", lw=1.8))
    ax.text(x, 2.72, title, ha="center", fontsize=13, fontweight="bold")
    ax.text(x, 2.15, body, ha="center", fontsize=11, color="#5F6368")
for x in [2.35, 4.75, 7.15]:
    ax.annotate("", xy=(x + 0.58, 2.48), xytext=(x, 2.48), arrowprops=dict(arrowstyle="->", lw=2, color="#5F6368"))
ax.text(5, 4.35, "GNS 构造：从状态和代数重建 Hilbert 空间", ha="center", fontsize=16, fontweight="bold")
ax.text(5, 0.8, r"$\varphi(a)=\langle\Omega_\varphi,\pi_\varphi(a)\Omega_\varphi\rangle$", ha="center", fontsize=17, color="#1A73E8")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
