# V1.0.1｜Knowledge 记录与 CSV 输出契约

> **2026-10-29 已确认的逻辑契约**，用于云端落地的接口设计；不代表 GitHub 已包含真实行情 CSV、Alpha 实验文件或已部署数据库。物理 DB 和目录绝对路径由公司环境决定。

## 1. 一个 Knowledge，两个基本记录对象

**Factor（定义）**：`factor_id, name, formula_or_code_ref, code_hash, parameters, required_data, time_info, source_refs, parent_factor_ids, created_by, created_at, expression_version`。可与作者提出的 Factor 建立引用，但不得把作者实验当成内部结果。

**Experiment（一次真实尝试）**：`experiment_id, factor_id, run_id, data_version, data_snapshot, sample_start, sample_end, eval_version, gate_version, model_version, seed, exposure_mode, created_at, stage, status, failure_code, failure_reason, stage1_metrics, ret_ann_gross, sr_gross, mdd_gross, to_daily_mean, to_ann, cost_ann, qualified, factor_csv_path, daily_metrics_csv_path, weights_csv_path, execution_log_ref, parent_experiment_id`。

- **角色生成来源建议字段**：`role_id, role_strategy_version, primary_domain, secondary_domains, research_question` 及有效材料引用。当前参考 [16角色策略 V0.2](research_design/README.md)；这是候选实验的来源追踪信息，**不是修改成功硬门槛**，每次策略版本升级必须保留可比较的历史记录。
- **一个 Factor 可对应多个 Experiment**：重跑/更改数据窗口或版本必须生成新的 `experiment_id`，不能覆盖成功/失败历史。
- `status` 可以为 `pending`、`blocked`、`technical_fail`、`statistical_fail`（含 `redundant` 原因）、`evaluation_error`、`financial_fail`、`qualified`。`qualified` 建议为三态：`true`（正式成功）、`false`（有效金融评价但未达标）、`null`（未跑完金融评价），而不是把未执行算作失败收益。
- `stage1_metrics` 保存技术/泄漏及统计结果；Alpha 相关性须记录 `winner_reference_ids`（或引用集合快照）、`winner_count`、`max_abs_corr`、`closest_winner_factor_id`、`correlation_status`（`NO_REFERENCE/PASS/FAIL/BLOCKED`）、计算方法/样本/门槛版本。空胜者集合时 `max_abs_corr=NULL`，只跳过相关性检查，不能把 NULL 当成零。当前 Alpha 最大绝对相关严格 `<0.65`，算法和样本细节仍待冻结。
- `ret_ann_gross/sr_gross/mdd_gross/to_daily_mean/to_ann/cost_ann` 为已计算的、可复算的**金融指标字段**；无 Evaluator 则为 NULL。收益、MDD 用小数比例，Sharpe 无量纲；`to_daily_mean` 是日均双边权重差换手，`to_ann=252*to_daily_mean`，`cost_ann=0.001*to_ann`（V1 假设）。
- `score` **非必存字段**；需要时从金融原始字段按评分版本生成。若缓存 Score，应同时保存 `score_version` 且不能让它决定 `qualified`。

**Related / Relation**：以 `source_refs`、`parent_factor_ids`、`experiment_id` 关联论文、作者结论、金融假设、Alpha 代码、重试与遗传谱系。任何 `external_reported` 类型的作者实验与本项目 `internal_executed` 结果必须有不同身份字段。

## 2. 逻辑视图，而非新建 Alpha 库

- `all_experiments`：所有生成候选与每次状态、阻断和评测结果。
- `qualified_alpha`：`status='qualified' AND qualified=true` 的 Experiment 连接 Factor 元数据和 CSV 路径；**达标即正式存档**。其中实际内部验证的成功 Alpha 是以后候选统计相关性的参照集合，失败候选和仅作者报告的因子不纳入。
- `technical_or_blocked`：第一关失败或未完成的实验（无金融字段）。
- `financial_failures`：完整有效评测但低于 Ret/SR 门槛的实验（包含实际金融指标）。

`qualified` 是**实验级**字段；某个 Factor 的“当前有效资格”只应按指定样本和评价版本查询，不应脱离版本永久写成常量布尔值。

## 3. CSV 的推荐最小结构（仅 Schema 示例，不是真实数据）

**Daily 的数值 CSV**：`trade_date, instrument, feature_id, value, data_version`；另在目录/元数据登记 `feature_id, code_hash, dependencies, window, first_usable_at, materialization_status, csv_path, correlation_metric, correlation_value, correlation_reference, correlation_version`。

**Alpha 的因子值 CSV**：`trade_date, instrument, factor_id, factor_value, data_version`，在公司环境存真实数值。只要存因子公式还不够，需有可追溯实际数值文件路径。

**Experiment 摘要 CSV**：`experiment_id, factor_id, data_version, gate_version, eval_version, status, stage1_status, qualified, ret_ann_gross, sr_gross, mdd_gross, to_daily_mean, to_ann, cost_ann, factor_csv_path`；第一关失败后金融指标为空值。CSV 可是数据库导出，而非第五个数据库。

**金融日级 CSV（供核算）**：`experiment_id, trade_date, gross_return, turnover, cost`；逐股票仓位单独保存 `experiment_id, trade_date, instrument, target_weight`，与 [Evaluator 数学口径](../../evaluation/PORTFOLIO_SCORING_STANDARD.md) 兼容。

## 4. 完整性与版本约束

- 所有成功、金融失败、技术失败和阻断实验**都记录**；写入必须能区分 `not_run`、`NULL`、真实数值零与计算异常。
- 早期材料来源的作者收益或 IC 只能记 `external_reported`，**不得填进内部 Experiment 的 `ret_ann_gross`**。
- CSV 数据要有 `factor_id/feature_id/experiment_id` 关联，至少 `data_version, code_hash, gate_version, eval_version, sample_range` 可复现。不要在 GitHub 上存公司真实 CSV 和访问凭据。
- 规则更新时保留旧实验、旧标记与版本；需要跨版本比较时按同一版规则重算标签，不能用旧版 `qualified` 冒充新版结果。
