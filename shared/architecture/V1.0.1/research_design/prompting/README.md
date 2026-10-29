# 16份专业 Alpha 挖掘 Prompt

每个 Agent 独立使用对应的一份 Prompt，均按**输入与工具 → 专业研究方向 → 研究过程 → 输出与交付**四部分编写。16个角色覆盖四个信息范围；最终产物为每股每日一个Alpha候选，交给M4 Candidate Register。

| 研究范围 | 角色Prompt |
|---|---|
| 单股日内（6） | [A01](roles/A01.md) · [A02](roles/A02.md) · [A03](roles/A03.md) · [A04](roles/A04.md) · [A05](roles/A05.md) · [A06](roles/A06.md) |
| 多股日内（5） | [C01](roles/C01.md) · [C02](roles/C02.md) · [C03](roles/C03.md) · [C04](roles/C04.md) · [C05](roles/C05.md) |
| 单股跨日（3） | [B01](roles/B01.md) · [B02](roles/B02.md) · [B03](roles/B03.md) |
| 多股跨日（2） | [D01](roles/D01.md) · [D02](roles/D02.md) |

[Prompt 文件清单](ALPHA_PROMPT_MANIFEST_V1.json) · [每轮动态输入](ALPHA_EPISODE_INPUT_V1.md) · [输出字段结构](ALPHA_OUTPUT_SCHEMA_V1.json) · [加载和提交方式](ASSEMBLY_ALPHA_V1.md)

研究输入按M2的实际工具能力访问四个库；未在仓库硬编码公司API、原始数据或运行口令。评价与入库按照已有M4/M5/M6流程。
