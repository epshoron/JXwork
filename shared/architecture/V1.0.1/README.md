# JXwork｜V1.0.1 当前唯一拍板架构

> **2026-10-29 确认**：最新 [Research Loop v9 双流程图](RESEARCH_LOOP.md) 正式替代旧版 `dual_loop_v1.0.1` 的 Research 侧设计。旧版退出当前工作树、可从 Git 历史查阅。架构已确定 ≠ 已实现/验证。

## Research Loop

Min 原始分钟数据 + 人工收录论文/研报 → 独立 Daily 沉淀 Agent → Daily 中间特征及知识库 → 统一**程序**读取接口 → Research Agent（数量 N 待定）自主研究与生成 → 后验全库去重 → 独立未来信息/数据泄漏硬关卡 → 独立 Evaluator → 全部成功、失败、阻断及实验结果记录入知识库 → 可复用中间特征申请 Daily 准入 / 历史候选参与遗传进化。所有候选和遗传子代都必须通过相同硬关卡。

**四库且仅四库：** Min、论文/研报、Daily、知识库，属于逻辑职责，并不代表一定采用四套物理数据库。知识库区分外部作者报告 `external_reported` 与内部真实执行 `internal_executed`。Daily 不是正式 Alpha 因子池，遗传种群也不是正式因子池。

输入可按 [V1.0.1 现行协议](RESEARCH_INPUT_PROTOCOL_V1.md) 使用 `full` / `masked` 可复现曝光；不允许遮蔽客观数据字段、时间可用性、代码安全和评分规则。现有 [单因子 Evaluator V1](../../evaluation/PORTFOLIO_SCORING_STANDARD.md) 口径不变，不等于池级边际贡献规则已经决定。

## Meta Loop

保留未来通过受控实验改进 Prompt、Skills、工具、搜索和 Agent 配置的方向，**当前尚未启动**，不把旧 Meta 实现细节或参数训练默认列为已确认开发任务。

## 未冻结事项

Agent 数/角色、模型 API、物理存储、检索选型、随机遮蔽比例、Daily 特征准入量化阈值、遗传调度与正式因子池晋级策略尚待研究和实测。Daily 准入 Prompt v0 仍是未审批候选，留在非共享的 `assistant/handoffs/`，不作为正式云端指令。
