# P033｜LABO: LLM-Accelerated Bayesian Optimization through Broad Exploration and Selective Experimentation

**公开来源**：[原文入口](https://proceedings.mlr.press/v306/chen26fx.html)

## 客观机制骨架

用廉价的 LLM 预测/评价覆盖更大候选空间，仅对具有较高不确定性或代理误差的区域投入真实昂贵实验；门控机制在单一 Bayesian Optimization 框架中协调模型预测与真实观测。

```mermaid
flowchart LR
 A["研究输入/候选"] --> B["论文中的特殊控制或更新机制"]
 B --> C["生成/选择与验证"]
 C --> D["候选/证据结果"]
```

## 证据与适用性边界

ICML 2026 公开正式论文，研究领域为通用科学优化；原论文实验不构成金融回测中的廉价评分可靠性保证，特别是已反复使用训练数据时仍有选择偏差。与 P010 AlphaSchema 的代理 LightGBM 存在作用位置交集，需做具体方法消融。

直接核对 PMLR 官方题录与摘要、作者公开机制概述；未逐项验证具体门控公式和实验证明；未复现。

**仅归档论文的核验事实及方法概述，不代表本项目已经决定实施，不对研究者新 Idea、学术首创、特化不足或 Delta 作审批记录。**

[来源核验](PAPER.md)
