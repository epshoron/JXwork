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

## 2026-10-26 补充工程核验

- 直接重新核对原文 §2–3、Appendix A.3–A.4、C/D：五维Plan与词表、10,000候选Plan抽样、16个实现名额、三路调度、LightGBM奖励预测、局部语义变异和Plan–Reward缓存。
- 已静态检查作者当前Python文件：`schema_space.py`、`selector.py`、`reward_model.py`、`pipeline.py`、`code_agent.py`、`configs/default_stock_search.json`及五类JSON词表。当前启用词条为Event54、Context43、Quality59、Direction3、Output8，总计**167条**；论文主实验为**140条**，不要混用。
- 论文正文以平滑衰减解释探索份额，而当前公开配置是随累计实验量变化的分段固定配额。论文称语义变异候选会按代理预测分排序；当前`selector.py`先接收合格变异子Plan，再记录其代理预测分及名次。这是需要锁定论文实验代码版本才能核定的实现口径差异，**不据此直接给出缺点结论**。
- 作者仓库有可运行的轻量demo和核心流程代码，但当前并未独立运行整篇实验、核验市场结果或判定学术首次。仅作原文与已见源码的客观说明。

[工程三列表](P010_工程复现问题清单_v1.csv) · [机制图解](P010_SEMANTIC_PLAN_GUIDE.md)
