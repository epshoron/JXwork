# TD001｜任务 Prompt 与变异 Prompt 联动进化（Promptbreeder）

> **首次入本方向库**：T001，研究者 2026-10-22 明确批准；**非学术首次提出的宣称**。研究者认可的是具体机制，不是泛泛“LLM 改 Prompt”或进化算法。

**解决什么**：固定的 Prompt 改写指令可能限制候选任务 Prompt 的搜索范围，如何让**改写策略本身**也接受试验反馈？

**输入**：领域描述 D、task-prompt P、mutation-prompt M、预设超变异规则/思维风格；训练题目与任务评价函数。

**干预与更新**：LLM 使用 M 修改 P；超变异使用 H/领域描述修改或重新生成 M。进化个体携带 P、M，以 P 的训练任务分数进行锦标赛选择，因此 M 能随其所生成后代的表现接受间接选择。**改变的是自然语言 P/M、种群状态，基础 LLM 参数与评分器不变**。

**原文依据**：[Promptbreeder ICML 2024](https://proceedings.mlr.press/v235/fernando24a.html)，[arXiv 原文 Fig.1–2、§3.1、§3.2.1 / §3.2.3、Appendix B](https://arxiv.org/pdf/2309.16797)。原论文报告可改善多个 benchmark，但不同算子的独立贡献应结合 ablation 读；尤其不能忽略 Prompt 初始化方式的重要性。

**区别/去重**：`TD002` 更新的是从成功推理构造新 P 与正确示例上下文；[D007](../../../A_alpha_mining/knowledge/deltas/D007_code_evolution.md) 在因子 Python **代码**上做遗传算子；[D017](../../../A_alpha_mining/knowledge/deltas/D017_joint_alpha_metric_evolution.md) 共同搜索因子与评分**代码**。TD001 特指**指导变异的 M 随 P 的下游任务评分被选择**，不是普通 Prompt 变动或算法评分器进化。

**对应特化不足**：[T001 IDEAS §1](../../papers/T001/IDEAS.md)：P/M 文本能进化，但算法/调用拓扑和评价函数仍固定；作者 §6 明示这一范围边界，非性能失效证明。

**证据与审批边界**：T001 客观骨架和原文已核；研究者批准此项目级特色及对应边界；无完整复现、无学术首创性结论。
