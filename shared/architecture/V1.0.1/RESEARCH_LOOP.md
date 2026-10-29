# Research Loop｜V1.0.1 当前正式流程图

> 更新：2026-10-29。设计已拍板，尚未实际部署验证。**以下流程优先于 10 月 28 日的旧图**；保留四库及 Full/Masked、后验去重、未来信息门禁、实验回流和遗传搜索，但不把 Score / 单独 Alpha 库作为必经步骤。

## 主流程

```mermaid
flowchart TD
  MIN[("Min 库：分钟行情 / 可用时点")]
  PAP[("论文研报库：原文与作者证据")]
  CUR["Daily 沉淀 Agent<br/>公式/依赖/合法性审查"]
  DAG{"Daily 检查<br/>含 corr ＜ 0.6"}
  DAILY[("Daily 库<br/>定义/版本/CSV")]
  KNOW[("Knowledge 库<br/>Factor + 所有 Experiment<br/>状态/原因/指标/谱系")]
  READER["统一程序读取<br/>目录、查询、按需 Python/原文"]
  RA["Research Agent<br/>N 可配置"]
  CAND["候选注册<br/>factor_id / experiment_id"]
  ST{"第一关：程序技术/统计检查<br/>未来信息/质量/重复/相关"}
  EVAL["第二关：独立金融 Evaluator<br/>Ret/SR/DD/TO/Cost"]
  GATE{"Ret ＞ 3% 且 SR ＞ 1 ?"}
  FAIL1["第一关失败 / 阻断<br/>金融字段 NULL"]
  FAIL2["第二类金融失败<br/>保留所有已测字段"]
  OK["正式成功<br/>qualified=true"]
  EVOLVE["经验复盘 / 遗传变异<br/>下一轮候选"]
  MIN --> CUR
  PAP --> CUR
  CUR --> DAG
  DAG -->|"确认合格"| DAILY
  DAG -->|"拒绝/未决"| KNOW
  PAP --> READER
  DAILY --> READER
  KNOW --> READER
  MIN --> READER
  READER --> RA
  RA --> CAND
  CAND --> KNOW
  CAND --> ST
  ST -->|"FAIL / BLOCKED"| FAIL1
  ST -->|"PASS"| EVAL
  EVAL -->|"有效评测"| GATE
  EVAL -->|"执行失败"| FAIL1
  GATE -->|"否"| FAIL2
  GATE -->|"是"| OK
  FAIL1 --> KNOW
  FAIL2 --> KNOW
  OK --> KNOW
  KNOW --> EVOLVE
  EVOLVE --> CAND
  RA -.->|"新可复用中间特征申请"| CUR
```

## 四库含义

- **Min**：不可随实验效果重写的真实分钟原始数据/字段/可用时点。
- **论文/研报**：人为收集的原始来源，作者陈述必须带 `external_reported` 标签。
- **Daily**：有合法定义、依赖、时点、数据版本和物化 CSV 的日频中间特征。Daily 相关性门槛是**其自身准入**，不是 Alpha 盈利评价。
- **Knowledge**：因子定义 + 每次真实测试与全链失败/成功记录；其中 `qualified=true` 的实验可以直接查询为正式成功 Alpha。它不需要额外的物理或逻辑 Alpha 库。外部作者实验与内部 `internal_executed` 结果分离。

## 避免生成阶段锚定

研究者可以选择 `full` 或按 `seed` 重现的 `masked` 信息暴露。只屏蔽部分已有 Alpha 结论/谱系，不遮蔽客观数据字段、数据时点、Evaluator 标准和工具安全。候选生成后恢复完整知识范围做去重与前置统计检查。查询由 Research Agent 自行调用统一接口，**不强制增加检索/材料分配 LLM**。

## 独立模块、按需工具

[模块与状态](PROCESS_AND_MODULES.md) · [两阶段门槛](GATES_AND_DECISIONS.md) · [CSV 字段契约](KNOWLEDGE_AND_CSV_CONTRACT.md)。每一次候选、阻断、财务/金融评价和遗传子代，都走相同的前置程序关卡；禁止 Agent 自行宣布其已通过或已入库。
