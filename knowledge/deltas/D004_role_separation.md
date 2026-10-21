# D004｜专职 Agent 分工与评价器隔离

**性质：通用 Agent 分工背景，不作为 P001 创新 Delta；卡内 P002 专项差异仍待研究者独立审阅。**

- **首次入库**：P001（KB-first）
- **机制**：WriterAgent 负责构造因子；JudgeAgent 负责逻辑/代码检查；BacktestEngine 提供数据驱动的性能检验；ReviewerAgent 消化指标，向下一轮生成反馈。职责分离有利于保持“生成建议”和“客观测量”的区别。
- **P001 依据**：[出版方摘要](https://www.sciencedirect.com/science/article/pii/S2666827026001520)、[作者架构说明](https://github.com/VMSSON345/Self-Improving-Alpha-Mining-for-Quantitative-Trading-via-Multi-Agent-Large-Language-Models-with-Know)。
- **学术首创性判断**：**不声称是新发明**。QuantAgent 2024 已描述 Writer/Judge 的 Agent 内循环及真实环境反馈；本论文的具体组件集合、审查方式与量化数据接入才值得做变体对照。
- **局限**：Judge 的主观金融评审是否可靠，是否有可重现的检验；多 Agent 成本是否被实际效益抵消，需要后续证据。
- **未来比较字段**：角色是否独立 LLM？代码判错/回测的确定性程度？自主规划还是预设流程？一对多 Agent 评价？
- **后续论文记录**：待新增。


## P002 · CogAlpha：角色分工变体（2026-10-21）

- **判定：D004 已有角色分工的具体变体**，不是“多 Agent”作为新机制再次建卡。
- **P001**：Writer / Judge / Reviewer / Backtest 等围绕生成、审查、复盘的职责分离。
- **P002**：21 个生成 Agent 按七大金融研究主题独立生成；此外 Code Quality、Code Repair、Judge、Logic Improvement 等进行不同类型审核；下游评分仍由指标规则执行。**不是训练 21 个有独立权重的 LLM，也不是必须相互辩论**。
- **细分新机制**：主题分工和五类 Guidance 的搜索先验性质见 [D006](D006_domain_guidance.md)，不与一般职责分离混写。
- **原文**：[P002 §3.1–3.3](https://arxiv.org/html/2511.18850#S3)，[P002 档案](../../papers/P002/ARCHITECTURE.md)。
