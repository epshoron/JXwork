# P008｜AlphaAgentEvo：原文与证据边界

- **题名**：AlphaAgentEvo: Evolution-Oriented Alpha Mining via Self-Evolving Agentic Reinforcement Learning
- **正式发表**：ICLR 2026 Conference；研究者作者 Ziyi Tang, Xuexiong Yin, Weixing Chen, Zechuan Chen, Yongsen Zheng, Wenxuan Ye, Keze Wang, Liang Lin。
- **正式题录/摘要**：[ML Anthology｜ICLR 2026](https://mlanthology.org/iclr/2026/tang2026iclr-alphaagentevo/)；[ICLR 官网论文搜索](https://proceedings.iclr.cc/papers/search?q=AlphaAgentEvo)。
- **原始论文讨论/全文入口**：[OpenReview 论文论坛](https://openreview.net/forum?id=lNmZrawUMu) · [论文 PDF](https://openreview.net/pdf?id=lNmZrawUMu)。
- **本项目研究范围**：**自动因子进化**：从种子 Alpha 开始，让 RL 训练的 LLM 通过多轮生成、调用因子评价工具、观察反馈、反思再生成，学习更有效的因子探索策略。**不是重新设计股票收益预测模型**。
- **已存在的前作线索**：[P003 同团队 AlphaAgent（KDD 2025）](../P003/README.md)，[P005 AlphaPilot（2026 预印本）](../P005/README.md)，[P007 AlphaRLM（2026 预印本）](../P007/README.md)。

## 本轮核验状态（2026-10-21）

- **已直接核对**：ICLR 2026 正式题录和摘要描述的多轮交互、分层奖励、长期规划/反思与 4B 模型实验主张。
- **待进一步直接核对**：OpenReview PDF 方法中的具体多轮 GRPO 优化目标、奖励各项精确公式、相关实验表和附录。OpenReview 当前向本工具显示浏览器验证，不能把其他公开解读当成已亲自逐页核验的原文；本篇架构图仅按可核查摘要/公开方法说明画高层逻辑。
- **用户审批结果**：本篇已有客观架构、权威入口和用户认可的两项具体机制；创新、相对 P003/P005/P007 的学术增量、特化不足及知识 Delta **未经研究者批准，一律不转正、不创建知识卡**。
- **公共仓库边界**：不转存未经确认许可可公开再分发的 PDF，也不上传公司内容或账号凭据。
