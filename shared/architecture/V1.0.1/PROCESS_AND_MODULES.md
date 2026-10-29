# V1.0.1｜单条候选从生成到归档的模块化流程

> **目标**：能为每一个实际执行模块单独实现、替换、测试和记录；此文是已确定的流程/输入输出契约，不是软件已经跑通的证明。

## 模块与执行顺序

| 模块 | 输入 | 输出 / 副作用 | 失败或阻断 |
|---|---|---|---|
| **M0 数据/文献来源** | Min Schema、分钟数据、来源 PDF/研报 | 原文定位、字段字典、`data_snapshot`、时间可用性 | 字段/许可缺失则仅记录、禁止假装存在 |
| **M1 Daily Curator** | 外部论文假设 + Min 或 Research 申请的中间表达式 | 源证据卡入 Knowledge；Daily 定义审核和相关性 `<0.6` 检查后可发布版本化 CSV | 字段、时间、计算、相关性未通过时不发布新特征 |
| **M2 统一读取 API（程序）** | Min / 文献 / Daily / Knowledge 的结构化目录 | 按需卡片、受控原文段落、Python 统计结果；可记录查询日志 | 不把整个 PDF/CSV 塞进 Prompt，不构造第五库 |
| **M3 Research Agent** | 当前任务、材料、`full/masked`、查询接口 | 因子假设、表达式/代码、依赖、父代和来源、可复现研究配置 | 不自行审核通过；生成后必须交程序 |
| **M4 Candidate Register** | 研究候选、版本/数据/随机种子/父代 | `factor_id` + `experiment_id`，在 Knowledge 注册并记录状态 `pending` | 失败也要保留记录，不等回测后才写 |
| **M5A Technical & Leakage Gate** | 真实字段、代码和时间依赖 | 独立核验数据可用性、可执行、信息时点与未来泄漏 | FAIL/BLOCKED 则止步，金融字段 `NULL` |
| **M5B Statistical Evaluator** | M5A PASS 的因子值、数据质量统计、Knowledge 已成功 Alpha 的实际因子 CSV | 非退化、覆盖率、异常/缺失、严格重复；仅对已成功胜者求最大绝对相关性 `<0.65`，记录胜者快照 | 无胜者时相关性子检查 `NO_REFERENCE`，仍检查其他统计项；失败不进入金融评价，计算方法未知时 `BLOCKED` |
| **M6 Financial Evaluator** | M5A 与 M5B 均 PASS 的因子 CSV、实际数据、标准版本与回测区间 | 按唯一评价口径计算 `ret/sr/dd/to/cost` 及必要的日级序列，全部写 Experiment | 执行失败状态另记；不能当作真实低效因子 |
| **M7 Qualification Flag** | 有效 M6 指标 | 两条硬门槛计算 `qualified`，成功即正式归档；失败为 `financial_fail` | 不用 Score 或人为再次选拔 |
| **M8 Knowledge Recorder** | 各模块的状态、输入输出、日志及文件路径 | 单个统一知识库中 Factor/Experiment/关系更新；所有成功和失败可追溯 | `NULL` 与 0 不同，写入失败需显式报错 |
| **M9 Replay / Evolution** | 先前真实经验、成功/失败及父子关系 | 下一候选/变异/交叉的任务与输入；再次从 M4 开始 | 不跳过 M5/M6，不写“已经完成”的伪结果 |
| **M10 Optional Score Tool** | 已保存的金融字段、评分口径 | 按需 Python 线性计算/排序，可以更换评分权重版本 | **不参与 M7 成功判定，也不触发额外回测** |

## 具体的一次 Episode

1. 初始化：锁定数据版本、知识版本、模型/工具配置、`run_id`、随机种子、暴露模式、预算、Eval 口径。
2. Research Agent 自主读取知识/特征目录，按需请求 Python 统计或来源章节；生成 Alpha 公式/代码。
3. **先注册实验**：立即保存 `factor_id / experiment_id / pending`、代码与依赖及数据版本。仅此时的“入库”指**留痕**，不意味着金融成功。
4. 恢复完整 Knowledge，先调用 M5A 技术/泄漏硬关，再由独立 M5B Statistical Evaluator 核查完整性与因子数值质量，并与 Knowledge 中已成功胜者逐一比较，要求 `max_abs_corr<0.65`。没有胜者时仅跳过相关性比较。失败、未知及引用的胜者快照均写回 Experiment，未通过则金融字段 NULL。
5. M5A 与 M5B 均 PASS 才运行独立 Financial Evaluator，输出金融原始指标以及用于复算的日收益、目标权重、换手数据；算出一项失败也要保留失败原因，不伪造 Ret/SR。
6. 只有完整有效金融指标可判定 `qualified = (ret > 0.03) AND (sr > 1)`。结果即为正式存档，失败也记全量可用指标。
7. 更新 Knowledge，按需形成 `qualified` 视图并供遗传进化；**Score 是以后需要排序才调用的工具**。
8. Research 若提议可复用 Daily 子表达式，交独立 Daily Curator 检查，不因为母 Alpha 表现好/坏自动决定准入。

## 模块边界中的三个重点

**一、存储不是执行。** Knowledge 负责保留记录，不负责自己计算未来信息、相关性、收益或回测。实际计算由独立程序执行并回写有版本的结果。

**二、第一关失败不是低收益。** `blocked/technical_fail` 的金融字段为 NULL；真正金融失败只能是完整有效的回测且 Ret 或 SR 未过线。复测同一因子创建**新的 Experiment**，绝不覆盖历史。

**三、Daily 的去相关 ≠ Alpha 的去相关。** Daily 的相关性门槛 `<0.6`；Alpha 只比较 Knowledge 已成功胜者，最大绝对相关性严格 `<0.65`，首次无胜者跳过此项。相关系数算法和样本对齐仍待冻结。并发时推荐在正式提交 `qualified=true` 前重新核验最新胜者快照，防止多个候选同时以空胜者库通过。
