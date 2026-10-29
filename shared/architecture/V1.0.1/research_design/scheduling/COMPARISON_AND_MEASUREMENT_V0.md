# Research调度与Full/Masked的对照实验 V0

本文件设计**如何比较**，不决定哪个模式优越，也不更改 `qualified` 规则。

## 1. 公平比较的基本配对

同一组对照固定：`data_snapshot`、`daily_snapshot`、`knowledge_snapshot`、研究角色和对应Prompt版本、底层模型及参数、预算、目标股票池/时段、数据权限、评价数学版本。两个研究episode分别使用 `full` 与 `masked` 的输入视图；只允许**信息暴露模式**不同。

建议先做小规模配对试运行；`full/masked` 比例、遮蔽概率、是否按角色做分层设计，**当前都尚未拍板**。若想研究mask的作用，两个模式需要可比的生成机会，且记录 `exposure_override` 是否发生。

## 2. 冷启动与动态胜者集问题

- 早期Knowledge没有内部Alpha实验，仍可有外部论文结果卡；若无任何可遮蔽结论，则masked等于full，比较应标记 `no_maskable_groups`。
- 新 Alpha 正式通过后会进入成功胜者参照集合；后一个episode可能面对更多胜者，从而更难过相关关。**实际 `qualified` 必须遵守M5已确定的当前胜者规则**，不可为做实验而篡改生产资格。
- 可额外保存基于**同一冻结成功者快照**的研究比较诊断，用来剔除“先提交者胜者少”的偏差；此诊断**不是生产上的PASS/QUALIFIED**，不能写成真实硬关通行。
- 配对生成所用材料的knowledge快照不随两次生成之间的实验结果变化，否则实验不再只比较mask。

## 3. 指标

分开记录两个层级：

**生成/模型层（调度器）**：有效候选产出率、工具成功率、模型API用量、实际研究来源覆盖、重复公式率、相邻角色候选的语义重叠、masked实际隐藏组数与检索例外。

**正式实验层（M4～M8）**：技术合法通过、统计通过、已成功因子相关性、有效金融评测次数、真实Ret/SR/DD/TO/成本及按现行门槛的qualified数；样本外结果需要按真实回测规则得到。绝对不能把第一关失败误称低收益，也不能把作者报告当内部验证。

## 4. 日志和结论边界

对照记录 `pair_id, full_episode_id, masked_episode_id, same_snapshot_refs, role_id, prompt_version, model_version, budget, mask_config, exposure_override, generation_result, factor_id/experiment_id(如有), observed_eval_status`。没有任何实验结果时只记录“待测试”，不能推测mask收益。

跨多个角色比较时既报告每个角色，也报告四领域分层结果，防止A组人数多就掩盖其他领域；不将角色计数直接转换成调用份额。