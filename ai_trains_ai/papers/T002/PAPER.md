# T002｜论文来源与研读证据界限

**原题**：GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning  
**简称**：GEPA（Genetic-Pareto）  
**正式来源**：International Conference on Learning Representations（ICLR 2026）。作者包括 Lakshya A Agrawal、Shangyin Tan、Dilara Soylu 等。

- [ICLR 2026 官方题录、摘要](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0e9e708b6f48e14fd0ac29e167413f76-Abstract-Conference.html)
- [ICLR 2026 官方完整论文 PDF（87 页，含附录）](https://proceedings.iclr.cc/paper_files/paper/2026/file/0e9e708b6f48e14fd0ac29e167413f76-Paper-Conference.pdf)
- [arXiv:2507.19457](https://arxiv.org/abs/2507.19457)
- [作者在论文中声明的代码仓库](https://github.com/gepa-ai/gepa)（未运行；仅作复现入口，不独立把 GitHub 项目登记为 B 的新资源）

## 本轮实际核验

- **§1–2**：论文问题设定、复合 LLM 系统形式 `Φ`、模块提示 `π` 与固定模型权重 `θ` 的区分、rollout 预算。
- **§3、Figure 3**：初始候选池、模块级反思变异、`μ` 与 `μ_f` 的分工、两类诊断轨迹、选优和 Pareto 选择策略。
- **Appendix C/D，Algorithms 1–4**：`D_feedback / D_pareto` 分组、小样本性能接受准则、逐实例胜出集合的采样概率、带共同祖先约束的可选 Merge。PDF 截图亦核对了 Table 1（第 6 页）。
- **Figure 2**：多跳检索的提示演化实例。
- **§4 Table 1 与 Table 3**：六任务 GRPO/MIPROv2/GEPA 结果及四任务候选选择消融；结果属于**作者报告**，与复现不同。
- **§5、Appendix E**：知道另有推理时优化代码的扩展试验；本轮没有独立逐表核算该扩展实验全部数值。

## 尚未核验／不得宣称

- 未执行作者源码、复现任务指标、核查全部 87 页附录的所有设置和统计稳定性；除已指明表格外，不声称附录全面审核完成。
- 没有测试在特定用户自己的 Executor、企业内部任务或金融数据上有效；不能从 Qwen3-8B 六任务推导所有模型/工作流普遍优于 RL。
- **GEPA/GEPA+Merge 不训练执行模型权重**。GRPO/LoRA 是论文的比较基线，不能归入 GEPA 的更新对象。
- 原文核心架构已入客观档案；**2026-10-22 研究者进一步批准三项具体特色机制及各自对应特化疑问**，已与两方向知识库去重，见 [已审特色](ARCHITECTURE.md)、[配对疑问](IDEAS.md) 和 TD003–TD005。**原创方案仍未批准，风险并非全部实证确定，学术首创性与复现均未确立**。
- 公共仓库只保存原文链接，不复制出版方 PDF。

[返回 T002 骨架](README.md) · [B 论文 Index](../INDEX.md)。
