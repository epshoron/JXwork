# 每轮研究输入

调度程序为每个研究角色加载 `roles/{role_id}.md`，并向该角色提供以下当前运行内容。输入内容由公司环境获取，不包含静态预设的因子公式或盈利结论。

```text
role_id: {{role_id}}
tool_registry: {{tool_registry}}
data_snapshot: {{data_snapshot}}
knowledge_snapshot: {{knowledge_snapshot}}
universe: {{universe}}
information_cutoff: {{information_cutoff}}
available_raw_fields_and_timing: {{available_raw_fields_and_timing}}
published_daily_catalog: {{published_daily_catalog}}
visible_knowledge_catalog: {{visible_knowledge_catalog}}
visible_paper_catalog: {{visible_paper_catalog}}
allowed_research_window: {{allowed_research_window}}
run_id: {{run_id}}
seed: {{seed}}
budget: {{budget}}
```

各专业Prompt按 `tool_registry` 中实际提供的权限调用M2读库和分析工具。`full/masked` 的知识可见性由运行程序过滤。候选输出依 [ALPHA_OUTPUT_SCHEMA_V1.json](ALPHA_OUTPUT_SCHEMA_V1.json) 由调度器提交至M4。
