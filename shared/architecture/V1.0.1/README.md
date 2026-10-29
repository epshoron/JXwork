# JXwork｜V1.0.1 当前拍板架构（2026-10-29）

> **设计已确认，尚未宣称代码已部署或通过真实数据验证。** 本目录为唯一有效架构入口。Research Loop v9 的四库、独立 Daily 沉淀 Agent、可配置 Research Agent、统一程序读取、full/masked、自主探索、独立未来信息硬关卡及遗传经验反馈全部保留；**新确认的两级检查、结果字段与成功判定以本目录为准**。旧图的“Score 决定晋级/另建 Alpha 库”等表述不再适用。

## 一句话

**四个逻辑库（Min、论文/研报、Daily、Knowledge），Research 候选先通过技术/统计关，再做昂贵金融评测，所有尝试统一进 Knowledge；通过金融硬门槛即正式成功，没有第五个 Alpha 库；Score 为独立的可选排序工具。**

## 权威文件（按职能拆分）

1. [RESEARCH_LOOP.md](RESEARCH_LOOP.md)：完整上下游流程图与两个回流循环。
2. [PROCESS_AND_MODULES.md](PROCESS_AND_MODULES.md)：执行次序、程序模块责任、独立接口与分支。
3. [GATES_AND_DECISIONS.md](GATES_AND_DECISIONS.md)：Alpha 两关、Daily 独立入库硬门槛、成功/失败定义与未冻结统计口径。
4. [KNOWLEDGE_AND_CSV_CONTRACT.md](KNOWLEDGE_AND_CSV_CONTRACT.md)：Factor、Experiment、Daily、成功标签、CSV 与复现字段。
5. [RESEARCH_INPUT_PROTOCOL_V1.md](RESEARCH_INPUT_PROTOCOL_V1.md)：full/masked、自主查阅、去重和实验记录。
6. [待定实现细节](OPEN_DECISIONS.md)：相关性口径、数据样本、并发与测试验收。
7. [当前专业研究 Agent 策略 V0.2（四范围 16 角色）](research_design/README.md)：M3的可替换研究分工，含[16份独立Alpha挖掘Prompt](research_design/prompting/README.md)，不修改评价规则。
8. [Research 调度与 Full/Masked 实施规范 V0](research_design/scheduling/README.md)：可替换的角色选择、轮转、预算、遮蔽和对照；不改16份Prompt。
9. [Overall Orchestrator 总编排实施规范 V0](orchestration/README.md)：仅模块衔接/状态/故障/验收，不重做S16/S17正在处理的M0/M1/M2/M4/M8或已定M5/M6。
10. [Evaluator V1 原始数学标准](../../evaluation/PORTFOLIO_SCORING_STANDARD.md)：横截面权重、VWAP、Return/SR/MDD/TO/成本；**Score 公式保留但不参与硬门槛**。

## 拍板的关键规则

- **全部候选留痕**：一生成就创建 `factor_id/experiment_id`，每一关 PASS/FAIL/BLOCKED、原因、运行版本可追溯；金融字段在没有运行 Evaluator 时必须是 `NULL`。
- **Alpha 第一关**：程序核验计算/字段、未来信息合法、完整性/有效性、严格重复和相关性等信号统计属性。失败就不做金融回测。**已确认：Alpha 只与 Knowledge 中内部真实实验通过金融硬门槛、已正式成功的胜者因子比较**。计算与各胜者的相关性并取最大绝对值，硬门槛严格 `<0.65`（等于也失败）；首次无胜者时仅跳过这个相关性子检查，其他技术/统计/金融门槛照常。具体相关系数算法和对齐样本尚未冻结。
- **Alpha 第二关**：独立 Evaluator 对第一关 PASS 的候选计算 Ret/SR/DD/TO/Cost；有效评测后严格 `Ret > 3%` **且** `SR > 1` 就标 `qualified=true`，这就是正式成功和归档，不需要额外选拔、Alpha 独立库或 Score。
- **Daily 特征门槛**：独立 Daily 沉淀 Agent 检查实际字段/时间/可复现/不重复，并对已有 Daily 特征执行**相关性严格小于 0.6** 的硬条件；统计方法、样本范围及空库行为尚待工程定义。否则不能声称自动通过。
- **Score 只按需**：既定 `Score = Ret + 0.05·SR − 0.1·DD − Cost_ann` 不在两关中运行，只有需要排序才按保存的字段和统一参数版本由 Python 计算。
- **库与档案不同**：`shared/A_alpha_mining/knowledge/` 是 D 系列论文研究机制卡，**不是**这里描述的运行时 Knowledge 数据库。后者保留所有 Alpha/Experiment 及外部作者报告，禁止混成已复现事实。

## 未冻结，但不得编造

评测 Ret 的收益口径应在接入公司数据时与 [Evaluator V1](../../evaluation/PORTFOLIO_SCORING_STANDARD.md) 对齐（原定义为年化**毛**收益）；Alpha 相关系数计算方式/样本、Daily 相关系数方法/样本、股票池、缺失/停牌、具体 CSV 布局、真实调用 API、物理数据库技术以及调度策略待测试后冻结。门槛数值（Ret 3%、SR 1、Alpha 相关 0.65、Daily 相关 0.6）本身已确认，**未确认的统计实现不能算“通过”**。

**Research与Daily职责明确分离**：16个专业Research Agent（A6/C5/B3/D2）各自拥有[独立Alpha Prompt](research_design/prompting/README.md)，只提出日频Alpha候选；独立M1 Daily Curator负责Daily中间特征的发现、构造、审核和发布。更换Prompt或角色分工不改变门槛和Evaluator。

**Meta Loop** 保留对 Prompt、Skills、工具、检索/工作流配置做受控优化的未来方向，当前尚未启动；研究内 Debug 不必等 Meta。
