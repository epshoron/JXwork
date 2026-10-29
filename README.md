# JXwork｜研究资源与 Agent 协作仓库

**2026-10-29 起：三个业务区，各自面向不同读者。**

| 入口 | 内容 | 对公司云端的关系 |
|---|---|---|
| [`shared/`](shared/README.md) | A / B / C 研究档案、**已确定的 V1.0.1 Research Loop**、统一评价规范 | **仅把它作为知识/架构输入**；研究归档约定不是运行时 Prompt |
| [`assistant/`](assistant/README.md) | 给 ChatGPT/文献研究 LLM 的审批、认领、协作、日志、交接 | 公司执行 Agent **不需要** |
| [`presentation/`](presentation/README.md) | HTML 地图、Excel、ZIP、离线展示 | 按需读取 |

**架构权威入口**：[V1.0.1](shared/architecture/V1.0.1/README.md)。四库：Min、论文/研报、Daily、Knowledge；Knowledge 记录一切候选与实验，第一关技术/统计检查通过后才开展金融评价；达标即正式存档，不增设第五个 Alpha 库。具体规则见架构文档。

**下载**：GitHub Actions 的 [Package shared folder](https://github.com/epshoron/JXwork/actions/workflows/package-shared.yml) 每次 `shared/` 合入 `main` 自动打包，可以在成功运行页面的 Artifacts 下载 `JXwork-shared`。普通 Code → Download ZIP 是整个仓库。

本仓库包含论文/研报研究资料，不是公司数据部署区；不能将外部作者宣称视为本系统已复现，也不得推送未获授权的公司资料或密钥。
