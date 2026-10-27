# JXwork · 三方向量化与 AI 研究工作区

> **研究状态（2026-10-27 更新方向 C）**：方向 A（AI Agent 因子挖掘）已有 P001–P010、D001–D020，仍以论文原文理解与单篇评审为主；方向 B（AI 优化 AI）已建立，**T001 Promptbreeder 已审两组特色/不足并入库 TD001/TD002；T003 Agent Lightning 2+2（TD008/TD009）和 T005 Self-Rewarding 2+2（TD006/TD007）均已审批入库；T002 GEPA 已审 3+3 并入库 TD003–TD005；T004 ADAS 已审 2+2 并入库 TD010/TD011；其他状态以 B 论文 Index 为准**。  
> **仓库用途**：A / B / C 各有独立的来源索引、研究档案及按需建立的知识体系，基础核验、去重、记录规则尽量共用。

## 三个独立研究方向

### A｜AI Agent 驱动的量化因子挖掘（既有研究，不迁移）

原来的 [papers/INDEX.md](papers/INDEX.md)（P001–P010）、[knowledge/DELTA_INDEX.md](knowledge/DELTA_INDEX.md)（D001–D020）与 [synthesis/](synthesis/) 保持原路径、编号和历史成果，**不移动、不重新命名**。

研究 **LLM / Agent 驱动的量化因子发现**：因子生成与搜索、验证反馈、自主迭代、Agent 协作，以及它们与自我改进 / RSI 的真正关系。先研究原始论文，不预设完整或互斥的技术流派。

当前在方向 A 暂用 **质量控制、经验学习、推理协作** 三个互补视角提问；它们可以并存，详见 [synthesis/RESEARCH_LENSES.md](synthesis/RESEARCH_LENSES.md)。

### B｜AI 优化 AI：Agent 优化与模型训练（新方向）

[ai_trains_ai/](ai_trains_ai/README.md) 研究**上层 AI 利用记忆、知识与可验证的任务反馈，改进下层执行 Agent** 的方法；**并行比较外部 Prompt/Skills/工具及记忆策略优化，与 SFT/RL 等模型权重训练**。LoRA 属参数高效微调手段。CLI + Executor 是目标研究场景，不是已经定稿的工程架构；**不预设哪条路线必然更好，或将 Prompt 优化误称模型训练/严格 RSI**。

- [B 论文 Index](ai_trains_ai/papers/INDEX.md)：**[T001 Promptbreeder 已审 2+2](ai_trains_ai/papers/T001/ARCHITECTURE.md)、[T002 GEPA 已审 3+3](ai_trains_ai/papers/T002/ARCHITECTURE.md)、[T003 Agent Lightning 2+2 已审](ai_trains_ai/papers/T003/ARCHITECTURE.md)、[T004 ADAS 已审 2+2](ai_trains_ai/papers/T004/ARCHITECTURE.md)、[T005 Self-Rewarding 2+2 已审](ai_trains_ai/papers/T005/ARCHITECTURE.md)**；[B 机制 Delta Index](ai_trains_ai/knowledge/DELTA_INDEX.md)：**TD001** 起；[B 综合目录](ai_trains_ai/synthesis/README.md)。
- 同一论文可跨方向交叉引用，**先查两个索引，避免重复归档或重复包装同一机制**。


### C｜分钟级量价数据构建日频特征（2026-10-27 新增）

[**方向 C 研究入口**](intraday_to_daily/README.md) · [学术论文索引 C001 起](intraday_to_daily/papers/INDEX.md) · [券商研报索引 CR001 起](intraday_to_daily/reports/INDEX.md)。研究分钟 OHLCV、成交信息及日内行为特征怎样聚合为 Daily 特征，并讨论与未来收益预测/选股的关系。**老师要求的目标标签、调仓频率、可用数据尚待确认**；当前先搜集、研读论文与券商金工研报，统计聚合、条件聚合、模型学习都不预设优劣。暂不创建空白知识卡或强行规定技术方案。与 A/B 严格分目录，不迁移旧成果。

## 研究顺序与轻量协作（2026-10-21）

**每个研究方向分别按顺序推进三个研究阶段**（A 以阶段一原文研读为主；B 刚初始化）：

1. **阶段一（现在）——完整研读理解论文。** 先把每篇原文研究的问题、算法/组件、输入输出、反馈控制、实验和结果弄清楚，能用原文证据准确复述。只找到标题、摘要或作者仓库不是完成阅读。
2. **阶段二（以后）——创新点与缺点的比较整合。** 读懂足够多论文后，辨认经证据支撑的贡献、实际缺点与各方法的互补性，再跨论文系统整理。
3. **阶段三（最后）——有机结合并提出自己的想法。** 论文积累与第二阶段比较足够后，基于创新与缺口的互补关系，提出可检验的研究假设或方法，不提前拼装技术方案。

以上三阶段**不等于**“质量控制、经验学习、推理协作”三个可组合的研究提问视角。具体门槛及阅读范围见 [RESEARCH_PLAN.md](RESEARCH_PLAN.md)。

**三方向共用的协作形式：先在所属方向 INDEX 认领去重 → 核实原文后可直接归档论文骨架并向研究者讲解 → 创新/特化不足经研究者审批与严格语义去重后正式入库 → 同一工作回合同步论文档案、所属方向论文 Index 和 Delta 索引 → 经确认后再形成成熟综合。**

- 开始论文前，先选择方向：A 登记在 [papers/INDEX.md](papers/INDEX.md)（P 号），B 登记在 [ai_trains_ai/papers/INDEX.md](ai_trains_ai/papers/INDEX.md)（T 号）；各方向 Index 互查 DOI/arXiv/题名避免重复，不以聊天窗口身份命名。
- **不同来源不同入库权限**：**正式论文**经核对可直接归档骨架；**非论文材料**（GitHub 项目、文章、技术笔记、实验记录等）必须先在对话中介绍其研究价值，得到研究者明确同意，**才可在 GitHub 建档、登记索引或写入骨架**。所有来源的创新、特化不足、独立想法和 Delta 仍须逐项批准并严格语义去重。不创建逐篇讨论流水账。
- Agent 优先自主阅读公开原文 HTML/PDF；访问受限才请研究者按需提供 PDF，索引始终保留原文链接。
- **各方向按需建立的 Delta 数据库**区分「机制基础」「论文特化增量」「学术新颖性」，不把通用 OOS、成本、市场变化等凑成创新或独有缺点；P001 首篇首次入库不代表学术首创。成熟综合才进入 [synthesis/](synthesis/)。
- **每个 Agent 必须负责本轮同步**：论文 Markdown 发生真实状态变化，**同一工作回合更新所属方向来源 Index**（[A](papers/INDEX.md) / [B](ai_trains_ai/papers/INDEX.md) / [C 论文](intraday_to_daily/papers/INDEX.md) / [C 研报](intraday_to_daily/reports/INDEX.md)）；Delta 改变则同步所属方向机制 Index（[A](knowledge/DELTA_INDEX.md) / [B](ai_trains_ai/knowledge/DELTA_INDEX.md)） 和相应论文引用；协作规范改变时同步 **[AGENTS.md](AGENTS.md)** 与 [RESEARCH_WRITING_STANDARD.md](RESEARCH_WRITING_STANDARD.md)。**结束前检查索引缺行、表格、链接、审批状态**。写共享文件前读最新 SHA，遇冲突合并，绝不覆盖其他 Agent。
- `CHANGELOG.md` 只记录**研究规范/架构变更与经确认的成果发布**，不充当逐篇研究流水账。

## 导航

- [JXWORK_START_HERE.md](JXWORK_START_HERE.md)：三个方向的快速入口（代替失效的旧导航指针）
- [ai_trains_ai/README.md](ai_trains_ai/README.md)：方向 B 研究边界和各自的论文、知识、综合目录
- [intraday_to_daily/README.md](intraday_to_daily/README.md)：方向 C 分钟级数据构建日频特征的独立研究入口

- [AGENTS.md](AGENTS.md)：研究 Agent 接续规范（**先读**）
- [RESEARCH_WRITING_STANDARD.md](RESEARCH_WRITING_STANDARD.md)：**必读**写作风格、骨架优先、特化筛选和研究者审批
- [RESEARCH_PLAN.md](RESEARCH_PLAN.md)：研究问题及对话研读方式
- [papers/INDEX.md](papers/INDEX.md)：**跨研究 Agent 论文去重索引**；其他来源经研究者批准后再登记
- [papers/P001/](papers/P001/README.md)：第一篇单篇论文档案范例
- [papers/P002/](papers/P002/README.md)：CogAlpha 结构化档案与 Mermaid 架构图
- [knowledge/DELTA_INDEX.md](knowledge/DELTA_INDEX.md)：跨论文机制 Delta 知识库
- [synthesis/](synthesis/)：工作性问题视角及后续确认的综合成果
- [evaluation/](evaluation/README.md)：**单因子多空组合评价 V1（研究口径已定，待实证）**；0.5/0.5 因子仓位、日频 VWAP、Delta Turnover、统一 10 bps 成本及线性 Objective
- [CHANGELOG.md](CHANGELOG.md)：架构与最终成果变更记录

旧版 `notes/` 逐篇笔记目录及模板已从当前分支删除，不再采用。

## 仓库与数据边界

仓库当前为 **Private**，但仍须保护版权、商业数据与研究权限。不提交公司内部材料、代码、数据、邮件、API Key、策略，也不上传未经授权可公开再分发的论文 PDF；原论文只登记公开链接及版权许可允许的内容。
