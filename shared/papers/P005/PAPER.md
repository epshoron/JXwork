# P005｜原文及核验边界

**原始题名**：AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning  
**作者**：Peiqi Jiang, Fan Zhang, Xin Xu, Tianhao Chen, Can Yang  
**版本**：arXiv:2610.15488v1，2026-10-11 首次提交；截至 2026-10-21 作为预印本处理，不推断已经同行评审或正式发表。

- [arXiv 正式记录](https://arxiv.org/abs/2610.15488)
- [arXiv HTML 全文](https://arxiv.org/html/2610.15488)

## 本轮核验的原始材料

原文§3–4：市场状态、表达式 DSL、多轮工具调用、Retained Factor Pool（Eq. 5–9）、轨迹终端奖励（Eq. 10–11）与 GRPO 训练（Eq. 12–14）；§5：时间划分、三个运行的结果和单轮 GRPO 控制对照；Appendix A.1–A.8：相关性/稳定性定义、组合模型、市场信息处理、参数、数据与基线；Appendix B：效率、训练动态和池规模。

**关键证据区分**：离线训练阶段可以使用未来窗口作为 reward manager 的监督目标，但**推理时只向 Agent 暴露可知的历史与市场状态**（作者原文声明）；仍无独立代码复现与时点审计。GRPO 是参数优化，部署阶段的每日自适应不等于每日梯度训练。

**未进行的工作**：没有核查并运行源码，没有独立复现训练或回测，没有完成学术首创性全面查新。P005 的「多轮工具反馈 + 池级更新 + 整池轨迹 GRPO 训练」已于 2026-10-21 经研究者批准，并在 [ARCHITECTURE.md](ARCHITECTURE.md) / [D016](../../knowledge/deltas/D016_pool_trajectory_grpo.md) 归档；其他创新判断、独立不足与研究方案仍未获得审批，不另入库。

本公开仓库只存链接与独立概括，不转存无授权的论文 PDF。
