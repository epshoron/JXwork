# C003｜原文来源、公式与核验边界

**正式期刊论文标题**：Does realized skewness predict the cross-section of equity returns?  
**作者**：Diego Amaya, Peter Christoffersen, Kris Jacobs, Aurelio Vasquez  
**发表**：*Journal of Financial Economics*, 118(1), 135–167 (2015)  
**正式 DOI**：[10.1016/j.jfineco.2015.02.009](https://doi.org/10.1016/j.jfineco.2015.02.009)  
**原始工作论文**：[CREATES Research Paper 2013-41，奥胡斯大学原始 PDF（50 页）](https://repec.econ.au.dk/repec/creates/rp/13/rp13_41.pdf)；[RePEc 工作论文记录](https://ideas.repec.org/p/aah/create/2013-41.html)  
**正式出版方摘要**：[Journal of Financial Economics／ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0304405X15001257)

## 本轮直接读取了什么？

- 已经**直接打开并截图核对 2013 年作者原始 PDF** 的 §2.1–2.2、公式 (1)–(7)，包括数据构造与频率，以及 §3 排序与回归结果和 §4/§6 主要方法、稳健性、结论文字。
- 原文数据：TAQ 美国股票逐笔成交价每 5 分钟抽样；美东 9:30–16:00，正常日 78 个 5 分钟收益；采样段无成交返回 0，剔除低于 $5 股票和日成交不足 80 笔的有效日。
- **Daily 计算原文 §2.2 Eq.(2)–(4)**：`RDVar = sum r²`；`RDSkew = sqrt(N) sum r³ / (RDVar)^(3/2)`；`RDKurt = N sum r⁴ / (RDVar)²`。原文采用未去均值（非 centered）的高频矩，§4.1 另做漂移调整验证。
- **Weekly 构造 §2.2 Eq.(5)–(7)**：周二标记、五交易日窗口；在股票存在部分无效交易日时依据可用 daily 估计值构造。原文研究按周而非按日进行截面评价。
- **实证 §3.2、Table 2、§3.4**：工作论文 24 bps/周（t=3.65，低偏度减高偏度）；Fama–MacBeth 和替代定义的稳健性是论文作者报告结果。
- 正式 *JFE* 2015 题录及摘要公开可见，给出**19 bps/周（t=3.70）**；这属于**不同版本**，本轮没有取得正式版逐页完整全文，因此不把工作论文的所有表格当成期刊终稿。

## 尚未做什么？

- 未逐页核完工作论文所有 50 页、理论模拟与每张表图、附录；没有独立复现 TAQ 原始数据处理和后续收益统计。
- **未核实 2013 工作论文和 2015 正式论文的具体修改原因**；尤其不能自动合并 24 / 19 bps，或声称它们是同一统计口径的严格横向对照。
- 未研究以单日特征预测次日收益的额外实验；论文能证实**日级指标被构造**，但验证主张是**周度**预测。
- 没有建立经审批的 `ARCHITECTURE.md`、`IDEAS.md` 或 CD 增量知识卡；不宣称学术首创性。

**归档权限**：这是正式学术论文的客观机制骨架，来源清楚后先归档；后续特色、配对特化不足及跨论文机制卡仍须研究者逐项审批和严格去重。仅保存原文链接与独立概述，不上传未经许可可再分发的 PDF；仓库虽为 Private，仍不存放公司材料、私有行情及密钥。
