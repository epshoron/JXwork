# P003｜原文来源与证据范围

**正式题名**：AlphaAgent: LLM-Driven Alpha Mining with Regularized Exploration to Counteract Alpha Decay  
**作者**：Ziyi Tang、Zechuan Chen、Jiarui Yang、Jiayao Mai、Yongsen Zheng、Keze Wang、Jinrui Chen、Liang Lin  
**出处**：KDD 2025, pp. 2813–2822。

- [正式 DOI: 10.1145/3711896.3736838](https://doi.org/10.1145/3711896.3736838)
- [arXiv:2502.16789](https://arxiv.org/abs/2502.16789)
- [可读原文 HTML](https://arxiv.org/html/2502.16789)
- [论文标示的作者代码仓库](https://github.com/RndmVariableQ/AlphaAgent)（**本次未复验源代码，不以当前默认分支推断论文算法实现**）

## 本次核对范围

依据**原始论文 HTML**的 §3.1–3.3（任务、AST/算子、Eq. 4–8、三个 Agent、反馈/知识库），§4.1–4.5（实验、基线、衰减分析、逐轮趋势与消融）以及原文 Figure 1–6 图注归纳。Figure 6 报告的是**整体 factor-modeling constraints** 的有无比较，不是三种约束各自的独立消融。

**未核实边界**：没有独立执行官方代码、检查实际 Eq. 8 的权重/符号逻辑，未重新训练、回测或证明真实市场拥挤下降。有关公式符号与原创性的评论均是依据原文提出的待验证分析，而非复现结果。

本公共仓库只保存来源链接与独立概括，不保存未经许可分发的论文 PDF。
