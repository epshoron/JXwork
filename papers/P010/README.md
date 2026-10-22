# P010｜AlphaSchema：先搜索金融语义，再实现因子（2026）

> **当前归档**：原文客观骨架与研究者已认可的**两项特色机制 + 两项对应待验证限制**。未作学术首创认定、未独立复现。

**一句话**：把因子构思拆为五维金融语义计划，先用可学习的**语义奖励代理评分器（LightGBM）**和预算调度挑选值得实现的方向，再让 LLM 写成可运行因子、回测并把「计划—奖励」反馈给评分器。**训练的是外部代理评分器，而不是微调生成 LLM。**

[原文与核验边界](PAPER.md) · [已审特色与证据](ARCHITECTURE.md) · [两项特化问题](IDEAS.md) · [D019](../../knowledge/deltas/D019_five_axis_semantic_plan_space.md) · [D020](../../knowledge/deltas/D020_semantic_reward_surrogate_scheduler.md) · [arXiv 全文](https://arxiv.org/html/2607.26642)

**已确认的研究主线（2026-10-22）**：「**五维语义 Plan → 可学习的预算调度 → LLM 实现 → 真实数据评价 → Plan–Reward 经验回流**」。在骨架获认可后，研究者进一步批准 [D019](../../knowledge/deltas/D019_five_axis_semantic_plan_space.md) 与 [D020](../../knowledge/deltas/D020_semantic_reward_surrogate_scheduler.md) 及两项一一对应的待验证问题；不表示世界范围首创。

## 一眼看懂：系统骨架（依据原文 Figure 1、§2–3 自绘）

```mermaid
flowchart TB
    V["人工整理的金融语义词表（Event/Context/Qualities/Direction/Output）"] --> PLAN["从五维语义空间采样候选 Plan"]
    PLAN --> SCHED["预算调度器：结构探索 / 代理评分引导 / 局部语义变异"]
    MODEL["LightGBM：根据历史 Plan→Reward 学习语义得分预测"] --> SCHED
    SCHED --> AGENT["LLM Code Agent：把选中 Plan 实现为快/慢两个时间尺度的因子"]
    AGENT --> GUARD["执行/数据契约/数值稳定性/未来信息检查；失败可修复一次"]
    GUARD --> REWARD["因子评价：RankIC + RankICIR − 时滞敏感度惩罚"]
    REWARD --> BUFFER["累计语义 Plan—Reward 记录（不可修复失败记零分）"]
    BUFFER --> MODEL
    REWARD --> VALID["有效因子 → 按奖励排序与相关性过滤"]
    VALID --> DOWN["入选因子池 → LightGBM 组合预测 → Top50/Drop5 回测"]
```

## 核心职责与反馈究竟进入哪里

1. **先定义要研究什么**：语义 Plan = **事件、背景/情境、品质限制、预期方向、输出形式**，不直接规定数学算子或参数。每项是一份有结构的金融假设（§2.2；Appendix C）。
2. **外部搜索调度器决定先实现哪些想法**：每轮从大量语义候选中筛选，预算由**新区域探索、LightGBM 预测高奖励、对优质语义 Plan 作局部替换**三部分分配。探索份额随累计评价数逐渐下降（§3.3；Appendix A.3–A.4）。
3. **LLM 主要负责翻译和实现**：将选中的 Plan 变成具体因子程序，各尝试 fast/slow 时间尺度；执行检查未通过允许修复一次，仍失败按零奖励计入缓存（§3.1–3.2）。
4. **学习环路发生在语义层**：RankIC、RankICIR、因子延迟敏感度组成奖励；累计 `(Plan, reward)` 重新训练 LightGBM，指导下轮选 Plan。更新的是**代理评分器的参数与候选探索分配**；未报告对 Code Agent 使用梯度微调，更不是严格 RSI（§3.2–3.3）。
5. **落地与评价**：有效候选按奖励排序、筛掉高度相关的因子；下游 LightGBM 合并因子信号，并按 Qlib Top50/Drop5 测试（Appendix A.5–A.11）。

## 主要实验口径（只记录作者报告）

- **CSI300**：训练 2016–2020，验证 2021–2022，测试 2023–2025；目标为未来五交易日收益。主要语义词表有 **140 个条目**（40 Event、40 Context、50 Qualities、3 Direction、7 Output）；每次 **80 轮×每轮 16 个 Plan**，前十轮纯探索，报告 **5 次独立运行**（§4.1）。
- **主要结果（Table 1）**：仅 OHLCV 计划形成的 **120 因子池**报告 IC **0.0382**、年化超额收益 **8.53%**；加入基本面语义后扩展为 **150 因子池**，报告 IR **1.0877**、年化超额收益 **11.94%**。该 AER 是论文定义的**扣交易成本、相对基准的复合年化超额收益**，不是总收益。表中并非所有预测指标都第一（LSTM 的 RankIC / RankICIR 更高）。
- **因子产生与模型参数层级不可混淆**：这里的 LightGBM 奖励代理**选择语义研究方向**；后面的 LightGBM 组合模型**预测股票收益/排序**，二者职责不同。
- 以上均是作者预印本的历史回测报告，**不是独立复现**；+Fundamental 比纯 OHLCV 多了数据与 30 个因子，不能仅凭组合收益差异把收益归因于“语义搜索算法”。

**已审的去重结论**：项目内将**生成前的五维语义 Plan 表示**记录为 [D019](../../knowledge/deltas/D019_five_axis_semantic_plan_space.md)，将**外部 LightGBM 奖励代理与三路动态调度**记录为 [D020](../../knowledge/deltas/D020_semantic_reward_surrogate_scheduler.md)。已对照 D002/D006/D009/D010/D012/D016/D017 等邻近机制；相同的普通 Agent 反馈不重复建卡。学术首次仍需查新。

**状态**：原文 HTML §2–5、Appendix A、C、D、E 的方法与主要证据已核；2026-10-22 研究者认可 2 项机制及 2 项对应的待验证问题，详见 [ARCHITECTURE](ARCHITECTURE.md) 和 [IDEAS](IDEAS.md)。代码与回测未独立复现；整体研究仍处阶段一。
