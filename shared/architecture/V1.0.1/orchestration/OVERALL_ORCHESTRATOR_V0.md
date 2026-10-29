# Overall Orchestrator｜模块编排与执行生命周期 V0

## 1. 设计边界

总编排负责工作流的**版本快照、任务派发、模块调用顺序、权限范围、状态追踪、重试/恢复和验收**。不计算Daily特征、不生成Alpha、不做技术统计门槛、不计算金融指标，也不承担 M2/M4/M8 已有模块的存储逻辑。

四库不变：Min、论文研报、Daily、Knowledge；本模块的run/episode/event元数据通过既有 M8/控制日志接口持久化，不新建科研意义上的第五库。M9 Replay/Evolution 暂列`not_enabled_waiting_teacher`，不能根据本文件自行选择父代或变异。

## 2. 一次 Run 的分步执行

| 阶段 | 入口和行动 | 输出/后续 |
|---|---|---|
| 0. 初始化 | 验证运行配置；从模块拥有者取得M0数据能力版本、M1已发布Daily目录版本、M2工具目录版本、Knowledge快照；锁定评测/门槛版本和股票池/时间边界 | `run_id, pinned_snapshots, config_hash`；不能宣称真实数据问题已解决 |
| 1. 研究可用性 | 对16角色按能力目录进行合格性检查，允许没有足够Daily时只选择依赖已存在Min能力的研究角色 | 合格角色清单与未合格原因；不产生虚假Factor |
| 2. 调度与可见性 | Research Scheduler按配置选择角色；Visibility Policy对本次`knowledge_snapshot`建立`full`或`masked`研究视图 | `EpisodePlan + exposure_view_id`；权限与seed保持不变 |
| 3. 独立挖掘 | 每个episode仅加载一份完整专业Prompt和对应动态输入，M2通过授权查询工具提供材料与计算 | 一个结构化`alpha_candidate`与查询/资源日志 |
| 4. 结束生成可见性 | 关闭生成期visibility上下文；将后续程序权限切换为**全量Knowledge**，不在注册前因相似性直接丢弃候选 | 实际生成的Alpha候选都提交M4登记，后续M5负责正式查重 |
| 5. 候选注册 | 调用M4的幂等写入接口，拿到`factor_id/experiment_id`；由M4/M8维护统一Knowledge的状态与版本 | 实际Experiment开始于注册时；调用故障应记运行日志而非伪造Alpha |
| 6. 第一关 | 对**已注册**候选按 M5A Technical/Leakage，再 M5B Statistical Evaluator（含全量Knowledge重复与胜者相关性）的现有规则执行；保持胜者参照版本与统计口径的审计信息 | FAIL/BLOCKED直接记录，金融字段NULL；PASS才进金融评价 |
| 7. 金融关 | 调用已确定的M6 Evaluator获得真实`Ret/SR/DD/TO/Cost`及需要的日级复算材料 | 有效金融结果触发M7的`Ret>3%, SR>1`；故障不能当作收益失败 |
| 8. 统一留痕 | 调用现有M8接口，保存真实指标、各关状态、来源、角色/Prompt及配置/快照引用、查询与工具日志 | 正式成功在同一Knowledge的`qualified`视图，不造Alpha新库 |
| 9. 收尾 | 完成预算与资源用量统计，保留未完成/取消任务状态和可恢复游标 | 新run可用新快照重新开始；M9不自动触发 |

**并行M1**：Daily Curator 自己决定何时发现和发布新 Daily。总编排只在开启一次Run/Episode时读取**已发布的稳定Daily快照**；生成过程中M1新发布的信息进入**后续**Episode/Run，不得混进已锁定的上下文。M1不依赖M3提出Daily申请。

**独立M2/M4/M8**：它们的内部函数、物理存储和事务实现由对应负责人设计；总编排只持有其接口版本及必要可观测返回，不替代其内部逻辑。

## 3. Run / Episode / Experiment 不是同一个东西

- `run_id`：一组共用预算和固定初始化配置的工作流执行。
- `episode_id`：一次研究Agent推理及工具查询尝试；其失败不必然意味着存在Alpha候选。
- `submission_id`：某次返回的候选在交给M4时的幂等提交标识；同一个episode可重传相同提交但不能重复创建Experiment。
- `factor_id / experiment_id`：**仅由M4注册后产生**；Experiment必须有具体合法候选身份，调用超时/响应格式错误不得伪造一个“不成功Alpha”。

调用侧`episode_status`建议 `planned, dispatched, generated, submitted, not_ready, timeout, tool_error, malformed_response, cancelled`；注册后状态完全使用 Knowledge 合同既有的 `pending, blocked, technical_fail, statistical_fail, evaluation_error, financial_fail, qualified`。两套状态分别记录，不在单个字段里混用。

## 4. 幂等、重试和故障恢复

1. 在发起LLM调用前保存 `EpisodePlan`、Prompt版本、权限快照、随机种子和 `dispatch_id`；进程重启后不能重复抽取不同遮蔽组却沿用同一episode ID。
2. LLM/工具超时先记录调用故障；是否重试由运行预算和版本化重试策略控制。同一次提交重传带同一`submission_id`，不能生成两个Factor/Experiment。
3. M4注册成功但调用方丢失响应时，应按`submission_id`查询既有注册结果再继续；不能直接再次`create`。
4. M5/M6任务崩溃时恢复同一Experiment并核对对应阶段是否已经完成；不得把未运行的Ret/SR等写0或FAIL。
5. 被阻断的Experiment不得直接进入金融关；恢复只能从未完成合法阶段继续，并保存已有真值。
6. 需要正式通过`qualified`的并发候选，应交由M5/M4拥有者实施**最新胜者集重验/并发版本校验**；编排器只等待该模块返回确认结果，不能拿旧快照自行宣称通过。
7. 对旧数据/门槛版本做新的测试必须创建新的Experiment；不可覆盖历史结论。M0或M1的接口版本变化通过新的Run快照体现。

## 5. 策略配置与未知问题

**已经确认的**：16角色是当前策略基线；每次只加载相应一份Prompt；Daily由M1独立生产；生成期`full/masked`、生成后全库审查、注册后技术统计再金融关；成功记录与失败记录均在Knowledge。

**没有拍板的**：每轮派发次数、各角色权重、mask概率、是否用自适应采样、失败重试次数、最大并发、M9遗传规则。它们必须由运行配置明确给出（或暂不启用），不能让云端开发Agent默认创造并宣称已确认。

**真实数据上线前必要依赖**：`OPEN_DECISIONS.md`列出的P0统计相关系数口径、实际字段/时间、VWAP收益对齐、毛净收益等必须由各模块负责人解决。P0不满足可运行合成数据联调，但绝不能把金融门槛判成真实PASS。

## 6. 端到端序列（逻辑而非现成API代码）

```text
validate_run_config
  -> pin(M0_capabilities, M1_published_daily, M2_tool_registry,
         Knowledge_generation_snapshot, Gate/Eval_versions)
  -> Scheduler.select_role
  -> Visibility.create_view(full | masked)
  -> M3(role_prompt + scoped_tools).generate(alpha_candidate)
  -> Visibility.close_generation_view
  -> M4.register_candidate(submission_id)
  -> M5A -> M5B(full_knowledge_duplicate_and_winner_check)
  -> [if PASS] M6 -> M7
  -> M8.record_actual_results
  -> Scheduler.record_usage_and_cursor
  -> finish_or_next_episode
```

伪调用名只是**接口责任描述**；必须与M2/M4/M8的真实提供者对齐后才能作为代码接口调用。