# V1.0.1 总编排｜可替换运行控制规范 V0

**本目录只规定“谁调用谁、何时交付、怎样记录和恢复”。** 不重复设计由其他会话实现的 M0 数据接口、M1 Daily Curator、M2 数据读取、M4/M8 写库或已经确定口径的 M5/M6 Evaluator。M9 遗传策略保留接口位置，**暂不实施/不启用**，等待老师反馈。

| 文件 | 内容 |
|---|---|
| [OVERALL_ORCHESTRATOR_V0.md](OVERALL_ORCHESTRATOR_V0.md) | 运行顺序、阶段状态、快照、并发和故障恢复 |
| [MODULE_HANDOFF_CONTRACT_V0.md](MODULE_HANDOFF_CONTRACT_V0.md) | 与 S16/S17 所属模块对接时需要确认的最小调用合同 |
| [INTEGRATION_TESTS_V0.md](INTEGRATION_TESTS_V0.md) | 合成数据下的端到端验收和隔离边界 |

Research Scheduler 与 Masking 单独定义于 [research_design/scheduling](../research_design/scheduling/README.md)。独立 Alpha Prompt 定义于 [research_design/prompting](../research_design/prompting/README.md)。

**状态区别**：本目录是工程实现规格草案，不是服务代码/云端部署报告；`selection_policy`、mask概率、并发上限和预算参数都允许独立配置。不得因为缺少 M2 真实函数名而臆造已可直接运行的 API。