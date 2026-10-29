# T004｜ADAS 两项已批准的特色机制（2026-10-22）

**审批范围**：研究者在 T004 客观骨架获认可后，进一步批准**两项机制与各自一项特化不足（2+2）**。项目内区分不等于全球学术首创；原文尚未独立复现。  
[原文骨架](README.md) · [证据边界](PAPER.md) · [对应不足](IDEAS.md) · [ICLR 2025 论文](https://proceedings.iclr.cc/paper_files/paper/2025/file/36b7acf6f6010652b3f2a433774a66fe-Paper-Conference.pdf)

## ① TD010｜把下层 Agent 的整个可执行程序作为搜索对象

**输入与更新位置**：已有基础模型/工具 API、任务/评价与预算固定；Meta Agent 生成新思路，编写 Python `forward(taskInfo)`，经两轮设计反思、必要的报错修复（最多五轮）与验证集实际测试后，保存候选。**被改写的是真正的 Agent 代码组织方式**：可以调整模块角色、提示、串并行调用、反馈与答案集成，而不只是改几句 Prompt；元设计器及执行 LLM 的权重不更新。

**区别现有卡**：[TD001/TD002](../../knowledge/DELTA_INDEX.md) 搜索任务/变异 Prompt 或示例；[TD003–TD005](../../knowledge/DELTA_INDEX.md) 对固定 Agent 模块的 Prompt 反思、选择与合并；[D007](../../../knowledge/deltas/D007_code_evolution.md) 进化的是量化因子计算代码，不是调度基础模型的 Agent 可执行程序。**普通 Python 生成、自动报错修复、基础模型调用不另称独立创新。**

**配对不足①**：代码搜索允许通过增加 LLM 调用/反馈轮数提高任务分数，原文主实验却主要以准确率/F1 评价，§6 将成本/延迟等多目标纳入未来方向。**性能增益有多少来自架构优化、多少来自额外推理计算**仍需同预算对照；作者承认评价范围，不等于证明所有发现的架构都只是在堆算力。详见 [TD010](../../knowledge/deltas/TD010_executable_agent_program_search.md) 和 [IDEAS①](IDEAS.md)。

## ② TD011｜历史 Agent 设计、代码及成绩构成可回流的探索踏脚石

**输入与更新位置**：Meta Agent 从 Archive 中阅读以往候选的**设计理念、可执行 `forward` 代码和真实得分**，借用不同设计中的机制构件、包括并非当前最佳的探索中间态，产生新程序并将测试结果写回 Archive。与 TD010 的「**搜索对象是什么**」不同，本项改变「**已评价的历史结构怎样进入下一轮生成上下文**」。并不是训练设计者模型的参数。

**区别现有卡**：[TD002](../../knowledge/deltas/TD002_success_trace_prompt_induction_context_evolution.md) 将单题成功工作过程反推 Prompt/示例；[D003](../../../knowledge/deltas/D003_success_memory.md) 保存成功因子；[D020](../../../knowledge/deltas/D020_semantic_reward_surrogate_scheduler.md) 训练语义 Plan 奖励预测模型。这里存取的是跨轮**Agent 代码设计和评价历史**，由 Meta Agent 直接用于提出新架构。普通记忆不另称首创。

**配对不足②**：Appendix J Table 6 显示 MGSM **带人工初始设计种子 53.4、空档案初始化 67.5**，其余任务总体带种子更有利。**空初始化不等于每轮不积累 Archive**，所以不能说持续记忆已经被证明限制探索。初始种子先验何时帮助/局限新结构搜索，以及动态档案独立贡献多少，是仍需正交消融的待核问题。详见 [TD011](../../knowledge/deltas/TD011_agent_design_archive_stepping_stones.md) 和 [IDEAS②](IDEAS.md)。

## 不新增的同义机制

运行时自修复、跨模型/跨任务迁移展示及作者提出的 higher-order Meta Agent 自我修改，均不另建卡：前者是通用工程环节，中者是测试结果，后者是论文未来工作，**没有在主实验中实现**。

**研究阶段**：仅批准 T004 单篇特色及特化疑问，不表示方向 B 进入跨论文比较阶段或已设计最终系统。
