# 并行工作交接：总编排只约定最小接口，不重写内部模块

> 对接 S16、S17／公司云端开发 Agent 使用。下方是需要满足的**逻辑操作与返回要求**，不是已经存在的函数名；**M2 与 M4/M8 作为高相关的一体化工作流协调接口/权限和事务，不分别指定两个独立实施负责人**；真实API由模块拥有者提供并登记 `tool_registry_version`。

| 所属模块 | 对编排器需要暴露的能力 | 最小返回/约束 | 本会话不处理的内部问题 |
|---|---|---|---|
| M0 数据/日历 | 取得当前可用字段、时段、股票池及数据快照 | `data_snapshot_id, capabilities, allowed_time_range, availability` | 文件读取器、Parquet/CSV、复权实现 |
| M1 Daily | 取得**已发布**Daily目录快照 | `daily_catalog_snapshot_id, feature_ids, formula_refs, first_usable_at` | 生成中间特征、相关性<0.6、物化CSV |
| M2 统一查询 | 向特定episode授予有版本的工具目录与研究视图读取能力；查询日志 | `tool_registry_version, scoped_query_handle, query_log_ref`；支持对Masked隐藏组统一过滤，并提供Knowledge研究结论谱系分组索引（组版本/成员关系） | 四库查询API、检索/数据计算后端、权限内部实现 |
| M4/M8 Knowledge | 幂等注册候选、读写真实阶段结果、查询当前胜者集版本及日志引用 | `submission_id`对应唯一`factor_id/experiment_id`，允许按提交ID找回 | DB表、CSV写入、事务和状态字段内部实现 |
| M5A | 对已注册候选检查真实字段/运行/时点 | `PASS / FAIL / BLOCKED`及原因、检查版本 | 具体技术/泄漏算法 |
| M5B | 读取全量Knowledge胜者，按固定统计规则审查 | 同上 + 胜者快照ID、最大相关结果、统计版本 | Pearson/Spearman、样本对齐算法、并发重验 |
| M6/M7 | 对第一关PASS实验做金融评价并按现行硬门槛资格判定 | 原始Ret/SR/DD/TO/Cost与`qualified`真实结果 | VWAP收益/回测数学、P0毛净收益口径 |
| M9 | 保留未来策略入口 | 目前 **未启用** | 父代选择/变异/交叉，等老师确认 |

## 合同对齐时尤其需要确认的五项

1. **权限分离**：M2生成期的`scoped_query_handle`不得与M5用的全量Knowledge读取句柄相同；mask过滤须在M2查询侧生效，隐藏ID点查必须和真正不存在的ID对研究者呈现等价响应，避免侧信道。
2. **快照生命周期**：data、Daily、Knowledge、tool registry、gate/eval版本何时固定，变更时是否必须新开run。
3. **候选交付**：LLM返回的Alpha结构如何交给M4；注册写入的幂等键与Factor/Experiment ID返回合同，不能因重试重复产生Experiment。
4. **结果写回**：每一关与M8如何交换状态/实际指标及失败原因；未执行指标必须NULL，历史实验不可覆盖。
5. **并发资格**：胜者集合更新与M5B相关性审查之间的事务边界由M4/M5负责人明确，总编排不能在模型端代办。

## 跨会话修改边界

本会话负责 `research_design/scheduling/*` 与 `orchestration/*`。既有M0、M1、M2/M4/M8、M5和M6文件只做必要索引链接，不另写其内部实现。接口暂不一致时记录`integration_blocker`，由真实拥有者确认，不用修改其他人正在维护的规范来“假装兼容”。