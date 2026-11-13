# P030｜GoAnt: Quality-Diversity Multi-Agent Search for Alpha Factor Discovery in Market Microstructure Data

**公开来源**：[原文入口](https://arxiv.org/abs/2609.08719)

## 客观机制骨架

论文介绍 Explorer、Exploiter、Connector 三类搜索岛、以可测执行特征建立的自适应 Mental Map（区域内保留精英）、以及按搜索状态分配预算的 Queen Dispatcher。另提出无需依赖地图设计的 effective yield 比较准则。

```mermaid
flowchart LR
 A["研究输入/候选"] --> B["论文中的特殊控制或更新机制"]
 B --> C["生成/选择与验证"]
 C --> D["候选/证据结果"]
```

## 证据与适用性边界

arXiv 预印本；价格-成交量及订单簿数据，非仅分钟 Close；作者报告的质量加权产出不是策略收益，不能直接迁移到现有公司场景。本文结果未独立复现。

直接核对 arXiv 题录/摘要、论文解读页面关于六项执行特征及评测协议的说明；**未成功直接读取原始 PDF/HTML 全文**，具体消融表尚待原文复核。

**仅归档论文的核验事实及方法概述，不代表本项目已经决定实施，不对研究者新 Idea、学术首创、特化不足或 Delta 作审批记录。**

[来源核验](PAPER.md)
