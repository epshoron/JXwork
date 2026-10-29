# Research Role Taxonomy V0.2｜四范围十六角色

**已采用当前研究策略，未证明覆盖全部金融问题或优于 P002 原 21 人方案。** 角色领域由最小必要信息范围决定，二级按独立研究问题划分；不能按具体论文标题、技术指标名或未经验证的经济故事分岗位。

| 角色 ID | 信息范围 | 主责 | 详细定义 |
|---|---|---|---|
| A01 | 单股日内 | 方向与幅度 | [A01](A_single_stock_intraday/A01.md) |
| A02 | 单股日内 | 波动风险 | [A02](A_single_stock_intraday/A02.md) |
| A03 | 单股日内 | 收益分布 | [A03](A_single_stock_intraday/A03.md) |
| A04 | 单股日内 | 路径顺序 | [A04](A_single_stock_intraday/A04.md) |
| A05 | 单股日内 | 时钟时段 | [A05](A_single_stock_intraday/A05.md) |
| A06 | 单股日内 | 多尺度结构 | [A06](A_single_stock_intraday/A06.md) |
| C01 | 多股日内 | 截面相对位置 | [C01](C_multi_stock_intraday/C01.md) |
| C02 | 多股日内 | 共动与残差 | [C02](C_multi_stock_intraday/C02.md) |
| C03 | 多股日内 | 跨股时序 | [C03](C_multi_stock_intraday/C03.md) |
| C04 | 多股日内 | 行业层级 | [C04](C_multi_stock_intraday/C04.md) |
| C05 | 多股日内 | 极端条件依赖 | [C05](C_multi_stock_intraday/C05.md) |
| B01 | 单股跨日 | 持续与记忆 | [B01](B_single_stock_cross_day/B01.md) |
| B02 | 单股跨日 | 稳定与结构变化 | [B02](B_single_stock_cross_day/B02.md) |
| B03 | 单股跨日 | 多特征条件关系 | [B03](B_single_stock_cross_day/B03.md) |
| D01 | 多股跨日 | 相对地位历史变化 | [D01](D_multi_stock_cross_day/D01.md) |
| D02 | 多股跨日 | 群体关系历史变化 | [D02](D_multi_stock_cross_day/D02.md) |

## 分类原则

1. 首先看股票信息范围：单股还是必须比较多股；其次看主问题是否必须跨交易日。行业标签、股票池和已审 Daily 特征作为合法辅助输入，不自动变成第五种信息范围。
2. A/C 可以先发现基础 Daily，中间结果必须经 Daily Curator 审核，才能作为可复用 Daily；B/D 通常利用多日特征，但允许按需合法读取历史 Min。这个依赖不是所有任务都必须经过的固定流水线。
3. 同一研究方法可能跨多个范围；按主要不可替代的信息依赖指定 primary_domain 和 role_id，其他范围写 secondary_domains。跨领域调用特征不等于可以重复注册同一公式。
4. 原始文献只是研究材料、例证和核验来源，不决定分类；论文作者的结果不等于本项目已验证收益。没有对应论文的领域仍可以提出待验证假设。
5. 所有可执行产物必须对应每只股票 × 每个交易日一个标量或 NULL；只研究市场整体状态而不产生股票间差异的数值，不能直接冒充横截面 Alpha。

当前 16 人为版本化基线，Prompt 修辞、角色数、遗传算法、遮蔽强度和调度预算均可更换，但必须保留版本并经实验比较。