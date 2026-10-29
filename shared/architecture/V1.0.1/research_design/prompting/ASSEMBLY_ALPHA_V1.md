# 16 份独立 Alpha Prompt 的加载协议

**唯一运行指示源**：在 [ALPHA_PROMPT_MANIFEST_V1.json](ALPHA_PROMPT_MANIFEST_V1.json) 中选择一个 role_id，读取对应 roles/Rxx.md **完整文件**，作为本轮角色的专业指示。**不是**公共Prompt+两句profile，也不把16个角色一次拼给单个调用。

1. 对应单一 `roles/Rxx.md` 是完整的专业Prompt：独立问题、专属研究路径、主责边界与共有正确性约束已经写在里面。为了方便离线独立运行，允许16份各自重复一小部分安全约束。
2. 本轮输入由 [ALPHA_EPISODE_INPUT_V1.md](ALPHA_EPISODE_INPUT_V1.md) 在公司电脑按实际授权数据填充。Role Prompt和动态输入分开版本化；公司实际字段、可用时间、模型API密钥不得上传公开仓库。
3. 响应使用 [ALPHA_OUTPUT_SCHEMA_V1.json](ALPHA_OUTPUT_SCHEMA_V1.json)，仅有 `alpha_candidate` 与 `no_candidate` 两种结果；不含 `daily_intermediate`。
4. 本轮角色可使用 **已发布** Daily 特征和受控 Min / 文献 / Knowledge读取工具；不负责Daily入库，不调用Daily Curator做自己的生成任务，也不生成Daily中间特征申请。若某个Alpha的必需数据不可获得，返回no_candidate并说明缺失信息。
5. 生成完成后关闭生成期遮蔽，程序恢复完整Knowledge，分配Factor和Experiment身份并运行既定独立检查；不由Prompt替代Evaluator。
6. 原P002的21种角色、原先V0.1错误草案保留在Git历史或废弃标记中，不能与当前16份Prompt混合加载。

这里的 V1 只代表**提示词组件修订版**，角色分类仍是Role Taxonomy V0.2；测试通过前都标记草案，不能声称已部署或已实测。
