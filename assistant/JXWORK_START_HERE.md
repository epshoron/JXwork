# JXwork｜研究 LLM 接手入口（2026-11-12）

仅对 ChatGPT / 文献研究维护 Agent 有效；**不是**公司云端 Alpha 执行 Agent 的系统指令。

## 最新进度在哪里（先核对来源，勿混用版本）

- **公开研究设计**：本仓库 `shared/architecture/V1.0.1/` 为 2026-10-29 已确认的设计基线，保留原貌供历史对照；它不是公司端 2026-11-12 的实际运行规范。
- **私有执行进度**：用户于 2026-11-12 提供一份公司 Agent 撰写的私有报告，文件名 **`EP001_FINAL_REPORT.md`**，所在位置为用户授权连接的 **Gmail**，可按 `filename:EP001_FINAL_REPORT.md after:2026/11/11` 搜索（邮件可能无主题）。报告描述公司端 **V1.0.2** 与首轮 **EP001** 的 dev/smoke 运行状态。它是当时的执行状态证据，但不能代替独立代码审计或此后最新状态核验。
- **接手动作**：若任务涉及公司端现状、执行顺序、门槛或已运行结果，先经用户授权只读该原始报告，再与仓库 V1.0.1 对照，明确标注“私有执行版本事实”和“公开历史设计”各自出处；不要把两版数值、对象或流程拼接成同一规范。附件可能以 `application/octet-stream` 识别为文本 `.md`，必要时在授权 Gmail 内按原始 MIME 读取；读不到就声明尚未核实。
- **安全边界**：JXwork 为 **Public**。本导航只保存报告定位信息和版本关系；不得将私有报告正文、公司内部路径、代码、配置、数据、实验指标、策略或邮件内容复制到本仓库或外部不获授权的系统。任何公司端规范变更应在授权环境核对并由研究者确认，不通过修改本公开历史设计来冒充执行系统已更新。


1. [AGENTS.md](AGENTS.md) 和 [研究写作规范](RESEARCH_WRITING_STANDARD.md)、[研究计划](RESEARCH_PLAN.md)。
2. A：[P 论文索引](../shared/A_alpha_mining/papers/INDEX.md)、[D 机制索引](../shared/A_alpha_mining/knowledge/DELTA_INDEX.md)。
3. B：[T 论文索引](../shared/B_ai_trains_ai/papers/INDEX.md)、[TD 机制索引](../shared/B_ai_trains_ai/knowledge/DELTA_INDEX.md)。
4. C：[C 论文索引](../shared/C_intraday_to_daily/papers/INDEX.md)、[CR 研报索引](../shared/C_intraday_to_daily/reports/INDEX.md)。
5. [V1.0.1 公开设计基线](../shared/architecture/V1.0.1/README.md)、[门槛](../shared/architecture/V1.0.1/GATES_AND_DECISIONS.md)、[字段与 CSV](../shared/architecture/V1.0.1/KNOWLEDGE_AND_CSV_CONTRACT.md)。
6. [CHANGELOG.md](CHANGELOG.md) 与 [原始研究协作说明](research_guides/)。

2026-10-29 公开设计基线：不增加 Alpha 库；技术/统计第一关之后才计算金融字段，所有实验与失败都进 Knowledge；Ret>3% 且 SR>1 即成功；Score 只按需。原始 A/B/C 研究审批、论文编号及证据纪律继续沿用，不把论文作者声称当成真实回测。
