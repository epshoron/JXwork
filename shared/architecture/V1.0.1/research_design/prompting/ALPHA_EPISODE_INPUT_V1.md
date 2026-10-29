# 每轮 Alpha 研究动态输入 V1｜供离线调度器填充

> 本文件是每轮输入模板，**不属于 Research Agent 独立专业 Prompt 的内容**。每次只加载本轮角色对应的一份 roles/Rxx.md 作为专业指示；下列材料按数据权限和 full/masked 规则动态提供。

研究目标：由当前角色独立生成可执行的日频横截面 **Alpha候选**，若无法生成可靠候选则返回 no_candidate。不要生成、申请或批准 Daily 中间特征。

- run_id: {{run_id}}
- role_id: {{role_id}}
- role_strategy_version: {{role_strategy_version}}
- prompt_version: {{prompt_version}}
- data_snapshot: {{data_snapshot}}
- authorized_data_schema_and_fields: {{authorized_data_schema_and_fields}}
- information_cutoff_and_trade_calendar: {{information_cutoff_and_trade_calendar}}
- valid_universe_and_historical_classification: {{valid_universe_and_historical_classification}}
- missing_or_unconfirmed_fields: {{missing_or_unconfirmed_fields}}
- permitted_min_query_tools: {{permitted_min_query_tools}}
- published_daily_feature_catalog: {{published_daily_feature_catalog}}
- permitted_daily_read_tools: {{permitted_daily_read_tools}}
- visible_research_materials: {{visible_research_materials}}
- visible_knowledge_records: {{visible_knowledge_records}}
- knowledge_visibility_mode: {{knowledge_visibility_mode}}
- allowed_history_window: {{allowed_history_window}}
- generation_budget: {{generation_budget}}
- seed: {{seed}}
- supplementary_constraints: {{supplementary_constraints}}

生成后用 [Alpha-only JSON Schema](ALPHA_OUTPUT_SCHEMA_V1.json) 提交一个对象；真实技术/统计/金融检查及持久化由外部模块完成。

**权限提醒**：模型不得拥有未来收益原始标签读取权限；masked不仅遮蔽最初展示，也要约束后续知识查询，且不能遮蔽字段存在性、安全时点与已发布Daily定义。
