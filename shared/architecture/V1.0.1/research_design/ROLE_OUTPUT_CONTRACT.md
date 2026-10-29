# Research Agent统一 Daily/Alpha 产物与接口

**核心输出不因角色专业、是否日内研究而改变：instrument × trade_date → scalar | NULL。** 输入可以是分钟序列、跨日历史、多个股票或已发布 Daily 特征，输出是日频横截面候选；不能提交分钟交易策略当成 Daily 因子。

角色提交字段：

- role_id、role_strategy_version、primary_domain、secondary_domains：明确版本化身份和跨领域依赖。
- research_question、financial_hypothesis、source_refs：可检验金融假设与文献来源，作者绩效不冒充内部实测。
- formula_or_code_ref、parameters、required_fields、dependencies：可计算且实际字段可得。不能臆造分钟成交量、盘口、真实分钟VWAP等。
- observation_end_time、first_usable_at：数据可用时点；使用全天分钟结果的信号不能在开盘时已经可用。
- history_lookback、cross_section_reference、data_version、null_policy、minimum_samples：重放数据的窗口、参考集合、缺失处理。
- candidate_kind = daily_intermediate 或 alpha_candidate：分别进入独立 Daily Curator 申请或候选 Factor 注册及下游评价。

**审批职责分离**：Research Agent 只产候选，不自行宣称已成为 Daily 或成功 Alpha。Daily 独立相关性严格 <0.6；Alpha 经技术/泄漏、统计(<0.65 对 KN 已成功者)与金融(Ret>3%、SR>1)评价后进同一 Knowledge。Score仅在需要时后算。统计计算方法仍参照待定文件，不可擅自当已通过。

若只得到所有股票同样的单个市场状态值，应进一步产生股票间有差异的暴露/响应，才能构成当前横截面 Alpha。

参考：[主模块流程](../PROCESS_AND_MODULES.md) · [Knowledge/CSV合同](../KNOWLEDGE_AND_CSV_CONTRACT.md) · [未定事项](../OPEN_DECISIONS.md)。