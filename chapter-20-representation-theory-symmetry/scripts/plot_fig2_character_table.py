"""fig2: 简化角色表。"""
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(__file__).resolve().parents[1] / ".mplconfig"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
out = Path(__file__).resolve().parents[1] / "images" / "fig2_character_table.png"

data = [["表示/共轭类","e","r","s"],["trivial","1","1","1"],["sign","1","1","-1"],["standard","2","-1","0"]]
fig, ax = plt.subplots(figsize=(7,4.5)); ax.axis("off")
tbl = ax.table(cellText=data, loc="center", cellLoc="center")
tbl.auto_set_font_size(False); tbl.set_fontsize(13); tbl.scale(1.2,1.8)
for (r,c), cell in tbl.get_celld().items():
    if r==0 or c==0:
        cell.set_facecolor("#E8F0FE"); cell.set_text_props(fontweight="bold")
    else:
        cell.set_facecolor("#FFFFFF")
ax.set_title("角色表：用迹记录表示的核心信息", fontsize=15, fontweight="bold", pad=20)
plt.tight_layout(); plt.savefig(out,dpi=150,bbox_inches="tight"); plt.close()
print(f"{out.name} saved")
