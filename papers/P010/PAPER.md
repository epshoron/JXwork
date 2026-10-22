# P010｜原文入口与证据边界

**题目**：AlphaSchema: Exploring the Space of Trading Semantics for LLM-Based Alpha Mining  
**作者**：Jingyang Yi, Jian Yang, Yifei Jin, Yuqi Li, Jian Li  
**版本**：arXiv:2607.26642v1，2026-07-29 提交；截至 2026-10-21 作为**预印本**记录，不自动假定已经正式同行评审。

- [arXiv 原始记录](https://arxiv.org/abs/2607.26642)
- [可读 HTML 全文](https://arxiv.org/html/2607.26642)
- [作者列明代码仓库](https://github.com/JingyangYi/AlphaSchema)（本轮未运行代码，也未将代码说明当作实证结论）

## 实际核验材料

- 原文 §2：Plan = (Event, Context, Qualities, Direction, Output) 的五维语义空间、与公式实现分离；
- §3：候选采样、固定预算调度、LLM 因子实现与一次修复、RankIC/RankICIR/时滞敏感度奖励、LightGBM 语义代理的经验缓存迭代；
- §4 Table 1：CSI300 主实验数据时间区间、140 词表、80×16 搜索规模、五次运行与结果；
- §5：五个语义字段逐一移除的消融、语义空间探索轨迹、重复实现效率、不同 LLM 代码实现差异；
- Appendix A：奖励公式与参数、10,000 Plan 采样、相关性去重、下游 LightGBM、Qlib Top50/Drop5、费用与指标；Appendix C/D：词表来源、JSON Schema 及完整 Plan→Code 示例。

**尚未完成**：未独立复现作者代码、核实实验数据/统计显著性、对同等搜索预算/模型大小的竞争系统作统一新实验，未系统核查学术首创性。**2026-10-22 研究者进一步审批**：两项机制及对应特化问题已在 [ARCHITECTURE.md](ARCHITECTURE.md)、[IDEAS.md](IDEAS.md) 与 [D019](../../knowledge/deltas/D019_five_axis_semantic_plan_space.md)、[D020](../../knowledge/deltas/D020_semantic_reward_surrogate_scheduler.md) 记录；独立复现、完整学术首创查新仍未开展。

原文 PDF 仅提供链接，不转存或再分发到公共仓库。
