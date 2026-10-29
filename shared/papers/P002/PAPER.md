# P002｜CogAlpha：论文来源、原文与核验范围

- **英文题名**：Cognitive Alpha Mining via LLM-Driven Code-Based Evolution
- **作者**：Fengyuan Liu, Yi Huang, Sichun Luo, Yuqi Wang, Yazheng Yang, Xinye Li, Zefa Hu, Junlan Feng, Qi Liu
- **正式出版**：*Proceedings of ACL 2026*, Volume 1 (Long Papers), pp. 11715–11749
- **正式原文入口**：[ACL Anthology](https://aclanthology.org/2026.acl-long.538/)
- **DOI**：[10.18653/v1/2026.acl-long.538](https://doi.org/10.18653/v1/2026.acl-long.538)
- **可在线阅读全文**：[arXiv:2511.18850v4 HTML](https://arxiv.org/html/2511.18850)
- **出版方 PDF 入口**：[ACL 官方 PDF](https://aclanthology.org/2026.acl-long.538.pdf)
- **公开提示词**：[作者 CogAlpha_Prompt 仓库](https://github.com/uwFengyuan/CogAlpha_Prompt)（仅 Prompt，**不要当成完整训练/运行框架开源**）
- **索引记录**：[P002](../INDEX.md)

## 研究对象

用 LLM 自动生成、修订、交叉组合新因子 **Python 代码**；以质量审查和预测指标筛选候选，使用历史反馈引导后续探索。生成结果交给 LightGBM/Ridge 等预测模型、Qlib 模拟回测。**不同于只做因子选择、训练 LLM 参数或直接执行交易**。

## 原文证据导航

| 主题 | 原文 |
|---|---|
| 作者贡献与现有路线区别 | [Introduction §1](https://arxiv.org/html/2511.18850#S1) / [Related Work §2](https://arxiv.org/html/2511.18850#S2) |
| 七层 21 个领域 Agent / 五类指导 Prompt | [§3.1–3.2](https://arxiv.org/html/2511.18850#S3) |
| 多 Agent 质量检查 / 打分 / 自适应生成 / 演化 | [§3.3–3.6](https://arxiv.org/html/2511.18850#S3) |
| 数据切分、比较实验、消融及泛化 | [§4](https://arxiv.org/html/2511.18850#S4)、[Appendix B](https://arxiv.org/html/2511.18850#A2) |
| 质量检查细节、Prompt | [Appendix A.3](https://arxiv.org/html/2511.18850#A1)、[Appendix C](https://arxiv.org/html/2511.18850#A3) |

## 已核与尚未完成

- **已核对/讨论**：正式出版信息、arXiv 正文中的系统流程、专业 Agent 结构、关键算法、指标与消融/回测设置，用户已要求将其归档。
- **未独立完成**：源码级运行与结果复现、所有时间泄漏边界的审计、多次独立种子验证、全球前作的系统性首创性检索、真实交易效果。
- **版权规则**：公开仓库只存上述权威链接与我们自己编写的总结；**不将可在线访问的论文 PDF 自动视为有权公开再分发**。
