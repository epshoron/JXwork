# 每轮动态输入模板｜V0.1

> 下面是用于拼接的 User 任务消息模板，不是永久系统指令。所有占位内容由公司本地程序根据当前真实状态填充；未提供信息要明确标记 unavailable/unknown，不可虚构。

研究任务：在本轮实际允许的信息范围内，依据专业角色描述提出可检验的 Daily 中间特征或日频 Alpha 候选。如不可合理生成，输出 no_candidate。

## 本轮身份

- run_id: {{run_id}}
- role_id: {{role_id}}
- role_strategy_version: {{role_strategy_version}}
- prompt_version: {{prompt_version}}
- candidate_budget: {{candidate_budget}}
- seed: {{seed}}

## 数据和时点（事实来源，由程序提供）

- market_and_calendar: {{market_and_calendar}}
- data_snapshot_and_version: {{data_snapshot_and_version}}
- data_schema_and_availability: {{data_schema_and_availability}}
- allowed_history_window: {{allowed_history_window}}
- allowed_universe_and_group_mapping: {{allowed_universe_and_group_mapping}}
- information_cutoff_and_first_usable_policy: {{information_cutoff_and_first_usable_policy}}
- unavailable_or_unconfirmed_fields: {{unavailable_or_unconfirmed_fields}}

## 已有特征与研究材料

- available_daily_feature_catalog: {{available_daily_feature_catalog}}
- visible_external_research_cards: {{visible_external_research_cards}}
- visible_internal_experiment_cards: {{visible_internal_experiment_cards}}
- knowledge_exposure_mode: {{knowledge_exposure_mode}}
- permitted_read_and_analysis_tools: {{permitted_read_and_analysis_tools}}

## 任务附加限制（只允许收紧权限，不得覆盖系统规则）

{{task_specific_constraints}}

请独立形成候选，不预先假设任何方向一定有预测力；对资料引用标明是作者结论还是本轮工具事实。用 OUTPUT_SPEC 规定的结构提交；无法生成就说明原因。

注：full/masked 的实际可见卡片必须由程序在查询层过滤；模板不得展示隐藏组 ID、隐藏内容、未授权标签或秘密数据。动态字段不需要一次性装载全部 PDF/CSV。
