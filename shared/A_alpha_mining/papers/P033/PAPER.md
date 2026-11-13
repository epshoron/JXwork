# P033｜论文身份与直接核查范围

- **原始题名**：LABO: LLM-Accelerated Bayesian Optimization through Broad Exploration and Selective Experimentation
- **权威来源**：https://proceedings.mlr.press/v306/chen26fx.html
- **方法概述**：用廉价的 LLM 预测/评价覆盖更大候选空间，仅对具有较高不确定性或代理误差的区域投入真实昂贵实验；门控机制在单一 Bayesian Optimization 框架中协调模型预测与真实观测。
- **本轮核验**：直接核对 PMLR 官方题录与摘要、作者公开机制概述；未逐项验证具体门控公式和实验证明；未复现。
- **外推限制**：ICML 2026 公开正式论文，研究领域为通用科学优化；原论文实验不构成金融回测中的廉价评分可靠性保证，特别是已反复使用训练数据时仍有选择偏差。与 P010 AlphaSchema 的代理 LightGBM 存在作用位置交集，需做具体方法消融。
- **版权/保密**：只存客观事实和论文链接，不转载原文 PDF，不记录公司内部数据、代码或讨论中的未批准项目方案。
