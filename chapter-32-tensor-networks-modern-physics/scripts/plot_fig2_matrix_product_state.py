"""fig2: Matrix product state chain."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig2_matrix_product_state.png"

fig, ax = plt.subplots(figsize=(9, 4.8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4.5)
ax.axis("off")
xs = [1.3, 3.1, 4.9, 6.7, 8.5]
for i, x in enumerate(xs):
    ax.add_patch(patches.Circle((x, 2.35), 0.42, facecolor="#E8F0FE", edgecolor="#1A73E8", lw=2))
    ax.text(x, 2.35, rf"$A^{i+1}$", ha="center", va="center", fontsize=12, fontweight="bold")
    ax.plot([x, x], [1.1, 1.93], color="#D93025", lw=2)
    ax.text(x, 0.82, rf"$s_{i+1}$", ha="center", fontsize=12, color="#D93025")
for x1, x2 in zip(xs[:-1], xs[1:]):
    ax.plot([x1 + 0.42, x2 - 0.42], [2.35, 2.35], color="#5F6368", lw=2.4)
    ax.text((x1 + x2) / 2, 2.62, "χ", ha="center", fontsize=12, color="#5F6368")
ax.text(5, 3.75, "矩阵乘积态：一维链上的局部张量 + 内部 bond", ha="center", fontsize=16, fontweight="bold")
ax.text(5, 0.28, "bond dimension χ 控制可表达的纠缠强度", ha="center", fontsize=12, color="#5F6368")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
