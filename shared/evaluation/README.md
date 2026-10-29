# Evaluator V1｜评测数学规范与可选 Score

[PORTFOLIO_SCORING_STANDARD.md](PORTFOLIO_SCORING_STANDARD.md) 定义原定的单因子多空组合：截面 1%/99% Winsorization、Demean、L1 权重归一化、日频 VWAP 理论收益、双边 Delta Turnover、每单位成交额 10 bps 成本。保存 Ret/SR/DD/TO/Cost 原始字段，以同一版本评价。

**2026-10-29 新决策**：正式成功只看 [两阶段门槛](../architecture/V1.0.1/GATES_AND_DECISIONS.md) 的第一关 PASS、Ret > 3%、SR > 1。原有线性 `Score = Ret + 0.05·SR − 0.1·DD − Cost_ann` 保持数学定义，但只在需要比较/排序时由 Python 按保存指标计算，**不是候选入库或成功的必要条件**。既有口径尚未声称被独立回测验证。
