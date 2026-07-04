"""fig2: Prime splitting types in a number field."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig2_prime_splitting.png"

fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis("off")

cases = [
    (1.6, "分裂", r"$(p)=p_1p_2$", ["p1", "p2"], "#E8F0FE"),
    (5.0, "惰性", r"$(p)=P$", ["P"], "#E6F4EA"),
    (8.4, "分歧", r"$(p)=p^2$", ["p", "p"], "#FCE8E6"),
]
for x, title, formula, labels, color in cases:
    ax.add_patch(patches.Circle((x, 3.35), 0.42, facecolor="#5F6368", edgecolor="white", lw=2))
    ax.text(x, 3.35, "p", color="white", ha="center", va="center", fontsize=13, fontweight="bold")
    ax.text(x, 4.25, title, ha="center", fontsize=15, fontweight="bold")
    if len(labels) == 1:
        ys = [(x, 1.75)]
    else:
        ys = [(x - 0.45, 1.75), (x + 0.45, 1.75)]
    for j, (xx, yy) in enumerate(ys):
        ax.plot([x, xx], [2.95, yy + 0.42], color="#9AA0A6", lw=2)
        ax.add_patch(patches.Circle((xx, yy), 0.42, facecolor=color, edgecolor="#BDC1C6", lw=1.8))
        ax.text(xx, yy, labels[j], ha="center", va="center", fontsize=12, fontweight="bold")
    ax.text(x, 0.65, formula, ha="center", fontsize=13, color="#3C4043")

ax.text(5, 0.15, "同一个有理素数，在扩张数域的整数环中可能有不同分解类型", ha="center", fontsize=12, color="#5F6368")
ax.set_title("素数进入数域后：分裂、惰性、分歧", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
