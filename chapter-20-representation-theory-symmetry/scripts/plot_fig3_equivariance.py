"""fig3: 等变交换图。"""
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
out = Path(__file__).resolve().parents[1] / "images" / "fig3_equivariance.png"

fig, ax = plt.subplots(figsize=(7,5)); ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")
pts = {"x":(0.25,0.75),"gx":(0.25,0.25),"Fx":(0.75,0.75),"gFx":(0.75,0.25)}
for k,p in pts.items():
    ax.text(*p,k,ha="center",va="center",fontsize=17,fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.35",fc="#E8F0FE",ec="#1A73E8"))
for a,b,label in [("x","Fx","F"),("gx","gFx","F"),("x","gx","g"),("Fx","gFx","g")]:
    ax.add_patch(FancyArrowPatch(pts[a],pts[b],arrowstyle="-|>",mutation_scale=18,lw=2.3,color="#202124",shrinkA=28,shrinkB=28))
    mx=(pts[a][0]+pts[b][0])/2; my=(pts[a][1]+pts[b][1])/2
    ax.text(mx+0.03,my+0.03,label,fontsize=13)
ax.text(0.5,0.08,r"$F(gx)=gF(x)$",ha="center",fontsize=17)
ax.set_title("等变性：变换和计算可以交换顺序",fontsize=15,fontweight="bold")
plt.tight_layout(); plt.savefig(out,dpi=150,bbox_inches="tight"); plt.close()
print(f"{out.name} saved")
