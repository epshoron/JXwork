# 方向 B｜论文 Index：AI 如何训练 AI

> **初始化于 2026-10-22；各来源的真实进度以本表为准。** 这里专用于 AI trains AI 方向的去重和真实进度；旧方向的论文见 [根目录 papers/INDEX.md](../../A_alpha_mining/papers/INDEX.md)。

| 编号 | 原始论文题名 | 权威原文／唯一标识 | 实际研究状态 |
|---|---|---|---|
| [T001](T001/README.md) | Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution | [ICML 2024 / PMLR 235](https://proceedings.mlr.press/v235/fernando24a.html) · [arXiv:2309.16797](https://arxiv.org/abs/2309.16797) | **原始机制与 [P/M/H 骨架](T001/README.md) 已归档；[两项已审特色](T001/ARCHITECTURE.md)＋[对应两项特化不足](T001/IDEAS.md) 已获批准，机制入库 TD001/TD002**；未独立复现/未宣告学术首创（2026-10-22） |
| [T002](T002/README.md) | GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning | [ICLR 2026 正式论文](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0e9e708b6f48e14fd0ac29e167413f76-Abstract-Conference.html) · [arXiv:2507.19457](https://arxiv.org/abs/2507.19457) | **[原文客观架构](T002/README.md)及证据已核；[TD003–TD005 三项特色](T002/ARCHITECTURE.md)与[各自对应三项待核问题](T002/IDEAS.md)已获研究者批准并归档**；未独立复现、不声称学术首创（2026-10-22） |
| [T003](T003/README.md) | Agent Lightning: Train ANY AI Agents with Reinforcement Learning | [arXiv:2508.03680（2025 原论文）](https://arxiv.org/abs/2508.03680) · [Microsoft Research 项目](https://www.microsoft.com/en-us/research/project/agent-lightning/) | **[2025 原论文骨架](T003/README.md)及[来源](T003/PAPER.md)已归档；[2 项已批准特色](T003/ARCHITECTURE.md)＋[配对 2 项特化不足](T003/IDEAS.md)获批，TD008/TD009 已严格去重入库**；未独立复现、2026 v1.0 不混入、学术首创未定（2026-10-22） |
| [T004](T004/README.md) | Automated Design of Agentic Systems | [ICLR 2025 官方论文](https://proceedings.iclr.cc/paper_files/paper/2025/hash/36b7acf6f6010652b3f2a433774a66fe-Abstract-Conference.html) · [arXiv:2408.08435](https://arxiv.org/abs/2408.08435) | **[客观骨架](T004/README.md)与[原文证据](T004/PAPER.md)已核；[TD010–TD011 两项特色机制](T004/ARCHITECTURE.md)及[各自对应两项特化问题](T004/IDEAS.md)已获研究者批准并归档**；未独立复现、不宣称学术首创（2026-10-22） |
| [T005](T005/README.md) | Self-Rewarding Language Models | [ICML 2024 / PMLR 235](https://proceedings.mlr.press/v235/yuan24d.html) · [arXiv:2401.10020](https://arxiv.org/abs/2401.10020) | **[原文骨架](T005/README.md)已归档；[2 项创新与对应 2 项不足](T005/ARCHITECTURE.md)已批准，[特化问题](T005/IDEAS.md)已存档，TD006/TD007 已去重入库；原文 Table 4 与 §6 已核，风险未独立实证**（2026-10-22） |

| [T006](T006/README.md) | Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?（Agent4Sci） | [arXiv:2610.28763](https://arxiv.org/abs/2610.28763)（2026-10-20） · [作者项目](https://github.com/maszhongming/agent4sci) | **[客观实验骨架](T006/README.md)与[原文/核验范围](T006/PAPER.md)已归档**：三阶段研究/封存评分/审计、三种外加 Skills 与作者报告结果；**arXiv PDF/HTML 本轮无法直接阅读，仍待原始全文复核；创新、特化不足与 TD 均未审批，未独立复现**（2026-10-26） |

## 认领与同步

- 用 `T001`、`T002`…… 编号；先检查**两个方向**的索引、 DOI / arXiv / 题名，避免撞号与无价值重复登记。
- **正式学术论文**：原文核实后可自主归档 `T00X/README.md`（自绘系统骨架）和 `PAPER.md`（来源边界），并**同一回合同步本索引**；仅认领不能写成已读完。
- **非论文材料**：向研究者证明来源价值、获明确批准后方可建档或登索引；不可用“客观骨架”绕过准入。
- **特色机制、特化不足、研究者原创想法以及机制 Delta**：逐项取得明确批准，且与**两方向已收录内容**严格语义去重后才记录；不抢跑跨论文综合。
- 新增、变更、撤回档案时同步本索引；有关机制卡同时同步 [本方向 Delta Index](../knowledge/DELTA_INDEX.md) 和对应论文引用。修改共享文件前读取最新版 SHA，冲突时重新读取并合并。

[本方向入口](../README.md) · [统一协作规范](https://github.com/epshoron/JXwork/blob/main/assistant/AGENTS.md)
