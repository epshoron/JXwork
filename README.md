# JXwork · AI 因子研究工作区

> **当前阶段：阶段一——在 LLM 对话中全面阅读、理解原始论文（2026-10-21）**  
> **仓库用途：研究规范、论文档案（papers/P00X）、跨论文 Delta 知识库（knowledge/）与经确认的综合结论。**

## 研究方向

研究 **LLM / Agent 驱动的量化因子发现**：因子生成与搜索、验证反馈、自主迭代、Agent 协作，以及它们与自我改进 / RSI 的真正关系。先研究原始论文，不预设完整或互斥的技术流派。

当前暂用 **质量控制、经验学习、推理协作** 三个互补视角提问；它们可以并存，也允许随研究修正，详见 [synthesis/RESEARCH_LENSES.md](synthesis/RESEARCH_LENSES.md)。

## 研究顺序与轻量协作（2026-10-21）

**必须按顺序推进三个研究阶段：**

1. **阶段一（现在）——完整研读理解论文。** 先把每篇原文研究的问题、算法/组件、输入输出、反馈控制、实验和结果弄清楚，能用原文证据准确复述。只找到标题、摘要或作者仓库不是完成阅读。
2. **阶段二（以后）——创新点与缺点的比较整合。** 读懂足够多论文后，辨认经证据支撑的贡献、实际缺点与各方法的互补性，再跨论文系统整理。
3. **阶段三（最后）——有机结合并提出自己的想法。** 论文积累与第二阶段比较足够后，基于创新与缺口的互补关系，提出可检验的研究假设或方法，不提前拼装技术方案。

以上三阶段**不等于**“质量控制、经验学习、推理协作”三个可组合的研究提问视角。具体门槛及阅读范围见 [RESEARCH_PLAN.md](RESEARCH_PLAN.md)。

**协作形式：先在 INDEX 认领去重 → 核实原文后可直接归档论文骨架并向研究者讲解 → 创新/特化不足经研究者审批与严格语义去重后正式入库 → 同一工作回合同步论文档案、papers/INDEX 和相关 Delta 索引 → 经确认后再形成成熟综合。**

- 开始某篇论文前，只在 [papers/INDEX.md](papers/INDEX.md) 登记**统一论文编号、权威原文链接和最小状态**，不以聊天窗口身份命名。
- **不同来源不同入库权限**：**正式论文**经核对可直接归档骨架；**非论文材料**（GitHub 项目、文章、技术笔记、实验记录等）必须先在对话中介绍其研究价值，得到研究者明确同意，**才可在 GitHub 建档、登记索引或写入骨架**。所有来源的创新、特化不足、独立想法和 Delta 仍须逐项批准并严格语义去重。不创建逐篇讨论流水账。
- Agent 优先自主阅读公开原文 HTML/PDF；访问受限才请研究者按需提供 PDF，索引始终保留原文链接。
- **Delta 数据库**区分「机制基础」「论文特化增量」「学术新颖性」，不把通用 OOS、成本、市场变化等凑成创新或独有缺点；P001 首篇首次入库不代表学术首创。成熟综合才进入 [synthesis/](synthesis/)。
- **每个 Agent 必须负责本轮同步**：论文 Markdown 发生真实状态变化，**同一工作回合更新 [papers/INDEX.md](papers/INDEX.md)**；Delta 改变则同步 [knowledge/DELTA_INDEX.md](knowledge/DELTA_INDEX.md) 和相应论文引用；协作规范改变时同步 **[AGENTS.md](AGENTS.md)** 与 [RESEARCH_WRITING_STANDARD.md](RESEARCH_WRITING_STANDARD.md)。**结束前检查索引缺行、表格、链接、审批状态**。写共享文件前读最新 SHA，遇冲突合并，绝不覆盖其他 Agent。
- `CHANGELOG.md` 只记录**研究规范/架构变更与经确认的成果发布**，不充当逐篇研究流水账。

## 导航

- [AGENTS.md](AGENTS.md)：研究 Agent 接续规范（**先读**）
- [RESEARCH_WRITING_STANDARD.md](RESEARCH_WRITING_STANDARD.md)：**必读**写作风格、骨架优先、特化筛选和研究者审批
- [RESEARCH_PLAN.md](RESEARCH_PLAN.md)：研究问题及对话研读方式
- [papers/INDEX.md](papers/INDEX.md)：**跨研究 Agent 论文去重索引**；其他来源经研究者批准后再登记
- [papers/P001/](papers/P001/README.md)：第一篇单篇论文档案范例
- [papers/P002/](papers/P002/README.md)：CogAlpha 结构化档案与 Mermaid 架构图
- [knowledge/DELTA_INDEX.md](knowledge/DELTA_INDEX.md)：跨论文机制 Delta 知识库
- [synthesis/](synthesis/)：工作性问题视角及后续确认的综合成果
- [CHANGELOG.md](CHANGELOG.md)：架构与最终成果变更记录

旧版 `notes/` 逐篇笔记目录及模板已从当前分支删除，不再采用。

## 公开仓库边界

仓库为 **Public**。不提交公司内部材料、代码、数据、邮件、API Key、策略，也不上传未经授权可公开再分发的论文 PDF；原论文只登记公开链接及版权许可允许的内容。
