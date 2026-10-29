# Research Alpha Prompt 加载与交付

1. 从 [ALPHA_PROMPT_MANIFEST_V1.json](ALPHA_PROMPT_MANIFEST_V1.json) 选择一个角色，加载其对应的 `roles/Rxx.md` **完整独立Prompt**。
2. 根据 [ALPHA_EPISODE_INPUT_V1.md](ALPHA_EPISODE_INPUT_V1.md) 注入本轮数据目录、真实可用工具、授权知识视图和运行配置。
3. Agent自主从M2获取材料、研究本专业问题，返回符合 [ALPHA_OUTPUT_SCHEMA_V1.json](ALPHA_OUTPUT_SCHEMA_V1.json) 的单个 Alpha 候选。
4. 调度器把候选交至 M4 Candidate Register；M4注册并留痕，M5A/M5B/M6执行独立评价。

角色研究范围、工具能力及提交对象都有稳定独立入口。提示词只表达研究任务，不承载 Daily Curator、统计关卡或金融评价器内部实现。

## 每次加载时必须注入的四库约束

- `tool_registry` 中 Min 只供字段/时点说明及可选历史 `sector_code/group_code`；分钟 C 数据的公式核验走授权后台计算器，不向 Agent 提供原始分钟 C 全表自由浏览。
- 注入可复现的 `research_mode=free/incremental/cross_domain`（各 1/3）及独立的 `exposure_mode=full/masked`；目录必须允许遍历全部授权论文，Agent 自己挑文献、一次重点精读一篇后可继续，不指定固定论文。
- 提供已发布 Daily Base/Curated、授权 Knowledge 和历史精读计数，记录真实阅读事件至极简 Episode；没有候选也留痕。M3 不代替 M1 审核 Daily。
- 若角色 Prompt 旧表述与以上权限冲突，统一遵守 [四库实施契约](../../FOUR_LIBRARY_RUNTIME_CONTRACT.md)。角色专业边界与 Alpha 输出结构不变。
