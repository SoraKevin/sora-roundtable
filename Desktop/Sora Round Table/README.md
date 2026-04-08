# Sora Round Table

结构化圆桌讨论框架 —— 融合多元思维视角，以"求真"为目标主持人，邀请真实历史/当代人物进行多轮辩证对话。

## 核心特性

- **内置5位名人视角**：Elon Musk、Steve Jobs、Zhang Yiming、Andrej Karpathy、MrBeast
- **严格忠于真实思维框架**：每位嘉宾使用其经典表达DNA，非泛泛而谈
- **动态对话循环**：根据讨论动态决定发言顺序，不是固定轮流
- **挖深不铺广**：每轮只追一条最深的裂缝
- **求真 > 和谐**：鼓励尖锐交锋，拒绝表面共识
- **知识归档**：自动生成 .org 文件，保存讨论成果

## 内置嘉宾

| 嘉宾 | 思维框架 | 擅长领域 |
|------|---------|---------|
| **Elon Musk** | 成本拆解、第一性原理、垂直整合 | 火箭/电动车/AI/工程制造 |
| **Steve Jobs** | 聚焦即说不、端到端控制、技术×人文 | 产品设计、用户体验、品牌 |
| **Zhang Yiming** | 延迟满足、底层映射、信息分发效率 | 推荐算法、全球化组织、产品战略 |
| **Andrej Karpathy** | 构建即理解、March of Nines、锯齿状智能 | LLM本质、AI可靠性、神经网络训练 |
| **MrBeast** | CTR×AVD、阶梯递进、全额再投资 | YouTube/B站内容创作、病毒传播 |

## 安装

```bash
# 方式一：克隆到 skills 目录
git clone https://github.com/SoraKevin/sora-roundtable.git ~/.claude/skills/sora-roundtable

# 方式二：直接复制
cp -r /path/to/sora-roundtable ~/.claude/skills/
```

## 使用方式

在 Claude Code 中直接触发：

```
Sora圆桌讨论 AI时代，什么能力最稀缺？
圆桌  内容创作的未来在哪里？
sora roundtable  产品创新的本质是什么？
多元视角探讨  LLM的商业化路径
```

## 嘉宾选择指南

| 议题领域 | 建议嘉宾 |
|---------|---------|
| AI/LLM/技术 | Karpathy、Musk、Zhang Yiming |
| 内容创作/YouTube | MrBeast、Jobs |
| 产品设计/品牌 | Jobs、Musk |
| 工程/制造/成本 | Musk |
| 全球化/组织管理 | Zhang Yiming |
| 创业/创新思维 | Musk、Jobs、Zhang Yiming |

## 执行流程

### 1. 解析议题
从用户输入提取核心议题。未提供议题时，询问用户。

### 2. 建议嘉宾组合
根据议题领域自动建议 3-5 位嘉宾，确保立场形成张力网络。

### 3. 主持人开场
展示嘉宾列表，提出定义性问题，每位嘉宾依次发言。

### 4. 对话循环
- **动态发言轮**：根据讨论动态决定谁该发言，每人必须回应前文
- **主持人综述**：提炼核心争议点，生成 ASCII 思考框架图
- **用户指令**：`可`（继续）、`止`（结束）、`深入此节`、`引入新人物`

### 5. 结束归档
- 主持人全局总结
- 生成完整知识网络 ASCII 图
- 列出未解决的开放问题
- 写入 .org 文件到 ~/Documents/notes/

## 嘉宾句式示例

**Elon Musk**
> 「先算。原材料成本是多少？白痴指数是多少？」
> 「物理定律是唯一硬约束，其他都是建议。」

**Steve Jobs**
> 「这就是垃圾（shit）。」
> 「不够amazing，就是在造垃圾。」

**Zhang Yiming**
> 「平庸有重力，需要逃逸速度。」
> 「延迟满足感程度在不同量级的人是没法有效讨论问题的。」

**Andrej Karpathy**
> 「The LLM has no hallucination problem. Hallucination is all LLMs do. They are dream machines.」
> 「imo，构建即理解——如果不能从零重建它，就不算理解。」

**MrBeast**
> 「CTR × AVD。这是YouTube唯一重要的两个数字。」
> 「60%前30秒留存率？不是低一点，是灾难级别。」

## 文件结构

```
Sora Round Table/
├── SKILL.md              # Skill 定义文件
├── README.md             # 本文件
└── .claude-plugin/
    └── plugin.json       # Claude Plugin 元数据
```

## 设计原则

- **求真 > 和谐**：鼓励尖锐但有建设性的交锋
- **挖深不铺广**：每轮只追一条最深的裂缝
- **忠于真实思想**：每位嘉宾严格基于其思维框架发言
- **结构可视化**：用 ASCII 拓扑图暴露讨论的深层结构
- **元认知**：暴露讨论的假设、前提、推理链

## License

MIT

---

**Author**: 开锁大师-索拉
- GitHub: https://github.com/SoraKevin
- Bilibili: https://space.bilibili.com/473308248
- YouTube: https://www.youtube.com/@开锁大师索拉
