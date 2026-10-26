# P006｜R&D-Agent-Quant：原文、代码与阅读边界

- **正式题名**：R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization
- **正式发表**：NeurIPS 2025, Datasets and Benchmarks Track，作者 Yuante Li、Xu Yang、Xiao Yang、Minrui Xu、Xisen Wang、Weiqing Liu、Jiang Bian
- **出版方页面**：[NeurIPS 2025](https://papers.neurips.cc/paper_files/paper/2025/hash/ac5c2b6e423883cbcacbcccf88491b78-Abstract-Datasets_and_Benchmarks_Track.html)
- **DOI**：[10.52202/085713-3967](https://doi.org/10.52202/085713-3967)
- **arXiv 原文**：[arXiv:2505.15155](https://arxiv.org/abs/2505.15155) · [HTML 全文](https://arxiv.org/html/2505.15155)
- **作者公开代码**：[microsoft/RD-Agent](https://github.com/microsoft/RD-Agent)（仓库同时包含通用 RD-Agent 等模块，不能把整个仓库都当作本文独占的实现）
- **论文用途**：研究 LLM/Agent 如何共同提出因子/预测模型假设、执行实现与回测，并自适应调配下一轮研究对象。

## 当前核验状态（2026-10-26）

- **已直接核对**：正式 NeurIPS 题录/摘要；arXiv §1、§2.1–2.5 的组件职责及反馈；**附录 A.1 Co-STEER 算法1、A.2 Contextual Thompson Sampling 算法2、C.1 模型与实验配置、E.1–E.5 Prompt 使用说明**；作者公开仓库中 `rdagent/scenarios/qlib/proposal/bandit.py`、`quant_proposal.py`、factor/model proposal 及部分 CoSTEER 实现。
- **尚待完整核查**：其余附录与全部消融的系统复核、论文对应代码版本固定、独立安装运行及结果复现、数据时点审计、与同领域前作的学术首创性边界。
- **内容标记**：这里仅有权威链接与客观机制骨架；贡献、特化缺点和我们自己的技术设想**须先在 LLM 对话内由研究者逐项批准**。
- **Public GitHub**：不上传公司材料、密钥或未经确认许可的论文 PDF。

**工程核验入口**：[arXiv §2](https://arxiv.org/html/2505.15155#S2) · [附录 A.1/A.2（Co-STEER / Bandit）](https://arxiv.org/html/2505.15155#Sx1) · [作者 bandit.py](https://github.com/microsoft/RD-Agent/blob/main/rdagent/scenarios/qlib/proposal/bandit.py)。

**论文与当前代码的口径边界**：论文描述 Bandit 根据研究动作带来的改进更新；当前 `bandit.py` 的 `EnvController.reward()` 根据8维指标的加权和计算反馈，尚未通过锁定版本与运行实验确认两者等价。当前 GitHub 默认分支持续演进，单个文件的静态核对不等于独立复现。
