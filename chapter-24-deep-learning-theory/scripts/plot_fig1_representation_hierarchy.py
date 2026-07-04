"""fig1: Representation hierarchy in a deep network."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig1_representation_hierarchy.png"

layers = [
    ("原始输入", "像素 / token\n局部信号", "#E8F0FE"),
    ("低层特征", "边缘 / 片段\n短程模式", "#E6F4EA"),
    ("中层组合", "纹理 / 部件\n局部结构", "#FEF7E0"),
    ("高层表示", "概念 / 关系\n任务相关", "#FCE8E6"),
    ("输出", "分类 / 生成\n决策", "#F3E8FD"),
]

fig, ax = plt.subplots(figsize=(10, 5.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5.2)
ax.axis("off")

xs = [0.7, 2.7, 4.7, 6.7, 8.55]
for i, ((title, body, color), x) in enumerate(zip(layers, xs)):
    width = 1.35 if i < 4 else 1.2
    rect = patches.FancyBboxPatch(
        (x, 1.5),
        width,
        2.15,
        boxstyle="round,pad=0.04,rounding_size=0.06",
        facecolor=color,
        edgecolor="#BDC1C6",
        lw=1.5,
    )
    ax.add_patch(rect)
    ax.text(x + width / 2, 3.12, title, ha="center", va="center", fontsize=13, fontweight="bold")
    ax.text(x + width / 2, 2.3, body, ha="center", va="center", fontsize=11, color="#3C4043")
    if i < len(xs) - 1:
        ax.annotate("", xy=(xs[i + 1] - 0.1, 2.58), xytext=(x + width + 0.12, 2.58),
                    arrowprops=dict(arrowstyle="->", lw=2.0, color="#5F6368"))

ax.text(5, 4.55, "深度表示学习：逐层改变坐标系，让任务结构更清楚", ha="center", fontsize=16, fontweight="bold")
ax.text(5, 0.72, r"$f_\theta=f_L\circ f_{L-1}\circ\cdots\circ f_1$", ha="center", fontsize=18, color="#1A73E8")

plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
