# Research Alpha Prompt 加载与交付

1. 从 [ALPHA_PROMPT_MANIFEST_V1.json](ALPHA_PROMPT_MANIFEST_V1.json) 选择一个角色，加载其对应的 `roles/Rxx.md` **完整独立Prompt**。
2. 根据 [ALPHA_EPISODE_INPUT_V1.md](ALPHA_EPISODE_INPUT_V1.md) 注入本轮数据目录、真实可用工具、授权知识视图和运行配置。
3. Agent自主从M2获取材料、研究本专业问题，返回符合 [ALPHA_OUTPUT_SCHEMA_V1.json](ALPHA_OUTPUT_SCHEMA_V1.json) 的单个 Alpha 候选。
4. 调度器把候选交至 M4 Candidate Register；M4注册并留痕，M5A/M5B/M6执行独立评价。

角色研究范围、工具能力及提交对象都有稳定独立入口。提示词只表达研究任务，不承载 Daily Curator、统计关卡或金融评价器内部实现。
