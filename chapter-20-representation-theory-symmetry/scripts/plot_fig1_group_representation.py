"""fig1: 群作用被表示成矩阵作用。"""
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
out = Path(__file__).resolve().parents[1] / "images" / "fig1_group_representation.png"

fig, ax = plt.subplots(figsize=(9, 4.8))
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
for xy, label, color in [((0.18,0.55),"g","#1A73E8"),((0.50,0.55),r"$\rho(g)$","#D93025"),((0.82,0.55),"矩阵作用\n在 V 上","#188038")]:
    c = Circle(xy, 0.11, facecolor=color, edgecolor="white", lw=2)
    ax.add_patch(c); ax.text(*xy, label, ha="center", va="center", color="white", fontsize=14, fontweight="bold")
for a,b,t in [((0.29,0.55),(0.39,0.55),r"$\rho$"),((0.61,0.55),(0.71,0.55),"作用")]:
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=18,lw=2.5,color="#202124"))
    ax.text((a[0]+b[0])/2,0.66,t,ha="center",fontsize=12)
ax.text(0.5,0.22,r"$\rho(g_1g_2)=\rho(g_1)\rho(g_2)$",ha="center",fontsize=16)
ax.set_title("表示：把抽象群元素变成线性变换", fontsize=16, fontweight="bold")
plt.tight_layout(); plt.savefig(out,dpi=150,bbox_inches="tight"); plt.close()
print(f"{out.name} saved")
