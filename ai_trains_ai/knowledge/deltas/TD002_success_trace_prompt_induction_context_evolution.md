# TD002｜成功执行轨迹反推 Prompt + Few-shot 示例演化（Promptbreeder）

> **首次入本方向库**：T001，研究者 2026-10-22 明确批准；**不称“成功经验可用来改提示”是学术首创**。

**解决什么**：如何利用模型**真实做对任务的 working out**，而不仅靠文本改写和随机变异，影响后续的任务指令或示例？

**输入**：任务 Prompt P、对真实问题的正确求解轨迹、few-shot 示例上下文、任务评价分数。

**干预与更新**：原文的 **Lamarckian mutation** 调用 LLM 根据一次正确解答过程反推新的 task-prompt；另外的 **context shuffling** 维护正确 working outs 作为 few-shot 示例，可随机替换/重采样，使上下文与 P、M 一起随个体变化。**两个是不同算子，归在同一“成功经验进入未来 Prompt/示例”可复用技术单元**。不会更新模型权重。

**原文依据**：[Promptbreeder ICML 2024](https://proceedings.mlr.press/v235/fernando24a.html)；[arXiv §3.2.4–3.2.5、Appendix J.5、Appendix B](https://arxiv.org/pdf/2309.16797)。

**区别/去重**：[D003](../../../knowledge/deltas/D003_success_memory.md) 是保存并检索**历史有效因子**，并非从正确执行的 **working out 反向生成 Prompt**；`TD001` 是变异 M 本身由任务下游表现选择。普通示例记忆/反思不单独拆卡，也不将 Lamarckian 作为首次学术发明。

**对应特化不足**：[T001 IDEAS §2](../../papers/T001/IDEAS.md)：作者 Appendix J.5 记录正确示例主导效果、P 漂移到无意义字符串的现象。需要把 P 与示例贡献隔离验证，**不等于全系统泛化失败已证实**。

**证据与审批边界**：研究者批准具体设计与对应不足。作者报告的现象属于原文证据，建议的隔离实验属于尚未实施的分析；无独立复现与学术首次结论。
