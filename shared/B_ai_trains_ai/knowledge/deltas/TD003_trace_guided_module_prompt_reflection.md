# TD003｜GEPA：执行与评价轨迹驱动的模块级反思式 Prompt 变异

**状态：研究者 2026-10-22 已批准机制①及对应特化疑问①**。来自 [T002 GEPA](../../papers/T002/README.md)，不声称首次提出 LLM 反思或 Prompt 优化；本卡记录具体的**反馈载体→控制位置→版本选择**。

## 机制指纹

- **输入**：现有多模块 AI 系统的一整套 Prompt、在小批量任务上的 **execution trace**（模块输入输出、推理/工具调用）和 **evaluation trace**（评分前的错误、测试或工具诊断），以及最终任务数值评分。
- **操作**：选中父代的一套 Prompt，指定一个模块（原文可按 round-robin 轮换）；反思 LLM 阅读该模块的旧 Prompt、执行细节及诊断文本，产生**针对该模块的完整新 Prompt**，其他模块不变。在同一反馈 minibatch 上与父代比较平均任务分数，只有实际改善才继续在 `D_pareto` 上完整评估、加入候选池。
- **更新对象 / 输出**：模块 Prompt 的新版本及候选池/版本谱系。下层模型权重、工具实现、控制流不是该主算法的更新对象；它不是 LoRA、SFT 或 GRPO 参数训练。**小批量接受过滤**与 [TD004](TD004_instancewise_pareto_parent_selection.md) 的后续父代采样分工不同。

## 语义去重与独有干预位置

- [TD002（T001）](TD002_success_trace_prompt_induction_context_evolution.md)：从**成功 working out**反推任务 Prompt、改变 few-shot 正确示例；GEPA 本卡强调将**执行失败及外部评价器的诊断轨迹**转成**指定模块的改写**，再按同批任务实际得分接受。两者都存在“经验→Prompt”，不声称这一上层观念独有。
- [TD001（T001）](TD001_coupled_task_mutator_prompt_evolution.md)：被进化的是**任务 Prompt P 与用于修改 P 的 mutation prompt M**；GEPA 这里固定反思框架，主要更新系统模块 Prompt，不将修改策略 M 一同进化。
- [D001](../../../knowledge/deltas/D001_nested_feedback.md)、[D003](../../../knowledge/deltas/D003_success_memory.md)：普通评测循环/成功经验缓存不是本卡的失败轨迹与评测诊断→**局部 Prompt 改写**的具体路径。
- [TD004](TD004_instancewise_pareto_parent_selection.md) 管父代候选的选择概率；[TD005](TD005_lineage_aware_module_merge.md) 管互补模块合并。与本卡三个干预位置不可互换。

## 对应已批准特化疑问①：反思改进 ≠ 原因归因已证实

原文指定模块可采取轮换方式，并不是每次都自动定位真正造成失败的模块。在多模块联动失败时，某个 Prompt 改写后得分上升，**不自动证明反思 LLM 找对原始因果错误**；它也可能是在补偿另一模块的问题。

**可检验问题**：固定父代选择与评测预算，对比完整 execution + evaluation traces、只给最终分数、仅执行轨迹、仅评测诊断；再检查修改建议是否准确定位致错模块、是否跨样例复用。此项是根据设计提出的**待验证归因边界**，不是论文已证实反思无效。

**原文证据**：[ICLR 2026 GEPA 论文](https://proceedings.iclr.cc/paper_files/paper/2026/file/0e9e708b6f48e14fd0ac29e167413f76-Paper-Conference.pdf) §2–3、Figure 2–3、Appendix C/D；作者报告的性能数据属论文实验，未经独立复现。

[单篇已审特色](../../papers/T002/ARCHITECTURE.md) · [配对疑问](../../papers/T002/IDEAS.md)。
