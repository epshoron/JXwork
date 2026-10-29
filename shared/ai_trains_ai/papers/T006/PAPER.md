# T006｜Agent4Sci 原始论文、版本与核验边界

**论文题名**：*Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?*  
**作者**：Ming Zhong、Stacy Li、Nicholas Carlini、Matthew Jagielski  
**原始记录**：[arXiv:2610.28763](https://arxiv.org/abs/2610.28763)，2026-10-20 首次提交（本轮按 v1 记录）。作者在摘要下的声明提到 NeurIPS 2026 Evaluations and Datasets Track 接收情况；尚未另行核对正式会议题录，不据此写成已验证的正式出版页。  
**论文 PDF**：[arXiv PDF 入口](https://arxiv.org/pdf/2610.28763) · [arXiv HTML 入口](https://arxiv.org/html/2610.28763)  
**作者公开实现**：[maszhongming/agent4sci](https://github.com/maszhongming/agent4sci) · [作者数据集](https://huggingface.co/datasets/MingZhong/agent4sci)。代码/数据作为**本论文配套核验与复现入口**，没有另行认领非论文研究来源。

## 本轮可证实的材料范围（2026-10-26）

**访问限制必须如实记录**：本轮工具对 arXiv 的 HTML / PDF 正文直接访问失败。因此，**没有声称直接看到或逐页检查原始 PDF、公式、图片细节和全部附录**。实际交叉核查的是：

1. arXiv 题录／作者摘要（经公开检索结果定位原始记录），确认研究问题、20 benchmarks / 11 domains、主要平均改善及三个 Skills 的作者结论。
2. [作者仓库 README](https://github.com/maszhongming/agent4sci) 公开的运行阶段、数据隔离、Docker 环境、Skill 启用与调度说明。该仓库会继续演进，**当前 README 的 CLI 默认模型配置不得冒充 2026-10-20 原论文的全部实验版本**。
3. 按章节、图表编号标注的公开[论文正文索引转录](https://paperlayer.ai/abs/2610.28763v1)（**非第一手 PDF 阅读**）用于交叉追踪：§2.1–2.4（任务筛选、先导 gaming、隔离评测）；§3.1–3.3 / Fig.3–4 / Table 5（预算、主结果、Agent 行为）；§4.1–4.3 / Table 2（三种 Skills、整体改善）；Appendix A（作者局限）、Appendix C.3/C.4（方差、只允许调参的对照）、Appendix D.1（Skill 细节）。这些章节级陈述尚应以原始 PDF 复核。
4. [另一公开展示](https://thelatestinai.com/papers/2610.28763) 所转录的 Figure 2、Table 2 与 Appendix 部分表格可作定位辅助，**不替代原文核验**。

## 目前可以下结论的与不可推断的事情

- **可以客观说明**：Agent4Sci 是研究型编程 Agent 的科学 ML 任务改进测试平台；论文提供经核查的起始基线、封存的独立测试评分、轨迹审计，以及三种**外部预设** Skills 的实验比较。
- **必须区分更新对象**：研究 Agent 可以重新训练/改写**科学任务模型**；论文没有据此更新研究 Agent 自身基础 LLM 的权重，也没展示由上层 Agent 自发演化三种 Skills。
- **只属于作者报告**：20 benchmark 的分数、Opus 10.4% → 20.1%、Codex 4.4% → 8.1%，以及没有审计发现违规；不表示我们独立复现或证明审计绝对完备。
- **待原始 PDF 直接核实**：图/表排版及数值逐项复核，附录中全部实验条件、统计口径与方差，三个 Skill 是否有完整单独消融、工具/版本快照与定时触发的确切实现。
- **作者明示的范围（附录 A；仍需原始 PDF 对照）**：以已有基线为起点不覆盖整个科研流程；长时运行方差妨碍将成绩当成稳定排行榜；单 Agent harness 有覆盖边界；保留集和审计无法排除所有行为；Skills 迁移性与研究员基线仍有局限。
- **未做**：下载论文到公开仓库、训练/运行代码、重现科研模型、验证与用户自己的 Executor 适配性、完成学术首次提出查新。

**审批状态**：当前只允许已核客观来源与骨架归档。[README](README.md) 不包含未经研究者批准的正式创新/特化不足判断；`ARCHITECTURE.md`、`IDEAS.md` 和新 TD 机制卡均暂不创建。后续先取得逐项批准并严格跨方向语义去重。

**公开安全**：仓库为 Public，不上传公司内部资料、账号/密钥、私有数据或无授权再分发的 PDF。
