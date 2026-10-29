# Research Role Scheduler｜可替换调度策略 V0

## 1. 输入和输出

**输入**（由总编排在本轮准备）：`run_id`、`campaign_id`、`role_manifest_version`、16份角色 Prompt 路径、`data_snapshot`、`daily_catalog_snapshot`、`knowledge_snapshot`、`tool_registry_version`、`generation_budget`、`seed`、`exposure_mode`、`mask_config`、`universe/time_cutoff`。预算、并发与所需信息必须由本地配置显式提供，不能在代码中猜默认值。

**输出**：按实际预算逐个生成 `EpisodePlan`：`episode_id, run_id, role_id, prompt_version, input_snapshot_refs, exposure_mode, exposure_view_id, episode_seed, limits, role_eligibility_result`；把完整独立 Prompt 加本轮动态输入交模型，取得一个 `alpha_candidate` 后移交 M4。

**不负责**：M1 Daily 产生、M2工具内部实现、M4/M8写库、M5/M6评估、M9父代选择；不创造额外“研究决策 LLM”。所有研究 Agent 的输出频率是每股每天一个 Alpha。

## 2. 角色合格性检查

从 `role_manifest.json` 读取16角色和唯一Prompt文件，不在调度代码硬编码行业岗位。调度前向 M0/M2 提供的**能力目录**核对该角色需要的输入类别与历史长度。仅检查**能否启动研究**，不预先决定哪种金融假设有效。

例如，历史行业标签未核实则 C04 的分组能力不满足；只有日度数据不能冒充有分钟价格；B/D 未拿到需要的历史长度不能以未来数据补齐。状态记录为 `eligible` 或 `not_ready(reason, missing_capabilities)`；属于**任务分派日志**，不生成 Factor/Experiment，也不算研究失败。能力目录及接口细节由 M0/M2 所属实现者提供。

## 3. 建议首版：覆盖优先的轮转

`coverage_round_robin_v0` 为**建议默认候选策略**，不是必须永久采用的权重法：

1. 基于一个配置版本加载 `enabled_roles`，按 M0/M2 能力目录过滤到 `eligible_roles`，保留未合格清单和原因。
2. 对未完成的有效角色轮次使用 `seed + campaign_id + round_index + role_manifest_version` 做**可复现洗牌**。一轮中每个合格角色有一次研究机会；不以某个角色的论文数量或历史收益作为先验优先级。
3. 从上次持久化的 `round_cursor` 继续依次调度；不足一轮的预算不重置队列，避免总是前几个角色先得到调用。调用失败的同一角色是否重试由独立运行故障策略决定，不能无限重试挤占其他角色。
4. 每个 Episode 只装载**对应的一份完整专业 Prompt**，读取本轮 M2 数据目录与权限受限的研究材料。生成一个 Alpha 候选交 M4；不得在此生成 Daily 入库申请。
5. 达到显式配置的 `max_episodes`、总 token/成本/时间预算之一即停止新的派发；已运行任务按照超时、取消或正常完成规则收尾。停止理由和游标持久化。
6. 每次轮次切换、角色能力变化或 Prompt 升级都要记录快照和配置版本。新角色或新版本不可悄悄接入旧实验轮次。

**角色数量与调用预算分离**：即使配置了 A6/C5/B3/D2，也不意味着每次需要运行全部16次。后续可引入固定组权重、基于实验结果的采样或自适应策略，但必须用新的 `selection_policy_version`，不能在首版偷偷按收益预筛选。

## 4. 运行状态、预算和并发

调度侧状态：`planned → dispatched → completed`，或者 `not_ready / timeout / tool_error / invalid_response / cancelled`。上述后四类是**调用/编排结果**，与已注册 Alpha 的 `technical_fail / statistical_fail / financial_fail` 完全不同。

- 每次派发有稳定 `episode_id` 和唯一 `dispatch_id`；同一次网络重试须用相同幂等键，防止一个模型答复被M4重复注册。
- 并发上限、每次生成 token/调用上限、总运行预算及重试上限来自运行配置，不在本文件拍板数字。
- 一个 episode 的 `data/daily/knowledge` 快照和 `exposure_view_id` 从派发到候选生成保持一致；M1在中途发布新Daily不能使本次Prompt使用时点不一致的混合版本。
- M2工具返回必须受相同的可见性策略约束。模型看见多少、实际查过哪些材料应分开记录：`available_visible_card_ids` 与 `queried_card_ids`。

## 5. 调度决策日志

最低字段：`run_id, campaign_id, episode_id, dispatch_id, role_id, role_strategy_version, prompt_version, selection_policy_version, round_index, round_cursor, seed, exposure_mode, exposure_view_id, data_snapshot, daily_snapshot, knowledge_snapshot, tool_registry_version, budget_limit, observed_usage, status, failure_reason, started_at, ended_at`。

调度日志由总编排/既有 M8 日志接口保存；不增设第五个科研数据仓库。下游成功/失败由 M4/M5/M6 记录，调度器不自行给 Alpha 贴 `qualified` 标签。

## 6. 首版验收

同一快照、seed 和配置，角色派发顺序可重现；连续两个不足16次预算的 run 能从游标继续；缺分组字段的 C04 不派发且留下原因；超时不产生虚假 Factor；并行调度不重复接收同一个候选；无论哪个角色都装载其唯一独立 Prompt。