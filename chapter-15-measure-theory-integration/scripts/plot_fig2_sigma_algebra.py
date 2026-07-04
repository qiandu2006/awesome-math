"""fig2: sigma 代数对补集和可数并封闭。"""
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig2_sigma_algebra.png"

fig, axes = plt.subplots(1, 3, figsize=(13, 4.6))
for ax in axes:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Rectangle((0.08, 0.15), 0.84, 0.68, facecolor="#F8F9FA", edgecolor="#5F6368", lw=2))

axes[0].add_patch(Circle((0.43, 0.49), 0.20, facecolor="#1A73E8", alpha=0.75, edgecolor="none"))
axes[0].text(0.43, 0.49, "A", ha="center", va="center", color="white", fontsize=15, fontweight="bold")
axes[0].set_title("集合 A 可测", fontsize=13, fontweight="bold")

axes[1].add_patch(Rectangle((0.08, 0.15), 0.84, 0.68, facecolor="#AECBFA", alpha=0.65, edgecolor="#5F6368", lw=2))
axes[1].add_patch(Circle((0.43, 0.49), 0.20, facecolor="white", edgecolor="#1A73E8", lw=2))
axes[1].text(0.68, 0.49, r"$A^c$", ha="center", va="center", color="#1A73E8", fontsize=15, fontweight="bold")
axes[1].set_title("补集也可测", fontsize=13, fontweight="bold")

for i, x in enumerate([0.30, 0.44, 0.58]):
    axes[2].add_patch(Circle((x, 0.50), 0.16, facecolor="#1A73E8", alpha=0.35 + 0.15 * i,
                             edgecolor="#1A73E8", lw=1.5))
axes[2].text(0.46, 0.50, r"$\bigcup_n A_n$", ha="center", va="center", color="#202124", fontsize=15, fontweight="bold")
axes[2].set_title("可数并也可测", fontsize=13, fontweight="bold")

fig.suptitle(r"$\sigma$-代数：允许测量的集合族必须对基本逻辑操作封闭",
             fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
