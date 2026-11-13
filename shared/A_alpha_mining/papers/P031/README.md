# P031｜FactorEngine: A Program-level Knowledge-Infused Factor Mining Framework for Quantitative Investment

**公开来源**：[原文入口](https://arxiv.org/html/2603.16365)

## 客观机制骨架

将程序结构变更（LLM 指导的 macro evolution）与数值超参数优化（本地 Bayesian micro search）分开，并保留由报告构造种子程序及经验反馈。两级搜索更新的对象不同：先决定计算什么，再优化合法参数。

```mermaid
flowchart LR
 A["研究输入/候选"] --> B["论文中的特殊控制或更新机制"]
 B --> C["生成/选择与验证"]
 C --> D["候选/证据结果"]
```

## 证据与适用性边界

arXiv 预印本；论文使用 OHLCV 等输入，实验 IC/组合改善来自作者报告，不能等同于现有分钟 Close-only 研究的实证，更不能证明任意程序调参不会过拟合。

直接核对 arXiv HTML v2 §1、§3、§4（macro/micro）和部分消融说明；完整参数表与论文更新版本未逐节审计，未复现。

**仅归档论文的核验事实及方法概述，不代表本项目已经决定实施，不对研究者新 Idea、学术首创、特化不足或 Delta 作审批记录。**

[来源核验](PAPER.md)
