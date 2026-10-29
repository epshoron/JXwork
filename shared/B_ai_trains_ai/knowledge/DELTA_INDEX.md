# 方向 B｜机制 Delta Index：AI 如何训练 AI

> **初始化于 2026-10-22，已有 TD001–TD011 十一项经研究者批准的机制卡。** 本索引记录 AI trains AI 论文中**经过研究者确认、严格语义去重**的具体机制，不自动等同学术首创。

| 编号 | 机制指纹／更新对象 | 来源 | 审批及证据状态 | 与已有机制的区别 |
|---|---|---|---|---|
| [TD001](deltas/TD001_coupled_task_mutator_prompt_evolution.md) | **T001**：任务 P 与修改任务的变异指令 M **联动进化**，以任务适应度间接筛选修改策略 | [T001](../papers/T001/ARCHITECTURE.md) | **特色机制① + 对应边界①经研究者批准（2026-10-22）**；论文原文 Fig.1–2 / §3 / §6，未复现 | 不同于 D007 因子代码变异、D017 评分函数代码进化；这里更新自然语言 P/M，评价规则保持固定 |
| [TD002](deltas/TD002_success_trace_prompt_induction_context_evolution.md) | **T001**：成功 working out **反推任务 Prompt**，并演化 Few-shot 正确示例上下文 | [T001](../papers/T001/ARCHITECTURE.md) | **特色机制② + 对应漂移风险②经研究者批准（2026-10-22）**；原文 §3.2.4–3.2.5 / Appendix J.5，未复现 | 不同于 D003 保存并检索成功因子；这里将正确执行轨迹转为提示指令/示例，亦不同于 TD001 的 M 自身变化 |
| [TD003](deltas/TD003_trace_guided_module_prompt_reflection.md) | **T002**：执行/评价轨迹诊断→反思式指定模块 Prompt 改写，反馈 minibatch 验收 | [T002](../papers/T002/ARCHITECTURE.md) | **机制①＋归因待核问题①已获研究者批准（2026-10-22）**；ICLR 2026 §2–3/Appendix C–D；未复现 | 区别 TD002 成功 working out→Prompt/示例；本卡用失败轨迹及评测诊断局部改写；改善不等于真实致错模块归因已证实 |
| [TD004](deltas/TD004_instancewise_pareto_parent_selection.md) | **T002**：对 D_pareto 各验证样例取局部领先候选，Pareto 抽父代保留搜索分支 | [T002](../papers/T002/ARCHITECTURE.md) | **机制②＋局部领先稳定性待核②已获批准（2026-10-22）**；Table 3 Pareto +12.44 vs global-best +6.05；未复现 | 不同于 TD001 锦标赛、D010 MCTS 路径回传、D020 LightGBM 预测计划奖励；按逐题胜出选择 Prompt 父代 |
| [TD005](deltas/TD005_lineage_aware_module_merge.md) | **T002**：GEPA+Merge 从共同祖先的互补模块进化分支合并整套 Prompt | [T002](../papers/T002/ARCHITECTURE.md) | **机制③＋合并时机/模块互补待核③已获批准（2026-10-22）**；Table 1 两模型反向结果；未复现 | 不同于 TD003 单模块反思、D007 Python 因子代码普通交叉；按祖先谱系/互补模块合并，Qwen 聚合结果未提升 |
| [TD006](deltas/TD006_shared_actor_judge_self_reward_dpo.md) | **T005**：同一 LLM Actor/Judge 自评候选→生成偏好对→迭代 DPO 更新共享参数 | [T005](../papers/T005/ARCHITECTURE.md) | **特色①和对应风险①已批准（2026-10-22）**；长度上升属作者观察，Reward Hacking 未证实 | 区别 TD001–TD005 的 Prompt 改写/搜索；区别 D013/D015/D016 因子专属奖励：这里用同权重普通回答自评价转为偏好训练 |
| [TD007](deltas/TD007_dual_task_judge_transfer.md) | **T005**：IFT+EFT 双任务初始化；回答偏好 DPO 训练向 Judge 能力间接迁移 | [T005](../papers/T005/ARCHITECTURE.md) | **特色②和对应不足②已批准（2026-10-22）**；Table 4 的 5-best 下降、Exact Match 持平，三模型阶段范围有限 | 区别 TD006 的自有偏好数据闭环；专指 Judge 任务初始化与跨任务迁移的可持续性证据，不是重新发明多任务学习 |
| [TD008](deltas/TD008_agent_call_transition_lightningrl.md) | **T003**：把复杂 Agent 多次 LLM 调用转换为单次 `(input, output, reward)` transition 接入 RL 参数训练 | [T003](../papers/T003/ARCHITECTURE.md) | **机制① + 对应跨调用信用分配不足①已批准（2026-10-22）**；2025 原论文 §3.2–3.3；未复现 | 与 D016 的因子池整轨 GRPO、TD006 自评分 DPO 不同：本机制控制**调用级训练单元映射**，不新发明 RL |
| [TD009](deltas/TD009_role_selected_agent_training.md) | **T003**：按多角色 Agent 的指定 LLM 决策筛选进入模型参数训练的数据 | [T003](../papers/T003/ARCHITECTURE.md) | **机制② + 对应共享权重/协作影响不足②已批准（2026-10-22）**；2025 原论文 §3.2.2、§4.1；未复现 | 不同于 TD007 Actor/Judge 跨任务能力迁移及 D004 普通角色分工：这里是**训练数据的角色级选择**，未选角色不保证参数隔离 |
| [TD010](deltas/TD010_executable_agent_program_search.md) | **T004**：Meta Agent 编写可执行 `forward(taskInfo)`，搜索整个下层 Agent 的模块与调用流程 | [T004](../papers/T004/ARCHITECTURE.md) | **特色①与配对待核问题①已批准（2026-10-22）**；ICLR 2025 §2–3/§6；未复现 | 对比 TD001–TD005 主要优化 Prompt、D007 优化金融因子计算代码；本项优化 Agent 可执行结构；主性能评价未隔离额外推理计算的贡献 |
| [TD011](deltas/TD011_agent_design_archive_stepping_stones.md) | **T004**：历轮 Agent 设计理念、Python 代码与实测成绩进入 Archive，作为新结构设计踏脚石 | [T004](../papers/T004/ARCHITECTURE.md) | **特色②与配对待核问题②已批准（2026-10-22）**；Figure 3、Appendix J/Table 6；未复现 | 区别 TD002 成功轨迹反推 Prompt、D003 成功因子记忆、D020 代理奖励预测；初始化种子消融不能归因于持续 Archive 效果 |
## 使用与同步

- 机制卡编号从 **TD001** 起，正式路径为 `deltas/TD001_*.md`；不创建空卡或未经批准的“候选创新”。
- 先核实**改变的对象**：训练数据、奖励/反馈、优化策略、模型参数或其他真实被更新的工件，区分提示修订与真实训练；同时区分作者主张、原文证据与我们的推断。
- 与本方向现有 TD 卡及 [方向 A 的 D001–D020](../../knowledge/DELTA_INDEX.md) 做**严格语义去重**，重复者作交叉引用，不新增同义卡。
- 每次新增、修改、撤回 TD 卡时，**同一回合同步本 Index、对应论文已审批引用和受影响的 [论文 Index](../papers/INDEX.md)**；共享文件写前读最新 SHA，冲突后合并。
- 研究阶段和审批标准均继承 [统一规范](https://github.com/epshoron/JXwork/blob/main/assistant/RESEARCH_WRITING_STANDARD.md)。

[本方向入口](../README.md) · [方向 A 的机制库](../../knowledge/DELTA_INDEX.md)
