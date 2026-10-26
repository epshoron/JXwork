# P008｜AlphaAgentEvo：原文与证据边界

- **题名**：AlphaAgentEvo: Evolution-Oriented Alpha Mining via Self-Evolving Agentic Reinforcement Learning
- **正式发表**：ICLR 2026 Conference；研究者作者 Ziyi Tang, Xuexiong Yin, Weixing Chen, Zechuan Chen, Yongsen Zheng, Wenxuan Ye, Keze Wang, Liang Lin。
- **正式题录/摘要**：[ICLR 2026 官方论文页](https://proceedings.iclr.cc/paper_files/paper/2026/hash/741aab8b41a2987867acc9939ad50383-Abstract-Conference.html)；[ML Anthology 题录](https://mlanthology.org/iclr/2026/tang2026iclr-alphaagentevo/)。
- **原始论文讨论/全文入口**：[本仓库私有归档 PDF](AlphaAgentEvo_ICLR2026.pdf) · [ICLR 官方 PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/741aab8b41a2987867acc9939ad50383-Paper-Conference.pdf) · [OpenReview 论文论坛](https://openreview.net/forum?id=lNmZrawUMu)。[PDF 来源及校验记录](P008_PDF_SOURCE.md)。
- **本项目研究范围**：**自动因子进化**：从种子 Alpha 开始，让 RL 训练的 LLM 通过多轮生成、调用因子评价工具、观察反馈、反思再生成，学习更有效的因子探索策略。**不是重新设计股票收益预测模型**。
- **已存在的前作线索**：[P003 同团队 AlphaAgent（KDD 2025）](../P003/README.md)，[P005 AlphaPilot（2026 预印本）](../P005/README.md)，[P007 AlphaRLM（2026 预印本）](../P007/README.md)。

## 本轮核验状态（2026-10-21）

- **已直接核对**：ICLR 2026 正式题录和摘要描述的多轮交互、分层奖励、长期规划/反思与 4B 模型实验主张。
- **待进一步直接核对**：PDF 方法中的具体多轮 GRPO 优化目标、奖励各项精确公式、相关实验表和附录。2026-10-26 已从 ICLR 官方 PDF 地址下载全文并校验 PDF 格式、论文标题与作者，已入本仓库私有目录；**存档和前两页身份检查不等于已经逐节核对方法公式、图表和附录**，此部分仍待进一步研读。OpenReview 原入口在部分访问环境会触发验证。
- **用户审批结果**：本篇已存核实过的原文入口与客观骨架；用户于 2026-10-21 明确认可两项**项目级特色设计**：[D014｜种子因子连续进化](../../knowledge/deltas/D014_seed_conditioned_evolution.md) 和 [D015｜五目标分层奖励](../../knowledge/deltas/D015_hierarchical_evolution_reward.md)。**另有两项已批准、分别对应创新①和②的评价不足**：[Pass@T 成功判定与五维奖励消融两项逐一对应的研究问题](IDEAS.md)。均不是实证发现方法失效，学术首创性及完整 PDF 原始公式/消融仍待核验。
- **存储边界**：仓库当前为 Private，全文只作私有研究存档；不因允许下载而擅自向公开仓库再分发，也不存放公司内容或账号凭据。
