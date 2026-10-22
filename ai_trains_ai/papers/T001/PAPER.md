# T001｜原始学术来源、核查边界

**论文题名**：Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution  
**作者**：Chrisantha Fernando、Dylan Sunil Banarse、Henryk Michalewski、Simon Osindero、Tim Rocktäschel  
**正式发表**：**ICML 2024**，*Proceedings of Machine Learning Research* **235:13481–13544**。

## 权威原文

- **正式论文题录**：[PMLR｜ICML 2024](https://proceedings.mlr.press/v235/fernando24a.html)
- **可直接阅读的原始预印本全文 PDF（2023-09-28）**：[arXiv:2309.16797](https://arxiv.org/pdf/2309.16797)
- **预印本记录**：[arXiv 摘要与版本信息](https://arxiv.org/abs/2309.16797)

## 本轮核查内容（2026-10-22）

- 官方 ICML/PMLR 题录：确认正式出版与作者身份。
- 原始 arXiv PDF **Fig.1 与 §3.1–3.2**：Population 初始化、进化单位（通常两段 task-prompts + mutation-prompt）、二元锦标赛、五类变异操作与反馈方向。
- **§4–5、Table 1、部分附录**：任务类型、样本抽样、实验设置与作者报告结果；注意不同 LLM 基线不可混为同一实验条件。
- **Appendix J.3–J.5 与 L**：核对变异 Prompt 成功率、GSM8K 不同变异算子产生优于父代后代的比例、few-shot 提示漂移示例，以及“分别移除超变异、成功示例反推、初始化方式”等消融的真实定义。**作者在 J.5 明言 few-shot 示例可能主导，任务提示变得无意义**；附录 L 中初始化方式的影响最大，但这是消融结果，不能把两者自动写成已审批的特化不足。
- **§6 与 Appendix F**：作者承认的边界：主要改变任务 Prompt 内容与变异 Prompt，而**没有进化整个 Prompting 算法的拓扑/独立评分器**；不能把“自指优化”夸大成无限制 RSI。
- **未核对的边界**：本轮未逐页对照 PMLR 正式 camera-ready PDF 与 arXiv 2023 版的所有改动；没做统计复算，也没独立执行原论文实验。

## 工程实现证据等级

- **论文中提出的算法与实验**是本档的正式来源。阅读原文不等于已核对“作者原始训练/实验仓库与论文严格一致”。
- **独立或轻量示例代码不能替代论文原实验实现**；未经研究者批准，不作为本项目单独的非论文研究来源注册。本篇不宣称已有可完整复现的官方算法发布。
- 后续若需针对某个开源仓库建立独立资料卡，须遵守 [来源准入与审批规则](../../../RESEARCH_WRITING_STANDARD.md)。

**审批边界**：研究者仅批准启动方向 B 论文研究；本文**客观骨架**按公共规范可自主入库。对其创新、新颖性、具体特化缺陷或 `TD00X` 机制卡，仍待逐项讨论、严格语义去重、明确批准后才归档。根目录方向 A 的所有论文/机制材料不动。
