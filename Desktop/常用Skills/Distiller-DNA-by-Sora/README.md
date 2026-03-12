# Distiller-DNA-by-Sora

**Academic Author Distillation Engine**：用于蒸馏学术论文作者、研究大佬、实验室/学派的研究 DNA。

触发词：

- `蒸馏DNA`
- `进入蒸馏模式`
- `进入Distiller模式`
- `进入Distiller-DNA-by-Sora`

## 核心变化

本版本以 **Hybrid 为默认，以 DNA Kernel 和 Open Framework 为双模式**。

| 模式 | 用途 | 适合场景 |
|---|---|---|
| Hybrid | 默认模式：先提核心 DNA，再保留开放思想场 | 生成可安装 academic-author skill |
| DNA Kernel | 高聚焦、高辨识度、强过滤、可操作 | 用某作者视角评审论文 idea / abstract / method |
| Open Framework | 低压缩，保留演化、张力、未完成问题 | 完整理解作者思想谱系和研究路线 |

## 安装

将整个目录复制到 Claude Code 的 skills 目录，例如：

```bash
mkdir -p ~/.claude/skills
cp -r Distiller-DNA-by-Sora ~/.claude/skills/
```

然后在 Claude Code 中输入：

```text
进入蒸馏模式，帮我蒸馏 Geoffrey Hinton 的 Academic DNA
```

或：

```text
蒸馏DNA：请用 Open Framework 模式梳理 Judea Pearl 的思想谱系
```

或：

```text
进入Distiller-DNA-by-Sora，用 DNA Kernel 模式蒸馏 Karpathy 的研究与论文写作 DNA
```

## 目录结构

```text
Distiller-DNA-by-Sora/
├── SKILL.md
├── references/
│   ├── extraction-framework.md
│   ├── skill-template.md
│   └── modes/
│       ├── hybrid-mode.md
│       ├── dna-kernel-mode.md
│       ├── open-framework-mode.md
│       └── application-mode.md
├── scripts/
│   ├── download_subtitles.sh
│   ├── srt_to_transcript.py
│   ├── merge_research.py
│   └── quality_check.py
└── examples/
    └── prompt-examples.md
```

## 使用示例

### 默认 Hybrid

```text
蒸馏DNA：帮我做一个 Geoffrey Hinton Academic DNA Skill，用于研究选题、论文写作和审稿。
```

### DNA Kernel

```text
进入Distiller模式，用 DNA Kernel 模式提炼 Karpathy 最核心的研究判断 DNA。
```

### Open Framework

```text
进入蒸馏模式，用 Open Framework 模式梳理 Judea Pearl 的研究思想谱系，不要压缩成几条原则。
```

## 安全边界

这个 Skill 不用于模仿作者本人、不伪造引用、不生成作者口吻投稿正文。它用于提炼公开研究痕迹中的可审计研究结构：选题、方法、证据、写作、审稿、谱系和边界。
