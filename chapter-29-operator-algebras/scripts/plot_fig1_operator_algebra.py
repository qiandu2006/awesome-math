"""fig1: From finite matrices to operator algebras."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig1_operator_algebra.png"

fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis("off")
items = [
    (1.4, "矩阵", r"$M_n(C)$", "有限维", "#E8F0FE"),
    (5.0, "有界算子", r"$B(H)$", "无限维", "#E6F4EA"),
    (8.4, "算子代数", r"$A\subset B(H)$", "闭合结构", "#FCE8E6"),
]
for x, title, formula, subtitle, color in items:
    ax.add_patch(patches.FancyBboxPatch((x - 1.05, 1.45), 2.1, 2.0,
                                        boxstyle="round,pad=0.04,rounding_size=0.08",
                                        facecolor=color, edgecolor="#BDC1C6", lw=1.8))
    ax.text(x, 2.95, title, ha="center", fontsize=14, fontweight="bold")
    ax.text(x, 2.38, formula, ha="center", fontsize=14, color="#1A73E8")
    ax.text(x, 1.88, subtitle, ha="center", fontsize=11, color="#5F6368")
for x in [3.0, 6.6]:
    ax.annotate("", xy=(x + 0.8, 2.45), xytext=(x, 2.45), arrowprops=dict(arrowstyle="->", lw=2, color="#5F6368"))
ax.text(5, 4.35, "算子代数：研究一族算子在代数运算和极限下的闭合结构", ha="center", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
