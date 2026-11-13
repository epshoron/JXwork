# P031｜论文身份与直接核查范围

- **原始题名**：FactorEngine: A Program-level Knowledge-Infused Factor Mining Framework for Quantitative Investment
- **权威来源**：https://arxiv.org/html/2603.16365
- **方法概述**：将程序结构变更（LLM 指导的 macro evolution）与数值超参数优化（本地 Bayesian micro search）分开，并保留由报告构造种子程序及经验反馈。两级搜索更新的对象不同：先决定计算什么，再优化合法参数。
- **本轮核验**：直接核对 arXiv HTML v2 §1、§3、§4（macro/micro）和部分消融说明；完整参数表与论文更新版本未逐节审计，未复现。
- **外推限制**：arXiv 预印本；论文使用 OHLCV 等输入，实验 IC/组合改善来自作者报告，不能等同于现有分钟 Close-only 研究的实证，更不能证明任意程序调参不会过拟合。
- **版权/保密**：只存客观事实和论文链接，不转载原文 PDF，不记录公司内部数据、代码或讨论中的未批准项目方案。
