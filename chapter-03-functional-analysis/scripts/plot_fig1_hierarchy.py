"""fig1: 从有限维到无穷维——空间层级图。

展示向量空间如何在附加结构后逐级收窄：
向量空间 → 赋范空间 → Banach 空间 → 内积空间 → Hilbert 空间
每一层增加什么条件、排除什么例子。
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as mpatches

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# 画同心椭圆来表示嵌套结构
from matplotlib.patches import Ellipse

levels = [
    (9.0, 'Vector Space\n向量空间', '#E8EAF6',
     '加法和标量乘法封闭', ['Rⁿ, C([a,b])\n多项式全体']),
    (7.5, 'Normed Space\n赋范空间', '#C5CAE9',
     '+ 定义范数 ‖x‖\n（长度/距离概念）', ['ℓᵖ 空间\nLᵖ 空间（p≥1）']),
    (6.0, 'Banach Space\nBanach 空间', '#9FA8DA',
     '+ 对范数完备\n（Cauchy 列收敛）', ['Lᵖ, ℓᵖ (p≥1)\nC([a,b]) with sup norm']),
    (4.5, 'Inner Product Space\n内积空间', '#7986CB',
     '+ 定义内积 ⟨x,y⟩\n（角度/正交概念）', ['ℓ² 序列空间\n有内积的赋范空间']),
    (3.0, 'Hilbert Space\nHilbert 空间', '#5C6BC0',
     '+ 对内积完备\n（完备的内积空间）', ['L², ℓ²\nFourier/wavelet 的舞台']),
]

center = (7, 5)
for i, (rx, title, color, cond, examples) in enumerate(levels):
    ry = rx * 0.55
    ellipse = Ellipse(center, rx * 2, ry * 2, facecolor=color, edgecolor='#3949AB',
                      linewidth=2, alpha=0.25 + i * 0.12, zorder=5 - i)
    ax.add_patch(ellipse)
    # 标签
    ax.text(center[0] + rx - 0.3, center[1] + ry - 0.2, title, fontsize=11,
            fontweight='bold', ha='right', va='top', zorder=10)
    # 条件（左上）
    ax.text(center[0] - rx + 0.2, center[1] + ry - 0.2, cond, fontsize=8,
            ha='left', va='top', color='#1A237E', zorder=10, style='italic')
    # 例子（右下）
    ax.text(center[0] + rx - 0.3, center[1] - ry + 0.3, examples, fontsize=7.5,
            ha='right', va='bottom', color='#283593', zorder=10)

# 标注从外到内的箭头方向
ax.annotate('← 结构越来越丰富', xy=(12.5, 8.5), fontsize=10, color='#1A237E',
            fontweight='bold')
ax.annotate('空间越来越"小"\n（更多约束条件）→', xy=(12, 7.8), fontsize=9,
            color='#3949AB')

# 底部说明
ax.text(7, 0.5, '傅里叶级数、傅里叶变换、小波变换本质上都是 Hilbert 空间 L² 上的基展开', fontsize=12,
        ha='center', fontweight='bold', color='#5C6BC0')
ax.text(7, 0.1, '泛函分析 = 把有限维线性代数的直觉系统地推广到无穷维', fontsize=10,
        ha='center', style='italic', color='gray')

plt.tight_layout()
plt.savefig('../images/fig1_space_hierarchy.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig1_space_hierarchy.png saved')
