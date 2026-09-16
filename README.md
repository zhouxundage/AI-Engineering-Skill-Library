# AI Engineering Skill Library

版本 **0.1.0** · 15 个独立技能 · 中文说明，英文稳定标识。

这是用于规划、实现和验收项目的初版技能库。Master 选择本轮需要的专业工作；专业技能也可独立使用。流程随任务规模裁剪，既支持小型脚本，也支持有 SOP 约束的临床 AI 项目。它提供工作指引和模板，不是自动运行的后台系统。

## 开始使用

在能加载本库的 Codex 环境中引用技能名称，例如：

```text
使用 $ai-project-architect，帮我创建一个 SAP→Shell 原型。
先检查现有环境；使用合成数据；输出字段必须有原文定位；完成可运行的首个切片和验收记录。
```

只处理某一类问题时可直接使用 `$testing-validation`、`$rag-engineering` 等，无需先经过 Master。需要提供实际项目文件时，另行提供对应材料；本库不包含真实公司 SOP 或研究数据。

每个技能含用途、触发条件、输入、输出、流程、执行规则、完成标准、调用示例和交付模板。自动匹配保持开启，但并不保证每次新项目必然命中；显式引用名称可明确意图。

## 内容索引

| 分类 | 技能入口 | 用途 |
|---|---|---|
| 00_Master | [AI Project Architect｜项目工程总控](00_Master/ai-project-architect/SKILL.md) | 把想法转成可交付项目；选择本轮必要的专业技能，维护范围、依赖、决策和证据。Master 是工作流入口，不是后台调度服务。 |
| 01_Engineering | [Architecture Design｜系统架构设计](01_Engineering/architecture-design/SKILL.md) | 从用例和约束推导最小可行架构，使每个模块有清晰责任、接口和可验证的业务路径。 |
| 01_Engineering | [Software Engineering｜可维护实现](01_Engineering/software-engineering/SKILL.md) | 把模块规格变成可运行、可维护、可排错的实现，控制配置与依赖，提供与变更风险相称的验证。 |
| 01_Engineering | [Testing & Validation｜测试与验收](01_Engineering/testing-validation/SKILL.md) | 证明用户路径和系统契约满足已定义需求，分清测试设计、执行结果和业务验收结论。 |
| 01_Engineering | [Deployment & Operation｜部署与运行](01_Engineering/deployment-operation/SKILL.md) | 让交付物在目标环境可启动、可观测、可恢复，发布范围与用户授权一致。 |
| 02_AI | [AI System Design｜AI 系统设计](02_AI/ai-system-design/SKILL.md) | 把业务问题转成可评估的 AI 任务，先确定 AI 是否必要，再选择最小可行实现。 |
| 02_AI | [RAG Engineering｜检索增强工程](02_AI/rag-engineering/SKILL.md) | 让回答可追溯到有权访问、版本明确的原文，并将检索失败与生成失败分开诊断。 |
| 02_AI | [Agent Engineering｜工具执行与状态管理](02_AI/agent-engineering/SKILL.md) | 把开放式工具调用约束成可观察、可停止、可恢复且不重复产生副作用的执行过程。 |
| 02_AI | [AI Evaluation｜模型质量评估](02_AI/ai-evaluation/SKILL.md) | 用代表性数据和可复核评分证明 AI 是否达到任务要求，并呈现变异、失败类型和证据局限。 |
| 03_Product | [Product Strategy｜产品策略](03_Product/product-strategy/SKILL.md) | 把产品想法变成可验证价值假设，区分用户需求证据、商业假设与技术可行性。 |
| 03_Product | [MVP Design｜最小可用产品](03_Product/mvp-design/SKILL.md) | 保留从输入到有用输出的完整用户路径，用最少实现验证最重要的假设。 |
| 03_Product | [UX/UI Design｜交互与界面](03_Product/ux-ui-design/SKILL.md) | 让用户理解当前状态、完成关键任务、检查 AI 结果并从失败中恢复。 |
| 04_Domain | [Clinical Trial AI｜临床试验 AI 工作流](04_Domain/clinical-trial-ai/SKILL.md) | 将临床研究资料转换为可追溯草稿或规格，使自动处理与统计/业务审核责任可区分。 |
| 04_Domain | [Biostatistics｜生物统计分析工程](04_Domain/biostatistics/SKILL.md) | 使研究问题、统计方法、实现与解释保持一致，保留假设、偏离计划和验证依据。 |
| 04_Domain | [Pharma Regulatory｜药企约束与证据映射](04_Domain/pharma-regulatory/SKILL.md) | 在明确用途、司法辖区和规则版本的前提下，把约束落实到工程选择与可审查证据。 |

## 文件布局

分类目录用于维护源文件；安装时将每个技能文件夹直接放入目标技能目录，避免依赖分类目录扫描行为。

```text
AI-Engineering-Skill-Library/
├── 00_Master/              1 个技能；含按需读取的路由和示例
├── 01_Engineering/         4 个技能
├── 02_AI/                  4 个技能
├── 03_Product/             3 个技能
├── 04_Domain/              3 个技能
├── library.json            名称、分类、相对路径、版本的登记表
├── README.md               使用和内容索引
├── MAINTENANCE.md           更新与验证规则
├── CHANGELOG.md            库版本变化
├── scripts/                结构检查与安全安装
└── VALIDATION.md           本次实际检查记录

每个技能/
├── SKILL.md
├── agents/openai.yaml
└── assets/deliverable-template.md
```

初版仅覆盖当前请求的五类；Git、Python、R 和数据库实践放在相关技能内，暂不增加独立 Tools 类。

## 本地安装与检查

安装脚本只复制技能内容，不修改全局提示、项目文件、账户或远程服务。先预览，再安装；已有完全相同的技能跳过，有差异的同名目录将报冲突，不覆盖。

```powershell
python scripts/install_library.py --target 'C:\Users\YOUR_NAME\.agents\skills' --dry-run
python scripts/install_library.py --target 'C:\Users\YOUR_NAME\.agents\skills'
python -m pip install PyYAML
python scripts/validate_library.py
```

`python` 指当前机器可用的 Python 3；如未加入 PATH，用它的绝对路径。目标目录可显式指定给既有安装环境。技能格式、按需加载和当前本地发现路径依据 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills) 核对（2026-09-16）。若新增技能未出现，重新打开应用后检查技能列表；文件安装成功与当前会话实际加载是两项不同状态。

## 交接与证据

工程过程沿用稳定 ID，例如 REQ-001、AC-001、TEST-001。技能之间传递目标、来源文件与版本、约束、期望结果和真实证据。设计稿、模拟结果、真实集成测试与正式业务批准分别记录，不把模板填写完等同于项目通过验收。

SAP→Shell 示例与路由见 [Master 路由表](00_Master/ai-project-architect/references/routing.md) 和 [情境示例](00_Master/ai-project-architect/references/scenarios.md)。
