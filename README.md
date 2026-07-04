---
layout: default
---

# 重学数学

这是一个面向重新理解现代数学的中文写作项目。它不是把定义、定理和公式按教材顺序重新抄一遍，而是尽量从问题出发：一个概念为什么会被发明出来，它解决了什么旧语言说不清的问题，又怎样和后面的理论连接起来。

项目目前按章节组织，每一章都是一篇独立的 Markdown 文章，并配有必要的示意图和生成脚本。阅读时可以从第一章顺序推进，也可以按主题跳读。

## 目录索引

### 站内导航

- [阅读方式](#阅读方式)
- [全部章节（按编号）](#全部章节按编号)
- [项目结构](#项目结构)
- [写作原则](#写作原则)
- [图片与脚本](#图片与脚本)
- [当前状态](#当前状态)

### 按主题跳读

- 基础主线：
  [01 傅里叶变换](chapter-01-fourier-transform/chapter.md) →
  [02 小波变换](chapter-02-wavelet-transform/chapter.md) →
  [03 泛函分析](chapter-03-functional-analysis/chapter.md) →
  [04 微分几何](chapter-04-differential-geometry/chapter.md) →
  [05 拓扑学](chapter-05-topology/chapter.md) →
  [06 同调与上同调](chapter-06-homology-cohomology/chapter.md) →
  [07 范畴论](chapter-07-category-theory/chapter.md)
- 概率统计与机器学习：
  [08 随机分析](chapter-08-stochastic-analysis/chapter.md)、
  [09 凸优化](chapter-09-convex-optimization/chapter.md)、
  [10 信息论](chapter-10-information-theory/chapter.md)、
  [11 统计学习理论](chapter-11-statistical-learning-theory/chapter.md)、
  [12 贝叶斯统计与概率图模型](chapter-12-bayesian-statistics-graphical-models/chapter.md)、
  [13 因果推断](chapter-13-causal-inference/chapter.md)、
  [24 深度学习理论](chapter-24-deep-learning-theory/chapter.md)、
  [30 随机控制与强化学习](chapter-30-stochastic-control-reinforcement-learning/chapter.md)、
  [31 信息几何](chapter-31-information-geometry/chapter.md)
- 几何、拓扑与现代数学物理：
  [14 动力系统与混沌](chapter-14-dynamical-systems-chaos/chapter.md)、
  [15 测度论与积分](chapter-15-measure-theory-integration/chapter.md)、
  [16 偏微分方程](chapter-16-partial-differential-equations/chapter.md)、
  [18 最优传输](chapter-18-optimal-transport/chapter.md)、
  [19 Lie 群与 Lie 代数](chapter-19-lie-groups-lie-algebras/chapter.md)、
  [20 表示论与对称性](chapter-20-representation-theory-symmetry/chapter.md)、
  [21 代数几何](chapter-21-algebraic-geometry/chapter.md)、
  [22 量子信息](chapter-22-quantum-information/chapter.md)、
  [25 微分拓扑](chapter-25-differential-topology/chapter.md)、
  [26 辛几何与 Hamilton 系统](chapter-26-symplectic-geometry-hamiltonian-systems/chapter.md)、
  [27 纤维丛与示性类](chapter-27-fiber-bundles-characteristic-classes/chapter.md)、
  [28 代数数论](chapter-28-algebraic-number-theory/chapter.md)、
  [29 算子代数](chapter-29-operator-algebras/chapter.md)、
  [32 张量网络与现代物理数学](chapter-32-tensor-networks-modern-physics/chapter.md)

### 按章节编号快速入口

`01` [傅里叶变换](chapter-01-fourier-transform/chapter.md) ·
`02` [小波变换](chapter-02-wavelet-transform/chapter.md) ·
`03` [泛函分析](chapter-03-functional-analysis/chapter.md) ·
`04` [微分几何](chapter-04-differential-geometry/chapter.md) ·
`05` [拓扑学](chapter-05-topology/chapter.md) ·
`06` [同调与上同调](chapter-06-homology-cohomology/chapter.md) ·
`07` [范畴论](chapter-07-category-theory/chapter.md) ·
`08` [随机分析](chapter-08-stochastic-analysis/chapter.md) ·
`09` [凸优化](chapter-09-convex-optimization/chapter.md) ·
`10` [信息论](chapter-10-information-theory/chapter.md) ·
`11` [统计学习理论](chapter-11-statistical-learning-theory/chapter.md) ·
`12` [贝叶斯统计与概率图模型](chapter-12-bayesian-statistics-graphical-models/chapter.md) ·
`13` [因果推断](chapter-13-causal-inference/chapter.md) ·
`14` [动力系统与混沌](chapter-14-dynamical-systems-chaos/chapter.md) ·
`15` [测度论与积分](chapter-15-measure-theory-integration/chapter.md) ·
`16` [偏微分方程](chapter-16-partial-differential-equations/chapter.md) ·
`17` [数值分析与科学计算](chapter-17-numerical-analysis-scientific-computing/chapter.md) ·
`18` [最优传输](chapter-18-optimal-transport/chapter.md) ·
`19` [Lie 群与 Lie 代数](chapter-19-lie-groups-lie-algebras/chapter.md) ·
`20` [表示论与对称性](chapter-20-representation-theory-symmetry/chapter.md) ·
`21` [代数几何](chapter-21-algebraic-geometry/chapter.md) ·
`22` [量子信息](chapter-22-quantum-information/chapter.md) ·
`23` [复杂系统与网络科学](chapter-23-complex-systems-network-science/chapter.md) ·
`24` [深度学习理论](chapter-24-deep-learning-theory/chapter.md) ·
`25` [微分拓扑](chapter-25-differential-topology/chapter.md) ·
`26` [辛几何与 Hamilton 系统](chapter-26-symplectic-geometry-hamiltonian-systems/chapter.md) ·
`27` [纤维丛与示性类](chapter-27-fiber-bundles-characteristic-classes/chapter.md) ·
`28` [代数数论](chapter-28-algebraic-number-theory/chapter.md) ·
`29` [算子代数](chapter-29-operator-algebras/chapter.md) ·
`30` [随机控制与强化学习](chapter-30-stochastic-control-reinforcement-learning/chapter.md) ·
`31` [信息几何](chapter-31-information-geometry/chapter.md) ·
`32` [张量网络与现代物理数学](chapter-32-tensor-networks-modern-physics/chapter.md)

## 阅读方式

- 如果想建立整体地图，建议从傅里叶、小波、泛函分析、微分几何、拓扑学一路读到同调与范畴论。
- 如果关心概率、统计和机器学习，可以从随机分析、凸优化、信息论、统计学习理论、贝叶斯统计、因果推断读起。
- 如果关心几何、物理和现代数学结构，可以从测度论、PDE、最优传输、Lie 群、表示论、代数几何、量子信息继续往后读。
- 如果只想查某个主题，直接进入对应的 `chapter-xx-*/chapter.md` 即可。

## 全部章节（按编号）

| 序号 | 章节 | 文件 |
| --- | --- | --- |
| 一 | 重学数学之一: 傅里叶变换 | [chapter.md](chapter-01-fourier-transform/chapter.md) |
| 二 | 重学数学之二: 小波变换 | [chapter.md](chapter-02-wavelet-transform/chapter.md) |
| 三 | 重学数学之三: 泛函分析——所有变换的统一语言 | [chapter.md](chapter-03-functional-analysis/chapter.md) |
| 四 | 重学数学之四: 微分几何——把线性代数贴到弯曲空间上 | [chapter.md](chapter-04-differential-geometry/chapter.md) |
| 五 | 重学数学之五: 拓扑学——只关心连续变形中不会消失的东西 | [chapter.md](chapter-05-topology/chapter.md) |
| 六 | 重学数学之六: 同调与上同调——把洞变成线性代数 | [chapter.md](chapter-06-homology-cohomology/chapter.md) |
| 七 | 重学数学之七: 范畴论——研究结构如何通过映射迁移 | [chapter.md](chapter-07-category-theory/chapter.md) |
| 八 | 重学数学之八: 随机分析——当路径不可微时，微积分如何重建 | [chapter.md](chapter-08-stochastic-analysis/chapter.md) |
| 九 | 重学数学之九: 优化与凸分析——为什么凸性让问题变得可解 | [chapter.md](chapter-09-convex-optimization/chapter.md) |
| 十 | 重学数学之十: 信息论——不确定性、压缩与通信的数学 | [chapter.md](chapter-10-information-theory/chapter.md) |
| 十一 | 重学数学之十一: 统计学习理论——模型为什么能在没见过的数据上工作 | [chapter.md](chapter-11-statistical-learning-theory/chapter.md) |
| 十二 | 重学数学之十二: 贝叶斯统计与概率图模型——把不确定性更新成推理 | [chapter.md](chapter-12-bayesian-statistics-graphical-models/chapter.md) |
| 十三 | 重学数学之十三: 因果推断——从相关性走向干预和反事实 | [chapter.md](chapter-13-causal-inference/chapter.md) |
| 十四 | 重学数学之十四: 动力系统与混沌——确定规则如何生成复杂长期行为 | [chapter.md](chapter-14-dynamical-systems-chaos/chapter.md) |
| 十五 | 重学数学之十五: 测度论与积分——把长度、面积和概率放进同一个语言 | [chapter.md](chapter-15-measure-theory-integration/chapter.md) |
| 十六 | 重学数学之十六: 偏微分方程——局部规律如何生成空间中的整体演化 | [chapter.md](chapter-16-partial-differential-equations/chapter.md) |
| 十七 | 重学数学之十七: 数值分析与科学计算——连续数学如何变成可靠计算 | [chapter.md](chapter-17-numerical-analysis-scientific-computing/chapter.md) |
| 十八 | 重学数学之十八: 最优传输——在概率分布之间搬运质量的几何 | [chapter.md](chapter-18-optimal-transport/chapter.md) |
| 十九 | 重学数学之十九: Lie 群与 Lie 代数——连续对称性如何被线性化 | [chapter.md](chapter-19-lie-groups-lie-algebras/chapter.md) |
| 二十 | 重学数学之二十: 表示论与对称性——把抽象群变成线性变换 | [chapter.md](chapter-20-representation-theory-symmetry/chapter.md) |
| 二十一 | 重学数学之二十一: 代数几何——方程组如何长成空间 | [chapter.md](chapter-21-algebraic-geometry/chapter.md) |
| 二十二 | 重学数学之二十二: 量子信息——当信息住进 Hilbert 空间 | [chapter.md](chapter-22-quantum-information/chapter.md) |
| 二十三 | 重学数学之二十三: 复杂系统与网络科学——局部连接如何长出整体行为 | [chapter.md](chapter-23-complex-systems-network-science/chapter.md) |
| 二十四 | 重学数学之二十四: 深度学习理论——表示、优化与泛化的现代交汇点 | [chapter.md](chapter-24-deep-learning-theory/chapter.md) |
| 二十五 | 重学数学之二十五: 微分拓扑——不量长度，只看光滑形状怎样变 | [chapter.md](chapter-25-differential-topology/chapter.md) |
| 二十六 | 重学数学之二十六: 辛几何与 Hamilton 系统——相空间里真正守恒的是什么 | [chapter.md](chapter-26-symplectic-geometry-hamiltonian-systems/chapter.md) |
| 二十七 | 重学数学之二十七: 纤维丛与示性类——局部像乘积，全局却可能扭起来 | [chapter.md](chapter-27-fiber-bundles-characteristic-classes/chapter.md) |
| 二十八 | 重学数学之二十八: 代数数论——把素数放进更大的数域里观察 | [chapter.md](chapter-28-algebraic-number-theory/chapter.md) |
| 二十九 | 重学数学之二十九: 算子代数——把无限维线性变换当成非交换空间 | [chapter.md](chapter-29-operator-algebras/chapter.md) |
| 三十 | 重学数学之三十: 随机控制与强化学习——在不确定世界里做长期决策 | [chapter.md](chapter-30-stochastic-control-reinforcement-learning/chapter.md) |
| 三十一 | 重学数学之三十一: 信息几何——把概率分布族看成弯曲空间 | [chapter.md](chapter-31-information-geometry/chapter.md) |
| 三十二 | 重学数学之三十二: 张量网络与现代物理数学——用纠缠结构压缩高维世界 | [chapter.md](chapter-32-tensor-networks-modern-physics/chapter.md) |

## 项目结构

每个章节目录通常包含三类内容：

```text
chapter-xx-topic/
  chapter.md      # 章节正文
  images/         # 本章使用的示意图
  scripts/        # 生成部分示意图的脚本
```

根目录下的 `images/` 存放一些跨章节使用的引导图片。章节正文中的配图已统一改为标准 Markdown 图片链接，GitHub 和普通 Markdown 阅读器都可以直接渲染；若个别图片仍无法显示，优先检查相对路径是否正确。

## 写作原则

- 先解释问题，再引入定义。
- 少做名词堆叠，多说明概念解决了什么困难。
- 公式服务于直觉，不把推导写成孤立的符号表演。
- 每章尽量包含动机、核心概念、典型例子、应用场景、与前后章节的连接和前沿展望。
- 对抽象概念保持克制：能用一个低维例子讲清楚的地方，不直接跳到最高抽象层。

## 图片与脚本

章节中的图片大多已经生成并提交在对应的 `images/` 目录中。若需要重新生成某章图片，可查看该章 `scripts/` 目录下的 Python 脚本。脚本通常依赖 Python 科学计算和绘图库，例如 `numpy`、`matplotlib` 等。

建议在修改正文时不要随意删除图片引用；如果图片暂时无法显示，优先检查路径和 Markdown 渲染器，而不是直接移除图片。

## 当前状态

项目已经覆盖 32 章，形成了从经典分析、几何拓扑、概率统计，到现代数学物理、机器学习理论和张量网络的第一版路线图。后续维护的重点主要是逐章润色、补充例子、修复公式展示问题，并让相邻章节之间的概念衔接更自然。
