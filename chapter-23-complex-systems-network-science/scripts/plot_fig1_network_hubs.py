"""fig1: A stylized network with hubs, communities, and shortcuts."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig1_network_hubs.png"

rng = np.random.default_rng(7)
centers = np.array([[-1.6, 0.3], [0.6, 0.6], [0.2, -1.2]])
points = []
groups = []
for idx, center in enumerate(centers):
    pts = center + rng.normal(scale=0.32, size=(11, 2))
    points.append(pts)
    groups.extend([idx] * len(pts))
pos = np.vstack(points)
groups = np.array(groups)

hub_indices = [0, 13, 25]
edges = []
for g in range(3):
    ids = np.where(groups == g)[0]
    hub = hub_indices[g]
    for i in ids:
        if i != hub:
            edges.append((hub, i))
    for _ in range(11):
        a, b = rng.choice(ids, 2, replace=False)
        edges.append((int(a), int(b)))
edges += [(0, 13), (13, 25), (5, 20), (9, 30), (2, 27)]

fig, ax = plt.subplots(figsize=(8.8, 6.2))
for a, b in edges:
    lw = 1.7 if a in hub_indices or b in hub_indices else 0.9
    color = "#5F6368" if (groups[a] != groups[b]) else "#B0BEC5"
    alpha = 0.62 if groups[a] != groups[b] else 0.48
    ax.plot([pos[a, 0], pos[b, 0]], [pos[a, 1], pos[b, 1]], color=color, lw=lw, alpha=alpha, zorder=1)

palette = np.array(["#1A73E8", "#D93025", "#188038"])
sizes = np.full(len(pos), 110.0)
sizes[hub_indices] = 330
ax.scatter(pos[:, 0], pos[:, 1], s=sizes, c=palette[groups], edgecolor="white", lw=1.8, zorder=3)

for idx, label in zip(hub_indices, ["hub A", "hub B", "hub C"]):
    ax.text(pos[idx, 0], pos[idx, 1] + 0.23, label, ha="center", fontsize=11, fontweight="bold")

ax.set_title("网络结构：枢纽、群落和少量长程连接", fontsize=16, fontweight="bold")
ax.text(-2.25, -1.9, "局部团块保持聚集；长程边让整体距离变短", fontsize=12, color="#5F6368")
ax.set_aspect("equal")
ax.axis("off")
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
