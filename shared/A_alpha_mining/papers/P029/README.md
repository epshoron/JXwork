# P029｜SetFit：少样本对比式文本表示适配

- **来源**：Tunstall et al.，2022，预印本 Efficient Few-Shot Learning Without Prompts；讨论预训练 Sentence Transformer 的低样本微调，不是金融概念嵌入或 Alpha 挖掘的实证。
- **方法**：用少量标注文本构成正/负样本对，对基础 Sentence Transformer 做对比训练；再用训练出的 Embedding 训练轻量分类头。目标是数据稀缺时的文本分类。
- **作者实验**：与多种 PEFT / PET Few-shot 方法比较，报告在一些文本分类任务上相对有效。该论文**不是**“冻结 Encoder 只训练线性投影矩阵”的直接实现；矩阵方案须独立设计和验证。
- **使用边界**：少量独立金融概念文本组成的数千个样本对，统计上不能被视作数千个独立金融机制样本；不得从通用 Few-shot 分类结果推导金融研究空间有效。

本条仅客观来源及方法骨架；无经审批项目创新、特化不足或 Delta。

[来源与核验](PAPER.md)
