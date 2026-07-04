"""fig5: 泛函分析统一图景——所有积分变换都是 Hilbert 空间中的基展开。

展示泛函分析如何将傅里叶变换、小波变换、Laplace 变换等
统一为"选择基底 + 计算内积"的框架。
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(13, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# 中心：泛函分析统一框架
center_box = FancyBboxPatch((4, 5.5), 6, 3, boxstyle="round,pad=0.3",
                             facecolor='#E8EAF6', edgecolor='#3949AB', linewidth=2.5)
ax.add_patch(center_box)
ax.text(7, 7.8, '泛函分析统一框架', fontsize=14, fontweight='bold',
        ha='center', color='#1A237E')
ax.text(7, 7.1, '信号 f ∈ Hilbert 空间 H\n变换系数 = ⟨f, ψ_α⟩\n重建 = Σ ⟨f, ψ_α⟩ ψ_α', fontsize=10,
        ha='center', color='#283593')
ax.text(7, 5.9, '基底 {ψ_α} 需满足：完备性 + 正交性\n（或框架条件 + Riesz 基条件）', fontsize=9,
        ha='center', color='#5C6BC0', style='italic')

# 分支：不同的基底选择
branches = [
    (1.5, 2, '傅里叶变换', '#FFCDD2',
     '基底：e^{iωt}\n参数：频率 ω\n性质：全局、平移不变\n完备性：Carleson 定理（1966）',
     (-0.3, -0.2)),  # 方向
    (5.5, 2, '小波变换', '#C8E6C9',
     '基底：ψ_{a,b}(t)\n参数：尺度 a + 位置 b\n性质：局部、尺度协变\n完备性：框架理论',
     (0, -0.3)),
    (9.5, 2, '正交多项式', '#BBDEFB',
     '基底：Legendre/Chebyshev/…\n参数：阶数 n\n性质：在加权 L² 中正交\n完备性：Weierstrass 逼近',
     (0.3, -0.2)),
    (1.5, 8, 'Sturm-Liouville', '#FFF9C4',
     '基底：特征函数\n⟨f, φ_n⟩_w（加权内积）\n来源：二阶线性微分算子\n完备性：SL 谱定理',
     (-0.3, 0.2)),
    (9.5, 8, '奇异值分解 (SVD)', '#E1BEE7',
     '基底：算子的左右奇异向量\n⟨f, v_k⟩ = σ_k ⟨u_k, …⟩\n最优低秩逼近\n完备性：紧算子的谱定理',
     (0.3, 0.2)),
]

for bx, by, title, color, desc, (dx, dy) in branches:
    box = FancyBboxPatch((bx-1.3, by-1.3), 2.6, 2.6, boxstyle="round,pad=0.15",
                          facecolor=color, edgecolor='#757575', linewidth=1.5, alpha=0.7)
    ax.add_patch(box)
    ax.text(bx, by + 1.0, title, fontsize=11, fontweight='bold', ha='center')
    # 通过箭头连接到中心
    ax.annotate('', xy=(bx + dx * 2, by + dy * 2 + 0.3),
                xytext=(7, 6.5),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.2,
                               connectionstyle='arc3,rad=0'))
    # 描述文字
    desc_lines = desc.split('\n')
    for i, line in enumerate(desc_lines):
        ax.text(bx, by + 0.3 - i * 0.4 - 0.3, line, fontsize=7.5, ha='center',
                color='#424242')

# 顶部标题
ax.text(7, 9.5, '所有积分变换 = 选择基底 + 计算内积', fontsize=16,
        fontweight='bold', ha='center', color='#1A237E')
ax.text(7, 9.1, '泛函分析的任务：建立语言，使这个类比在数学上严格', fontsize=11,
        ha='center', style='italic', color='gray')

# 底部：关键定理
ax.text(7, 0.5, '关键定理：投影定理 | Riesz 表示定理 | Hahn-Banach | Banach-Steinhaus | 开映射定理 | 闭图像定理 | 谱定理', fontsize=9,
        ha='center', color='#5C6BC0')

plt.tight_layout()
plt.savefig('../images/fig5_unified_view.png', dpi=150, bbox_inches='tight')
plt.close()
print('fig5_unified_view.png saved')
