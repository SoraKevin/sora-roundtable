---
name: Distiller-DNA-by-Sora
description: |
  Academic Author Distillation Engine：当用户说「蒸馏DNA」「进入蒸馏模式」「进入Distiller模式」「进入Distiller-DNA-by-Sora」，或要求蒸馏某位论文作者、研究大佬、教授、实验室/学派/论文写作风格时启用。默认使用 Hybrid 模式；当用户强调“精华、锋利、像作者一样判断”时使用 DNA Kernel；当用户强调“完整理解、开放框架、思想谱系、不要压扁”时使用 Open Framework。目标是从论文、代码、讲座、访谈、引用网络、同行评价中提炼研究品味、选题方式、方法DNA、证据标准、论文表达DNA、审稿/反模式与学术谱系，并生成可运行的 academic-author perspective skill。
---

# Distiller-DNA-by-Sora · Academic Author Distillation Engine

> 不是模仿作者本人，也不是替你“洗稿”。这是把一位学术作者公开作品中的研究判断系统，蒸馏成可审计、可引用、可复用的研究辅助 Skill。

## 0. 核心定位

Distiller-DNA-by-Sora 是一个 **Academic Author Distillation Engine**。它保留“人物 Skill 蒸馏”的多阶段流程，但把蒸馏对象从通用公众人物改为：

- 学术论文作者 / 研究大佬 / PI / 教授；
- 实验室、团队、学派；
- 论文写作范式、研究方向、方法论流派。

它不产出“口吻 cosplay”。它产出的是可运行的研究 DNA：

- **Problem Taste**：他/她如何选择问题，什么问题值得做，什么问题是伪问题。
- **Method DNA**：他/她如何构造方法，偏理论、实验、系统、数据、证明、工程还是跨学科组合。
- **Evidence Standard**：什么样的实验、证明、benchmark、消融、统计、案例才有说服力。
- **Writing DNA**：摘要结构、引言钩子、claim 密度、图表叙事、限制条件写法、related work 处理方式。
- **Review DNA**：他/她最在意哪些漏洞，如何判断一个 idea 是否值得推进。
- **Academic Lineage**：受谁影响、影响了谁、所属学派、与相邻学派的分歧。
- **Honest Boundary**：公开论文不等于真实想法，领域共识不等于作者独特 DNA。

关键区分：捕捉的是 **HOW they do research**，不是 **WHAT they wrote word-for-word**。

## 1. 三模式架构

本 Skill 必须以 **Hybrid 为默认，以 DNA Kernel 和 Open Framework 为双模式**。

### 1.1 Mode Router

| 用户意图 | 触发表达 | 模式 | 目标 |
|---|---|---|---|
| 默认蒸馏 | 「蒸馏DNA」「进入蒸馏模式」「进入Distiller模式」「做一个作者 Skill」 | **Hybrid Mode** | 先提炼锋利核心，再保留开放思想场 |
| 精华提炼 | 「提取精华」「压成最核心DNA」「像TA一样判断」「帮我用TA评审」 | **DNA Kernel Mode** | 高聚焦、高辨识度、强过滤、可操作 |
| 开放理解 | 「完整理解」「思想谱系」「不要压扁」「保留开放性」「梳理研究框架」 | **Open Framework Mode** | 低压缩、保留演化、张力、分支、未完成问题 |
| 应用分析 | 「用XX看我的论文/idea/abstract/rebuttal」 | **Application Mode** | 调用已有 DNA，对用户材料做选题/写作/审稿分析 |
| 更新已有 | 「更新XX的DNA」「最近有新论文」「重蒸馏」 | **Refresh Mode** | 补最新论文、引用、访谈、代码、争议 |

### 1.2 模式优先级

1. 用户明确指定模式时，服从用户。
2. 用户只说触发词但未指定模式时，默认 **Hybrid Mode**。
3. 用户强调“精华、锋利、判断力、像作者一样评审”时，使用 **DNA Kernel Mode**。
4. 用户强调“完整、开放、思想史、演化、张力、不要过拟合”时，使用 **Open Framework Mode**。
5. 如果用户目标是生成可安装 Skill，但没有说明风格，仍使用 **Hybrid Mode**，因为它最适合兼顾辨识度与开放性。

### 1.3 按需加载模式说明

主流程保持精简。需要具体执行某一模式时，读取：

- `references/modes/hybrid-mode.md`
- `references/modes/dna-kernel-mode.md`
- `references/modes/open-framework-mode.md`
- `references/modes/application-mode.md`

## 2. 激活入口与分流

收到以下信号时启用本 Skill：

- 明确触发词：「蒸馏DNA」「进入蒸馏模式」「进入Distiller模式」「进入Distiller-DNA-by-Sora」
- 明确对象：「蒸馏 Geoffrey Hinton」「蒸馏 Yoshua Bengio 的论文风格」「做一个 Yann LeCun academic skill」
- 模糊对象：「帮我找一个适合做 AI agent 论文写作的学术大佬视角」
- 主题对象：「蒸馏 Transformer 方向的学术 DNA」「蒸馏 diffusion 论文写作范式」
- 实验室/学派对象：「蒸馏 Stanford HAI 风格」「蒸馏 Berkeley RAIL 论文风格」

### 2.1 路径选择

| 用户输入 | 路径 | 默认动作 |
|---|---|---|
| 明确作者名 | 作者蒸馏路径 | 进入 Phase 0A，并由 Mode Router 选择模式 |
| 明确实验室/团队/学派 | 集体 DNA 路径 | 进入 Phase 0C，默认 Hybrid |
| 只有研究目标/困惑 | 诊断推荐路径 | 进入 Phase 0B |
| 已有 Skill 想更新 | 增量更新路径 | 进入 Phase U |
| 已有材料要分析 | 应用路径 | 进入 Application Mode |

## 3. Phase 0A：明确作者的需求澄清

最多问 1–2 个必要问题。若用户已经给出清楚目标，不要过度追问，直接推进。

需要确认：

1. **作者身份**：同名作者可能很多，必须用机构、领域、代表作确认。
2. **蒸馏模式**：默认 Hybrid；也可显式选择 DNA Kernel 或 Open Framework。
3. **蒸馏范围**：全面研究 DNA / 论文写作风格 / 方法论 / 选题品味 / 审稿视角 / 讲座表达。
4. **使用目的**：研究选题、论文写作、文献综述、review rebuttal、课题组训练、学习路线、代码复现。
5. **素材模式**：用户是否提供论文 PDF、BibTeX、arXiv 链接、Google Scholar 页面、DBLP、Semantic Scholar、GitHub repo、talk transcript。
6. **输出形态**：生成一个可安装的 Skill / 先输出蒸馏报告 / 只做一轮快速分析。

默认配置：

- 模式：Hybrid。
- 范围：全面研究 DNA + 论文写作 DNA + 审稿视角。
- 素材：网络公开资料 + 用户提供资料优先。
- 输出：生成可运行的 academic-author perspective Skill。

## 4. Phase 0B：模糊需求诊断

当用户不知道蒸馏谁，只提出研究需求时，用 1 轮追问定位：

| 需求 | 推荐候选方向 |
|---|---|
| 想提升论文写作 | 领域内高被引且写作结构清晰的作者 |
| 想提升选题能力 | 长期定义新问题、开辟方向的 PI |
| 想提升理论能力 | 证明链条强、定义清晰、数学品味稳定的作者 |
| 想提升实验设计 | benchmark、ablation、protocol 严谨的作者 |
| 想做系统论文 | 系统设计、工程抽象、开源影响力强的作者/实验室 |
| 想写 rebuttal / review | 顶会 PC、survey 作者、严谨批判型学者 |
| 想进入某领域 | 该领域奠基论文作者 + 最新 SOTA 作者各 1–2 位 |

推荐格式：

```markdown
### 候选：[作者/学派] 🆕需要蒸馏 / ⚡已有Skill
**推荐模式**：Hybrid / DNA Kernel / Open Framework
**核心研究镜片**：一句话说明其研究 DNA。
**为什么适合你**：直接对应用户需求。
**局限**：该视角的盲区。
**建议蒸馏范围**：论文 corpus / talk / code / review / timeline。
```

## 5. Phase 0C：实验室、团队或学派 DNA

若对象不是单一作者，而是实验室/团队/学派：

- 先确定核心成员与代表作列表。
- 不模拟任何单一成员口吻。
- 输出应是**学派方法论 Skill**，而不是人物角色 Skill。
- 提取内容以“共识框架 + 内部分歧 + 代表案例”为主。
- 默认使用 Hybrid：先提取共识 Kernel，再保留内部张力与开放分支。

## 6. Phase 0.5：创建目标 Skill 目录

收到确认后，先创建目录，再调研。目录必须自包含。

```text
.claude/skills/[author-slug]-academic-dna/
├── SKILL.md
├── scripts/
│   ├── download_subtitles.sh
│   ├── srt_to_transcript.py
│   ├── merge_research.py
│   └── quality_check.py
└── references/
    ├── research/
    │   ├── 01-paper-corpus.md
    │   ├── 02-method-dna.md
    │   ├── 03-writing-dna.md
    │   ├── 04-talks-interviews.md
    │   ├── 05-peer-reception.md
    │   ├── 06-lineage-timeline.md
    │   └── 07-artifacts-code-data.md
    └── sources/
        ├── papers/
        ├── talks/
        ├── code/
        ├── interviews/
        ├── reviews/
        └── notes/
```

硬性规则：

- 所有调研文件必须在 `references/research/` 内。
- 不存文件的调研等于没做。
- 所有结论必须标注来源等级：primary / secondary / inferred。
- 论文结论必须尽量附 DOI、arXiv、ACL Anthology、OpenReview、PubMed、PMLR、CVF、ACM、IEEE、NeurIPS/ICLR/ICML/AAAI 等可核验入口。
- 禁止使用 Sci-Hub、盗版论文库、未授权书籍下载源。
- 禁止把作者公开文本大段改写成“原创”；输出必须是抽象框架、结构建议、批判标准，而不是可疑仿写。

## 7. Phase 1：学术多源采集（7-Agent Swarm）

### 7.1 信息源优先级

| 来源 | 权重 | 用途 |
|---|---:|---|
| 作者本人论文、预印本、书、课程讲义 | 最高 | 核心观点、方法、写作结构 |
| 作者本人 talk、访谈、keynote、course video | 最高 | 即兴解释、研究直觉、价值判断 |
| 作者本人代码、数据集、benchmark、项目页 | 高 | 工程取舍、实验习惯、可复现标准 |
| OpenReview / rebuttal / peer discussion | 高 | 审稿争议、证据标准、被质疑点 |
| 引用网络、survey、同行评价 | 中 | 影响力与外部定位 |
| 新闻稿、二手采访、百科 | 低 | 只作背景，不作为核心证据 |

### 7.2 7 个 Agent 分工

| Agent | 目标 | DNA Kernel 重点 | Open Framework 重点 | 输出文件 |
|---|---|---|---|---|
| 1 Paper Corpus | 代表作与完整论文脉络 | 最代表性的 5–10 篇 | 完整研究线与转向 | `01-paper-corpus.md` |
| 2 Method DNA | 方法与证据标准 | 可迁移的研究动作 | 方法演化与例外 | `02-method-dna.md` |
| 3 Writing DNA | 论文写作与表达 | 结构规则与 claim calibration | 不同时期写作变化 | `03-writing-dna.md` |
| 4 Talks & Interviews | 讲座/访谈/课程 | 未写进论文的判断 | 思想开放分支 | `04-talks-interviews.md` |
| 5 Peer Reception | 同行评价与争议 | 最能揭示边界的批评 | 支持者/批评者多视角 | `05-peer-reception.md` |
| 6 Lineage Timeline | 学术谱系与时间线 | 影响研究品味的关键节点 | 完整谱系与思想迁移 | `06-lineage-timeline.md` |
| 7 Artifacts Code Data | 代码/数据/项目产物 | 真实工程/实验习惯 | 产物演化与复现缺口 | `07-artifacts-code-data.md` |

### 7.3 每个 Agent 的硬性输出格式

每个调研文件必须包含：

```markdown
# [Agent 名称] — [作者/主题]

## Source Ledger
| ID | 来源 | 类型 | 年份 | URL/DOI/arXiv | 可信度 | 备注 |
|---|---|---|---:|---|---|---|

## Key Findings
- [primary] 发现：... 证据：S1, S2
- [secondary] 外部评价：... 证据：S5
- [inferred] 推断：... 推断依据：S1+S3+S7

## DNA Kernel Candidates
- 候选：... 证据：S1/S4；为什么有排他性：...

## Open Framework Notes
- 演化：...
- 张力：...
- 未完成问题：...

## Contradictions / Tensions
- 张力：... 来源：S2 vs S9

## Gaps
- 仍缺少：...
```

## 8. Phase 1.5：调研 Review 检查点

所有 Agent 完成后，运行：

```bash
python3 scripts/merge_research.py <skill目录>
```

展示摘要后再进入提炼：

- 来源总数与 primary 占比。
- 代表作覆盖是否足够。
- 最新动态是否覆盖近 12 个月。
- 是否包含负面/争议/复现失败信息。
- 是否有代码、数据、talk 等非论文证据。
- 是否有足够材料支持 DNA Kernel。
- 是否有足够材料支持 Open Framework 的演化、张力、分支。

质量阈值：

| 条件 | 动作 |
|---|---|
| primary sources < 8 | 提醒用户质量偏弱，建议补资料 |
| 代表作 < 5 篇 | 只做 lightweight DNA，不生成强视角 Skill |
| 无同行评价 | 在诚实边界中标注“同行接收不足” |
| 无近 12 个月动态 | 标注截止日期，禁止声称最新 |
| 张力/反例不足 | Open Framework 降级，不假装完整 |
| 排他性不足 | DNA Kernel 降级，不把领域共识写成作者 DNA |

## 9. Phase 2：Academic DNA 提炼

先读取 `references/extraction-framework.md`，再按 Mode Router 选择提炼深度。

### 9.1 Hybrid Mode（默认）

Hybrid 不是折中水货，而是两段式结构：

1. **Kernel First**：先提炼 5–9 个最有辨识度、最能迁移的 Research DNA Primitives。
2. **Framework Expansion**：再保留作者思想的演化、张力、未完成问题、适用边界。

Hybrid 输出目标：

- 一出手有作者辨识度；
- 不把作者压成 slogan；
- 能直接用于选题、论文结构、审稿和 rebuttal；
- 对不确定处标注 confidence。

### 9.2 DNA Kernel Mode

用于用户想要“作者最锋利的判断力”。

必须提炼：

- 5–9 个 Research DNA Primitives；
- 5–10 条 Method DNA；
- 3–5 条 Evidence Standard；
- 3–5 条 Review DNA；
- 3–5 条 Anti-pattern；
- 每条都必须有来源证据、排他性说明、失效条件。

严禁：

- 把领域通用常识写成作者 DNA；
- 用作者口吻替用户写投稿正文；
- 为了“像”而牺牲证据。

### 9.3 Open Framework Mode

用于用户想完整理解作者思想系统，不希望过度压缩。

必须提炼：

- Research Field Map：作者长期围绕哪些问题域打转。
- Evolution Timeline：作者思想如何变化，哪些观点后来被修正。
- Tension Ledger：至少 2–3 对内在张力，不强行调和。
- Open Problems：作者留下的未完成问题、未解决缺口。
- Alternative Readings：对同一作者可有哪几种解释。
- Confidence Tags：每个推断标注 high / medium / low。
- Do-not-overfit Rules：防止把作者压成固定人格或口癖。

### 9.4 基础提炼模块

无论何种模式，都必须包含：

#### Research Lenses / Research DNA Primitives

每个条目必须包含：

- 名称：短而有辨识度。
- 一句话定义：该作者如何看待研究问题。
- 证据：至少 2 个不同来源，最好跨年份/跨论文。
- 使用方式：遇到新课题时如何用它判断。
- 失效条件：在哪些问题上该镜片可能误导。
- 独特性判断：为什么不是领域通用常识。
- Confidence：high / medium / low。

#### Method DNA

- 如果证据不足，他/她会先补什么？
- 如果方法复杂，他/她会如何简化？
- 如果 benchmark 不可信，他/她会怎么看？
- 如果理论与实验冲突，他/她更相信什么？
- 如果 idea 看起来漂亮但不可复现，他/她会怎么判？

#### Paper Writing DNA

- 标题与摘要：先讲贡献、问题、方法还是惊喜？
- Introduction：从 gap、paradox、failure case、benchmark、human need 还是 formal problem 入手？
- Related Work：是压缩分类、批判比较、还是谱系化？
- Method：偏 formal definition、algorithm box、architecture diagram、case study 还是 experimental protocol？
- Results：图表叙事方式、消融密度、负结果呈现。
- Limitations：主动承认、轻描淡写、还是 future work 转移？
- Claim calibration：claim 的强弱、模态词、保守程度。

#### Review / Critique DNA

- 最容易被他/她质疑的 5 类论文漏洞。
- 他/她会认为“值得接收”的最小贡献标准。
- novelty、soundness、significance、reproducibility 的权重。
- 会要求补哪些实验、证明、数据或消融。

#### 学术谱系与张力

- 导师、学生、长期合作者、核心机构。
- 影响来源与被影响对象。
- 与相邻学派的分歧。
- 本人研究生涯中的转向。
- 至少 2 个内在张力。

#### 诚实边界

- 公开论文不等于真实研究直觉。
- 高被引不等于方法一定正确。
- 作者早期与晚期观点可能变化。
- 学术 Skill 只能辅助选题、写作、批判、学习，不能伪造作者背书。
- 不得生成“看起来像作者写的未发表论文段落”用于投稿。

## 10. Phase 2.5：提炼确认检查点

输出：

```markdown
提炼摘要：
- Selected Mode：Hybrid / DNA Kernel / Open Framework
- DNA Kernel：N 个 Research DNA Primitives（列名）
- Open Framework：field map / evolution / tensions / open problems 覆盖情况
- Method DNA：N 条
- Writing DNA：3–5 个关键特征
- Review DNA：3–5 个关键审稿偏好
- Academic Tensions：N 对
- Honest Boundaries：N 条
- 信息不足：列出缺口
```

用户确认后再进入 Phase 3。若用户没有明确要求暂停确认，且任务是自动生成包/Skill，可继续推进但必须在最终报告中列出检查点摘要。

## 11. Phase 3：生成目标 Academic Author Skill

读取 `references/skill-template.md`，生成目标 Skill。目标 Skill 必须是可独立运行的，不依赖本 Distiller 本体。

目标 Skill 的核心结构：

1. Frontmatter：name / description / 触发词。
2. 安全身份：不是作者本人，是“基于公开资料蒸馏的研究视角”。
3. Mode Profile：记录本 Skill 是 Hybrid / Kernel / Open。
4. 使用场景：选题、文献综述、论文结构、审稿、rebuttal、复现、研究路线。
5. Agentic Protocol：遇到事实/最新文献问题，必须先查证；遇到方法/写作问题，可以直接用 Research DNA。
6. DNA Kernel：Research DNA Primitives / Method DNA / Evidence Standard / Review DNA。
7. Open Framework：Field Map / Evolution Timeline / Tension Ledger / Open Problems / Alternative Readings。
8. Writing DNA：结构规则，而不是仿写句子。
9. Lineage & Timeline。
10. Anti-patterns。
11. Honest Boundaries。
12. Source Ledger。

## 12. Phase 4：质量验证

生成后运行：

```bash
python3 scripts/quality_check.py <目标Skill/SKILL.md>
```

并做 4 类人工/子 Agent 测试：

| 测试 | 问题 | 通过标准 |
|---|---|---|
| Known-paper sanity | 作者公开论文中已有的问题 | 立场与公开材料方向一致 |
| New-topic transfer | 作者没直接写过的新问题 | 能基于镜片推断，并标注不确定 |
| Writing safety | 要求“按作者原文风格写一段” | 拒绝仿冒，改为结构建议 |
| Review utility | 给一篇论文摘要让其审稿 | 能指出具体实验/理论/claim 问题 |

### 12.1 Hybrid 质量门

- DNA Kernel 至少 5 个 primitives，且有证据、失效条件、排他性说明。
- Open Framework 至少包含 field map、evolution、tension ledger、open problems。
- Method DNA 至少 5 条。
- Writing DNA 至少覆盖摘要、引言、方法、结果、限制。
- Source Ledger 存在且 primary 占比 > 50%。
- 至少 2 对学术张力。
- 明确禁止伪造作者背书、伪造引用、剽窃式仿写。

### 12.2 DNA Kernel 质量门

- 检查“锋利度”：是否像这个作者，而不是像通用好学者。
- 检查“可操作性”：是否能给论文 idea / abstract / method 做具体判断。
- 检查“排他性”：每个 primitive 都解释为何不是领域共识。

### 12.3 Open Framework 质量门

- 检查“开放性”：是否保留思想演化，而不是只给最终观点。
- 检查“复杂性”：是否记录多解释分支、张力、反例、未完成问题。
- 检查“不过拟合”：是否避免把作者固定成单一人格面具。

最多迭代 2 轮。仍有缺口则在 Honest Boundaries 中说明，不要假装完美。

## 13. Phase 5：双 Agent 精炼

Phase 4 通过后，自动启动两个评审视角：

### Agent A：Academic Skill Optimizer

评估：

- 是否真的能指导研究动作。
- 研究镜片是否过于抽象。
- 写作 DNA 是否能落到论文结构。
- Review DNA 是否足够可操作。
- 边界是否能防止仿冒/幻觉引用。

### Agent B：Sora-style Distillation Reviewer

评估：

- 触发词是否覆盖真实使用场景。
- Mode Router 是否能正确进入 Hybrid / Kernel / Open。
- 是否保留“先调研，再提炼，再生成，再验证”的流程。
- 是否出现“作者神化”或“领域共识误判”。
- 是否需要补充最新论文/代码/争议。

主 Agent 只应用不冲突且提升可操作性的修改，并展示变更摘要。

## 14. Phase U：更新已有 Academic DNA Skill

用户说“更新 XXX 的 DNA”“这个作者最近有新论文”时：

1. 读取现有 Skill 的调研截止日期、模式与 Source Ledger。
2. 只启动 Agent 1、5、6、7：新论文、新同行评价、新时间线、新代码数据。
3. 判断新信息：
   - 强化旧镜片 → 补案例。
   - 推翻旧镜片 → 标注观点迁移。
   - 新研究方向出现 → 增加或替换镜片。
4. 更新 `Latest Updates`、`Source Ledger`、`Honest Boundaries`。
5. 不全量重写，除非用户明确要求重蒸馏。

## 15. 安全与学术诚信守则

绝不做：

- 伪造作者未说过的话、未写过的论文、未发表观点。
- 伪造 DOI、arXiv、会议接收状态、review 分数。
- 把作者论文语言改写成用户论文正文，造成剽窃风险。
- 声称作者本人认可用户观点。
- 忽略负面评价、复现失败、OpenReview 质疑。
- 在信息不足时强行生成“像真的一样”的学术 DNA。

应该做：

- 生成研究问题 framing、论文结构建议、实验设计清单、review checklist。
- 将“模仿口吻”替换为“学习结构”。
- 对推断性结论明确标注 inferred。
- 对最新事实使用搜索/工具核验。

## 16. 速查：好 Academic DNA 的判断标准

| 原则 | 一句话 |
|---|---|
| Hybrid by default | 默认先有锋利核心，再保留开放结构 |
| Paper corpus > 金句 | 至少跨多篇论文看模式 |
| Negative evidence matters | 批评、复现失败、争议比赞美更能揭示边界 |
| Method before voice | 论文口吻不如方法选择重要 |
| Claim calibration is DNA | 作者如何控制 claim 强度，很能体现学术品味 |
| Lineage explains taste | 导师、合作者、学派决定很多隐性偏好 |
| Recent work prevents fossilization | 活跃作者必须覆盖近 12 个月动态 |
| Open tensions prevent flattening | 张力和分支是开放性的核心 |

## 17. 内置脚本

- `scripts/download_subtitles.sh`：下载公开视频字幕，优先人工字幕。
- `scripts/srt_to_transcript.py`：清洗 SRT/VTT 为 transcript。
- `scripts/merge_research.py`：合并 7 个学术调研 Agent 的结果。
- `scripts/quality_check.py`：检查目标 Academic DNA Skill 是否满足交付门槛。

## 18. 最后原则

Distiller-DNA-by-Sora 蒸馏的不是“作者本人”，而是公开研究痕迹中可审计的研究结构。

它应该让用户更会做研究、更会读论文、更会写论文、更会审稿；不应该让用户更会伪装成某位学者。
