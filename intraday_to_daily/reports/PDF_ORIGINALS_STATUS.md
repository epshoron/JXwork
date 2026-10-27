# 方向 C｜CR001–CR008 原始研报 PDF 获取清单

> **检查日期：2026-10-27**。本页只记录原始文件的获取入口及其**实际核验范围**，不代表已取得 PDF 或获得转载/上传许可。GitHub 仓库内目前仅有对应研究的 Markdown；**截至本次检查，未向 CR001–CR008 新上传 PDF**。第三方网页摘要、图片预览、OCR 文本不等于原始 PDF。用户可在获得合适使用/存储权限后逐篇自行下载，并放入对应目录。

## 当前找到的入口

| 档案 | 对应原文入口 | 目前实际确认到的状态 | 下载后的拟存路径 |
|---|---|---|---|
| [CR001](CR001/README.md) 东吴证券《重拾自信选股因子更新》 | [完整PDF直链（file.iyanbao.com）](https://file.iyanbao.com/pdf/57c21-06bf3c6e-87ae-450a-a1a2-3ba8b81f1ed2.pdf) | **完整PDF可由网页阅读器打开，22页、封面及题名已核**；本次二进制下载通道失败，未转存文件。可以自行打开后使用阅读器下载按钮 | `CR001/original.pdf` |
| [CR002](CR002/README.md) 招商证券《基于分钟数据的价变共振因子》 | [迈博汇金报告入口](https://www.microbell.com/repinfodetail_3796270.html) · [股票报告网题录](https://www.nxny.com/report/view_5834964.html) | 报告入口显示23页PDF；第三方入口涉及用户登录/加密下载；**未拿到可直接下载的PDF文件** | `CR002/original.pdf` |
| [CR003](CR003/README.md) 国盛证券《基于趋势资金日内交易行为的选股因子》 | **[国盛金工署名公开文章](https://finance.sina.cn/2024-06-03/detail-inaxmham4932631.d.html)** 提供的[百度网盘原文](https://pan.baidu.com/s/1ab9uNgS2Ydhimlu1jf5raA)，**提取码 `hgei`**；备选[研报题录](https://www.nxny.com/report/view_5657498.html) | **原作者公开文章明示这是“报告原文下载链接”**，但当前未进入网盘核对实际文件；研报题录显示15页PDF、登录/加密条件 | `CR003/original.pdf` |
| [CR004N](CR004N/README.md) 开源证券《高频资金流分布因子的构建方法》 | [慧博报告摘要](https://www.microbell.com/wap_detail.aspx?id=5211813) · [研报客PDF获取页](https://www.yanbaoke.com/info/V22NDELuwZfmGkLtdjSR4Q) · [作者署名公开长文](https://finance.sina.com.cn/roll/2026-09-06/doc-iniqwnkx0140930.shtml) | 可确认14页PDF题录与公开原作者解读；**PDF本体未取得**，研报客入口可能要求下载客户端/账户 | `CR004N/original.pdf` |
| [CR005](CR005/README.md) 民生证券《基于分钟K线的“主力波动率”构造及应用》 | [迈博汇金23页研报入口](https://www.microbell.com/repinfodetail_3469891.html) · [署名公开解读](https://finance.sina.com.cn/roll/2024-08-06/doc-inchswif6806062.shtml) | 23页报告题录和公开长文可读；PDF下载需在平台操作，**未取得直链或二进制** | `CR005/original.pdf` |
| [CR006N](CR006N/README.md) 国盛证券《高频数据+离散化构建方式的重要性》 | [股票报告网24页PDF下载页](https://www.nxny.com/report/view_5966903.html) · [公开全文转录](https://www.vzkoo.com/read/202505161482bab3c39fda0ce4460240.html) | 网站显示“无限制—登录即可下载”，**并不是免登录PDF直链**；登录后的文件未核实 | `CR006N/original.pdf` |
| [CR007](CR007/README.md) 方正证券《“滴水穿石”因子》 | [股票报告网20页下载页](https://www.nxny.com/report/view_6177409.html) · [慧博报告入口](https://m.hibor.com.cn/wap_detail.aspx?id=67a0ed010d2d505422d32703b38d1c97) | PDF题录可查，但第三方页面标为**加密报告**；未发现可直接确认的原始PDF直链 | `CR007/original.pdf` |
| [CR008](CR008/README.md) 东吴证券《CPV分时版》 | [股票报告网22页PDF下载页](https://www.nxny.com/report/view_5844264.html) · [公开研报摘要](https://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/11/rptid/788798601713/index.phtml) | PDF下载页标“无限制—登录即可下载”；**当前未取得免登录直链** | `CR008/original.pdf` |

## 人工获取与核验约定

1. **优先完整PDF**：先核对封面**报告原题、券商、日期、页数**与本表一致，再保存为各目录的 `original.pdf`；如有不同版本，在相应 `PAPER.md` 另记来源和版本差异，不用“全文转录”充作PDF。
2. **权限要求**：即使第三方网站可以免费下载，也不等于拥有在 GitHub 上再分发的许可；按券商版权声明和账户下载条款判断是否可以存放。对内部研究限制、明确禁止外传或付费受限的全文，不擅自上传；必要时保留受限的本地副本，仅在仓库记合法来源链接。
3. **内容核验**：取得文件后可以通过 `pdfinfo original.pdf` 查看页数，通过 `sha256sum original.pdf` 记录校验值，避免不同版本错放、网页转PDF冒充原文或空白/损坏文件。
4. **实际上传才更新状态**：本清单的“拟存路径”是建议，不表示文件已存在。每次用户或授权协作者完成合法上传后，复核 GitHub 文件存在性，再把对应报告和本清单的状态更新为“PDF已存档”，不能提前声称完成。

**安全说明**：研究资料需合法取得；不通过绕过加密、账号限制或DRM获取文件；不把第三方有偿下载页转换为公共直链。原文件仅供核查报告实际定义、结果和证据范围，不能自动证明报告因子在现有数据上的收益。
