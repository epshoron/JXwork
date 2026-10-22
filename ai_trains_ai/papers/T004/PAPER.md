# T004｜ADAS 原论文与证据边界

**原文**：[Automated Design of Agentic Systems（ICLR 2025 正式论文题录）](https://proceedings.iclr.cc/paper_files/paper/2025/hash/36b7acf6f6010652b3f2a433774a66fe-Abstract-Conference.html)；[正式 PDF（34 页）](https://proceedings.iclr.cc/paper_files/paper/2025/file/36b7acf6f6010652b3f2a433774a66fe-Paper-Conference.pdf)；[arXiv:2408.08435](https://arxiv.org/abs/2408.08435)（2024-08-15 初稿、2025-03-02 v2）。作者 Shengran Hu、Cong Lu、Jeff Clune。作者公开代码 [ShengranHu/ADAS](https://github.com/ShengranHu/ADAS) 仅作为论文附带复现入口，**并未作为第二份独立非论文来源认领**。

## 研读和原文核查范围

- 摘要/§1、§2/Figure 2：ADAS 抽象为搜索空间、搜索算法、评价函数；Python 代码空间理论表达力不等于实际搜索能覆盖所有可能 Agent。
- §3/Figure 1、Appendix C/D/I：Meta Agent 以历史设计/评价档案为条件，先写设计理念及 `forward(taskInfo)` 代码，经过两次设计反思；运行错误时可以反思修复至多五轮；再用实际任务验证并保存代码、描述与成绩。基础 FM/Info/工具 API 由固定框架提供。
- §4/Figure 3、Table 1–3：ARC、DROP、MGSM、MMLU、GPQA；跨领域、跨底层模型测试；GPT-4 担任设计 Meta Agent，GPT-3.5 运行候选系统，ARC 搜索 25 轮，其余各目标领域独立搜索 30 轮。
- Appendix J/Table 6：无人工种子初始化对照；MGSM 空初始化 67.5，高于带种子 53.4，其他 3 个域一般反向，不得将历史档案量与性能单调关系当作已证实。
- §5–6 与 Appendix K：作者对高阶 Meta Agent 自改、上线后持续优化和多目标成本/安全优化讨论是**未来方向**；原文描述隔离执行与人工代码审核，论文时期实验 API 成本约 ARC $500/轮完整搜索、其他域约 $300/次。

## 明确界限

1. **没有独立运行论文代码、重现指标或做当前模型复测**；所有数字都是论文报告。
2. 本篇的可更新工件是**下层 Agent 的 Python 调用程序/流程**及搜索档案，而不是执行 LLM 权重。上层 Meta Agent 也未被所描述算法更新权重。
3. 不是整个 Agent 生产部署体系的自主管控证明：安全依赖实验约束、隔离与人工审查；任务目标和评价指标为研究者预先设定。
4. **用户尚未批准 T004 的具体创新、特化不足、原创方案或 TD 机制卡**；这里只归档可核对的论文结构，不擅自推进阶段二/三。

[返回 T004 架构](README.md) · [方向 B 论文 Index](../INDEX.md)。
