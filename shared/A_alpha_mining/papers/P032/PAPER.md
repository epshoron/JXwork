# P032｜论文身份与直接核查范围

- **原始题名**：Alpha Discovery via Grammar-Guided Learning and Search
- **权威来源**：https://arxiv.org/html/2601.22119
- **方法概述**：AlphaCFG 先以 alpha-oriented context-free grammar 限定语法/语义合法的树状表达，再以 grammar-aware MCTS 和树结构表征的 policy/value 网络进行搜索；关注表达式复杂度与语义等价候选造成的浪费。
- **本轮核验**：直接核对 arXiv HTML 摘要、§1 与 §3、§4 的机制描述；未检验作者代码运行、全部消融或公司的表达式形式。
- **外推限制**：arXiv 预印本，不宣称已获 ICML 正式录用；论文中中美市场实验是作者报告。生成前约束与已有算子库、AST 去重可能重合，金融预测优势未经本项目复现。
- **版权/保密**：只存客观事实和论文链接，不转载原文 PDF，不记录公司内部数据、代码或讨论中的未批准项目方案。
