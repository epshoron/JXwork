# 16个Research Agent统一Alpha输出合同

**Research Agent的唯一候选产物是日频Alpha**，不是Daily库中间特征。M1 Daily Curator独立发现、构造、审核与发布Daily；M3的16个专业Agent只读取已发布的Daily、必要时受控读取Min及来源材料。

**输出形状**：每只股票 × 每交易日 → 一个Alpha数值或NULL。不可输出分钟交易指令替代日频Alpha，不可输出Daily入库申请、审核状态或自行写Daily库。

模型应提交`role_id, alpha_name, research_question, financial_hypothesis, alpha_formula_or_code, required_raw_fields, required_daily_feature_ids, parameters, history_window, universe_definition, cross_section_reference, observation_end_time, first_usable_at, missing_data_policy, source_refs, assumptions`。其值须遵循本轮真实输入和确定的信号可用时点。详细格式：[Alpha候选JSON Schema](prompting/ALPHA_OUTPUT_SCHEMA_V1.json)。

调度器先根据可用字段与工具权限选取适合的角色任务；Research返回结构化Alpha候选并交M4注册。工具或运行故障由调度器独立记录，不能伪造Alpha计算结果。M4注册后的候选经独立技术/未来信息、Statistical Evaluator（成功胜者相关性<0.65）、Financial Evaluator（Ret>3%且SR>1）评价；Daily准入相关性<0.6仍属于M1业务规则。

参考：[主模块流程](../PROCESS_AND_MODULES.md) · [Knowledge字段合同](../KNOWLEDGE_AND_CSV_CONTRACT.md) · [16份Prompt](prompting/README.md)。