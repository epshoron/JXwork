# T003｜原文、版本和核查边界

**题名**：Agent Lightning: Train ANY AI Agents with Reinforcement Learning  
**作者**：Xufang Luo、Yuge Zhang、Zhiyuan He、Zilong Wang、Siyun Zhao、Dongsheng Li、Luna K. Qiu、Yuqing Yang  
**原始来源**：[arXiv:2508.03680](https://arxiv.org/abs/2508.03680)，2025-08-05 初次提交；本档按其**2025 原论文**理解。  
**研究机构**：Microsoft Research。

## 核对路径

- [原文 HTML 全文](https://arxiv.org/html/2508.03680) · [arXiv 题录及版本](https://arxiv.org/abs/2508.03680)。
- **§3.1–3.2、Fig.2**：状态、组件调用、`(input_t, output_t, reward_t)` 数据接口、Agent→训练 transition 抽取。
- **§3.3、Fig.3**：LightningRL 先在 LLM 调用之间分配轨迹最终奖励，再在调用内部接单轮 RL。**在当前实验实现中所有调用分配同一个终端 return R**；不把可扩展的 credit assignment 说成已实现动态归因。
- **§3.4、Fig.4**：训练 Server + 现有 Agent Runtime Client 解耦、OpenAI-like 模型端点、trace 采集、错误处理、AIR 中间奖励。
- **§4、Table 1 / Figs.5–7**：LangChain/Spider、OpenAI Agents SDK/MuSiQue、AutoGen/Calc-X 三个原作者实验，准确率/奖励曲线均是**作者报告**，不是我们测出的性能。
- **§5.2**：作者关于更多优化方法（含自动 Prompt 优化）、改进 credit assignment 和服务体系的展望；与已经完成的实验证据区别对待。

## GitHub 代码注意

- 原始项目主页：[microsoft/agent-lightning](https://github.com/microsoft/agent-lightning)。
- **仓库在 2026 年升级为 v1.0 并重构**，对应另一份研究报告 [arXiv:2608.17528](https://arxiv.org/abs/2608.17528)。本档不混用两个版本的系统架构、代码目录和实测数字。若未来研究 v1.0，应明确是同一项目的**新版本不同论文**，先查重再决定是否独立研究。
- 目前**未运行**训练代码、未独立复现实验、未核算每条曲线；实证外推到用户的 CLI + Executor 架构、模型 API 权限与资源成本仍属开放问题。

**审批状态**：研究者于 2026-10-22 明确批准 [2 项特色机制](ARCHITECTURE.md) 与 [对应 2 项特化不足](IDEAS.md)，经严格去重分别归档 [TD008](../../knowledge/deltas/TD008_agent_call_transition_lightningrl.md)、[TD009](../../knowledge/deltas/TD009_role_selected_agent_training.md)。未批准新工程方案；无独立复现，不称学术首次。
