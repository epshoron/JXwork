# Research Agent 研究空间与专业分工（当前采用 V0.2）

**当前采用：A 单股日内 6、C 多股日内 5、B 单股跨日 3、D 多股跨日 2，共 16 个专业思考角色。** 这是可替换的研究策略基线，不是已被真实实验验证最优的配置；角色可以共用公司允许的底层模型/API，不是 16 个模型。

**命名隔离**：本目录 A/B/C/D 是 Research Agent 的信息范围，与仓库文献方向 A_alpha_mining、B_ai_trains_ai、C_intraday_to_daily 不是同一套分类。

| 范围 | 人数 | 入口 |
|---|---:|---|
| A 单股 × 日内 | 6 | [A01–A06](A_single_stock_intraday/README.md) |
| C 多股 × 日内 | 5 | [C01–C05](C_multi_stock_intraday/README.md) |
| B 单股 × 跨日 | 3 | [B01–B03](B_single_stock_cross_day/README.md) |
| D 多股 × 跨日 | 2 | [D01–D02](D_multi_stock_cross_day/README.md) |

## 独立文档入口

- [16 人的职责索引](ROLE_TAXONOMY.md)
- [相邻角色边界和主观重叠处理](ROLE_BOUNDARIES.md)
- [分钟研究→Daily 输出的稳定合同](ROLE_OUTPUT_CONTRACT.md)
- [核心规则与可替换策略划分](STRATEGY_AND_CONTRACTS.md)
- [角色采样和实验对照（尚未冻结）](ROLE_SCHEDULING_AND_VALIDATION.md)
- [现有 C/CR 论文仅作为实例](ROLE_EXAMPLE_CROSSWALK.md)
- [16份独立Alpha Prompt](prompting/README.md)：每个角色按输入工具、专业研究、研究过程、输出去向四部分完整规定。
- [role_manifest.json](role_manifest.json)：可供离线本地 Agent 读取的 16 角色清单。
- [Research Scheduler / Full-Masked 具体规范](scheduling/README.md)：本次专门负责的可替换运行策略。

**研究空间不是生产调度的刚性顺序。** A/C研究原始分钟价格与跨股日内信息，B/D可利用已有Daily及合法历史Min；四组**全部只负责日频Alpha生成**，不发现/申请/审核Daily中间特征。M1 Daily Curator独立负责Daily生产。所有Alpha最终为股票×日期一个信号值，后续技术、统计及金融审核独立运行。
