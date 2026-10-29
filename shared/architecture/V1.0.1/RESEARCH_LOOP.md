# Research Loop｜V1.0.1 当前正式流程图

> 更新：2026-10-29。设计已拍板，尚未实际部署验证。**以下流程优先于 10 月 28 日的旧图**；保留四库及 Full/Masked、后验去重、未来信息门禁、实验回流和遗传搜索，但不把 Score / 单独 Alpha 库作为必经步骤。

## 主流程

```mermaid
flowchart TD
  MIN[("Min 库：分钟行情 / 可用时点")]
  PAP[("论文研报库：原文与作者证据")]
  CUR["Daily 沉淀 Agent<br/>公式/依赖/合法性审查"]
  DAG{"Daily 检查<br/>含 corr ＜ 0.6"}
  DAILY[("Daily Feature<br/>已发布 Base + Curated / 数值")]
  KNOW[("Knowledge 库<br/>Factor + 所有 Experiment + Episode<br/>状态/原因/指标/阅读历史")]
  READER["统一程序读取<br/>目录、查询、按需 Python/原文"]
  RA["16 个专业 Research Agent<br/>只生成日频 Alpha 候选；人数可配置"]
  CAND["候选注册<br/>factor_id / experiment_id"]
  ST{"第一关 A：技术/未来信息检查<br/>数据字段/可执行性"}
  STAT{"第一关 B：Statistical Evaluator<br/>质量/重复/胜者相关性 ＜ 0.65"}
  EVAL["第二关：独立金融 Evaluator<br/>Ret/SR/DD/TO/Cost"]
  GATE{"Ret ＞ 3% 且 SR ＞ 1 ?"}
  FAIL1["第一关失败 / 阻断<br/>金融字段 NULL"]
  FAIL2["第二类金融失败<br/>保留所有已测字段"]
  OK["正式成功<br/>qualified=true"]
  EVOLVE["经验复盘 / 遗传变异<br/>下一轮候选"]
  REVIEW["Daily Review<br/>全部审核和无候选记录"]
  MIN --> CUR
  PAP --> CUR
  CUR --> DAG
  DAG -->|"确认合格"| DAILY
  DAG -->|"审核留痕"| REVIEW
  DAG -->|"拒绝/阻断/无候选"| REVIEW
  PAP --> READER
  DAILY --> READER
  KNOW --> READER
  MIN --> READER
  READER --> RA
  RA --> CAND
  CAND --> KNOW
  CAND --> ST
  ST -->|"FAIL / BLOCKED"| FAIL1
  ST -->|"PASS"| STAT
  STAT -->|"PASS"| EVAL
  STAT -->|"FAIL / BLOCKED"| FAIL1
  KNOW -.->|"只读取成功 Alpha；无胜者跳过相关比较"| STAT
  EVAL -->|"有效评测"| GATE
  EVAL -->|"执行失败"| FAIL1
  GATE -->|"否"| FAIL2
  GATE -->|"是"| OK
  FAIL1 --> KNOW
  FAIL2 --> KNOW
  OK --> KNOW
  KNOW --> EVOLVE
  EVOLVE --> CAND
```

## 四库含义

**最新四库读写与研究日志实施契约**：[FOUR_LIBRARY_RUNTIME_CONTRACT.md](FOUR_LIBRARY_RUNTIME_CONTRACT.md)。图中的 M1 审核历史写入 Daily Review，**不**把审核失败误写入 Knowledge Experiment；文献结构化、全量自主检索和三模式随机探索由本契约补充。


- **Min**：不可随实验效果重写的真实分钟原始数据/字段/可用时点。
- **论文/研报**：人为收集的原始来源，作者陈述必须带 `external_reported` 标签。
- **Daily**：由独立 Daily Curator 自主构造与审核的日频中间特征，具有合法定义、依赖、时点、数据版本和物化 CSV；相关性 `<0.6` 是它自己的准入条件。Research Agent 只能读取已发布 Daily，不负责申请、构造或入库。
- **Knowledge**：因子定义 + 每次真实测试与全链失败/成功记录；其中 `qualified=true` 的实验可以直接查询为正式成功 Alpha。Alpha 与当前 Knowledge 中已成功胜者逐一比较最大绝对相关性，严格 `<0.65`；首个无胜者时只跳过这一比较。它不需要额外的物理或逻辑 Alpha 库。外部作者实验与内部 `internal_executed` 结果分离。

**职责隔离**：Research Agent 的日频 Alpha 输出与 Daily 库的中间特征不能混称。当前 Research 使用 [16份独立专业 Alpha Prompt](research_design/prompting/README.md)（草案未试跑）；Daily Curator 是独立 M1。两者可分别更换内部 Prompt，不影响统一技术、统计与金融评价。

## 避免生成阶段锚定

研究者可以选择 `full` 或按 `seed` 重现的 `masked` 信息暴露。只屏蔽部分已有 Alpha 结论/谱系，不遮蔽客观数据字段、数据时点、Evaluator 标准和工具安全。候选生成后恢复完整知识范围做去重与前置统计检查。查询由 Research Agent 自行调用统一接口，**不强制增加检索/材料分配 LLM**。

## 独立模块、按需工具

[模块与状态](PROCESS_AND_MODULES.md) · [两阶段门槛](GATES_AND_DECISIONS.md) · [CSV 字段契约](KNOWLEDGE_AND_CSV_CONTRACT.md)。每一次候选、阻断、财务/金融评价和遗传子代，都走相同的前置程序关卡；禁止 Agent 自行宣布其已通过或已入库。
