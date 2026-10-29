# Research Agent 独立 Alpha Prompt｜V1 草案（16份）

**重要纠正**：M3 的16个专业Research Agent只负责生成**日频Alpha因子候选**，不能把Daily中间特征生成/准入作为其任务。Daily库由独立的M1 Daily Curator管理。上一版 `SYSTEM_COMMON_V0` + `ROLE_PROFILES_V0.json` 的两句角色配置方案已废弃，禁止作为当前指示装配方式。

## 16份独立专业 Prompt

| 范围 | 独立Prompt文件 |
|---|---|
| A 单股日内（6） | [A01](roles/A01.md) · [A02](roles/A02.md) · [A03](roles/A03.md) · [A04](roles/A04.md) · [A05](roles/A05.md) · [A06](roles/A06.md) |
| C 多股日内（5） | [C01](roles/C01.md) · [C02](roles/C02.md) · [C03](roles/C03.md) · [C04](roles/C04.md) · [C05](roles/C05.md) |
| B 单股跨日（3） | [B01](roles/B01.md) · [B02](roles/B02.md) · [B03](roles/B03.md) |
| D 多股跨日（2） | [D01](roles/D01.md) · [D02](roles/D02.md) |

## 独立组件

- [加载方式](ASSEMBLY_ALPHA_V1.md)：每个角色读取自己的一份完整专业Prompt。
- [本轮动态输入](ALPHA_EPISODE_INPUT_V1.md)：真实数据和可见知识由运行时提供。
- [Alpha-only输出Schema](ALPHA_OUTPUT_SCHEMA_V1.json)：只接受Alpha候选或no_candidate。
- [16角色→Prompt映射](ALPHA_PROMPT_MANIFEST_V1.json)。
- [仍需验证的问题](REVIEW_CHECKLIST_V0.md)：旧检查清单已重定向为V1的待定项。

**Prompt不是Evaluator，也不是Daily Curator**：Alpha提交后由M4、M5A/M5B、M6和Knowledge执行既定审查；Daily版本、相关性0.6等属于独立M1，不在16个角色Prompt中实现。

状态：已完成写稿，尚未在公司环境试跑，不能宣称最佳或无偏。