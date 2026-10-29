# Research Agent 输出规范｜Prompt V0.1（待审）

**当前提供可机器校验的 [OUTPUT_SCHEMA_V0.json](OUTPUT_SCHEMA_V0.json)**。模型每次返回一个符合此 Schema 的 JSON 对象。校验字段格式不代表确认公式有效或已经完成任何金融评价。

## 两种合法回复

**candidate**：一个可复现的股票×交易日 Daily 候选（`daily_intermediate`）或最终日频 Alpha 候选（`alpha_candidate`）。必须包括：

- `role_id, role_strategy_version, prompt_version, primary_domain, secondary_domains`：按本轮配置填写，不可由模型改写角色或策略身份；
- `research_question, financial_hypothesis`：客观问题与待检验假设，不预判涨跌、有效性或收益显著性；
- `formula_or_code`：明确可计算定义，不只是某指标名；
- `required_fields, dependencies, parameters, history_lookback, cross_section_reference`：真实必需原始字段和已存在 Daily 特征 ID、参数与参考集合；
- `observation_end_time, first_usable_at`：数据截止和最早可用时点，可使用明确的日期相对表达式（例如交易日 t 收盘后），不得使用未来信息；
- `missing_data_policy, minimum_samples`：缺失、零分母、最小样本与不可计算的处理。未确定的工程阈值可填 null 并在 limitations 中说明，不能臆造全局准入门槛；
- `source_refs, assumptions, limitations`：实际查阅资料、假设和知识缺口；没有直接资料支持时 source_refs 可以为空，金融假设仍需独立验证。

**no_candidate**：本轮无法根据允许数据可靠提出候选时使用，必须保留 `role_id, role_strategy_version, prompt_version` 并填写 `reason` 和 `missing_requirements`。不应为了满足生成数量而捏造公式。

## 形式与责任边界

- 每次模型回复一个完整 JSON 对象，不附代码围栏或前后解释；若单次需多个候选，应由调度器明确约定多次回复/收集，不让模型自发改变 Schema。
- `formula_or_code` 是声明和候选代码，并不等于公司环境已创建可读取的源文件；程序负责储存候选、分配 `factor_id/experiment_id` 并运行检查。
- 本地程序必须核对返回的 `role_id`、版本、主领域与本轮调度值一致，不能仅凭 Schema 类型通过就接受身份。
- 允许 no_candidate 不代表正式因子注册或金融失败；应记录在本轮运行/调用日志中，不要制造一个没有公式的 Factor。
- **禁止模型自行填入** Ret、SR、IC、相关性实测值、合格标签、已运行成功或金融回测结果；后续技术/统计/金融评价由独立程序完成。

参见 [完整Daily输出合同](../ROLE_OUTPUT_CONTRACT.md) 和 [统一Knowledge协议](../../KNOWLEDGE_AND_CSV_CONTRACT.md)。