# C004｜来源、原始证据与核验范围

> **原文 PDF 已归位（2026-10-28）**：研究者自行上传的 [PDF 原文](AM_Realized_moments_and_the_cross_sectional.pdf) 已放在本目录。文件归档**不等于本轮重新逐页核对**，下述既有核验范围及版本差异仍须保留。

## 1. 正式题录

- **论文原题**：*Realized moments and the cross-sectional stock returns around earnings announcements*
- **作者**：Qingxia Wang; Robert Faff; Min Zhu
- **正式发表**：*International Review of Economics & Finance*, 79 (2022), 408–427
- **DOI**：https://doi.org/10.1016/j.iref.2022.02.036
- **出版方正文/摘要**：https://www.sciencedirect.com/science/article/pii/S1059056022000570
- **Bond University 机构库**：https://research.bond.edu.au/en/publications/realized-moments-and-the-cross-sectional-stock-returns-around-ear/
- **公开作者接受稿（50 页 PDF）**：https://pure.bond.edu.au/ws/files/190520552/AM_Realized_moments_and_the_cross_sectional.pdf
- **文献类别**：正式期刊论文；不是券商研报、AI 系统论文，也不是本项目因子回测结果。

## 2. 已核对原文（2026-10-27）

| 来源位置 | 确认的客观内容 |
|---|---|
| 摘要、§1（作者稿 PDF 约第 2–8 页） | 研究财报公告前的 realized moments 与公告后 CAR；作者提出事件信息含量、日内不对称和可能市场反应的解释；需区分假设与结果 |
| §2 Eq.(1)–(8)（PDF 第 9–10 页附近） | 五分钟对数收益、Daily RV / RSkew / RKurt、正负半方差差值 signed jump、按 RV 标准化的相对值 |
| §2 Eq.(9)–(12)（PDF 第 10–11 页附近） | 分别对过去五个交易日 Daily realized measures 求算术平均，形成 weekly 变量 |
| §3（PDF 第 11–12 页附近） | TRTH、nearest-tick、9:30–16:00、78 个五分钟区间、排除隔夜；零收益筛除、I/B/E/S/CRSP/Compustat 与 1998–2015 S&P500 范围 |
| §4.2–4.3（PDF 第 15–18 页附近）、Table 2–3 文字说明 | 分组及单/多变量 CAR 回归；RDvar、RDJ 方向，RDskew 单变量与多变量符号变化；RDkurt 不显著；四个事件窗口 |
| §4 后续相关段落（PDF 第 19–22 页附近） | 作者比较不同 jump 定义、财报与非财报期间、控制意外盈余 SUE 后的关系；这里只记录已核正文所支持的定性结果 |

**来源层次**：大学机构库版本为作者接受稿；与出版版题录/摘要交叉核对。文中所有作者实验结果都注明**作者报告**，不是本项目实证。PDF 文字解析可查阅原文论述，但部分公式字形提取混乱；在可执行实现前仍需要把数学排版与全部表格逐式核验。

## 3. 原文事实与解释的区分

- **公式定义**：原文 Eq.(7) 的 signed jump 为**正、负已实现半方差之差**，Eq.(8) 再除以 RV；不是以阈值或检验识别的逐分钟价格突变。
- **作者预期/解释**：含信息的财报公告期间，已实现矩与后续收益关系或更明显；讨论信息不对称、过度反应、日内分布不对称的解释。它们不应被改写为经独立因果识别的金融定律。
- **作者实证观察**：方差正向、相对 jump 负向；偏度系数依控制条件换向；峰度基本未表现稳定显著关系（负结果）。事件与非事件结果不同。
- **未证实外推**：没有独立测试 A 股分钟 K 线、固定 240 根分钟、次日收益 RankIC、每日实盘调仓、交易费用或新的金融行为假设。

## 4. 未核验与版权边界

- 本次**未**下载原始 TRTH / I/B/E/S / CRSP / Compustat 数据、重算统计量或复现回归；**未逐页完整复核** Table 1–7、所有稳健性分析及附录。故当前为客观金融知识整理，**不是全文精校、模型验证或已证实的普适市场规律**。
- 使用网页 PDF 解析读取正文及部分公式，页面截图复核工具当前未能成功抓取该源，故仍保留原始排版与表格的待核范围；没有用 OCR 猜补缺失字符。
- Bond University 题录显示 **CC BY-NC-ND**；本仓库仅保存原创研究说明及来源链接，**不上传论文 PDF 全文**。
- 本档案只供检索原文金融知识，不附加 Agent 行动提示、搜索目标、推荐指标或衍生 Idea Seeds；未取得贡献、独立不足或 CD 知识卡的研究者审批。

[本篇金融知识与算法说明](README.md) · [所属方向 C Index](../INDEX.md)
