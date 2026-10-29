# M3 Research 调度与 Full/Masked 输入控制｜实施规范 V0

本目录只负责 **16 个专业 Alpha Research Agent 的任务选择与输入可见性**。Agent 的 [16份独立 Prompt](../prompting/README.md) 已有第一版，此处不修改其研究内容；Daily Curator 为独立 M1，M2/M4/M8 属另一实施工作流，M5/M6 使用已确定的评价合同。

| 文件 | 职责 |
|---|---|
| [ROLE_SCHEDULER_SPEC_V0.md](ROLE_SCHEDULER_SPEC_V0.md) | 角色抽样、覆盖、预算、并发与恢复 |
| [MASKING_SPEC_V0.md](MASKING_SPEC_V0.md) | full/masked 的精确过滤域、分组、可复现抽样、越权防护 |
| [COMPARISON_AND_MEASUREMENT_V0.md](COMPARISON_AND_MEASUREMENT_V0.md) | 同条件实验和对照分析，避免将新胜者导致的资格变化误当成 Prompt 优劣 |
| [SCHEDULER_CONFIG_SCHEMA_V0.json](SCHEDULER_CONFIG_SCHEMA_V0.json) | 运行时配置的类型和必要字段；不代表某个超参数已被拍板 |

**设计状态**：流程和隔离边界沿用已确定的 [Research 输入协议](../../RESEARCH_INPUT_PROTOCOL_V1.md)；选择顺序、预算、遮蔽概率均是**可替换策略/实验配置**，以下算法是供公司开发 Agent 实现与验证的**建议首版**，不是已测最优。不能将本目录视为已部署代码。

**运行边界**：此模块向运行时提供 role_id、Prompt 路径、权限受限的研究视图、run/episode 标识及记录；只接收结构化 `alpha_candidate`，交 M4 注册。超时/无响应/格式错误记录为**调用故障**，而不是一个 Alpha 候选或金融失败。