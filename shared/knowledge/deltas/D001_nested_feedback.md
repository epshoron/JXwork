# D001｜嵌套反馈：内循环质量审查 + 外循环回测

**性质：架构背景机制，不作为 P001 创新 Delta；P002 未经审批的比较已撤回。**

- **首次入库**：P001（KB-first，数据库从空开始）
- **研究任务**：生成新 Alpha 因子代码并借助反馈反复改写。
- **机制**：Writer 生成 → Judge 检查并返回修正建议（内循环）；可执行候选 → Backtest 测量历史预测能力 → Reviewer 把评估反馈交给 Writer（外循环）。
- **更新对象**：主要是当前候选表达式/代码和下一轮生成提示，并非已证实更新 LLM 参数。
- **P001 依据**：[期刊摘要](https://www.sciencedirect.com/science/article/pii/S2666827026001520)、[官方实现说明](https://github.com/VMSSON345/Self-Improving-Alpha-Mining-for-Quantitative-Trading-via-Multi-Agent-Large-Language-Models-with-Know)。
- **学术首创性判断**：**已有**。[QuantAgent (2024)](https://arxiv.org/abs/2402.03755) §3 描述同样的内外两层循环与 Writer/Judge/环境反馈。P001 不能据此声称首创双循环；两篇的实现细节仍需原文细比。
- **局限/开放问题**：回测反馈重复筛选的过拟合风险；成本/试验次数；不同模型与环境泛化能力，均需实证对照。
- **未来比较字段**：Judge 的判断依据是什么？反馈影响候选、提示、种群、知识库还是搜索策略？内外层谁控制退出规则？ 
- **后续论文记录**：待新增（每次需标“已有/变体/新机制/待核”及原文位置）。
