# Delta Index · 机制增量总表

**审批状态：D001–D007 均为研究 Agent 提议的候选机制卡，等待研究者逐项审阅；目前没有已批准的 Delta 基线。** 不得据此直接把新论文判成「重复／创新」，也不得把「首次入库」等同学术原创。

**建立日期**：2026-10-21　 **起点论文**：[P001](../papers/P001/README.md)　 **库内基线**：此前为空

> 因为是第一篇，**下列所有条目都是本项目“第一次记录（KB-first）”**，并不都属于 P001 的学术原创。学术创新级别另列；**主张/证实/待核**不得混写。

| 机制 ID | 技术单元（对比粒度） | 首次进入本库 | 相对更早文献 / 学术新意判断 | 证据 |
|---|---|---|---|---|
| [D001](deltas/D001_nested_feedback.md) | 双循环：生成/审核 + 外部回测反馈 | P001 · KB-first | **已有先前工作**：QuantAgent (2024) 明确内外循环；P001 是具体实现 | P001 作者 README；QuantAgent §3 |
| [D002](deltas/D002_structured_alpha_prior.md) | WorldQuant 101 结构化公式检索先验 | P001 · KB-first | **作者明确主张的关键贡献**；相对全部前作是否首次尚待核 | P001 期刊摘要/Highlights |
| [D003](deltas/D003_success_memory.md) | 历史有效因子的 Main KB / 跨次检索复用 | P001 · KB-first | **已有先前思想**：QuantAgent (2024) 将反馈写入 KB；本文保存符合阈值的优胜因子 | P001 作者 README；QuantAgent §3 |
| [D004](deltas/D004_role_separation.md) | 专职生成/审查/回测/复盘的 Agent 分工 | P001 · KB-first | 模块化具体实现；Writer/Judge 在 QuantAgent 已存在，**非已证实首次发明** | P001 作者 README；QuantAgent §3 |
| [D005](deltas/D005_oos_evaluation.md) | 时序拆分、冻结 KB 的样本外验证 | P001 · KB-first | **评价实践，不声称算法创新**；费用净回测等还有待补证 | P001 作者 README、期刊 Highlights |
| [D006](deltas/D006_domain_guidance.md) | 21 个金融主题 Agent + 5 类提示多样化（候选机制） | P002 · KB-first 候选 | 与 P001 101 公式 KB 的先验形式不同；学术首创尚未核实 | P002 §3.1–3.2 |
| [D007](deltas/D007_code_evolution.md) | LLM Python 因子代码级变异/交叉与种群筛选（候选机制） | P002 · KB-first 候选 | 与 P001 的候选优化方式有差别；进化式程序搜索已有前作 | P002 §3.4–3.6 |


## P002 候选入库对照（2026-10-21；等待研究者审阅）

| P002 技术变化 | 相对已存机制 | 入库决策 | 学术首创判断 |
|---|---|---|---|
| 代码审查 + 指标筛选 + 正反样例 Prompt 反馈 | [D001](deltas/D001_nested_feedback.md) | **已有反馈机制的变体**，在 D001 更新 | 自反馈并非首创，具体组合待查新 |
| 21 个主题 Agent、五类 Guidance | [D004](deltas/D004_role_separation.md)、[D002](deltas/D002_structured_alpha_prior.md) | **候选新增 [D006](deltas/D006_domain_guidance.md)**：主题搜索先验和提示多样化，与 101 公式 KB 不同 | KB-first，学术 novelty 待核 |
| 质量审查与生成岗位分工 | [D004](deltas/D004_role_separation.md) | **已有机制的角色变体** | 不能将多 Agent 本身算作首创 |
| LLM Python Mutation/Crossover、精英种群与后代搜索 | [D001](deltas/D001_nested_feedback.md) | **候选新增 [D007](deltas/D007_code_evolution.md)**：独立的搜索操作与种群控制层 | KB-first；此前 FunSearch、AlphaEvolve 已有进化编程相关方法 |
| 当轮成功/失败示例 vs 长期 Main KB | [D003](deltas/D003_success_memory.md) | **不同，不混为一个持久记忆机制** | 不推断存在跨任务持久 KB |
| 多市场/有成本的 Qlib 时序回测 | [D005](deltas/D005_oos_evaluation.md) | **评价范式的不同实现** | 不宣称新算法 |

**证据入口**：[P002 正式档案](../papers/P002/README.md)、[CogAlpha 原文 §3–4](https://arxiv.org/html/2511.18850)。  
**规则**：P002 的 D006/D007 是新入**本项目**知识库，不表示 CogAlpha 在学术上首创变异、交叉、多 Agent 或 LLM 代码进化。

## 以后比较新论文时怎么用

- **存在完全同等机制**：归到 D001 等原卡，关联论文；不是新 Delta。
- **同一机制但具体改动**：在原卡写清变体，比如“反馈从 prompt 扩展到长期记忆/优化器”，明确对照依据；这是*差异*而非无条件“创新”。
- **真正出现不同机制**：创建 D006 等新卡，和最相近旧卡明确对比。
- **证据无法区分**：标待核，不以“看起来更新潮”强行添加。

**项目级目标**：随论文积累，逐渐形成可比较的模块库/机制图谱。研究者确认后，才根据既有机制、论文实证和缺口推导我们的创新方向；当前主要任务仍是理解文献本身。
