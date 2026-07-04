"""fig2: cusp and node singularities."""
import os
from pathlib import Path
import numpy as np
os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
out=Path(__file__).resolve().parents[1]/"images"/"fig2_singularities.png"
t=np.linspace(-1.3,1.3,500)
fig,axes=plt.subplots(1,2,figsize=(11,5))
axes[0].plot(t**2,t**3,color="#1A73E8",lw=3); axes[0].set_title("尖点奇点",fontweight="bold")
x=np.linspace(-1.2,1.2,600); val=x**2*(x+1)
mask=val>=0
axes[1].plot(x[mask],np.sqrt(val[mask]),color="#D93025",lw=3); axes[1].plot(x[mask],-np.sqrt(val[mask]),color="#D93025",lw=3); axes[1].set_title("交叉/节点奇点",fontweight="bold")
for ax in axes:
    ax.scatter([0],[0],s=70,color="#202124",zorder=5); ax.axhline(0,color="#ddd"); ax.axvline(0,color="#ddd"); ax.set_aspect("equal"); ax.grid(alpha=.2)
fig.suptitle("奇点：代数曲线局部不再像光滑流形",fontsize=16,fontweight="bold")
plt.tight_layout(); plt.savefig(out,dpi=150,bbox_inches="tight"); plt.close(); print(f"{out.name} saved")
