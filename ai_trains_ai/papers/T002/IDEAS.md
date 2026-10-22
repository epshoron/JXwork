# T002｜GEPA 已批准的三项机制对应特化疑问（2026-10-22）

> 研究者已明确批准与 [ARCHITECTURE.md](ARCHITECTURE.md) 三个特色设计的 **3 对 3**。以下区分「原文直接观察」「对机制的审慎推断」「尚未做的实验」，不把通用 Prompt 过拟合、OOS 或成本重复包装为独有缺点。

## ① TD003 ↔ 反思修改的因果归因尚未被验证

- **特色机制**：[TD003](../../knowledge/deltas/TD003_trace_guided_module_prompt_reflection.md) 使用 execution/evaluation traces 的细粒度文本诊断，让 LLM 改写选定模块 Prompt，并靠反馈 minibatch 选优。
- **特化原因**：原文模块可轮换，改写被接受只说明小批量均分改善，不直接证明识别了真正致错模块；多模块依赖下，一个模块的修改可能补偿另一模块的错误。
- **待验证**：控制父代选择与预算，对比完整轨迹、仅数值分数、仅执行轨迹、仅评价诊断；对可人为定位致错模块的任务做归因核验，再看新 Prompt 的可迁移性。**作者没有实证证明系统已经发生这一失效**。

## ② TD004 ↔ 样例级赢家的稳定性和代表性

- **特色机制**：[TD004](../../knowledge/deltas/TD004_instancewise_pareto_parent_selection.md) 根据 `D_pareto` 逐样例局部领先挑父代，而非只挑验证均分第一。
- **特化原因**：一个在少数样例上偶然领先的版本也可能获得演化预算；搜索中反复使用同组局部赢家可能选择到任务特例，而非稳定的可复用专长。
- **待验证**：不改变总执行预算和反思机制，改变验证样例子集/随机种子，追踪 Pareto 前沿、父代概率、独立 holdout 成绩及样例级领先的重复出现率。**Table 3 的父代消融正向，不能被改写成 Pareto 搜索已证实不稳定**。

## ③ TD005 ↔ 跨模块合并的交互效应与时机预算

- **特色机制**：[TD005](../../knowledge/deltas/TD005_lineage_aware_module_merge.md) 的 GEPA+Merge 根据共同祖先与互补模块改动做版本合并。
- **原文实证**：Qwen3-8B 的六任务聚合 GEPA **54.85**，Merge **52.40**；GPT-4.1 Mini 聚合 Merge 则由 **65.22** 升至 **66.36**。这是作者报告的**模型条件下净效果**，不是已确认的因果原因。
- **作者解释与待核问题**：Observation 5 指出合并时机、搜索预算配置、统一超参数可能影响结果；**模块 A/C 分别改进不保证合并互相兼容**是需独立测试的原因假设。固定总预算，比较是否 merge、merge 时机和父代交互程度，量化合并的边际净收益。

**证据**：[ICLR 2026 GEPA 原文](https://proceedings.iclr.cc/paper_files/paper/2026/file/0e9e708b6f48e14fd0ac29e167413f76-Paper-Conference.pdf) Figure 2–3、Table 1/3、§2–4、Appendix C/D；阅读范围见 [PAPER](PAPER.md)。没有独立复现或学术首创性定论。
