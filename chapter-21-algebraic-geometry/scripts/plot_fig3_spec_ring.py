"""fig3: Spec ring conceptual points."""
import os
from pathlib import Path
os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
out=Path(__file__).resolve().parents[1]/"images"/"fig3_spec_ring.png"
fig,ax=plt.subplots(figsize=(9,5)); ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")
ax.text(.5,.86,r"$\mathrm{Spec}(R)$",ha="center",fontsize=22,fontweight="bold")
for i,(x,y,lbl) in enumerate([(.2,.45,"(2)"),(.38,.32,"(3)"),(.56,.52,"(5)"),(.75,.37,"(p)"),(.5,.2,"(0)")]):
    ax.add_patch(Circle((x,y),.055,facecolor="#1A73E8" if lbl!="(0)" else "#D93025",edgecolor="white",lw=2))
    ax.text(x,y,lbl,ha="center",va="center",color="white",fontsize=12,fontweight="bold")
ax.text(.5,.08,"素理想成为空间中的点；环的代数结构变成几何结构",ha="center",fontsize=13,color="#5F6368")
ax.set_title("概形思想：把环看成空间",fontsize=16,fontweight="bold")
plt.tight_layout(); plt.savefig(out,dpi=150,bbox_inches="tight"); plt.close(); print(f"{out.name} saved")
