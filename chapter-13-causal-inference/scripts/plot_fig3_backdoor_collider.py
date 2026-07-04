"""fig3: 后门调整与碰撞点偏差。"""
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

out = Path(__file__).resolve().parents[1] / "images" / "fig3_backdoor_collider.png"


def node(ax, xy, label, color):
    circ = Circle(xy, 0.09, facecolor=color, edgecolor="white", lw=2, zorder=3)
    ax.add_patch(circ)
    ax.text(*xy, label, ha="center", va="center", color="white", fontsize=14, fontweight="bold")


def arrow(ax, start, end, color="#202124"):
    arr = FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=18,
                          color=color, lw=2.4, shrinkA=16, shrinkB=16)
    ax.add_patch(arr)


fig, axes = plt.subplots(1, 2, figsize=(11, 5))
for ax in axes:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")

# Backdoor
axes[0].set_title("后门路径：应该控制 Z", fontsize=14, fontweight="bold")
node(axes[0], (0.50, 0.78), "Z", "#188038")
node(axes[0], (0.28, 0.35), "X", "#1A73E8")
node(axes[0], (0.72, 0.35), "Y", "#D93025")
arrow(axes[0], (0.45, 0.70), (0.33, 0.44))
arrow(axes[0], (0.55, 0.70), (0.67, 0.44))
arrow(axes[0], (0.38, 0.35), (0.62, 0.35))
axes[0].plot([0.40, 0.60], [0.63, 0.63], color="#188038", lw=4)
axes[0].text(0.50, 0.16, r"控制 Z 阻断 $X \leftarrow Z \to Y$", ha="center",
             fontsize=12, color="#5F6368")

# Collider
axes[1].set_title("碰撞点：不要随便控制 C", fontsize=14, fontweight="bold")
node(axes[1], (0.28, 0.70), "X", "#1A73E8")
node(axes[1], (0.72, 0.70), "Y", "#D93025")
node(axes[1], (0.50, 0.35), "C", "#F9AB00")
arrow(axes[1], (0.35, 0.63), (0.45, 0.43))
arrow(axes[1], (0.65, 0.63), (0.55, 0.43))
axes[1].plot([0.42, 0.58], [0.24, 0.24], color="#D93025", lw=4)
axes[1].text(0.50, 0.16, r"控制 C 会打开 $X \to C \leftarrow Y$", ha="center",
             fontsize=12, color="#5F6368")

fig.suptitle("控制变量的对象必须由因果图决定", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
