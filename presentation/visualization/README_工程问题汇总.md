# P001–P010 工程问题汇总与资料包

**当前有效版本（2026-10-26）**：旧的手写 XLSX 曾触发 Excel 修复提示并截断文本，已废弃。现由 [openpyxl 脚本](build_engineering_package.py) 从原始 CSV **重新生成**，不要使用旧 ZIP。

- **Excel**：[十 Sheet 工作簿](JXwork_P001-P010_Engineering_QA.xlsx)，共 136 个工程问题；统一列宽、左对齐、垂直居中、自动换行，按内容估算行高。
- **ZIP**：[完整资料包](JXwork_P001-P010_Engineering_QA_Pack.zip)，含工作簿、`README.html` 与 `resources/` 离线说明；须**完整解压**并保持同级目录才能使用 D 列相对路径链接。
- **原始来源**：本项目图解在包内提供 HTML/Markdown；论文及作者源码保留本地导航页，访问原网站仍需联网。
- **验证**：[GitHub Actions 记录](https://github.com/epshoron/JXwork/actions/runs/40280727878) 已成功；执行 openpyxl 重新加载、逐表行数/换行/对齐/行高/链接检查、ZIP 内容检查。**尚未在用户 Windows Excel 环境实机打开验证**。

本次只修复展示文件与打包流程；各篇原始 CSV/XLSX、创新/局限与 Delta 不改动。
