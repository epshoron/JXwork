# P010｜AlphaSchema：已认可的两项特色机制

[一页架构图](README.md) · [原文与已核范围](PAPER.md) · [已审特化问题](IDEAS.md)

**一句话**：先把「研究什么金融机制」定义为五维可搜索语义 Plan，再用累积评价训练 LightGBM 决定**哪份计划值得花 LLM 实现预算**；LLM 主要负责 Plan→因子程序。**训练的是外部搜索代理，不是生成 LLM 的参数。**

## 研究者认可①：五维金融语义 Plan（D019）

- **具体变化**：Event、Context、Qualities、Direction、Output 共同定义一份**生成之前**的金融研究计划，可组合、去重、变异，计划不预设具体公式与参数；LLM 实现是下一环。
- **相对前作**：[D002](../../knowledge/deltas/D002_structured_alpha_prior.md) 检索经典公式结构；[D006](../../knowledge/deltas/D006_domain_guidance.md) 用专业角色 Prompt；[D012](../../knowledge/deltas/D012_literature_operator_assembly.md) 文献观点加算子生成；[D009](../../knowledge/deltas/D009_hypothesis_factor_alignment.md) 生成后检查语义一致性。**P010 的独立控制对象是生成前的显式五维 Plan 搜索空间**，不是这些模块的别名。
- **对应特化边界①**：一次在线搜索只能组合当前预设的语义记录；未被词表表达的金融机制可能缺席。原文允许**搜索周期之间离线扩展词表**，不是声称永远封闭。需比较相同预算下固定/扩展词表对**词表外新增有效信息**的影响。
- **原文证据**：Appendix E 的五维逐一去除试验以 100 个已筛高奖 Plan 为参照，完整计划平均 `|RankIC|=0.0185`，去掉任意一维降至 `0.0131–0.0147`，说明字段约束在这一试验中有作用，但**不能证明已覆盖未知经济机制**。[机制主卡 D019](../../knowledge/deltas/D019_five_axis_semantic_plan_space.md)

## 研究者认可②：语义奖励代理 + 三路搜索配额（D020）

- **具体变化**：累积 `(Plan, Reward)`；按语义标识、类别、成对交互训练 LightGBM **预测未实现 Plan 的奖励**，让调度器动态分配**结构探索／预测高分优先／高分计划局部变异**的代码实现预算。
- **相对前作**：不是 [D010](../../knowledge/deltas/D010_mcts_multidimensional_search.md) 的公式树节点回传，不是 [D016](../../knowledge/deltas/D016_pool_trajectory_grpo.md) 的 GRPO 权重训练，也不是 [D017](../../knowledge/deltas/D017_joint_alpha_metric_evolution.md) 的评分函数代码共进化。**更新对象是外部代理评分器的参数及语义搜索预算**。
- **对应特化边界②**：Appendix E 的 held-out 代理预测 **Spearman 0.239、Top10% lift 1.519×**（包含辅助采样的独立分析档案），支持有一定可学习关系，**并非完整搜索器在相同预算下优于无代理版本的独立因果证据**；需固定实施与评估预算，单独开关 surrogate/配额调度。[机制主卡 D020](../../knowledge/deltas/D020_semantic_reward_surrogate_scheduler.md)

## 结果与证据边界

作者 Table 1 在 CSI300 的 2023–2025 测试期报告 OHLCV 120 因子池 IC **0.0382**、年化超额收益 **8.53%**；加基本面语义和 30 个因子后的 150 因子池年化超额收益 **11.94%**，两组输入/因子数不同，不能单独归因于语义搜索。均是**预印本报告的回测，不是独立复现**。

**审批身份**：2026-10-22 研究者确认上面两项特色机制和一一对应的**待验证问题**；它们是项目内值得积累的机制差异，**不表示学术首创或缺点实证定论**。原文：[arXiv:2607.26642 §2–5、Appendix A/C/E](https://arxiv.org/html/2607.26642)。
