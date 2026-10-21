# D005｜时间顺序切分、知识库冻结与评价口径

- **首次入库**：P001（KB-first；属于**验证范式**，不是声称的新算法）
- **机制**：按时间分 discovery/train、validation 与 held-out test；最后测试阶段冻结 Main KB，减少把测试反馈反灌到后续生成/筛选的风险。
- **P001 依据**：[作者 README 的 Chronological Split](https://github.com/VMSSON345/Self-Improving-Alpha-Mining-for-Quantitative-Trading-via-Multi-Agent-Large-Language-Models-with-Know)。
- **作者报告**：449 只筛选后股票，held-out 平均 IC 0.048 / Sharpe 2.39；[期刊 Highlights](https://www.sciencedirect.com/science/article/pii/S2666827026001520) 明示 Sharpe 为 **gross-of-cost**。
- **新颖性判断**：时间切分与测试冻结属于审慎评价实践，不宣称 P001 在学术上首创这一模式。
- **尚未证明**：扣交易成本后收益、跨市场稳健性、所有时间戳无泄漏、优化与测试严格隔离；当前仅可说作者**声称并设计了相关控制**。
- **未来比较字段**：标签持有期、交易频率、样本外长度、成本、随机种子、选择偏差、多重检验、跨 regime/跨市场。
- **后续论文记录**：待新增。
