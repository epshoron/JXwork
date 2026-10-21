# P006｜R&D-Agent-Quant：原文、代码与阅读边界

- **正式题名**：R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization
- **正式发表**：NeurIPS 2025, Datasets and Benchmarks Track，作者 Yuante Li、Xu Yang、Xiao Yang、Xisen Wang、Weiqing Liu、Jiang Bian
- **出版方页面**：[NeurIPS 2025](https://papers.neurips.cc/paper_files/paper/2025/hash/ac5c2b6e423883cbcacbcccf88491b78-Abstract-Datasets_and_Benchmarks_Track.html)
- **DOI**：[10.52202/085713-3967](https://doi.org/10.52202/085713-3967)
- **arXiv 原文**：[arXiv:2505.15155](https://arxiv.org/abs/2505.15155) · [HTML 全文](https://arxiv.org/html/2505.15155)
- **作者公开代码**：[microsoft/RD-Agent](https://github.com/microsoft/RD-Agent)（仓库同时包含通用 RD-Agent 等模块，不能把整个仓库都当作本文独占的实现）
- **论文用途**：研究 LLM/Agent 如何共同提出因子/预测模型假设、执行实现与回测，并自适应调配下一轮研究对象。

## 当前核验状态（2026-10-21）

- **已直接核对**：正式 NeurIPS 题录/摘要；arXiv §1、§2.1–2.5 的组件定义、信息流、执行反馈，以及与代码开发和 Bandit 路径选择相关的核心原理。
- **尚待完整核查**：附录全部算法、实验指标与消融、数据泄漏约束、独立复现、与同领域前作的创新性边界。
- **内容标记**：这里仅有权威链接与客观机制骨架；贡献、特化缺点和我们自己的技术设想**须先在 LLM 对话内由研究者逐项批准**。
- **Public GitHub**：不上传公司材料、密钥或未经确认许可的论文 PDF。

**结构主证据**：[arXiv §2 R&D-Agent(Q)](https://arxiv.org/html/2505.15155#S2)。
