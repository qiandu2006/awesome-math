"""fig3: Characteristic class as a cohomological shadow of twisting."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig3_characteristic_class.png"

fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis("off")

boxes = [
    (0.7, 1.55, 2.0, 1.8, "向量丛 E", "局部平凡\n全局可能扭曲", "#E8F0FE"),
    (4.0, 1.55, 2.0, 1.8, "曲率 / 粘合", "转移函数\n联络曲率", "#FEF7E0"),
    (7.3, 1.55, 2.0, 1.8, "示性类", r"$c(E)\in H^*(M)$", "#E6F4EA"),
]
for x, y, w, h, title, body, color in boxes:
    ax.add_patch(patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.08",
                                        facecolor=color, edgecolor="#BDC1C6", lw=1.8))
    ax.text(x + w / 2, y + 1.17, title, ha="center", fontsize=13, fontweight="bold")
    ax.text(x + w / 2, y + 0.55, body, ha="center", fontsize=12, color="#3C4043")
for x in [3.05, 6.35]:
    ax.annotate("", xy=(x + 0.65, 2.45), xytext=(x, 2.45), arrowprops=dict(arrowstyle="->", lw=2, color="#5F6368"))
ax.text(5, 4.35, "示性类：把全局扭曲投影成上同调不变量", ha="center", fontsize=16, fontweight="bold")
ax.text(5, 0.65, "它不记录所有几何细节，但能抓住无法消除的拓扑障碍", ha="center", fontsize=12, color="#5F6368")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
