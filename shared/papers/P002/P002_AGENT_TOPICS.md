# P002｜七层 21 个金融专题 Agent（点击展开说明）

> 本页是 [P002 工程问题主表](P002_工程复现问题清单_v1.csv) 中“金融专题 Agent”一项的**补充阅读入口**，不是第二张研究表格。分类及模板文件名依据作者公开的 [Seven-Level Agent Hierarchy README](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/README.md) 核对。

## 实际怎么实现

所谓 21 个 Agent，是**21 种金融研究专题 Prompt**，并非 21 个分别微调的金融大模型。各角色的差异主要来自两部分：`Agent-Specific Intro`（角色/研究任务）与 `Agent-Specific Factor Design Guidance`（因子构造指引）；共享系统提示、代码约束、库规则和输出格式。已有有效/无效因子时，还可以把成败分析插入生成 Prompt；部分 Guidance 可先经过五种风格之一改写。详见作者 [Prompt 组装说明](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/README.md)。

## 七层分类与具体 Prompt

**I｜市场结构与周期（2）**：[市场周期 Market Cycle](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_market_cycle.md)、[波动状态 Volatility Regime](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_volatility_regime.md)。关注市场周期与波动状态变化。

**II｜极端风险（2）**：[崩盘预警 Crash Predictor](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_crash_predictor.md)、[尾部风险 Tail Risk](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_tail_risk.md)。关注突发下跌与尾部脆弱性。

**III｜量价关系（4）**：[流动性 Liquidity](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_liquidity.md)、[订单失衡 Order Imbalance](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_order_imbalance.md)、[量价协同 Price-Volume Coherence](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_price_volume_coherence.md)、[成交量结构 Volume Structure](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_volume_structure.md)。关注成交量、订单与价格的关系。

**IV｜价格与波动行为（5）**：[日频趋势 Daily Trend](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_daily_trend.md)、[滞后响应 Lag Response](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_lag_response.md)、[区间波动 Range Vol](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_range_vol.md)、[反转 Reversal](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_reversal.md)、[波动非对称 Vol Asymmetry](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_vol_asymmetry.md)。关注趋势、反转、价格区间及非对称性。

**V｜多尺度复杂性（3）**：[回撤 Drawdown](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_drawdown.md)、[分形 Fractal](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_fractal.md)、[羊群行为 Herding](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_herding.md)。研究不同时间窗口下的复杂结构与群体行为。

**VI｜稳定性与状态门控（2）**：[状态门控 Regime Gating](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_regime_gating.md)、[稳定性 Stability](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_stability.md)。研究不同市场状态下哪些信号更稳健。

**VII｜几何形态与融合（3）**：[K线形态 Bar Shape](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_bar_shape.md)、[组合因子 Composite](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_composite.md)、[创造性设计 Creative](https://github.com/uwFengyuan/CogAlpha_Prompt/blob/main/prompts/seven_level_agent_hierarchy/agent_creative.md)。关注K线形态与组合、变换式因子设计。

**合计：2＋2＋4＋5＋3＋2＋3＝21。** 作者目录把 Herding 列在第五层，不能误放第七层。点击上述任意角色即可阅读相应原始 Prompt，查看它的具体研究任务、生成要求和用词。

## 证据边界

这里核对的是作者公开的 Prompt 模板及其 README，不是完整调度源码；不能据此证明 21 角色采用并发进程、分别训练模型，或每个角色都产生独立有效的 Alpha。论文原文入口见 [PAPER.md](PAPER.md)。
