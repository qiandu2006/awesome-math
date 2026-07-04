"""fig1: Markov decision process loop."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig1_mdp_loop.png"

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 8)
ax.set_ylim(0, 6)
ax.axis("off")
nodes = {
    "状态 s": (2, 4.2, "#E8F0FE"),
    "策略 π": (6, 4.2, "#FEF7E0"),
    "动作 a": (6, 1.8, "#E6F4EA"),
    "环境 P": (2, 1.8, "#FCE8E6"),
}
for label, (x, y, color) in nodes.items():
    ax.add_patch(patches.FancyBboxPatch((x - 0.9, y - 0.45), 1.8, 0.9,
                                        boxstyle="round,pad=0.04,rounding_size=0.08",
                                        facecolor=color, edgecolor="#BDC1C6", lw=1.8))
    ax.text(x, y, label, ha="center", va="center", fontsize=13, fontweight="bold")
arrows = [((2.9, 4.2), (5.1, 4.2), "选择"), ((6, 3.75), (6, 2.25), "执行"),
          ((5.1, 1.8), (2.9, 1.8), "转移"), ((2, 2.25), (2, 3.75), "新状态")]
for start, end, text in arrows:
    ax.annotate("", xy=end, xytext=start, arrowprops=dict(arrowstyle="->", lw=2.2, color="#5F6368"))
    ax.text((start[0] + end[0]) / 2, (start[1] + end[1]) / 2 + 0.18, text, ha="center", fontsize=11, color="#5F6368")
ax.text(4, 0.75, r"回报 $r(s,a)$ 反馈给学习过程", ha="center", fontsize=13, color="#1A73E8", fontweight="bold")
ax.set_title("MDP：状态、策略、动作和随机环境形成闭环", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
