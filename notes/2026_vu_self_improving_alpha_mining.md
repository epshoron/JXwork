# Self-improving alpha mining for quantitative trading via multi-agent large language models with knowledge base accumulation · 阅读笔记

- **责任窗口**：S5（研究中；用于 S5/S6 去重，非排他锁）
- **状态**：已核验出版来源、摘要及作者公开代码说明；论文全文方法/实验尚待逐项精读
- **来源**：Minh-Son Vu, The-Trung Pham, Hong-Viet Tran. *Machine Learning with Applications*, 25 (2026), 100987.
- **正式 DOI**：https://doi.org/10.1016/j.mlwa.2026.100987
- **出版方原文**：https://www.sciencedirect.com/science/article/pii/S2666827026001520
- **作者代码与实验说明**：https://github.com/VMSSON345/Self-Improving-Alpha-Mining-for-Quantitative-Trading-via-Multi-Agent-Large-Language-Models-with-Know
- **核验日期**：2026-10-21
- **研究标签（初步，等待全文细节佐证）**：经验学习、推理协作、质量控制

## 1. 一句话问题陈述

直接研究**公式化 Alpha 因子的自动生成、修订和验证**。其摘要声称：以多 Agent 嵌套循环，结合 WorldQuant 101 公式知识先验和实验反馈，提高因子生成的有效性与收敛效率。注意：这是作者的研究目标/主张，不等于已经证明能够持续自我改进。

## 2. 输入、输出与核心机制（待全文核验）

- 输入：交易假设/想法、市场历史数据、WorldQuant 101 因子公式、已积累的因子记录（依据作者摘要与官方代码仓库说明）。
- 输出：可执行 Alpha 因子代码、公式、历史表现与入库记录（作者官方代码说明）。
- 主体：WriterAgent、JudgeAgent、BacktestEngine、ReviewerAgent；两级循环分别处理代码质量和回测表现（作者代码仓库 README）。
- **原文证据位置**：目前已核摘要，论文正文页码、具体算法和图表待补。
- **未核实问题**：是如何把 Reviewer 的反馈注入 Writer、知识库是否真的支持跨任务效率提升、是否存在模型权重更新。

## 3. 迭代与 RSI 的区分（待确认）

目前可确认作者描述的是**Agent 工作流级反馈 + 因子知识库积累**；尚不能据此宣称模型参数训练、递归自我改写或严格 RSI。需要检查累积知识在时间序列测试中的因果贡献。

## 4. 评价方式与证据（初步）

- 作者 README 描述越南股票市场数据、训练/验证/测试的时间顺序切分及冻结测试阶段知识库；具体实施需从论文实验章节和代码交叉核验。
- 摘要/README 提供 IC、Sharpe、胜率等指标，**均属于作者报告值，不是独立复现**。
- 重点待审：Sharpe 是否未扣成本、五日标签及重叠收益的处理、因子筛选与冻结时点、前视泄漏、不同 baselines 的预算公平性、跨市场稳健性。
- 公开 PDF 再分发许可证未核实，**不上传 PDF 到 Public 仓库**。

## 5. 三个研究视角（暂定）

- [ ] **质量控制**：JudgeAgent 代码/前视偏差审查；需找原论文明确证据。
- [ ] **经验学习**：Main KB 的新因子积累和检索反馈；需查明跨轮更新对象与实验验证。
- [ ] **推理协作**：Writer/Judge/Reviewer 职责分工；需区分简单串行分工与协同辩论。
- [ ] **其他**：结构化领域知识检索（WorldQuant 101）能否作为单独工程机制，待比较其他论文。

## 6. 当前理解与下一步

下一步阅读正式论文方法、实验和消融，补充图/表/公式证据，特别检验“self-improving”的精确定义与限制；更新本笔记与 INDEX 阅读状态。**当前只能称为“来源与摘要已核验”，不可写“已读全文”。**
