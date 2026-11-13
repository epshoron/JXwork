# P032｜Alpha Discovery via Grammar-Guided Learning and Search

**公开来源**：[原文入口](https://arxiv.org/html/2601.22119)

## 客观机制骨架

AlphaCFG 先以 alpha-oriented context-free grammar 限定语法/语义合法的树状表达，再以 grammar-aware MCTS 和树结构表征的 policy/value 网络进行搜索；关注表达式复杂度与语义等价候选造成的浪费。

```mermaid
flowchart LR
 A["研究输入/候选"] --> B["论文中的特殊控制或更新机制"]
 B --> C["生成/选择与验证"]
 C --> D["候选/证据结果"]
```

## 证据与适用性边界

arXiv 预印本，不宣称已获 ICML 正式录用；论文中中美市场实验是作者报告。生成前约束与已有算子库、AST 去重可能重合，金融预测优势未经本项目复现。

直接核对 arXiv HTML 摘要、§1 与 §3、§4 的机制描述；未检验作者代码运行、全部消融或公司的表达式形式。

**仅归档论文的核验事实及方法概述，不代表本项目已经决定实施，不对研究者新 Idea、学术首创、特化不足或 Delta 作审批记录。**

[来源核验](PAPER.md)
