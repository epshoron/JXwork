# JXwork｜研究资源与 Agent 协作仓库

> **版本边界（2026-11-12）**：本公开仓库的 `shared/architecture/V1.0.1/` 是 2026-10-29 的**公开研究设计基线**，不能用来断言公司执行系统的最新代码、门槛或运行进度。后续另有经授权的私有执行进度报告；查阅位置和交接要求见 [研究 Agent 接手入口](assistant/JXWORK_START_HERE.md)。私有报告及公司数据/结果不复制到本公开仓库。


**2026-10-29 起：三个业务区，各自面向不同读者。**

| 入口 | 内容 | 对公司云端的关系 |
|---|---|---|
| [`shared/`](shared/README.md) | A / B / C 研究档案、**已确定的 V1.0.1 Research Loop**、统一评价规范 | **仅把它作为知识/架构输入**；研究归档约定不是运行时 Prompt |
| [`assistant/`](assistant/README.md) | 给 ChatGPT/文献研究 LLM 的审批、认领、协作、日志、交接 | 公司执行 Agent **不需要** |
| [`presentation/`](presentation/README.md) | HTML 地图、Excel、ZIP、离线展示 | 按需读取 |

**架构权威入口**：[V1.0.1](shared/architecture/V1.0.1/README.md)。四库：Min、论文/研报、Daily、Knowledge；Knowledge 记录一切候选与实验，第一关技术/统计检查通过后才开展金融评价；达标即正式存档，不增设第五个 Alpha 库。具体规则见架构文档。

**下载**：GitHub Actions 的 [Package shared folder](https://github.com/epshoron/JXwork/actions/workflows/package-shared.yml) **仅在用户点击 Run workflow 手动触发时**打包；打开工作流页选择 `main` 并运行，完成后在该次成功运行的 Artifacts 下载 `JXwork-shared`。修改 shared 或 push main 均**不会自动打包**。普通 Code → Download ZIP 是整个仓库。

本仓库包含论文/研报研究资料，不是公司数据部署区；不能将外部作者宣称视为本系统已复现，也不得推送未获授权的公司资料或密钥。
