# D005｜时间顺序切分、知识库冻结与评价口径

**性质：通用实验与评价口径，研究者已明确要求从创新 Delta 候选中排除。此文件只保留历史参考及 P002 已记录的对照，不能作为专属创新或特化不足。**

- **首次入库**：P001（KB-first；属于**验证范式**，不是声称的新算法）
- **机制**：按时间分 discovery/train、validation 与 held-out test；最后测试阶段冻结 Main KB，减少把测试反馈反灌到后续生成/筛选的风险。
- **P001 依据**：[作者 README 的 Chronological Split](https://github.com/VMSSON345/Self-Improving-Alpha-Mining-for-Quantitative-Trading-via-Multi-Agent-Large-Language-Models-with-Know)。
- **作者报告**：449 只筛选后股票，held-out 平均 IC 0.048 / Sharpe 2.39；[期刊 Highlights](https://www.sciencedirect.com/science/article/pii/S2666827026001520) 明示 Sharpe 为 **gross-of-cost**。
- **新颖性判断**：时间切分与测试冻结属于审慎评价实践，不宣称 P001 在学术上首创这一模式。
- **尚未证明**：扣交易成本后收益、跨市场稳健性、所有时间戳无泄漏、优化与测试严格隔离；当前仅可说作者**声称并设计了相关控制**。
- **未来比较字段**：标签持有期、交易频率、样本外长度、成本、随机种子、选择偏差、多重检验、跨 regime/跨市场。
- **后续论文记录**：待新增。


## P002 · CogAlpha：评价设置差异（2026-10-21）

- **判定：已有评价框架的另一种具体实现；不把时间切分/回测再登记为新算法机制**。
- **P002**：多市场/多指数数据，主 CSI300 使用训练 2011–2019、验证 2020、测试 2021–2024；预测未来 10 日收益，Qlib top-50/drop-5 **每日**检查排名、最多换 5 只，计入作者指定的买卖费用。
- **对照 P001**：P001 报告越南市场、Main KB 在测试期冻结，Sharpe 口径是 **gross-of-cost**；P002 在所报告 Qlib 回测中列出成本。**两篇市场、因子、预测模型/标签和统计口径不同，不能直接比较 2.39 与 1.8999 判算法高下**。
- **不确定性**：P002 附录 B.6 称主要是单次因子挖掘运行；防泄漏测试不能取代交易信息可知时点的全面审计。
- **证据**：[P002 §4 与 Appendix B.1/B.2/B.6](https://arxiv.org/html/2511.18850#S4)，[P002 档案](../../papers/P002/ARCHITECTURE.md)。
