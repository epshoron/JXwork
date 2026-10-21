# D015｜P008：五目标分层奖励训练连续 Alpha 进化

**审批状态（2026-10-21）**：研究者认可**五项奖励的结构化组合与目标制衡**是有价值的训练设计贡献；**“目标有张力”是设计目的，不按缺点登记**。没有批准另加的特化风险。

- **输入**：以种子 Alpha 为锚展开的整条多轮因子进化轨迹；包含工具调用、候选结构、历史改进与市场性能。
- **具体奖励**：**Tool Call** 管理合法/失败操作与使用效率；**Consistency** 保留与种子的关联；**Exploration** 鼓励不同于已试候选的探索；**Performance** 奖励预测表现改善；**Streak** 额外鼓励**连续多轮进步**。
- **真正的干预位置**：这些指标汇总为**分层的轨迹奖励**，训练 Agentic RL 因子进化策略的参数；不是生成后再排序几个独立因子的常规 IC 评价，也不是“五项基础指标都由本论文首创”。原文包含截断与非简单求和组合，旨在平衡效率、方向、创新和长期收益。
- **为什么目标张力是设计价值**：Consistency 过强可能只局部修改，Exploration 过强可能偏离种子，Performance 只看一次高分可能忽略持续改善；多目标设计试图提供互补的学习信号。**有冲突不等于论文已暴露缺陷。**
- **严格语义去重**：
  - [P005 AlphaPilot](../../papers/P005/README.md)：同样用多轮 RL，但基于**最终因子池的 IC/RankIC 轨迹奖励**；此卡奖赏**种子保持、尝试差异、表现改善和连续进步**，不是同一个训练信号。
  - [D013/P007](D013_tmb_rl_factor_policy.md)：对**单个公式有效性和分组收益差**进行策略训练；本卡评估**从种子生成连续后代的一条轨迹的行为品质**。
  - [D008/P003](D008_ast_originality_penalty.md)：相似结构惩罚发生在候选**生成审核**；本卡把与种子/前序尝试的相关性放进**轨迹策略训练奖励**，操作对象/更新层级不同。
  - [D010/P004](D010_mcts_multidimensional_search.md)：回传**搜索树节点价值**，不是梯度训练 LLM 进化策略。
  - **结论：独立机制卡**，而不为五项奖励各建一张重复卡。
- **实验证据**：公开 PDF 摘录/转录报告 AlphaEvo500 **Pass@3 0.65（全部奖励）／0.54（去 Exploration）／0.51（去 Consistency）**；说明二者在作者实验中互补。**不能据此认定 Tool/Performance/Streak 每项已被单独消融、也不能将 Pass@3 当作投资回测年化收益。**
- **证据局限**：ICLR 2026 [正式摘要](https://mlanthology.org/iclr/2026/tang2026iclr-alphaagentevo/)核实分层奖励总体机制；[OpenReview PDF](https://openreview.net/pdf?id=lNmZrawUMu)当前有浏览器验证，具体公式与消融请以后直接逐页复核，现据[公开方法与表格细读](https://m0rtzz.github.io/paper-notes/ICLR2026/llm_agent/alphaagentevo_evolution-oriented_alpha_mining_via_self-evolving_agentic_reinforc/)记录。审批不等于证据质量自动升级。
- **原文与单篇定位**：[P008 评价](../../papers/P008/ARCHITECTURE.md)、[原文](https://openreview.net/forum?id=lNmZrawUMu)。
