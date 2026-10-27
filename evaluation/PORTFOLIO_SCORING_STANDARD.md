# 因子多空组合构建与综合评分口径（研究记录 v0.1）

> **状态：讨论版 / 待确认，不是已实施的回测标准。** 记录日期：2026-10-27。方向 A：AI / Agent 因子挖掘的**外部评价器（Evaluator）**。依据为研究讨论中转述的手写公式；参数、异常值处理和执行细节未完成核定。本文仅保存可公开讨论的一般数学与工程口径，不附原始手稿、内部数据或专有策略。
>
> **不属于某篇论文的已审创新或 Delta；不代表方向 A 已转入跨论文综合/原创系统研究阶段。** 研究目标：先准确建立“单因子 → 可交易多空组合 → 净收益/风险 → 可比较分数”的评价链，供后续因子挖掘实验统一使用。

## 0. 一眼看懂：两类「权重」不要混淆

~~~mermaid
flowchart LR
    A["每个日期×股票的 alpha"] --> B["可交易股票池/缺失处理/可选去极值"]
    B --> C["按日横截面去均值"]
    C --> D["除以绝对值和：股票持仓权重 w[t,i]"]
    D --> E["下一交易日 VWAP 执行与收益对齐"]
    E --> F["每日组合毛收益 + 实际调仓换手"]
    F --> G["扣成本得到每日净收益"]
    G --> H["年化收益 / Sharpe / 最大回撤等"]
    H --> I["评分系数 lambda 合成 Score"]
    D --> J["按日期×股票保存完整仓位"]
    I --> K["保存 Score、指标和评分配置版本"]
    J --> L["用 run_id / factor_id / 日期连接"]
    K --> L
~~~

1. **持仓权重** \(w_{t,i}\)：某个因子在信号日 \(t\) 对股票 \(i\) 的目标多/空资金权重；每一天、每只股票都不同，必须保存**完整时间序列**，不是一个标量。
2. **评分系数** \(\lambda_R,\lambda_{SR},\lambda_{DD},\lambda_{TO}\)：把组合收益、Sharpe、回撤、换手等**统计指标**合成为一个 Score 的系数；它们必须连同**计算口径和版本**一起保存，不能与 \(w_{t,i}\) 混在同一概念里。
3. **此处只构造“一个 Alpha 对应一个多空组合”并评分**，**没有**给出“多个 Alpha 组合成一个总 Alpha”的因子间权重学习方法。如果后续需要因子池组合，属于另一层建模。

## 1. 从 Alpha 到 0.5 Long / 0.5 Short

### 1.1 数据约定

设 \(a_{t,i}\) 为信号日 \(t\) 股票 \(i\) 的因子值；矩阵行=日期、列=股票。每天仅对**在当时可知且可交易**的有效股票横截面计算，缺失/停牌/不可交易须先定义处理规则；历史股票池不得按未来存活情况反向筛选。

### 1.2 横截面 Demean（去均值）

\[
d_{t,i}=a_{t,i}-\bar a_t,\qquad
\bar a_t=\frac{1}{N_t}\sum_{i\in U_t}a_{t,i}.
\]

于是 \(\sum_{i\in U_t}d_{t,i}=0\)。在 pandas「行=日期、列=股票」约定下：

~~~python
demeaned = alpha.sub(alpha.mean(axis=1), axis=0)
~~~

这里的 \`mean(axis=1)\` 是**每个日期横向对所有股票求均值**；\`sub(..., axis=0)\` 是让按日期求出的均值正确广播到各列。若矩阵方向反过来，代码必须同步调整。

### 1.3 按绝对值和归一化（因子值加权）

\[
G_t=\sum_{j\in U_t}|d_{t,j}|,\qquad
w_{t,i}=\frac{d_{t,i}}{G_t},\quad G_t>0.
\]

\[
\sum_i w_{t,i}=0,\qquad
\sum_i|w_{t,i}|=1,\qquad
\sum_{w_i>0}w_i=+0.5,\qquad
\sum_{w_i<0}w_i=-0.5.
\]

**为什么**：去均值让正负偏离量总和相等；按总绝对偏离量缩放后，正权重总计 +50%，负权重总计 -50%，净敞口 0、总绝对敞口 100%。**0.5/0.5 是两侧总仓位，不是每边股票数各占一半，也不是每只股票等权。** 若所有有效因子值相同、\(G_t=0\) 或有效股票不足，**该日权重不可定义，应记录无效/跳过**，而非用除零或自动补零伪造评价。

**可手算示例**（仅用于验证公式）：股票 A/B/C/D 的 \(a=[4,2,0,-2]\)，均值 1，\(d=[3,1,-1,-3]\)，\(G=8\)，于是 \(w=[0.375,0.125,-0.125,-0.375]\)。多头 +0.5，空头 -0.5；A 的仓位大于 B，足见**不是等权**。

对应成熟通用工具的定义：Alphalens \`factor_weights(demeaned=True, equal_weight=False, group_adjust=False)\` 使用去均值、除以绝对值和构造资金中性因子加权组合。文档：<https://alphalens.ml4trading.io/api-reference.html>；源码：<https://github.com/quantopian/alphalens/blob/master/alphalens/performance.py>。这是**通用实现参考**，不代表导师公式来源已核定，也不能冒充独有创新。

**限制**：资金中性（dollar-neutral）≠ 股票 beta 中性、行业中性、市值中性或风险中性；还可能有借券限制和真实执行障碍。

## 2. 先区分异常值的「1%–99%」和手稿中的「2%」

手稿上出现类似 \`alpha.abs().sum(1) * 2%\` 的记法，口头转述又提及按横截面 1%–99% 分位数截断；**两者不能直接画等号**。

| 解释 | 算法作用位置 | 目的与判定 |
|---|---|---|
| **A. 因子值分位数 Winsorization** | 在 Demean 之前，对每日原始 \(a\) 按 \([Q_{0.01},Q_{0.99}]\) clip | 降低极端 Alpha 值影响；**1%/99% 是分位数，不是单票权重比例**；口头确认过此解释，但仍须核对实际实现 |
| **B. 单票权重上限 2%** | 构建/约束 \(w\) 时要求 \(|w_{t,i}|\le 0.02\) | 控制集中度；**与 Winsorize 不同**；手稿右上式不足以证明已要求这一方案 |
| **C. 按横截面绝对值总和的 2% 做阈值** | 对原始或去均值 Alpha 施加 \(|a_i|\) 或 \(|d_i|\le 0.02\sum_j|\cdot|\) | 类似 L1 占比裁剪，但**处理对象、先后顺序、是否重新归一化未说明**；不能直接视作最终仓位必然 ≤2% |

**工程约束**：如果既强制 \(\sum w^+=0.5\)、\(\sum w^-=-0.5\)，又强制每只股票 \(|w_i|\le0.02\)，至少需要 25 只可做多和 25 只可做空的股票；单纯 \`clip\` 再 \`w /= sum(abs(w))\` 可能重新突破 2% 或破坏多空 0.5/0.5。真正的仓位上限要用**满足两侧预算与上下界的再分配/约束优化**。

**当前基线记录方式**：把 \`winsor_quantiles\`、\`position_cap\`、\`l1_threshold\` 记为**互斥含义不同的独立配置项**；在确认前不得写成“2% 就是 1%–99%”。

## 3. 时间对齐：因子、下一日 VWAP、再下一日收益

手稿类似 \`weight * vwap_return.shift(-2)\`。一种**条件成立时正确的解释**：

- \(t\) 收盘后取得信号 \(a_t\)，产生目标权重 \(w_t\)；
- \(t+1\) 交易日按 VWAP **假设执行**该权重；
- \(t+2\) 交易日 VWAP 对应持有区间终点，计算一段价格变动。

如果 \`vwap_return = vwap.pct_change()\`（即 \(r_{s,i}=VWAP_{s,i}/VWAP_{s-1,i}-1\)），则

\[
r^{\mathrm{fwd}}_{t,i}
=(\mathrm{vwap\_return.shift(-2)})_{t,i}
=\frac{VWAP_{t+2,i}}{VWAP_{t+1,i}}-1.
\]

\[
R^{gross}_t=\sum_i w_{t,i}\,r^{\mathrm{fwd}}_{t,i}.
\]

**严格条件**：索引必须按交易日顺序，\`pct_change\` 不能偷偷前向填补缺失价格；因子在 \(t\) 确实已可用；执行价格和持仓收益在同一交易日历/股票池上对齐。若源数据的 \`vwap_return\` 本身定义为**前瞻收益**，或信号在盘中已知，则 \`shift(-2)\` 未必正确。**\`-2\` 不等于连续持有两天**：以上定义的收益期间只有 \(t+1\to t+2\) 的一段。

假设“每天各信号形成的一期持仓依次换仓”，可把这些一期收益组成每日收益序列；但**收益时间标签、同时在持仓的组合层数、执行日换仓成本**必须固定，否则可能重复记账。VWAP 成交只是回测简化，不是能够无滑点全额成交的保证。

## 4. Turnover 与成本：明确单/双边，保存仓位历史

### 4.1 两种常用口径

**最简目标权重差分近似**（尚未考虑自然价格漂移）：

\[
TO^{both}_t=\sum_i|w^{target}_{t,i}-w^{target}_{t-1,i}|,
\qquad
TO^{oneway}_t=\tfrac12\,TO^{both}_t.
\]

如果上一目标权重与本次真实交易前持仓不同，真实换手应按**调仓执行时点**的持仓计算：

\[
TO^{both}_{\tau}=\sum_i|w^{target}_{\tau,i}-w^{pretrade}_{\tau,i}|.
\]

\`pretrade\` 已包含上一期仓位的涨跌漂移、现金流和组合会计影响；需通过回测器更新，而不是把昨天的信号权重原样当作今天实际持仓。真实卖出/买入受不可交易、借券和成交约束时，还需记录实际成交后的 \`executed_weight\`。

例：A 昨天 +30%→今天 +20%，B 昨天 -30%→今天 -20%，对应双边成交额换手 20%，单边口径 10%。两种约定都可用，**成本系数必须与口径配套**。

### 4.2 1 bp = 0.0001

若假定每 1 单位**实际双边成交额**付 \(1\) bp，成本模型可写：

\[
c=0.0001,\quad Cost_{\tau}=c\,TO^{both}_{\tau}.
\]

以组合权益为分母的成本率约为 \`0.0001 × 双边成交额换手率\`。这一设定仅是**假设系数**；不自动涵盖交易手续费、价差、冲击、印花税、融券费或融资利息。若用单边 TO，需要重新换算成本系数。

\[
R^{net}_{\tau}=R^{gross}_{\tau}-Cost_{\tau}-OtherCosts_{\tau}
\]

上式为单期的近似扣费表达，真正回测要让成交、持仓损益、费用都落在**相同实际发生的日期**。如果目标是净收益评价，优先先形成**完整日度净收益序列**，再算 Sharpe、净值和最大回撤。

### 4.3 为什么日频调仓可能高换手

归一化仓位会随着每天的 Alpha 横截面数值与排序变化而变化。权重从 +2% 翻到 -2%，仅这一只股票就贡献 4% 的双边成交额。持续高换手既可能来自因子信号不稳定，也可能来自每日完整重新配仓、交易约束或执行规则；**不能仅凭换手高就断言因子预测失败**。

## 5. Objective / Fitness：保留手稿示意，另给可执行的清晰版本

手稿左下角的字可读作 **Objective Function（目标函数）**。示意约为：

\[
S_{\mathrm{sketch}}
=1\times Returns +0.05\times SR +(-0.1)\times DD
+(\text{符号待核})\times TO\times0.0001.
\]

注意：以上 \`1\`、\`0.05\`、\`-0.1\`、\`0.0001\` **均未被确认为经过优化或实证验证的最终系数**。末项若表达交易成本惩罚，应当是**负号**；照片所示的末项正负及其具体写法不能充分确认。DD 若定义为“正值的最大回撤幅度”（例如 20%=0.20），其系数应为负；若记录成 -0.20，则不能不经转换再乘 -0.1。**所有 Return/Drawdown 用小数而非百分数字符串。**

### 5.1 原式至少存在三个口径问题

1. **时间单位**：日均收益与年化 SR 相加，会因尺度不同而让一项主导得分。Returns 到底是累计、日均、年化还是 CAGR，必须明确。
2. **重复惩罚**：如果 \`Returns\`、\`SR\` 和 \`DD\` 已经从**扣成本的净收益序列**计算，再对同一 1 bp 的 turnover 成本减一次，就会重复扣费。若额外 TO 项意图表达非线性的容量/实施难度惩罚，必须单独定义、单独校准，而不称“同一笔交易费”。
3. **多目标系数的稳定性**：收益和 Sharpe 通常相关；任意线性系数会改变候选排名。需要固定验证窗口/尺度，对不同系数做稳健性测试，不能在测试段反复调权重。

### 5.2 建议的首版无重复扣费评分（**待批准方案，不是手稿原式**）

先把成交额费用从每日日度毛收益中扣除，再由**同一净收益序列**计算：

- \(R_{\mathrm{ann,net}}\)：年化净复合收益（需固定交易日数、收益时间索引、净值计算方法）；
- \(SR_{\mathrm{net}}\)：年化净收益 Sharpe（约定无风险利率/融资成本，若零近似要明示）；
- \(MDD_{\mathrm{net}}\ge0\)：根据净值曲线计算的最大回撤幅度；
- \(TO^{both}\)：另外报告平均日度、累计或年化双边换手，不在首版得分里重复当手续费扣除。

\[
\boxed{S_{\mathrm{v1}}=
1.0\,R_{\mathrm{ann,net}}+
0.05\,SR_{\mathrm{net}}-
0.1\,MDD_{\mathrm{net}}}
\]

**这些 1/0.05/0.1 仍只是便于对照的示例系数。** 若研究需要一个真正独立的换手惩罚，可另外定义、标注 \`score_version=v2\`，基于**明确单位**加入 \(-\lambda_{TO}\times TO_{\mathrm{annual}}\)；它衡量的是交易强度偏好，不再简单重复已扣的 1 bp 成本。

一个纯演示例子：年化净收益 0.12、净 Sharpe 1.5、最大回撤幅度 0.20，则 \(S_{\mathrm{v1}}=0.12+0.075-0.02=0.175\)。**分数不是 17.5% 的组合收益率，也不是跨评分版本可直接比较的绩效。**

### 5.3 指标和选择防护

建议与 Score 并列输出 \`gross_return\`、\`net_return\`、\`Sharpe\`、\`MDD\`、\`turnover_both\`、\`n_valid_days\`、\`n_assets\`，便于解释因子排名。RankIC/RankICIR、暴露、样本外稳定性等是**附加诊断**，没有证据支持现在立即塞进同一个线性式。对于 AI 大规模批量因子搜索，更应固定 train/validation/test 边界，避免在测试数据上调函数和不断选择最优因子。

**树式筛选 vs 线性聚合**：先用有效天数、数据合法性、持仓可行性等**硬门槛**决定是否有效，再对有效候选按连续 Score 排序；简单阈值筛选不是必须训练一个 ML 决策树。

## 6. 权重必须“保存在一起”：推荐持久化数据契约

**核心缺口不是少算一个平均值，而是缺少可追溯的“权重—调仓—收益—评分”同一评测运行记录。** 由于粒度不同，建议统一用 \`run_id\` 连接多张表/文件，**而非把每只股票仓位和整个回测只有一个的评分系数强行塞进一格**：

| 工件 | 键 / 最小字段 | 作用 |
|---|---|---|
| **positions**（逐日逐股） | \`run_id, factor_id, signal_date, execution_date, asset_id, raw_alpha, cleaned_alpha, demeaned_alpha, target_weight, pretrade_weight, executed_weight, valid_flag\` | **保存每一天全部股票权重**；用多空两侧总权重做审计；记录哪一天计划、哪一天实际成交 |
| **returns_and_trades**（逐日） | \`run_id, return_date, gross_pnl, gross_return, turnover_both, turnover_oneway, cost_rate, total_cost, net_return, nav\` | 换手、成本、收益时点一一对齐 |
| **metrics_and_score**（逐因子/回测运行） | \`run_id, factor_id, score_version, ann_net_return, net_sharpe, mdd, avg_turnover_both, objective_score, valid_days, status\` | 保存独立指标及最终评分，不只留一个 Score |
| **evaluation_config**（冻结配置） | \`run_id, data_window, universe_rule, alpha_availability, winsor_rule, cap_rule, rebalance_rule, vwap_definition, return_shift, turnover_convention, fee_bps, annualization_rule, lambda_R, lambda_SR, lambda_DD, lambda_TO, code_version\` | **把所有评分权重/口径与股票仓位链接在同一个运行版本中** |

示意配置（**含义而非默认上线值**）：

~~~yaml
run_id: eval_example_001
factor_id: example_alpha
signal_to_execution_trading_days: 1
return_horizon_trading_days: 1
vwap_return_shift_if_defined_as_backward_pct_change: -2
long_book_target: 0.5
short_book_target: -0.5
gross_exposure_target: 1.0
winsor_quantiles: pending_confirmation
single_name_cap: pending_confirmation
turnover_convention: both_sides_traded_notional_over_equity
fee_bps_per_traded_notional: 1
score_version: discussion_v1
score_coefficients:
  annual_net_return: 1.0
  annual_net_sharpe: 0.05
  positive_max_drawdown: -0.1
  extra_turnover_penalty: 0.0  # 净收益已扣费用
~~~

如以后使用 Parquet/CSV，按**因子 ID × 日期 × 股票**保存权重，并与 \`run_id\` 的配置、逐日收益、评分结果关联；日期、证券标识、缺失规则不能省。既能看单只股票持仓，也能聚合整天多头/空头；既能复算 turnover，也能比较不同因子、不同版本评分。**本文只定义保存结构，目前没有真实因子序列，故没有可实际写入的历史仓位文件。**

## 7. 实施前核对表（明确“不知道什么”）

1. **2% 真实含义**：分位数去极值、单票仓位上限，还是 Alpha 的 L1 比例阈值？对象在去均值前还是后？是否二者并用？
2. **Alpha 可用时刻**：是否严格 \(t\) 日收盘后可知？VWAP 用全天还是指定窗口？\`vwap_return\` 当前数据的具体定义？是否每日重建一期持仓？
3. **持仓与换手**：计算仅目标权重差，还是考虑漂移的实际成交额？调仓成本落在哪一天？无法交易的股票如何处理？
4. **Objective 口径**：Returns 的时间单位、Sharpe 的年化方式、DD 的正负定义、TO 项究竟是单独偏好还是 1 bp 交易费？末项书写符号需核实。
5. **可比性**：各因子是否使用同样的股票池、时段、缺失值处理、可交易约束、参数版本？长短期数据不足的因子如何标记失败？
6. **保存权重**：不只存最终 Score；在一次 \`run_id\` 里保存逐日逐股目标/实际仓位与评分系数/版本，并能按同一时序重算所有指标。

## 8. 来源与边界

- **原始手写记录**：提供了 Demean、绝对值归一化、0.5/0.5 多空、VWAP 时序、组合收益与 Objective 的大体结构；**未**提供完整的回测数据/可验证代码/精确定义。本文标“手稿/转述”的内容是研究记录而非独立事实验证。
- **可核对的公共背景**：[Alphalens factor_weights 官方文档](https://alphalens.ml4trading.io/api-reference.html) 及 [开源实现](https://github.com/quantopian/alphalens/blob/master/alphalens/performance.py)：可支撑“去均值 + 绝对值归一化得到 dollar-neutral、gross 1 的 factor-weighted 权重”，但**不能证明 2% 的含义、VWAP 执行、turnover 及评分系数**。
- 与本库已有 [D005 通用样本外评测背景](../knowledge/deltas/D005_oos_evaluation.md)、[P009 动态评价函数演化](../papers/P009/ARCHITECTURE.md)不同：**本文只固定外部评价口径和数据契约**，不把标准组合构建或线性目标函数包装成 P009/D017 一类新型搜索创新，不新增 Delta。
- **保密**：不归档手稿图像、内部证券池、实盘账户、真实仓位/收益、公司代码或内部参数来源。若后续需要真正的历史持仓记录，先核实数据公开/共享授权。
