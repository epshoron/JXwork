# Delta Index · 机制增量总表

**审批进度**：仅 **D002（P001 的 WorldQuant 101 结构化先验及其特化风险）**已获研究者讨论确认，可作为重点机制记录；**学术首创性、真实过拟合尚未验证**。D001/D003/D004 是背景机制对照而非创新 Delta；D005 是通用评测规范，**不应计作创新 Delta**。P002 的 D006/D007 等新增条目仍待研究者审阅，不自动转正。

**建立日期**：2026-10-21　 **起点论文**：[P001](../papers/P001/README.md)　 **库内基线**：此前为空

> 本库从 P001 建立基础机制参照；P002 等后续论文的机制差异须再与已有知识比较。**首次入本库不代表学术首次发明；背景组件与通用评价口径不算创新 Delta**。研究者审批状态与证据支持程度须分别标明。

| 机制 ID | 技术单元（对比粒度） | 首次进入本库 | 相对更早文献 / 学术新意判断 | 证据 |
|---|---|---|---|---|
| [D001](deltas/D001_nested_feedback.md) | 双循环：生成/审核 + 外部回测反馈 | P001 · 背景基线 | **非创新 Delta**；QuantAgent (2024) 已有相关循环，仅作后续机制差异对照 | P001 作者 README；QuantAgent §3 |
| [D002](deltas/D002_structured_alpha_prior.md) | WorldQuant 101 结构化公式检索先验 | **P001 · 已讨论确认的重点机制** | **作者强调的贡献**；研究者确认应追问先验是否锁定搜索、增加同质化/选择过拟合；效果与原创边界尚待核 | P001 期刊摘要/Highlights；[P001 特化疑问](../papers/P001/IDEAS.md) |
| [D003](deltas/D003_success_memory.md) | 历史有效因子的 Main KB / 跨次检索复用 | P001 · 背景基线 | **非创新 Delta**；QuantAgent (2024) 已有知识反馈；P001 的具体保存方式可留作比较 | P001 作者 README；QuantAgent §3 |
| [D004](deltas/D004_role_separation.md) | 专职生成/审查/回测/复盘的 Agent 分工 | P001 · 背景基线 | **非创新 Delta**；Writer/Judge 已见于 QuantAgent，重点比较特化分工差别 | P001 作者 README；QuantAgent §3 |
| [D005](deltas/D005_oos_evaluation.md) | 时间切分 / 样本外验证 | 既有候选记录，**从创新 Delta 候选排除** | **通用评测规范**；保留原链接以免破坏 P002 已写的研究对照，但不作为 P001 特化机制、缺点或创新 Delta | 两篇论文的实验口径记录 |
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

## 贡献及不足的审批门槛

每篇先画架构、理解原文；**创新点、特化不足和我们的推论必须先在 LLM 对话中逐项提出，经研究者明确拍板，才更新对应已批准知识卡**。研究 Agent 不得为了凑数量录入一般 OOS、成本、市场变化或套话式过拟合；风险要明确关联某篇的独特设计及可检验证据。完整规范见 [RESEARCH_WRITING_STANDARD.md](../RESEARCH_WRITING_STANDARD.md)。

## 以后比较新论文时怎么用

- **存在完全同等机制**：引用基础机制记录或已批准的旧 Delta；没有特化增量就不创建新 Delta。
- **同一机制但具体改动**：先在对话说明改动与证据；**获批后**在旧卡追加变体（例如提示反馈变为持久记忆），不能把所有变体都称作创新。
- **真正出现不同机制**：**先在对话中给出特化差异及证据，获研究者批准后**才新建卡，并与最相近旧机制对比。
- **证据无法区分**：标待核，不以“看起来更新潮”强行添加。

**项目级目标**：随论文积累，逐渐形成可比较的模块库/机制图谱。研究者确认后，才根据既有机制、论文实证和缺口推导我们的创新方向；当前主要任务仍是理解文献本身。
