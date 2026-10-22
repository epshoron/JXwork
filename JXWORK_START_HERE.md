# JXwork｜研究仓库快速入口（2026-10-22）

> 本文件是**导航指针**，不是论文知识正文，也不覆盖仓库实时内容。研究状态以 GitHub 最新文件为准。

**仓库：** https://github.com/epshoron/JXwork （`main`）

## 先找方向，再读文件

| 方向 | 研究任务 | 论文索引 | 机制知识 |
|---|---|---|---|
| A｜AI Agent 因子挖掘 | LLM/Agent 如何发现量化 Alpha、利用反馈改进搜索 | [papers/INDEX.md](papers/INDEX.md)（P001–P010） | [knowledge/DELTA_INDEX.md](knowledge/DELTA_INDEX.md)（D001–D020） |
| B｜AI 如何训练 AI | 上层 AI 反馈优化下层 Executor 的 Prompt/Skills/工具/记忆策略 **与** SFT/RL 参数训练的比较 | [ai_trains_ai/papers/INDEX.md](ai_trains_ai/papers/INDEX.md)（T001、T005 已归档骨架；其他进度见实时索引） | [ai_trains_ai/knowledge/DELTA_INDEX.md](ai_trains_ai/knowledge/DELTA_INDEX.md)（TD001、TD002 已审；后续继续编号） |

- **先读 [AGENTS.md](AGENTS.md)**：跨方向审批、来源准入、去重、并行同步、安全边界。
- **再读 [RESEARCH_PLAN.md](RESEARCH_PLAN.md)**、[RESEARCH_WRITING_STANDARD.md](RESEARCH_WRITING_STANDARD.md)：三个研究阶段与写作/审批要求。方向 B 的研究场景和两条优化路线详见 [ai_trains_ai/README.md](ai_trains_ai/README.md)，不要先把“训练”限定为修改权重，也不要把自动改 Prompt 当成权重训练。
- [README.md](README.md)：总导航；[CHANGELOG.md](CHANGELOG.md)：最新结构或已审批成果变更。
- 在各自的 `papers/T00X` 或 `papers/P00X` 中，`README.md` 是系统骨架、`PAPER.md` 是来源证据、`ARCHITECTURE.md` 是获批特色机制、`IDEAS.md` 是获批特化不足；对应知识卡位于各方向的 `knowledge/deltas/`。
- 两方向的 `synthesis/` 只放**研究者确认**的跨论文综合成果，不是会话笔记。

## 继续研究的硬要求

原文核实后可自主归档**论文骨架**并向研究者讲解；非论文学术来源必须先获研究者批准。创新、特化不足、原创研究想法、Delta 卡必须**逐项获批并严格语义去重**。**每个 Agent 同一回合同步其方向内的论文 Markdown 与索引、Delta 卡与索引**；写公共文件前先刷新 SHA，冲突合并。

不沿用旧指针中的 `notes/TEMPLATE.md`：该旧路径已删除。仓库是 **Public**，不得上传公司内部资料、代码、API Key 或未经许可再分发的 PDF。
