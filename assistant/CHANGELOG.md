# 研究更新日志（Changelog）

## 2026-10-29 · Alpha 胜者相关性 0.65 正式确认

- 用户拍板：Alpha 对 Knowledge 库中已正式成功的内部 Alpha 值逐一比较，最大绝对相关性严格 `<0.65`；没有历史胜者时仅跳过这个子检查，其余合法性/统计性/盈利性检查照常。
- 模块明确分为前置 Technical/Leakage Gate、独立 Statistical Evaluator 和独立 Financial Evaluator；结果、胜者引用及失败原因存入 Knowledge。
- 相关系数具体计算方法、日度/股票样本对齐、Daily `<0.6` 的统计口径和毛/净收益门槛对应关系继续列为待定，不得假装已验证。


## 2026-10-29 · 确认双阶段研究验收与共享资源 A/B/C 归类

- 研究者拍板：四库不变；Knowledge 同时保存全部因子候选、第一关技术/统计检查、第二关金融评价和失败记录。第一关不通过禁止昂贵金融回测；通过第一关的实验不论金融成功与否都记录 Ret/SR/DD/TO/成本。
- 因子是否正式成功只按 `Ret > 3%`、`SR > 1`（且两关实际通过）判定；达标即存档。无需第五个 Alpha 库，成功标签和查询视图保留于 Knowledge/Experiment；Score 不必在入库时计算，保留既有数学定义用于后续 Python 按需排序。
- Daily 库须执行与已有 Daily 特征的相关性 `< 0.6` 硬门槛，具体统计定义和 Alpha 第一关相关性参数尚需真实数据口径；未定不假装已测试。
- `shared/` 归并为 A_alpha_mining、B_ai_trains_ai、C_intraday_to_daily，历史研究 Agent 的专用导读移入 `assistant/research_guides/`；原始论文及编号不改。



## 2026-10-29 · 三目录重构与现行 V1.0.1 架构确认

- 研究者明确批准 shared（公司云端可用研究资料）/ assistant（研究 LLM 协作规则）/ presentation（本地展示）三类分离；原 A/B/C 编号与文件保留。
- 最新 Research Loop v9 双流程图取代旧双 Loop 研究侧草图，成为 shared/architecture/V1.0.1/ 的当前拍板架构；Meta Loop 尚未启动。
- 系统仍未实现或验证：模型/API 数量、检索、遮蔽比例、Daily 准入数值阈值及正式因子池晋级规则仍待研究，Evaluator V1 不变。
- GitHub Actions 新增 shared 单独 ZIP 工件；移动脚本与文档路径，保留二进制原始资料及 Git 历史。


## 2026-10-26 · P001–P010 工程问题合并 Excel 重制与验证

- 将十篇 **136 条工程问题**汇总到 [visualization/](../presentation/visualization/README_工程问题汇总.md) 的十 Sheet 工作簿，附带本地补充说明和 ZIP。
- **修复交付事故**：旧版手写 XLSX 内部结构不规范，Windows Excel 提示修复且长文本显示截断；已**舍弃旧版**，改用 [openpyxl 构建脚本](../presentation/visualization/build_engineering_package.py) 从各篇 CSV 重新生成，统一列宽、自动换行、居中对齐与按文本估算行高。
- [GitHub Actions 构建与校验](https://github.com/epshoron/JXwork/actions/runs/40280727878) 已通过：重新读取 XLSX 检查 10 Sheet、136 行、格式及超链接，核对 ZIP 内相对路径目标。**未在 Windows Excel 实机复测**；论文内容、审批状态与 Delta 未改。

> **新用途**：只登记研究协作规则/架构变更，以及用户确认后归档的最终综合成果；**不记录逐篇研读过程、临时见解或 LLM 聊天流水账**。

## 2026-10-22 · T004 ADAS 2+2 正式审批归档

- **研究者批准两项特色和一一对应的特化问题**：① [TD010｜可执行 Agent 程序与模块结构搜索](../shared/B_ai_trains_ai/knowledge/deltas/TD010_executable_agent_program_search.md) ↔ 性能导向评价没有隔离复杂结构带来的额外模型调用/Token/延迟预算；② [TD011｜历史 Agent 代码设计与成绩积累为搜索踏脚石](../shared/B_ai_trains_ai/knowledge/deltas/TD011_agent_design_archive_stepping_stones.md) ↔ Appendix J 显示 MGSM 空初始化好于人工种子，但这并**未隔离持续 Archive 本身**的作用。
- **语义去重**：对照方向 B TD001–TD009 与方向 A D003/D007/D017/D020，分别记录「**搜索的可执行对象**」和「**历史设计怎样回流新结构搜索**」；不将普通代码修复、通用记忆或跨任务实验另建机制卡。
- **同步**：[T004 论文骨架](../shared/B_ai_trains_ai/papers/T004/README.md)、[已审特色](../shared/B_ai_trains_ai/papers/T004/ARCHITECTURE.md)、[配对问题](../shared/B_ai_trains_ai/papers/T004/IDEAS.md)、[B 论文索引](../shared/B_ai_trains_ai/papers/INDEX.md) 和 [B 机制索引](../shared/B_ai_trains_ai/knowledge/DELTA_INDEX.md)。未经独立复现，阶段一单篇研究不等于阶段二/三正式启动。


## 2026-10-22 · T003 Agent Lightning 2+2 审批归档

- **研究者批准两组特色及一一对应的不足**：① [TD008｜多轮 Agent 的 LLM 调用拆为单次 RL transition](../shared/B_ai_trains_ai/knowledge/deltas/TD008_agent_call_transition_lightningrl.md) ↔ 原论文各调用共享同一轨迹最终回报 R，缺细粒度跨调用信用分配；② [TD009｜多角色调用选择性进入参数训练](../shared/B_ai_trains_ai/knowledge/deltas/TD009_role_selected_agent_training.md) ↔ 共享权重可能波及未参与训练的角色、多角色协作依赖未得到独立控制。
- **严格证据边界**：原文 §3.2–3.3 / §4.1 / §5.2 可证实结构与当前奖励组织；“坏的调用已遭错误强化导致失败”“未选中的 Checker 已经退化”均**不是原文已证实的事实**。2025 原论文与 2026 Agent Lightning v1.0 分开；学术首创性与独立复现未确认。
- **双方向严格去重**：区别方向 B TD001–TD005（Prompt 文本/搜索）、TD006 自有偏好 DPO、TD007 共享权重下 Judge 跨任务能力迁移，以及方向 A D016（因子池整轨 GRPO）；TD008 聚焦**通用 Agent 多次调用→训练单元的转换**，TD009 聚焦**训练角色/调用选择**，不另称 RL/多 Agent 分工为新发明。
- **同步归档**：[T003 架构](../shared/B_ai_trains_ai/papers/T003/README.md)、[已审特色](../shared/B_ai_trains_ai/papers/T003/ARCHITECTURE.md)、[配对不足](../shared/B_ai_trains_ai/papers/T003/IDEAS.md)、[B 论文 Index](../shared/B_ai_trains_ai/papers/INDEX.md)、[B Delta Index](../shared/B_ai_trains_ai/knowledge/DELTA_INDEX.md)。阶段一单篇评价，不代表开展跨论文阶段二或提出原创工程方案。

## 2026-10-22 · T005 自奖励模型两项机制与配对不足获批

- **研究者明确批准 2+2**：① [TD006｜同一 Actor/Judge 自评分偏好对→迭代 DPO 参数更新](../shared/B_ai_trains_ai/knowledge/deltas/TD006_shared_actor_judge_self_reward_dpo.md) ↔ 同源评分可能强化长度/格式偏好；② [TD007｜IFT/EFT 双任务初始化与 Judge 跨任务间接能力提升](../shared/B_ai_trains_ai/knowledge/deltas/TD007_dual_task_judge_transfer.md) ↔ Judge 细项指标未持续同步增长、只测试三模型阶段。
- **原文/推断明确分开**：作者报告平均回复长度 `1092→1552→2552`，Table 4 中 `M2→M3` 5-best `44.3%→43.2%`、Exact Match `14.3%→14.3%`；**Reward Hacking 已发生、Judge 整体退化、无限迭代必然失败都不是已证实结论**。作者同时报告人评及 Pairwise Accuracy 增益。
- **双方向语义去重**：T001/TD001–002、T002/TD003–005 优化外部 Prompt 或搜索调度；方向 A D013/D015/D016 是因子专属奖励/轨迹的权重训练。T005 具体区别是普通指令回答的**同模型自产偏好反馈**与**IFT/EFT 初始化促成的 Judge 迁移**。DPO/多任务学习/LLM-as-a-Judge 不是学术首次主张，创新与不足均经研究者逐项批准。
- **同步**：[T005 已审评价](../shared/B_ai_trains_ai/papers/T005/ARCHITECTURE.md)、[配对不足](../shared/B_ai_trains_ai/papers/T005/IDEAS.md)、[原文架构](../shared/B_ai_trains_ai/papers/T005/README.md)、[方向 B 论文 Index](../shared/B_ai_trains_ai/papers/INDEX.md)、[B Delta Index](../shared/B_ai_trains_ai/knowledge/DELTA_INDEX.md)；方向 A 没有改动。研究仍属阶段一，无独立复现或学术世界首创证明。

## 2026-10-22 · GEPA T002 三项机制＋对应三项特化问题获批

- **研究者明确批准 3+3**：① [TD003｜执行/评价轨迹驱动模块级 Prompt 反思](../shared/B_ai_trains_ai/knowledge/deltas/TD003_trace_guided_module_prompt_reflection.md) ↔ 模块级错误归因仍待隔离验证；② [TD004｜逐验证样例 Pareto 父代选择](../shared/B_ai_trains_ai/knowledge/deltas/TD004_instancewise_pareto_parent_selection.md) ↔ 局部胜出能否跨子集稳定迁移待核；③ [TD005｜同祖先互补模块合并](../shared/B_ai_trains_ai/knowledge/deltas/TD005_lineage_aware_module_merge.md) ↔ Merge 时机/模块交互与成本归因未被完全隔离（作者 Table 1 报告两种模型聚合收益方向不同）。
- **严格语义去重**：对照已审 T001/TD001–TD002 与方向 A 的 D001、D003、D007、D010、D020 等；三个更新环节分别是**生成新 Prompt 的诊断与局部改写、选择下一轮父代的逐样例调度、跨谱系合并互补模块**。不将普通反思、遗传交叉或 Pareto 概念宣称世界首创。
- 已同步 [T002 客观骨架](../shared/B_ai_trains_ai/papers/T002/README.md)、[已审贡献](../shared/B_ai_trains_ai/papers/T002/ARCHITECTURE.md)、[配对不足](../shared/B_ai_trains_ai/papers/T002/IDEAS.md)、[本方向论文 Index](../shared/B_ai_trains_ai/papers/INDEX.md) 与 [TD 总表](../shared/B_ai_trains_ai/knowledge/DELTA_INDEX.md)。原文为 ICLR 2026，尚无独立复现；未进入项目阶段二/三。


## 2026-10-22 · Promptbreeder T001 两项机制与特化不足获批

- **研究者明确批准 2+2**：① [TD001｜任务 Prompt 与变异 Prompt 联动进化](../shared/B_ai_trains_ai/knowledge/deltas/TD001_coupled_task_mutator_prompt_evolution.md)，对应作者明确承认“仅改变 Prompt 内容，未自动进化外层 Prompting 算法/调用结构”的边界；② [TD002｜成功工作过程反推任务 Prompt + Few-shot 正确示例上下文进化](../shared/B_ai_trains_ai/knowledge/deltas/TD002_success_trace_prompt_induction_context_evolution.md)，对应作者 Appendix J.5 观察到 Few-shot 示例主导结果、任务 Prompt 漂移到无意义文本的现象。风险不是已证实的普遍泛化失败。
- **严格语义去重**：与方向 A 的 D003 成功因子持久检索、D007 因子代码进化、D017 因子/指标代码双轨进化比较；TD001 更新自然语言**变异策略 M**，TD002 把**成功执行推理转成 P 与上下文**，既与彼此不同，也不冒充基础遗传算法/提示工程的新发明。
- **同步**：[T001 已审特色](../shared/B_ai_trains_ai/papers/T001/ARCHITECTURE.md)、[两项特化不足](../shared/B_ai_trains_ai/papers/T001/IDEAS.md)、[T001 骨架](../shared/B_ai_trains_ai/papers/T001/README.md)、[B 论文 Index](../shared/B_ai_trains_ai/papers/INDEX.md) 与 [B Delta Index](../shared/B_ai_trains_ai/knowledge/DELTA_INDEX.md)。另 [T003 Agent Lightning](../shared/B_ai_trains_ai/papers/T003/README.md) 已按论文来源归档**客观骨架**，其创新/不足尚未经审批；项目方向 B 仍以阶段一研究为主，不宣布阶段二/三或系统方案启动。

## 2026-10-22 · 明确方向 B 的双层优化研究问题

- **研究者提出的目标研究场景（未定稿方法）**：上层 AI 通过 CLI 等界面与用户沟通，利用知识库、记忆与任务反馈，持续改进下层 API/Executor Agent 的提示、技能、工具和记忆策略；是否进一步更新下层模型参数仍是开放问题，不创建新论文或创新知识卡。
- **两类作用对象并列研究**：① Prompt / Skills / 工具路由 / 记忆策略等**外部 Agent 优化**；② SFT、RL、蒸馏等**参数训练**，LoRA 是参数高效微调方式，不等同于训练目标。允许比较/混合，但不在研究前宣告优选或效果。
- 已同步 [方向 B 总览](../shared/B_ai_trains_ai/README.md)、[仓库首页](../README.md)、[研究计划](RESEARCH_PLAN.md)、[Agent 规范](AGENTS.md)、[写作标准](RESEARCH_WRITING_STANDARD.md) 与 [快速指针](JXWORK_START_HERE.md)。B 的 T/TD 索引仍为空，方向 A 的 P/D 保持不动。

## 2026-10-22 · 正式建立双研究方向（研究者批准）

- **方向 A 原位保留**：现有 `papers/P001–P010`、`knowledge/deltas/D001–D020`、`synthesis/` 不移动、不重编号，当前阶段仍以单篇原文理解和评审为主。
- **方向 B 独立创建**： [ai_trains_ai/](../shared/B_ai_trains_ai/README.md) 用于“AI 如何训练 AI”；[论文索引](../shared/B_ai_trains_ai/papers/INDEX.md) 使用 `T001` 起，[机制索引](../shared/B_ai_trains_ai/knowledge/DELTA_INDEX.md) 使用 `TD001` 起，[综合目录](../shared/B_ai_trains_ai/synthesis/README.md) 独立。**尚无论文认领或已审创新，不建立空机制卡。**
- **统一工作门禁**：[AGENTS.md](AGENTS.md) 与 [RESEARCH_WRITING_STANDARD.md](RESEARCH_WRITING_STANDARD.md) 同步规定：先判方向，各自查 DOI/题名且跨方向去重；经原文核验的**论文骨架**可直接归档，**非论文来源须获准入批准**；创新、特化不足、研究想法、Delta **逐项经研究者审批与严格语义去重**；每个 Agent 自己同回合同步所属方向 Markdown 与两份 Index。
- **统一导航已修正**：[README](../README.md)、[RESEARCH_PLAN](RESEARCH_PLAN.md)、[JXWORK_START_HERE.md](JXWORK_START_HERE.md) 及相关目录说明支持双方向；废弃旧指针里已删除的 `notes/TEMPLATE.md`。本轮仅改变研究资料组织，未开展方向 B 文献或研究阶段二/三。

## 2026-10-22 · P009 SJS 双轨共同进化 2+2 获批

- 研究者明确认可 P009 **2 项机制 + 2 项特化不足**：① 同时搜索因子 `f` 和可执行评分指标 `g`，由非自我裁定规则晋级指标；② SJS 通过定向通信、按数据来源与角色过滤、跨轮容量限制、技能库权限等结构约束管理双轨搜索。
- **特化不足**：① 指标晋级参照训练 Sharpe，而 Alpha 搜索也面向这一目标，可能产生指标/因子的目标共适应（作者承认循环性，未证实真实失效）；② 作者未做单 Agent 联合进化对照，冻结技能库等消融与 Agora 的迭代轮数/PPO 设置不一致，贡献难单独归因。
- **严格语义去重与入库**：对照最新 D001–D016（含其他 Agent 新增 D014–D016）和 P010。两条分别改变**评分函数本身与晋级状态**、**角色/数据来源信息流拓扑**，不与 D004 通用分工、D005 通用 OOS、D010 MCTS 评价回传或 P010 奖励代理学习重复；新增 [D017](../shared/A_alpha_mining/knowledge/deltas/D017_joint_alpha_metric_evolution.md)、[D018](../shared/A_alpha_mining/knowledge/deltas/D018_sealed_joint_search_information_topology.md)，风险仅归 [P009 IDEAS](../shared/A_alpha_mining/papers/P009/IDEAS.md)，不滥开知识卡。
- 已同步 [P009 骨架](../shared/A_alpha_mining/papers/P009/README.md)、[已审批评价](../shared/A_alpha_mining/papers/P009/ARCHITECTURE.md)、[论文索引](../shared/A_alpha_mining/papers/INDEX.md)、[Delta Index](../shared/A_alpha_mining/knowledge/DELTA_INDEX.md)。原始预印本及单种子/短严格 holdout 的证据边界不变，不宣告阶段二/三开始。

## 2026-10-21 · P005 池级 GRPO 机制获批

- **研究者明确认可**：P005 AlphaPilot 的**多轮真实数据工具反馈 → 因子池边际增删/替换 → 最终因子池轨迹奖励 → GRPO 更新 LLM 搜索策略参数**作为一项具体特色机制；归档至 [P005 已审评价](../shared/A_alpha_mining/papers/P005/ARCHITECTURE.md) 和 [D016](../shared/A_alpha_mining/knowledge/deltas/D016_pool_trajectory_grpo.md)，同步 [papers/INDEX](../shared/A_alpha_mining/papers/INDEX.md) 与 [Delta Index](../shared/A_alpha_mining/knowledge/DELTA_INDEX.md)。
- **严格去重**：与 P007 D013 单公式 TMB/DAPO、P008 D014–D015 种子进化多目标 RL、P002 D007 固定 LLM 代码种群搜索的**任务对象、奖励对象、更新层级**相区别。GRPO/强化学习微调、多轮工具调用、池级优化的基础思想均不称学术首创。LoRA/全参数实施方式尚未确认。
- **审批边界**：仅上述机制获批；未批准的独立不足与研究方案均未归档。论文属于 2026-10-11 arXiv 预印本，结果非独立复现，项目整体仍在阶段一。

## 2026-10-21 · P008 两项创新与一一对应的两项特化不足获批

- **研究者认可的 P008 创新**：[D014](../shared/A_alpha_mining/knowledge/deltas/D014_seed_conditioned_evolution.md)（从种子 Alpha 出发的连续多轮因子进化）与 [D015](../shared/A_alpha_mining/knowledge/deltas/D015_hierarchical_evolution_reward.md)（Tool/Consistency/Exploration/Performance/Streak 五目标分层奖励）。
- **对应特化不足①（D014）**：Pass@T（Eq.6）只要在前 T 轮至少出现一个 IR 优于种子且为正的因子便成功，无法单凭成功率分辨小幅和大幅改善；作者另有 IR 轨迹和组合评估，不能断言“只报告成功率”。
- **对应特化不足②（D015）**：§3.4 Figure4 主要消融 Exploration、Consistency，尚未同等充分地分别证明 Tool/Performance/Streak 与截断、乘法耦合、工具项分母的必要性。**奖励目标制衡本身是创新设计价值，而非此不足**。
- **去重与证据**：前者是**种子持续改进任务的成功指标表达局限**，后者是**五目标训练奖励的独立归因局限**，非同义缺点，也不同于 D010 树搜索评分回传、D013 TMB 历史分组极值风险。两项经研究者分别批准，**不是已证实算法故障**；正式 ICLR 题录可查，实验图表通过公开原始 PDF 可检索片段及转录核对，完整 PDF 仍待直接逐页验证。已同步 [论文评价](../shared/A_alpha_mining/papers/P008/ARCHITECTURE.md)、[逐项问题](../shared/A_alpha_mining/papers/P008/IDEAS.md)、[论文索引](../shared/A_alpha_mining/papers/INDEX.md)与[知识总表](../shared/A_alpha_mining/knowledge/DELTA_INDEX.md)。


## 2026-10-21 · 各 Agent 强制同步 Index 与 Markdown

- **研究者显式要求**：每个研究 Agent 在正式研究归档、客观骨架写入、创新/不足审批状态变化及 Delta 卡新增/修改后，必须在**同一回合**主动同步相关 Markdown、`papers/INDEX.md`、`knowledge/DELTA_INDEX.md`，不许等待别的 Agent 补漏；工作结束前检查链接、状态、Markdown 表格完整性。纯对话、无真实状态改变时不刷屏。
- **AGENTS/规范同步**：研究规则变化要同时修改 `AGENTS.md`、`RESEARCH_WRITING_STANDARD.md` 并检查 README、RESEARCH_PLAN 与目录指引无冲突。完整规则现已同步到 [AGENTS](AGENTS.md)、[写作标准](RESEARCH_WRITING_STANDARD.md)、[论文 Index](../shared/A_alpha_mining/papers/INDEX.md)、[Delta Index](../shared/A_alpha_mining/knowledge/DELTA_INDEX.md) 和相关指引；不改变原来的审批/保密权限。
- **这次修复**：`papers/INDEX.md` 中 P004/P005 空行导致的表格中断已修正，P002 的两项已审批机制与一项风险状态同步到 Index；`knowledge/DELTA_INDEX.md` D011/D012 间的空行也已修正。**只调整展示和真实同步状态，不增写未经批准观点**。

## 2026-10-21 · P007 的 2＋1 已审批归档

- **用户批准**：P007 AlphaRLM 只保留**两项具体贡献**：金融文献题名/摘要与允许算子的 LEGO 公式构造（[D012](../shared/A_alpha_mining/knowledge/deltas/D012_literature_operator_assembly.md)），以及单因子 TMB 分组收益差/合法性奖励配合 DAPO 更新生成模型（[D013](../shared/A_alpha_mining/knowledge/deltas/D013_tmb_rl_factor_policy.md)）；学术原创性仍待更广查新。
- **唯一审慎保留的不足**：TMB 使用最高与最低历史分组均值之差，可能对偶然极值给出较高奖励；研究者认为此疑问也偏弱，所以明确标为**低置信度、未实证的研究问题**。此前「文献假设与公式可能脱节」未批准，不写入正式评价。
- **提交前语义去重**：D012 的作用在**文献→公式生成**，不同于 D002 现成 WQ101 公式先验、D006 领域角色提示和 D009 的生成后语义检查；D013 的作用在**单公式市场奖励→生成 LLM 权重**，不同于 P005 的多轮最终因子池奖励、D007 代码种群进化与 D010 的 MCTS 节点反馈。
- **成果入口**：[P007 首页图与历史回测](../shared/A_alpha_mining/papers/P007/README.md) · [已审评价](../shared/A_alpha_mining/papers/P007/ARCHITECTURE.md) · [问题](../shared/A_alpha_mining/papers/P007/IDEAS.md)；原始实验表仍待直接逐表核实，不冒充实盘。

## 2026-10-21 · P004 审批归档及严格语义去重门禁

- **P004 已获研究者认可**：[原架构](../shared/A_alpha_mining/papers/P004/README.md)及[精炼评价](../shared/A_alpha_mining/papers/P004/ARCHITECTURE.md)共记录**2 项机制亮点（MCTS 多维反馈树搜索、FSA 高频子树规避）+ 2 项相应特化风险假设（动态历史评分偏向、频率规避误伤）+ 1 项作者 Appendix J 自述的新颖性/生成空间限制**；风险未实证，学术首创尚待核查。
- **Delta 语义去重并行合并**：P003 已占 D008–D009，不覆盖。P004 使用 [D010](../shared/A_alpha_mining/knowledge/deltas/D010_mcts_multidimensional_search.md)、[D011](../shared/A_alpha_mining/knowledge/deltas/D011_frequent_subtree_avoidance.md)；特别核查 D011 与 D008 的区别（全库高频模式作为后续生成约束，vs 候选对参考公式的最大公共子树惩罚）。作者自述局限只在 P004 档案保留，**不再复制成新的 Delta**。
- **新强制规则**：[RESEARCH_WRITING_STANDARD.md](RESEARCH_WRITING_STANDARD.md) 与 [AGENTS.md](AGENTS.md) 明确要求每次上云创新、局限、知识卡前**显式比对最新全库语义重复**，对比干预点与失效原因；无法证明真正增量的内容先合并/关联或暂缓提交。**研究者审批、原文证据、严格去重缺一不可**。
- 其他 Agent 的 P002、P003 成果和索引状态保持，未擅自修改其审批结论。

## 2026-10-21 · P002 代码级种群演化贡献获批

- 研究者认可 **Thinking Evolution 的 Python 代码级因子种群搜索**（父代选择、变异/交叉、精英保留）作为 P002 的另一项特色贡献，已同步 [P002 架构](../shared/A_alpha_mining/papers/P002/ARCHITECTURE.md) 和 [D007](../shared/A_alpha_mining/knowledge/deltas/D007_code_evolution.md)；不声称遗传算子或 LLM 演化式编程学术首创。
- 研究者认为此前提出的“Python 更自由所以难以验证”的特化不足证据不足、过于牵强，**明确不批准**；没有给 D007 强行配缺点。至此 P002 已确认两项特色机制 D006/D007、仅一项尚待实证的专业 Agent 同质化风险。

## 2026-10-21 · P003 去重归档（研究者认可）

- [P003 单篇骨架与原文入口](../shared/A_alpha_mining/papers/P003/README.md) 已依原文 §3–4 归档；特化贡献与问题经对话认可，见 [ARCHITECTURE](../shared/A_alpha_mining/papers/P003/ARCHITECTURE.md) 与 [IDEAS](../shared/A_alpha_mining/papers/P003/IDEAS.md)。
- 去重后仅新增 [D008｜AST 最大公共子树惩罚](../shared/A_alpha_mining/knowledge/deltas/D008_ast_originality_penalty.md) 和 [D009｜假设—描述—公式双层对齐](../shared/A_alpha_mining/knowledge/deltas/D009_hypothesis_factor_alignment.md)。三 Agent/普通反馈沿用已有背景卡；与 P001 公式正向先验、P002 主题引导、P004 FSA 均标明机制边界；P004 创新不代审。
- **风险均是待验证研究判断**；Eq. 8 方向疑点尚未查源码，组合消融不代表两个约束各自已被证明有效。当前项目仍主要处于阶段一。

## 2026-10-21 · P002 专业搜索贡献及风险经研究者批准

- **已批准的 P002 特色贡献（D006）**：七组 21 个专业 Agent + 五类提示引导，以金融研究主题组织因子搜索；与 P001 的 WorldQuant 101 检索式公式先验不同。认可是项目级有辨识度的机制，不表示世界首次发明。
- **已批准的特化风险假设（未实证）**：固定的金融专业角色可能产生代码不同、预测信息重复的因子；需要以独立因子贡献、去重及相同生成预算对照检验。
- **已按新规则收敛档案**：[P002 架构](../shared/A_alpha_mining/papers/P002/ARCHITECTURE.md)、[P002 已审问题](../shared/A_alpha_mining/papers/P002/IDEAS.md)、[D006](../shared/A_alpha_mining/knowledge/deltas/D006_domain_guidance.md)、[Delta 索引](../shared/A_alpha_mining/knowledge/DELTA_INDEX.md) 只保留本次获批的核心判断。之前未经逐项审批的 D007 知识卡与其他 P002 比较判断已从正式数据库撤下；代码演化仍作为论文架构事实保留，等待后续审批。
- **研究阶段**：仍为阶段一；没有将候选缺点当成已发生的事实，也没有批准后续原创技术方案。

## 2026-10-21 · P001 定稿写作范围与创新审批门禁

- **已获研究者确认的单篇内容**：[P001 架构图与总览](../shared/A_alpha_mining/papers/P001/README.md)已精简；创新只突出**WorldQuant 101 结构化公式先验**（作者主张的关键贡献，不宣称世界首次），特化不足只记录**先验可能锁定生成方向、降低独立探索并带来搜索层面过拟合风险**（待实证，不写成已证实）。[核心评价](../shared/A_alpha_mining/papers/P001/ARCHITECTURE.md)、[研究疑问](../shared/A_alpha_mining/papers/P001/IDEAS.md)同步。
- **明确剔除泛泛内容**：不将 OOS、交易成本、普通多 Agent、市场变化等通用问题凑成 P001 创新/独有不足。D001/D003/D004 降为背景对照；D005 作为历史实验口径参考，**排除于创新 Delta 候选**。P002 的独立候选内容与已有对照保留且仍需另行审阅。
- **全局必须遵循的顺序与风格**：新增 [RESEARCH_WRITING_STANDARD.md](RESEARCH_WRITING_STANDARD.md)：**先画骨架讲清机制；作者贡献的独立评价、特化缺点和研究者想法先在 LLM 对话讨论，逐项得到研究者拍板才更新论文和 Delta 知识库**；言简意赅、术语易懂、只取具有辨识度的知识，不凑字数。已同步 README、AGENTS、RESEARCH_PLAN、papers/INDEX 与 knowledge 指引。
- **证据界限**：P001 目前仍未完成 PDF 原文逐页研读或独立复现；本人/公司内部经验和数据未写入 Public 仓库。

## 2026-10-21 · P002 按新规则迁入 papers/P002 并登记 Delta

- **单篇档案（用户要求）**：按 P001 的格式建立 [P002 首页和 Mermaid 图](../shared/A_alpha_mining/papers/P002/README.md)、[原文入口与核验边界](../shared/A_alpha_mining/papers/P002/PAPER.md)、[作者贡献与客观评价](../shared/A_alpha_mining/papers/P002/ARCHITECTURE.md)、[研究者问题](../shared/A_alpha_mining/papers/P002/IDEAS.md)。移除旧 `synthesis/` 中重复的单篇文件；不恢复 `notes/`。
- **知识库增量**：P002 相对 P001 的反馈/职责/评价差异更新 D001、D003、D004、D005；新增 [D006 领域研究方向与提示多样化](../shared/A_alpha_mining/knowledge/deltas/D006_domain_guidance.md) 和 D007 代码级进化（原候选已撤回待用户审批）。这两项暂为**待研究者审阅的候选 KB-first**，不等于已批准机制或学术首次提出；详情见 [DELTA_INDEX](../shared/A_alpha_mining/knowledge/DELTA_INDEX.md)。
- **范围**：仍处于项目阶段一；作者结果与我们的疑问分离，未完成独立复现、学术首创性查新或阶段二/三正式整合。其他论文的认领与材料未修改。

## 2026-10-21 · 建立 papers/P001 单篇档案与 knowledge/Delta 机制数据库

- **研究者明确要求的架构调整**：每篇用户确认的研究成果统一归入 `papers/P00X/`，而不是堆在 `synthesis/`。P001 已落地 [来源/原文入口](../shared/A_alpha_mining/papers/P001/PAPER.md)、[架构示意与概览](../shared/A_alpha_mining/papers/P001/README.md)、[客观贡献及限制](../shared/A_alpha_mining/papers/P001/ARCHITECTURE.md)、[独立研究问题](../shared/A_alpha_mining/papers/P001/IDEAS.md)。
- **Delta 知识库初建**：[knowledge/DELTA_INDEX.md](../shared/A_alpha_mining/knowledge/DELTA_INDEX.md) 将 P001 分为五个可复用机制卡 D001–D005，供下一篇判断「已有／变体／新增／待核」。P001 是首篇，所以都是**第一次入本项目知识库**，但**不等于学术原创**；双循环、知识反馈等已见 QuantAgent 2024。
- **原始证据与边界**：已核正式期刊摘要/Highlights、作者仓库 README 和 QuantAgent 原文；P001 PDF 正文尚未逐页验证，客观评价中的未证实缺口均以待核标示。论文正文留权威链接，不擅自上传 PDF。
- **保留阶段顺序**：阶段一先理解单篇；记录客观评价与候选思考是研究者本轮明确指示，**不代表跨论文系统比较或原创方案已定稿**。
- **已同步**：README、AGENTS、RESEARCH_PLAN、papers/INDEX、papers/README、synthesis/README；保留其他 Agent 论文的认领状态。

## 2026-10-21 · 用户明确要求归档 CogAlpha 专题架构总结

- 新增 [CogAlpha 架构与研究问题（已迁入 P002）](../shared/A_alpha_mining/papers/P002/README.md)：包含自绘 Mermaid 流程图、21 领域 Agent 的七组任务、作者声称的贡献及原文证据、可检验的疑问。
- 严格分离作者声明、实验结果、我们自己的待验证分析；这是用户批准的 P002 专题归档，**不是恢复逐篇 notes 或全面进入阶段二/三**。
- 索引仍只记录最小状态，其他 Agent 仍通过 `papers/INDEX.md` 去重。

## 2026-10-21 · P001 架构骨架归档（研究者明确要求）

- 按研究者本轮明确要求，在 [`papers/P001/README.md`](../shared/A_alpha_mining/papers/P001/README.md) 归档精炼架构与 Mermaid 图、作者明确主张的贡献、此前 QuantAgent 的相关基础、作者报告结果和**待后续文献核验**的缺点/改善假设。
- **资料完整性边界**：核实期刊摘要/Highlights、作者仓库说明与相关前作摘要；未逐页核对 P001 PDF 全文，故这份骨架总结**不等于阶段一完整研读完成**，也不宣告进入阶段二/三。
- 其他研究 Agent 的认领不受影响；索引继续仅用于最小去重状态。

## 2026-10-21 · 确立三阶段顺序与通用研究 Agent 协作

- **用户确定的研究顺序**：**阶段一（当前）先完整阅读全文并理解论文本身在做什么 → 阶段二才在足够的高质量研读基础上整合创新点与缺点 → 阶段三在证据积累充足后有机结合创新与缺口，提出我们自己的可检验想法**。三个先后阶段不同于「质量控制、经验学习、推理协作」三个可组合研究视角。
- **保留最新轻量架构**：各研究 Agent 在 LLM 对话中阅读全文、理解、讨论和纠错；GitHub 仅负责规范与 `papers/INDEX.md` 的最低限度认领去重。用户要求或确认后才归档经核实的精炼成果，不恢复逐篇 `notes/` 或研究过程流水账。
- **统一匿名化认领**：不再以聊天窗口代号标记研究者或论文，采用 `P001、P002…` 编号与「已认领／阶段一研读中／讨论未定稿」等真实状态。另一篇论文的历史非统一编号已改为 P002；论文身份与实际已读进度不变。
- **原文可达性**：优先由研究 Agent 自主阅读公开 HTML/PDF，访问受限才请研究者按需提供；公开仓库只保存原文链接，不上传未授权 PDF。
- **已同步**：`README.md`、`AGENTS.md`、`RESEARCH_PLAN.md`、`papers/INDEX.md`、相关目录指引与 `synthesis/RESEARCH_LENSES.md`。

## 2026-10-21 · 删除逐篇读书笔记设计，切换对话研读→结束后总结

- **用户决定**：取消 `notes/` 逐篇读书笔记目录、模板和既有临时笔记；这些文档不再作为交付或去重依据。
- **流程**：开始处理时仅在 `papers/INDEX.md` 快速认领，保留题名、DOI/arXiv/官方链接和最小状态；研读、讨论和修正都发生在 LLM 对话内。
- **写作时机**：等用户和 LLM 研读完、完成总结且确认要归档后，再将精炼且有原文依据的共识写入 `synthesis/` 或用户指定的位置；不再每读完一篇就自动提交文档。
- **协作**：各研究 Agent 不互读其他 Agent 的聊天；去重仅看仓库最新 `papers/INDEX.md`；修改共享文件前拉取最新版本并处理冲突。
- **现有论文认领**：原有两篇论文均继续保留在 INDEX，采用统一编号和真实状态；旧的逐篇研究细节已从 CHANGELOG 中删除。
- **已同步规范**：README、AGENTS、RESEARCH_PLAN、papers/INDEX、papers/README、synthesis/README、synthesis/RESEARCH_LENSES。

## 2026-10-21 · 确立文献优先与三种互补研究视角

- 聚焦 LLM/Agent 量化因子发现、验证反馈、搜索迭代与 RSI 边界；从原始论文出发，不先定完整技术路线。
- **质量控制、经验学习、推理协作** 是可组合的研究问题，而非互斥算法分类或从低到高的能力阶段。
- 公共仓库不可上传内部公司材料、密钥或未经许可再分发的论文 PDF。
