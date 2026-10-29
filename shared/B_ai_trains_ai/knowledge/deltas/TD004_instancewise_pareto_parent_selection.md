# TD004｜GEPA：逐验证样例的 Pareto 父代选择与演化调度

**状态：研究者 2026-10-22 已批准机制②及对应特化疑问②**。来自 [T002 GEPA](../../papers/T002/README.md)。这里不是首次使用 Pareto 或进化算法，也不是对准确率、耗时、成本等**不同指标**做传统多目标优化。

## 机制指纹

- **输入**：多个不同完整 Prompt 候选，以及它们在 `D_pareto` **每个验证样例**上的分数向量。
- **操作位置**：不总从全局平均分第一的单个版本继续变异，而是从逐样例表现靠前/最优的**候选前沿**采样父代；某个候选在多少样例占据领先位置会影响抽样权重。以此分配“下一个要让反思 LLM 改谁”的搜索机会，保护不同任务上的局部强者。
- **输出 / 更新对象**：父代抽样分布、后续 Prompt 演化轨迹和候选池；**不是更新 LLM 权重或改写奖励指标**。搜索预算结束后，最终仍以 `D_pareto` 的平均验证分选出一整套 Prompt 交付，不构成在线多专家路由。

## 原文支持

- 论文 Algorithm 1、Pareto 选择方法及 Table 3：在固定反思式候选生成框架下，对比父代选择机制；Qwen3-8B 四任务的汇总提升为 **GEPA Pareto +12.44、全局最佳 +6.05、Top-4 beam +5.11**。是作者的**聚合增益口径**，不是交易收益，也不是每项任务均如此。
- `D_feedback`（产生反思和接受过滤）与 `D_pareto`（选择/完整评价）不同；`D_pareto` 仍属搜索中的验证集，不是最终独立测试集。

## 去重

- [TD001](TD001_coupled_task_mutator_prompt_evolution.md)：固定锦标赛评价任务 Prompt 和其变异指令 M 的种群；**没有本卡特指的逐验证样例 Pareto 抽父代**。
- [D010/P004](../../../A_alpha_mining/knowledge/deltas/D010_mcts_multidimensional_search.md)：搜索树节点与统计回传，结合因子池相关的多维评分；这里是**每个验证样例当成一个比较维度**决定 Prompt 父代，既无 MCTS 树路径回传，也非金融因子评分。
- [D020/P010](../../../A_alpha_mining/knowledge/deltas/D020_semantic_reward_surrogate_scheduler.md)：LightGBM 估算未实施语义 Plan 奖励分配实施预算；本机制**不训练代理分数预测器**，直接利用已测试候选的逐样例分数抽样。
- [TD003](TD003_trace_guided_module_prompt_reflection.md) 负责新 Prompt 的诊断生成；本卡只记录**候选选择**。

## 对应已批准特化疑问②：样例级局部领先是否稳定？

如果某个候选偶然只在少数 `D_pareto` 样例上领先，它也可能获得继续繁殖的机会；长期重复利用同一批样例可能偏重其局部偶然性。**这属于待检验的稳定性假设**：论文在独立测试上有正向结果，不能说该风险已经发生。

**检验**：控制模型、总 rollout 预算、候选改写机制，变化验证样例子集和随机种子，观察 Pareto 前沿、父代分配、候选家族稳定性及独立测试分数；将“偶然局部赢”与可迁移专长区分开。

**原文**：[GEPA ICLR 2026 §3、Table 3、Appendix D](https://proceedings.iclr.cc/paper_files/paper/2026/file/0e9e708b6f48e14fd0ac29e167413f76-Paper-Conference.pdf)。

[已审特色](../../papers/T002/ARCHITECTURE.md) · [对应问题](../../papers/T002/IDEAS.md)。
