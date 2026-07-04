"""fig1: 多项式方程定义几何形状。"""
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
out = Path(__file__).resolve().parents[1] / "images" / "fig1_varieties.png"
t=np.linspace(0,2*np.pi,500)
x=np.cos(t); y=np.sin(t)
xe=np.linspace(-1.2,1.2,600); ye2=xe**3-xe
fig,axes=plt.subplots(1,2,figsize=(11,5))
axes[0].plot(x,y,lw=3,color="#1A73E8"); axes[0].set_title(r"$x^2+y^2=1$",fontweight="bold")
mask=ye2>=0
axes[1].plot(xe[mask],np.sqrt(ye2[mask]),color="#D93025",lw=3)
axes[1].plot(xe[mask],-np.sqrt(ye2[mask]),color="#D93025",lw=3)
axes[1].set_title(r"$y^2=x^3-x$",fontweight="bold")
for ax in axes:
    ax.axhline(0,color="#ccc"); ax.axvline(0,color="#ccc"); ax.set_aspect("equal"); ax.grid(alpha=.2)
fig.suptitle("多项式方程的零点形成几何对象",fontsize=16,fontweight="bold")
plt.tight_layout(); plt.savefig(out,dpi=150,bbox_inches="tight"); plt.close(); print(f"{out.name} saved")
