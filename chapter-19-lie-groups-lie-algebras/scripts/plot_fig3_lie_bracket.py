"""fig3: Lie 括号的小回路直觉。"""
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
out = Path(__file__).resolve().parents[1] / "images" / "fig3_lie_bracket.png"

fig, ax = plt.subplots(figsize=(7, 6))
pts = [(0,0), (1,0.15), (1.15,1.05), (0.1,1.0), (0,0)]
for a,b in zip(pts[:-1], pts[1:]):
    ax.add_patch(FancyArrowPatch(a,b, arrowstyle="-|>", mutation_scale=16, lw=2.5, color="#1A73E8"))
pts2 = [(0,0), (0.05,1.0), (1.05,1.18), (1.0,0.12)]
for a,b in zip(pts2[:-1], pts2[1:]):
    ax.add_patch(FancyArrowPatch(a,b, arrowstyle="-|>", mutation_scale=16, lw=2.5, color="#D93025", alpha=0.75))
ax.scatter([1.0,1.0],[0.12,0.15], color=["#D93025","#1A73E8"], s=80)
ax.text(1.15,0.14,"小偏差\n≈ [A,B]", fontsize=12, color="#202124")
ax.text(0.5,-0.18,"先 A 后 B 与先 B 后 A 不完全相同", ha="center", fontsize=13, color="#5F6368")
ax.set_xlim(-0.25,1.55); ax.set_ylim(-0.3,1.45)
ax.set_aspect("equal"); ax.axis("off")
ax.set_title("Lie 括号：非交换性的无穷小痕迹", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
