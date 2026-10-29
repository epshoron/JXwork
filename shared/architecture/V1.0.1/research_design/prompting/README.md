# Research Agent 中立 Prompt｜V0.1 草案（待审，未自动启用）

**目的**：为当前16个专业研究角色提供一套干净、可组合的研究指示。只有信息范围和研究问题边界不同，所有角色共用同一套研究规则和输出规范。不要把已有论文的具体因子公式或作者收益塞进公共Prompt。

| 文件 | 作用 |
|---|---|
| [SYSTEM_COMMON_V0.md](SYSTEM_COMMON_V0.md) | 共同研究指示；只约束真实性、合法数据、Daily粒度和独立假设 |
| [ROLE_PROFILES_V0.json](ROLE_PROFILES_V0.json) | 16个简短专业职责描述：研究焦点 + 排除边界，不给指标配方 |
| [EPISODE_INPUT_V0.md](EPISODE_INPUT_V0.md) | 每轮由程序提供合法可见数据、Daily特征、知识材料、预算 |
| [OUTPUT_SPEC_V0.md](OUTPUT_SPEC_V0.md) | 输出字段与候选/不可提出候选的语义 |
| [OUTPUT_SCHEMA_V0.json](OUTPUT_SCHEMA_V0.json) | machine-readable JSON Schema Draft 2020-12 格式约束草案 |
| [ASSEMBLY_AND_ISOLATION_V0.md](ASSEMBLY_AND_ISOLATION_V0.md) | 指示组装顺序、角色信息注入、Full/Masked隔离方式 |
| [REVIEW_CHECKLIST_V0.md](REVIEW_CHECKLIST_V0.md) | 未定工程接口及中立性/角色重叠验收 |

## 最小组装

1. 通用系统约束（System Common + Output Spec）。
2. 选定角色在ROLE_PROFILES_V0.json中对应的唯一 focus/boundary。
3. 本轮可见且授权的动态数据与研究材料（Episode Input）；full/masked真实过滤由程序负责。
4. 模型以Schema生成候选或no_candidate；下游独立Evaluator与Knowledge负责核验和记账。

**版本状态**：提示词可更换，角色数量仍采用Role Taxonomy V0.2的A6/C5/B3/D2；本目录不修改已拍板Daily/Alpha准入标准。该Prompt只在代码接入并通过测试后才可作为运行时正式版本，当前是供审查的首稿。

相关：[当前16角色](../ROLE_TAXONOMY.md) · [Daily输出接口](../ROLE_OUTPUT_CONTRACT.md) · [Research输入协议](../../RESEARCH_INPUT_PROTOCOL_V1.md)。