# V1.0.1｜四库读写与研究运行实施契约（2026-10-29）

> **状态**：本轮已拍板的逻辑设计，供云端/本地 Agent 实现；不代表已写代码、部署或用真实数据验收。原有 Alpha/日频准入、技术/泄漏检查及金融评价门槛保持不变；未冻结参数不得自行认定通过。
> **公开仓库边界**：只能公开架构与匿名字段语义，不得提交公司原始数据、内部文件路径、实际公司资料报告、密钥、收益标签、运行数值或未授权 PDF。

## 0. 最高层原则

- **只保留四个逻辑库**：Min、Papers/Reports、Daily、Knowledge。物理数据库和 CSV/Parquet/JSONL 形式由环境决定，不强制每一类对象对应一张 SQL 表。
- **M2 统一程序化读取**：只负责 list/search（可分页全量授权目录及筛选）、get_detail（按 ID 取完整定义/文献原文章节）、get_values（授权数值/Pandas 统计）。M2 不是第五个库，不增加“选论文”LLM、固定 Top-K 检索 Agent 或复杂知识图谱。
- Research Agent 自行查阅、自行选论文和构想 Alpha；现有 16 个专业角色的研究产物仍是每股票每日日频 Alpha，不负责 Daily 提取或审核。独立 M1 Daily Curator 负责 Daily 研究与发布。
- 大规模行情和因子数值由受控 Python/计算程序处理，LLM 只读取目录、语义定义、有限统计和必要原文段落。

## 1. Min：默认字段说明，可选历史行业

- 当前确认用于日内价格计算的原始字段为**分钟 Close(C)**。不能虚构分钟 O/H/L/V/VWAP；实际时间跨度、存储位置、市场日历、缺失/停牌规则由公司环境的运行时 schema 核实。
- Research Agent 默认只获知 C 的字段、时间索引、覆盖和最早可用时点；**不强制阅读 Min**。所有专业 Prompt 应明确存在可选历史 `sector_code` / `group_code` 分类。
- 只给 Research Agent 受控的日频行业 pandas/DataFrame 视图，可以按历史日期、股票、类别做筛选/groupby。分类代码是类别而非大小排名；代码到行业名称/层级标准尚待真实映射；严格按历史 as-of 日期读取，禁止未来分类回填。
- **不向生成 Agent 提供原始分钟 C 大表自由浏览。** 生成 Alpha 或核验公式需要分钟 C 时由受控后台计算工具读取、执行并返回必要统计/结果；M1 与评价模块在获授权后仍可读取底层数据。
- universe 仅供合法样本/计算筛选，复权因子的方向必须核实；未来 VWAP 收益数据严格属于标签/评价端，生成端不可见。

## 2. 文献库：独立结构化处理，Agent 自主探索

- 同一个库有三级读取深度：**Index 全量目录**（ID、标题、类型、主题、来源、版本、处理状态）→ **Research Card**（金融现象、假设、公式/方法、数据需求、时点、作者正/负结果、局限、证据页码和核验状态）→ **Original**（授权的 PDF/Markdown 原文/章节）。原始研究资料目录和 ID 保留不重排。
- **建立独立的文献结构化模块**，负责读原文、抽取结构化卡、回溯证据及增量更新；不负责选论文、替 Agent 设定研究任务或宣称内部验证。缺公式/仅摘要/未核实原文时明确标缺，不补造。
- Agent 能遍历**所有当前授权文献目录**（大目录分页），不按角色只分配“匹配论文”，不强行使用固定 Top-K；Agent 自己筛选、一次**重点精读一篇**，然后可接着精读下一篇，不是每轮只能读一篇。
- 文献的跨篇关系可通过主题/金融机制、source_id 和真实关联的 Daily/Factor ID 表达；Daily 不是唯一关联载体；V1 不建独立知识图谱。

### 三种等概率研究模式

| research_mode | 倾向 | V1 概率 |
|---|---|---|
| free | 自由探索、自选论文 | 1/3 |
| incremental | 优先未精读或累计精读较少的论文 | 1/3 |
| cross_domain | 主动考察跨领域文献是否能补充本专业研究 | 1/3 |

- 调度器在每次 run_id 开始前按 seed 随机抽**研究倾向**，而非替 Agent 直接抽/指定论文。三个模式只改变考察优先级，不改变专业最终输出边界，也不强制凑论文或因子。
- `research_mode` 与已有 `exposure_mode=full/masked` 是**独立配置轴**，不可混淆。V1 不用 MCTS/GRU/Bandit 调权；未来 Meta Loop 可在有真实有效 Alpha 产出和研究成本记录后做受控优化，当前不实现。

### 文献精读历史

- **结构化处理完成 ≠ Agent 已经精读。** 运行时对真实阅读行为增量留痕：paper_id、run_id、role_id、阅读层次（目录/卡/章节/精读）、章节范围、研究问题、时间；打开一次卡片不能自动记为精读。
- 在 Alpha 生成/评价**之前**即可记录阅读；每篇累计精读次数从日志按论文或角色统计，提供给 Agent 决策。允许重读，但既往精读不能在新一轮丢失。

## 3. Daily：两类逻辑记录 + 数值文件

**Feature（仅已发布特征）**：至少保存 feature_id、name、description、feature_type、精确代码/哈希/参数、required_fields/dependencies、window、first_usable_at、source_refs、data/feature 版本和数值路径。

- `feature_type=base`：由程序**优先初始化**从分钟 C 构造真实可得的基础日频字段：`close_1m_first`（首分钟收盘）、`close_1m_last`（末分钟收盘）、`close_1m_max`（分钟收盘最大）、`close_1m_min`（分钟收盘最小）。这些**不是**真实 Open/High/Low；不得误命名或将未观察到的极值补造。必须校验时区、日历、复权、缺失、可用时点。
- `feature_type=curated`：M1 独立发现/审核通过的可复用日频研究特征，满足独立/中立、经济含义、非平凡、非重复及技术/时间合法性。
- Base 是基础处理，不适用 M1 的研究型“非平凡性”审核，**不进入 Curated 的相关性参照集合**；但要检查字段真实、结果正确、时间合法、可复现。Curated 与 Base 定义等价时也不能重复创建。

**Review（全部 M1 审核记录）**：至少保存 review_id、来源/母 Factor、候选定义、四项检查、相关性值/参照集/算法版本、decision（approved/rejected/blocked/no_candidate）、失败原因和时间。

- M1 可主动研究 Min、文献及研究过程；**每出现一个新 Alpha Factor，必须独立回看一次；每次最多提出一个 Daily 候选，允许零个**。不由 M3 负责，也不取决于母 Alpha 的 Ret、Sharpe 或 Score。
- **Curated 的入库相关性只能与已正式发布且有效的 Curated Feature 比较，严格 `<0.6`**；Review 中失败/阻断/无候选及 Base 一律不参加。完全等价复用旧 ID。具体相关性算法、绝对值、样本交集及空库语义尚未冻结，不能伪造 PASS。
- Research Agent **只读已发布 Feature 目录**（Base+Curated）及必要定义/数值，不能把 Review 失败候选作为可用 Daily。数值独立存公司环境 CSV/Parquet，并通过 trade_date、instrument、feature_id、data_version 及路径追溯。

## 4. Knowledge：Factor + Experiment + 极简 Episode

- **Factor**：唯一 ID、金融假设/研究问题、精确公式或代码、code_hash、参数与依赖、实际参考 source_refs、Daily feature_ids、父代 IDs、角色/版本、信息时点。
- **Experiment**：每一次真实测试的 experiment_id、factor_id、run_id、版本/样本/快照、执行关卡与失败原因、参考成功胜者集合和相关结果、已实际得到的 Ret/SR/MDD/TO/Cost、qualified、数值/日志路径。新候选一产生即创建 pending；重测新增 Experiment，不覆盖。失败、阻断、未完成、成功都存。
- **Episode 只是极简研究日志**，不增加独立研究数据库或复杂“树”：按 run_id 在 JSONL 或等价日志保存 role_id、research_mode、seed、model/Prompt 版本、data_snapshot、knowledge_snapshot、exposure_mode、reading_events、研究问题及 generated_factor_ids（允许空）。即使没有 Factor 也要保留，供论文精读累计和未来 Meta Loop 研究。读论文记录即时产生。
- 关联直接用 source_refs、daily_feature_ids、parent_factor_ids、factor_id、experiment_id、run_id，不必建 Relation 表。作者报告必须标 `external_reported`，内部实际运行为 `internal_executed`；外部收益/IC 不得写进内部 Experiment 绩效字段。
- **保持现有 Alpha 规则**：M5A 技术/未来信息 → M5B 统计/严格重复/已成功内部胜者相关 `max_abs_corr<0.65`（无胜者 `NO_REFERENCE`，只跳过此项）→ M6 Financial Evaluator → M7 只有有效计算且 `ret_ann_gross>0.03 AND sr_gross>1` 才正式 qualified。Score 仅按需计算；各阶段失败的金融字段必须保持 NULL。详见原 Gates 和 Evaluator 口径。

## 5. M2 查询权限、时点和全流程

| 库 | 查询重点 | Agent 获得的数值边界 |
|---|---|---|
| Min | C 字段说明；可选按历史日期查询 sector/group 并 groupby | 只返回行业视图或后台分钟 C 计算的必要结果 |
| Papers | 全量授权目录/筛选/累计精读 → 卡片 → 原文章节 | 文本与证据，及时记阅读事件 |
| Daily | 已发布 Base+Curated 定义目录和详情 | 按需授权 CSV/Parquet 数值/统计 |
| Knowledge | 授权 Factor/Experiment/Episode 目录及详情 | 实验已记录数值/历史统计；不泄漏隐藏结论 |

- M2 查询必须真正执行 full/masked 和时间/权限限制，**覆盖列表、计数、搜索、分页、详情、统计和 ID 关联**，不是只在 Prompt 里遮蔽文字。基础字段/时点和安全检查规则不被随机遮蔽。
- 每轮固定 run_id、role_id、research_mode、seed、exposure_mode、data_snapshot、knowledge_snapshot、information_cutoff、budget；Prompt 说明历史行业字段可选、论文自选并逐篇精读、Daily 只使用已发布内容。
- 读取文献和探索时增量写 Episode → 生成 Alpha 后 M4 立即注册 Factor/Experiment → M5A/M5B/M6/M7 检查 → M8 全量记录；独立 M1 回看新 Factor 并写 Review/发布合格 Feature；M9 重放仍走同样关卡。
- M2 只提取，不替 Agent 挑论文、制定 Alpha、评价金融有效性。错误、空值、权限阻断与未知均必须真实反映，不以零或“已通过”替代。

## 6. 云端 Agent 实现验收清单（先合成数据）

- [ ] 文献全量可分页、Agent 自选；三模式概率各 1/3 并可凭 seed 重现；full/masked 可独立配置。
- [ ] 文献 Card 有真实出处与未核实状态；阅读日志在生成之前已可记录；无候选轮次不丢失精读历史。
- [ ] Research Min 无原始分钟 C 全表自由读取，但有 C 字段说明、可选历史行业 DataFrame；后台计算仍支持分钟 C。
- [ ] Base 四个字段准确命名、不是伪造 OHLC；Curated 相关性参照只取已发布 Curated，不含 Base 和 Review 失败候选。
- [ ] 每个新 Alpha 触发 M1 回看 0/1 候选、Review 全量记录；Knowledge Factor/Experiment/轻量 Episode 正确关联。
- [ ] 所有 full/masked 查询路径、时间信息、行业 as-of、生成功能与未来收益标签隔离，越权访问不能绕过。
- [ ] 原有 `<0.6`、`<0.65`、`Ret>3%`、`SR>1` 和 NULL/NO_REFERENCE 等判定在模拟测试中得到验证；没有核实的统计口径不报 PASS。

## 7. 尚未拍板的实现口径

相关性统计方法/绝对值/样本对齐/空参照、实际市场日历与缺失/复权、标签单位与收益时序、行业代码名称映射、真实数据覆盖、阅读精读的可审计判定规则、物理存储和 API 参数均需公司环境核实，不能把建议字段误称为已部署数据库。

**请实现 Agent 先读本文件，再读本目录 README、PROCESS_AND_MODULES、GATES_AND_DECISIONS、DAILY_CURATOR_RULES、KNOWLEDGE_AND_CSV_CONTRACT 及 16 角色 Prompt；发现旧文字与本文件的四库新增约定矛盾时统一采用本文件，不改变旧评价硬门槛。**
