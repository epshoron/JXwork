# D002｜WorldQuant 101 结构化公式检索先验

- **首次入库**：P001（KB-first）
- **研究任务**：减少 LLM 无约束因子生成产生的无效代码与漫无目的搜索。
- **机制**：从 **WorldQuant 101 Formulaic Alphas** 获取可复用的公式结构和运算模式，以检索上下文作为 Writer 生成因子的先验，而非只依赖自然语言自由编写。
- **P001 依据**：[正式论文摘要/Highlights](https://www.sciencedirect.com/science/article/pii/S2666827026001520) 明确称之为 **key contribution**，并称相对于无约束生成可提高因子质量与搜索效率；[作者公开项目说明](https://github.com/VMSSON345/Self-Improving-Alpha-Mining-for-Quantitative-Trading-via-Multi-Agent-Large-Language-Models-with-Know) 介绍 101 Alpha KB。
- **学术新颖性判断**：**作者明确主张是其论文的关键贡献，但尚未证明世界范围首次提出**；需要比较更多早期的领域检索、公式约束等论文。这里“新”指 **P001 的具体公式先验与多 Agent 生成系统的整合**。
- **更新对象**：生成时使用的知识检索/上下文；无证据表明基础模型参数训练。
- **已报告效果**：作者摘要称对照 unconstrained generation 更好；精确消融表格与统计不确定性尚待 PDF 全文核实。
- **待检验的局限**：强先验会否约束真正新颖的探索？效果是新 Alpha 还是复现/变体经典因子？多样性/同质化如何衡量？
- **未来比较字段**：结构化先验来源、检索粒度（公式/AST/语义）、是否动态调节探索、代码有效率与样本外质量。
- **后续论文记录**：待新增。
