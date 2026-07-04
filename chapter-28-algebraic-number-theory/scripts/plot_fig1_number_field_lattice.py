"""fig1: Lattice picture of a quadratic number field embedding."""
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

out = Path(__file__).resolve().parents[1] / "images" / "fig1_number_field_lattice.png"

pts = []
for a in range(-4, 5):
    for b in range(-4, 5):
        pts.append((a + b * np.sqrt(2), a - b * np.sqrt(2), a, b))
pts = np.array(pts, dtype=float)

fig, ax = plt.subplots(figsize=(7.5, 6.2))
ax.scatter(pts[:, 0], pts[:, 1], s=28, color="#1A73E8", alpha=0.78)
for vec in [(1, 1), (np.sqrt(2), -np.sqrt(2))]:
    ax.arrow(0, 0, vec[0], vec[1], width=0.025, head_width=0.16, color="#D93025", length_includes_head=True)
ax.text(1.1, 1.05, "1", color="#D93025", fontsize=13, fontweight="bold")
ax.text(np.sqrt(2) + 0.1, -np.sqrt(2) - 0.1, r"$\sqrt{2}$", color="#D93025", fontsize=13, fontweight="bold")
ax.axhline(0, color="#DADCE0", lw=0.8)
ax.axvline(0, color="#DADCE0", lw=0.8)
ax.set_xlabel(r"嵌入 $\sigma_1(a+b\sqrt{2})$")
ax.set_ylabel(r"嵌入 $\sigma_2(a+b\sqrt{2})$")
ax.set_title(r"$Z[\sqrt{2}]$ 在两个实嵌入下形成格", fontsize=16, fontweight="bold")
ax.set_aspect("equal")
ax.grid(alpha=0.2)
plt.tight_layout()
plt.savefig(out, dpi=150, bbox_inches="tight")
plt.close()
print(f"{out.name} saved")
