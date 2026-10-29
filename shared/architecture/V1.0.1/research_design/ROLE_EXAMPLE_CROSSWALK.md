# 现有C/CR研究档案的示例映射（论文不决定Agent岗位）

| 来源 | 可映射角色/研究范围 | 限制 |
|---|---|
| [C001](../../../C_intraday_to_daily/papers/C001/README.md) | A03正负半方差、A02波动强度；周度聚合思路涉及B01 | 日度中间指标可计算不等于原文已验证日度选股收益 |
| [C003](../../../C_intraday_to_daily/papers/C003/README.md) | A03日度偏度峰度；历史聚合B01 | 作者原实证主要是周频 |
| [C004](../../../C_intraday_to_daily/papers/C004/README.md) | A02/A03已实现矩 | 原文财报事件检验还需事件字段 |
| [C010](../../../C_intraday_to_daily/papers/C010/README.md) | A03收益分布形状；参数跨日变化B02 | 峰肩尾是概率分布，不是价格路径高低点 |
| [CR001](../../../C_intraday_to_daily/reports/CR001/README.md) | A04/A05异常涨跌分钟顺序；截面残差还涉及C01 | 时段设置与公式冲突需核对 |
| [CR002](../../../C_intraday_to_daily/reports/CR002/README.md) | C02同期市场共振；条件结构可涉及C05 | 摘要缺完整公式，成交量相关部分未必可算 |
| [CR003](../../../C_intraday_to_daily/reports/CR003/README.md) | 仅作领域及输入边界材料 | 依赖分钟成交量，不能用分钟Close冒充 |
| [CR010](../../../C_intraday_to_daily/reports/CR010/README.md) | 仅作词义和输入边界材料 | 量峰/量岭/量谷是成交量状态，不是收益分布峰或股价路径峰谷 |

同一篇研究可以涉及多种信息范围，作者报告属于external_reported，不等于公司内部回测。先划分研究问题和信息依赖，再引用论文作为证据，而不是因论文存在而新建岗位。