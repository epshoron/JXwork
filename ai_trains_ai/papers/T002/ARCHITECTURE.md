# T002｜GEPA：研究者已批准的三项特色机制（2026-10-22）

**证据与身份**：基于 [ICLR 2026 GEPA 原文](https://proceedings.iclr.cc/paper_files/paper/2026/file/0e9e708b6f48e14fd0ac29e167413f76-Paper-Conference.pdf) §2–4、Figure 2–3、Table 1/3、Appendix C/D 的单篇理解；研究者明确批准下列 **3 项特色机制 + 各自 1 项特化疑问**。**项目内机制区分不等于学术首创，疑问不等于缺陷已经发生，也未独立复现**。

[整体系统图与客观骨架](README.md) · [配对疑问与检验](IDEAS.md) · [原文范围](PAPER.md)

## ① TD003｜执行与评价轨迹 → 指定模块的反思式 Prompt 变异

**机制位置**：已有多模块执行系统先在 `D_feedback` 的小批任务运行；保存模块输入输出/工具调用和来自评分器的文本诊断。反思 LLM 利用旧 Prompt、execution/evaluation traces 和得分生成某一指定模块的新 Prompt，其他模块保持不变；同批平均分若未超过父代即拒绝，超过才进入 `D_pareto` 扩大评测与候选池。**优化对象是 Prompt，不是权重或 Agent 流程结构**。

**相邻机制去重**：[TD002（T001）](../../knowledge/deltas/TD002_success_trace_prompt_induction_context_evolution.md) 用**成功 working out**反推任务 Prompt 与 few-shot 示例，而这里把**错误执行与评测诊断**用作模块级定向修改的语义依据；[TD001](../../knowledge/deltas/TD001_coupled_task_mutator_prompt_evolution.md) 让修改策略 M 也变，本系统的反思指令并不作为同样的演化工件。

**对应不足①**：系统可以轮换待改模块，Prompt 变好并不单独证明 reflection LLM 正确找到了原始致错模块；多模块交互错误可能由别的模块引起。是**隐式归因待检验问题**，不等于作者证明误归因。见 [TD003](../../knowledge/deltas/TD003_trace_guided_module_prompt_reflection.md)。

## ② TD004｜按验证样例的局部优势进行 Pareto 父代选择

**机制位置**：在 `D_pareto` 比较完整 Prompt 候选对**每一道验证样例**的得分，依据逐样例领先集合抽选下一轮父代，保护特定问题上表现好的分支；不是只改平均分最高者，也不是在线根据问题调用不同专家。最终仍按聚合验证得分选单个 Prompt 向量。

**实证支持**：Table 3（Qwen3-8B、四任务汇总）对比固定其他反思演化部分的父代策略：Pareto **+12.44**，全局最佳 **+6.05**，Top-4 beam **+5.11**（作者报告的汇总表现变化，非交易收益）。

**对应不足②**：某候选可能在少数验证题目上偶然领先并获得继续繁殖机会；重复使用固定 `D_pareto` 的局部赢家是否稳定、可迁移，仍应固定预算与种子单独检验。论文独立测试有正向结果，不能声称已证实失效。见 [TD004](../../knowledge/deltas/TD004_instancewise_pareto_parent_selection.md)。

## ③ TD005｜共同祖先 + 互补模块的可选 Merge

**机制位置**：`GEPA+Merge` 从具有共同祖先的不同候选谱系中，定位各自改变的**不同模块**并合成完整 Prompt 候选，再验证整体表现；不是盲目拼接 Prompt 文本，**也不是基础 GEPA 每一轮必执行的步骤**。

**实证与作者解释**：Table 1 在 Qwen3-8B 六任务聚合 **GEPA 54.85，GEPA+Merge 52.40**；GPT-4.1 Mini 聚合 **65.22→66.36**。作者 Observation 5 讨论合并时机及预算/超参数。不同模型表现方向不一致，不能以模块互补就推断整体必提升。

**对应不足③**：两个独立模块的有益 Prompt 改写合并后未必兼容；**何时合并及是否值得分配评测预算**才是该扩展的特化约束。Qwen 聚合下降是**论文观测**，模块交互导致下降则是**未隔离证实的解释**。见 [TD005](../../knowledge/deltas/TD005_lineage_aware_module_merge.md)。

## 与两方向知识库总体关系

- **T001/TD001–TD002**：同属自然语言提示演化，但 T001 改 P/M 和成功工作过程/few-shot；GEPA 的三项分别控制**诊断输入与局部改写、样例级父代选择、谱系级模块合并**。
- **方向 A**：[D007](../../../knowledge/deltas/D007_code_evolution.md) 进化因子代码；[D010](../../../knowledge/deltas/D010_mcts_multidimensional_search.md) 做因子公式树搜索；[D020](../../../knowledge/deltas/D020_semantic_reward_surrogate_scheduler.md) 训练语义计划奖励代理。和 T002 三个更新对象均不同。**普通遗传算法、Pareto 搜索、LLM 反思本身不另称首创**。
- **整体边界**：T002 仍属方向 B 阶段一的**已批准单篇特色评审**；不表示已进入跨论文阶段二、原创阶段三，或已实现针对某个用户 Executor 的优化系统。
