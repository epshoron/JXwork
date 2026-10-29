# shared｜只面向云端的可引用研究资源

**这是知识和设计说明，不是公司云端 Agent 的行为指令。** 每个论文条目保留原文、核验边界和作者实验状态；不得把外部论文结果视为本系统已执行的实验。此目录不包含公司行情数据或已部署的系统。

| 方向 | 路径 | 使用对象 |
|---|---|---|
| **A：AI 因子挖掘** | [A_alpha_mining/](A_alpha_mining/README.md) | P 系列论文、D 机制卡、跨论文综合；参考 Research Loop 搜索方法 |
| **B：AI 优化 AI** | [B_ai_trains_ai/](B_ai_trains_ai/README.md) | T 系列论文、TD 机制、上层 Agent 改进研究；供未来 Meta Loop |
| **C：分钟到 Daily** | [C_intraday_to_daily/](C_intraday_to_daily/README.md) | C/CR 论文、金融现象、计算条件、字段限制；供 Daily 与 Research |
| **V1.0.1 已确认架构** | [architecture/V1.0.1/](architecture/V1.0.1/README.md) | 四库 + 两阶段检查 + Knowledge 统一记录 |
| **评价数学口径** | [evaluation/](evaluation/PORTFOLIO_SCORING_STANDARD.md) | VWAP/组合/Ret/SR/DD/TO；Score 仅按需计算 |

## 区分三类事实

- **研究档案**：论文机制、作者报告和研究者已核实的解读；不构成已完成复现。
- **已拍板设计**：Research Loop 模块、两阶段检查、成功硬门槛、所有尝试入 Knowledge；**不构成已部署系统**。
- **待补工程定义**：Alpha 第一关相关阈值；Daily 相关系数计算口径（但阈值严格小于 0.6）；具体数据切分、字段许可与物理数据库选型。未确认的实现细节不得当成默认值。

工作用 Agent 的论文认领、研究审批、更新日志在仓库其他目录 `assistant/`，不随这个资源目录单独打包。原始 PDF 的版权/再分发授权须逐项检查。
