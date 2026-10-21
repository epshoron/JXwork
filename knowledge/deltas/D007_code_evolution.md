# D007｜LLM Python 代码级因子进化 + 种群优胜劣汰

- **首次入项目知识库**：P002 · CogAlpha（**KB-first，不等于学术首次提出**）。
- **研究任务**：从合格候选继续探索新的因子，而不是每轮从零生成或局限于固定公式语法。
- **输入**：已筛选的因子 Python 代码与金融说明、父代/精英池及客观评价结果。
- **核心机制**：LLM 执行 **Mutation（单候选修改）**、**Crossover（两候选融合）** 或 **Crossover + Mutation**；新子代再次接受质量检查与 IC/ICIR/RankIC/RankICIR/MI 等打分，经过父代筛选和精英保留进入下一轮。
- **真正被更新的对象**：候选 Python **代码**、种群/亲本选择、后续生成 Prompt；**不是 LLM 权重或自我重训练**。CogAlpha 的 Adaptive Generation 会抽取成败示例反馈，参见 [D001 的 P002 变体](D001_nested_feedback.md)。
- **P002 原文证据**：[§3.4 Fitness、§3.5 Adaptive Generation、§3.6 Thinking Evolution](https://arxiv.org/html/2511.18850#S3)，[Appendix B.4 / B.7](https://arxiv.org/html/2511.18850#A2)。
- **相对 P001 的项目增量**：P001 重点在 Writer 生成、Judge/Backtest 反馈及 Main KB 保存有效结果；P002 显式引入**父代种群选择＋代码级变异/交叉＋精英继承**。这不是把 D001 相同的“有反馈”重新包装，而是**候选状态与搜索算子层面的不同控制机制**。
- **学术先例**：遗传算法的 mutation/crossover 是传统算子，CogAlpha §2 引用 **FunSearch（2024）**、**AlphaEvolve（2025）** 等既有 LLM 进化代码搜索；**不能宣称 P002 发明了 LLM 演化编程**。可讨论的是其在金融因子任务上的具体设计和验证。
- **作者的消融证据**：仅加 Thinking Evolution 时部分预测指标（如 IC）可下降，但随 A/G/H 累积加入，整体回测指标改善；单次挖掘实验不能证明稳定统计增益。
- **潜在风险**：反复尝试的选择偏差、进化代码的可用时点、表达式/因子同质化、推理成本、单次 LLM 运行随机性；均需针对性实验，不预设一定已经出现问题。
- **未来比较字段**：公式级还是代码级；可变异对象；选择/精英机制；反馈影响提示或搜索策略；预算与独立 OOS 质量。
- **机制关系**：[D001](D001_nested_feedback.md) 描述反馈循环，本卡描述**进化搜索操作与种群控制**，二者交叉但不应合并。
