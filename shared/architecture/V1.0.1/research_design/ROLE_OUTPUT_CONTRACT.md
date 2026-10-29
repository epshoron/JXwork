# 16个Research Agent统一Alpha输出合同

**Research Agent的唯一候选产物是日频Alpha**，不是Daily库中间特征。M1 Daily Curator独立发现、构造、审核与发布Daily；M3的16个专业Agent只读取已发布的Daily、必要时受控读取Min及来源材料。

**输出形状**：每只股票 × 每交易日 → 一个Alpha数值或NULL。不可输出分钟交易指令替代日频Alpha，不可输出Daily入库申请、审核状态或自行写Daily库。

模型应提交role_id、role_strategy_version、prompt_version、primary_domain、secondary_domains、research_question、financial_hypothesis、alpha_formula_or_code、required_raw_fields、required_daily_feature_ids、parameters、history_window、cross_section_reference、observation_end_time、first_usable_at、missing_data_policy、minimum_samples、source_refs、assumptions、limitations。详细格式：[Alpha-only JSON Schema](prompting/ALPHA_OUTPUT_SCHEMA_V1.json)。

无法合理生成时可返回no_candidate并记录调用日志，不伪造Factor或Experiment。Alpha候选再由M4注册并经独立技术/未来信息、Statistical Evaluator（成功胜者相关性<0.65）、Financial Evaluator（Ret>3%且SR>1）评价，Knowledge保留真实结果。Daily的相关性<0.6仅对M1负责，与M3研究Prompt无关。

参考：[主模块流程](../PROCESS_AND_MODULES.md) · [Knowledge字段合同](../KNOWLEDGE_AND_CSV_CONTRACT.md) · [16份Prompt](prompting/README.md)。