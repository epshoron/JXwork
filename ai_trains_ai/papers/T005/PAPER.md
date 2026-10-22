# T005｜Self-Rewarding Language Models：原文与核验边界

- **原始题名**：Self-Rewarding Language Models
- **作者**：Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Xian Li, Sainbayar Sukhbaatar, Jing Xu, Jason E. Weston
- **正式发表**：**ICML 2024**，*Proceedings of Machine Learning Research*，Vol. 235，pp. 57905–57923。
- **正式题录**：[PMLR 原文](https://proceedings.mlr.press/v235/yuan24d.html)
- **原始开放全文**：[arXiv HTML](https://arxiv.org/html/2401.10020) · [arXiv 记录](https://arxiv.org/abs/2401.10020)
- **研究归属**：B｜AI 如何训练 AI；具体比较**自生成偏好反馈导致的权重训练**与外部 Agent/Prompt 优化，不将其误称为自动设计下层工具链。

## 直接核实内容（2026-10-22）

- §1–2、Fig. 1：基于种子 IFT/EFT 的训练、同一模型生成回答和评分、最高最低候选构成偏好对、DPO 更新 `M1→M2→M3`。
- §2.2、§3.1 的关键实施边界：主实验使用**固定的另一模型生成新指令**，当前模型负责生成候选回答和打分；因此不是封闭、无外部组件的自主系统。
- §3.2 Table 1、Table 4：训练后的指令遵循及评价能力；已核作者报告的 AlpacaEval 2.0 不同迭代胜率，**没有独立复算或重跑训练**。
- §6：作者自述需更多迭代、跨模型检验、长度偏好与 reward hacking 分析、安全评估等；均保留其原文局限身份，**不提前写成研究者已认可的特化风险**。
- **证据状态**：PMLR 发表信息和 arXiv 全文已直接读取；当前是方法、主实验及局限的针对性研读，**尚未逐项复核所有附录及 PMLR 终版与 arXiv 差异**。

**审批结果（2026-10-22）**：在客观骨架基础上，研究者已明确批准[两项具体机制](ARCHITECTURE.md)和[与之对应的两项特化不足](IDEAS.md)，并经 A/B 两方向语义去重创建 [TD006](../../knowledge/deltas/TD006_shared_actor_judge_self_reward_dpo.md) 和 [TD007](../../knowledge/deltas/TD007_dual_task_judge_transfer.md)。作者观察到长度上升和 Judge 部分指标不单调；**奖励投机、长期自我增强失效仍属待验证推断**，不冒充实证定论或学术首创。

**公共安全边界**：不上传公司内部材料、账号/密钥、受版权限制的论文 PDF。
