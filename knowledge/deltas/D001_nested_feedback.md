# D001｜嵌套反馈：内循环质量审查 + 外循环回测

**性质：架构背景机制，不作为 P001 创新 Delta；卡内 P002 机制变体仍为待审候选。**

- **首次入库**：P001（KB-first，数据库从空开始）
- **研究任务**：生成新 Alpha 因子代码并借助反馈反复改写。
- **机制**：Writer 生成 → Judge 检查并返回修正建议（内循环）；可执行候选 → Backtest 测量历史预测能力 → Reviewer 把评估反馈交给 Writer（外循环）。
- **更新对象**：主要是当前候选表达式/代码和下一轮生成提示，并非已证实更新 LLM 参数。
- **P001 依据**：[期刊摘要](https://www.sciencedirect.com/science/article/pii/S2666827026001520)、[官方实现说明](https://github.com/VMSSON345/Self-Improving-Alpha-Mining-for-Quantitative-Trading-via-Multi-Agent-Large-Language-Models-with-Know)。
- **学术首创性判断**：**已有**。[QuantAgent (2024)](https://arxiv.org/abs/2402.03755) §3 描述同样的内外两层循环与 Writer/Judge/环境反馈。P001 不能据此声称首创双循环；两篇的实现细节仍需原文细比。
- **局限/开放问题**：回测反馈重复筛选的过拟合风险；成本/试验次数；不同模型与环境泛化能力，均需实证对照。
- **未来比较字段**：Judge 的判断依据是什么？反馈影响候选、提示、种群、知识库还是搜索策略？内外层谁控制退出规则？ 
- **后续论文记录**：待新增（每次需标“已有/变体/新机制/待核”及原文位置）。


## P002 · CogAlpha：反馈控制的一个变体（2026-10-21）

- **判定：变体，不新开“反馈闭环”卡**。CogAlpha 的代码质量检验和五指标选择构成筛选流程；Thinking Evolution 的子代重新评估，Adaptive Generation 从合格/失败候选及其评价中抽取案例进入下一轮 Prompt。
- **相对 P001**：P001 主要 Writer↔Judge 修复、Backtest/Reviewer 的外层反馈与长期 Main KB；P002 采用**种群选择 + 代码进化 + in-context 正反案例反馈**，没有证据证明其形成与 P001 Main KB 同等的跨任务持久检索。
- **更新层级**：候选代码、亲本池和提示上下文；**都不构成 LLM 参数级 RSI**。
- **原文**：[P002 §3.3–3.6](https://arxiv.org/html/2511.18850#S3)，[P002 档案](../../papers/P002/ARCHITECTURE.md)；进化机制单独见 [D007](D007_code_evolution.md)。
