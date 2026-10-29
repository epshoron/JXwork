# New-Root Exploration｜独立探索入口原型

**问题**：Agent如果不断沿现有 Alpha 研究结论展开，可能集中在少数金融研究 root；随机隐藏一些旧记录并不保证产生新 root。

**建议用三种独立的研究起点**：① 时间合法、来源可查的客观数据观察；② 真实论文/研报中的未解研究问题；③ 观察与已有解释之间的未解释差异。它们只为现有16个专业 Alpha Agent 提供研究问题，不创建第17个专业角色，也不改变其完整Prompt。

## 最小流程

1. M2或文献模块提供包含 `seed_id, kind, statement, role_ids, source_refs, required_fields, first_usable_at, source_snapshot` 的证据条目，真实性和未来信息合法性由来源模块保证。
2. [root_probe.py](root_probe.py) 将条目转换成按role_id路由、稳定编号的 `research_task`。这个阶段尚未出现新root，也不生产因子。
3. 原有Research Agent据此独立提出 **Alpha候选**，仍由M4登记、M5/M6评价，既定金融门槛不变。
4. 另由独立审阅者在**完整**Knowledge下比较金融机制、必要观察与可证伪预测；`review`命令只准备对照材料，**不自动判定新root**。

## 运行与验证

只使用Python标准库、公开合成样例，无API密钥或公司数据：

```bash
python root_probe.py prepare sample_synthetic.json
python -m unittest discover -p 'test_root_probe.py' -v
```

`python root_probe.py review proposal.json existing_roots.json` 可准备root比较材料。提案字段为 `probe_id, mechanism_claim, necessary_observation, falsifiable_prediction`；已有root多一个 `root_id`。

这只是**可运行的研究问题准备原型**。尚未实现：公司数据观察的自动发现、M2真实工具适配、LLM生成金融机制、正式root审核、线上收益验证；这几件事不会被这段原型假装已完成。

## 研究依据（只作方法启发）

- [SHELDON（2026）](https://arxiv.org/abs/2610.18025)：观察空间与假设空间独立探索，寻找现有解释没有覆盖的观察。不是股票Alpha实证。
- [NOVA（ACL 2025）](https://aclanthology.org/2025.findings-acl.1099/)：规划外部知识检索扩大创意来源。
- [EvoDiverse（ICML 2026）](https://proceedings.mlr.press/v306/wang26gx.html)：讨论假设搜索的质量-多样性平衡；本模块不实现或启用M9进化。
- [Si等（ICLR 2025）](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ea94957d81b1c1caf87ef5319fa6b467-Abstract-Conference.html)：LLM科研想法的自评及多样性有局限，因此不直接相信Agent自称的新颖性。

**范围**：这是一个独立、可选的探索策略原型，不修改Full/Masked、不设抽样概率、不改M9、不覆盖S16/S17正在处理的M1/M2/M4/M8文件。