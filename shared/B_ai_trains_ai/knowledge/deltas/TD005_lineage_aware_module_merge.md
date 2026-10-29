# TD005｜GEPA+Merge：共同祖先约束的互补模块 Prompt 合并

**状态：研究者 2026-10-22 已批准机制③及对应特化不足③**。这是论文的**可选 GEPA+Merge 扩展**；不要将它误写成基本 GEPA 每轮必经步骤或“拼接两个长 Prompt”。

## 机制指纹

- **输入**：多模块 AI 系统中有共同祖先的两条候选谱系；两边分别对不同模块的 Prompt 做过性能筛选后的局部改进。
- **操作**：根据候选家族历史追踪共同祖先，检查两个分支改动的模块是否互补，再将**各自模块级改动**汇入同一个完整 Prompt 候选，并经任务评价与接受规则检验；不是任意文本段落交叉，也不更新模型权重或 Agent 控制图。
- **输出与更新对象**：融合后的完整 Prompt 向量及后续候选池。与 [TD003](TD003_trace_guided_module_prompt_reflection.md) 的单模块反思改写、[TD004](TD004_instancewise_pareto_parent_selection.md) 的 Pareto 父代调度属于不同搜索算子。

## 已核原文证据

- 原文 Appendix D.1 的 `GEPA+Merge` 说明了**家族谱系/互补模块**约束和有限的合并机会。
- Table 1 的六任务聚合（Qwen3-8B）：**GEPA 54.85、GEPA+Merge 52.40**，合并版本总体更低；在 GPT-4.1 Mini 对照上，作者报告 **65.22 → 66.36**，方向相反。两者均属论文报告的任务聚合分数，不是相同任务上无条件的改进定律。
- 正文 Observation 5 将表现差异与**合并时机、分配预算、沿用同样超参数**相关联；这是作者的解释，**不能宣称合并失败原因已被完全隔离确认**。

## 去重

- [TD001](TD001_coupled_task_mutator_prompt_evolution.md)：进化 P/M 内容与变异指令，不是按共同祖先把两个分支的**互补模块**组合。
- [D007/P002](../../../knowledge/deltas/D007_code_evolution.md)：父代选择、Python 因子代码 mutation/crossover；**遗传交叉本身已有先例**。GEPA 特化点在于**候选代表一整套多模块 Prompt，利用模块身份 + 共同谱系合并各自已演化的组件**。
- [TD003](TD003_trace_guided_module_prompt_reflection.md) 负责独立模块的 Prompt 改写；本机制解决的是**已有不同模块改进如何合并**，不是再次换名叙述“改 Prompt”。

## 对应已批准特化不足③：互补模块不一定形成互补性能

同一个祖先下两个分支分别改善模块 A/C，不保证合到同一个执行流程就兼容；**何时合并、是否值得花预算合并**影响最终表现。Qwen3-8B 聚合数据确有合并版本低于普通 GEPA 的观测，GPT-4.1 Mini 则反向；这支持“收益条件性”，**不等于已经证明具体的模块冲突就是原因**。

**验证**：固定候选生成/评价预算，按共同祖先、模块交互程度和合并时机分组；区分带 merge/无 merge、早合/晚合和不同预算份额，检查合并的**额外边际收益**与跨任务稳定性。

**原文**：[GEPA ICLR 2026 Figure 3、Table 1、§3–4、Appendix D.1](https://proceedings.iclr.cc/paper_files/paper/2026/file/0e9e708b6f48e14fd0ac29e167413f76-Paper-Conference.pdf)。

[已审特色](../../papers/T002/ARCHITECTURE.md) · [对应问题](../../papers/T002/IDEAS.md)。
