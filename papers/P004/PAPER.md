# P004｜原文来源与核对范围

**正式题名**：Navigating the Alpha Jungle: An LLM-Powered MCTS Framework for Formulaic Alpha Factor Mining

**作者**：Yu Shi、Yitong Duan、Jian Li

**正式出处**：*Proceedings of the AAAI Conference on Artificial Intelligence*, 40(2), 997–1005 (2026)。

- [AAAI 正式发表页面](https://ojs.aaai.org/index.php/AAAI/article/view/37069)
- [DOI: 10.1609/aaai.v40i2.37069](https://doi.org/10.1609/aaai.v40i2.37069)
- [arXiv:2505.11122 原文入口](https://arxiv.org/abs/2505.11122)
- [arXiv 可读 HTML 全文](https://arxiv.org/html/2505.11122)

## 目前实际核实

本次骨架根据**原文 §3 Methodology**（Selection、Expansion、Multi-Dimensional Alpha Evaluation、Backpropagation、Frequent Subtree Avoidance）及 **Appendix F Pseudo-Code** 核对，并参考 §1 的总体任务与 Figure 1/2 的说明。已能重建「MCTS 定向选点 → LLM 按较弱维度改公式 → 回测多维评价 → 树上回传反馈 → 有效因子进入 Alpha Zoo → FSA 约束下一步生成」的核心流程。

**尚待单独讨论与审批**：作者主张的学术贡献、相对已知系统的真实 Delta、针对这一机制的特化局限和我们自己的创新思考。实验表、消融、附录可继续深入，但目前不标记“全文全部研读完成”。

仓库为 Public：保留原始来源的链接，不未经许可转存论文 PDF。
