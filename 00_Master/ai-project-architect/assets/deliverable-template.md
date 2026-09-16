# 项目工程简报

项目：{{project_name}}  版本：{{version}}  本轮范围：{{scope}}
任务模式：设计 / 实现 / 修复
目标用户：{{user}}  用户成功状态：{{observable_outcome}}
现有成果：{{existing_artifacts}}  不包含：{{out_of_scope}}

## 环境契约

OS/运行时与已核实版本：{{environment}}
依赖来源/锁文件：{{dependency_lock}}
配置与密钥入口：{{configuration_without_secrets}}
从干净环境安装、启动和验证的步骤：{{reproduce_steps}}
网络/离线条件：{{network}}  预期启动耗时（项目目标）：{{target_time}}

## 约束与需求

| ID | 约束/需求 | 来源、版本、定位 | 硬性/偏好/待核实 | 影响 | 验收证据 |
|---|---|---|---|---|---|
| C-001 | {{constraint}} | {{source}} | {{kind}} | {{design_impact}} | {{evidence}} |
| REQ-001 | {{user_need}} | {{request}} | {{priority}} | {{component}} | AC-001 |

## 架构与首个切片

业务路径：{{input_to_output}}
横向边界：{{shared_capabilities_with_justification}}
纵向切片：{{first_complete_user_journey}}
API/CLI/UI 入口：{{entrypoints}}
模块契约：{{input_schema_output_schema_error_contract}}
关键决策：{{decision_alternatives_reason_revisit_trigger}}

## 执行与交接

| 顺序 | 技能/工作 | 选择理由 | 输入/版本 | 产物 | 依赖 | 完成证据 |
|---|---|---|---|---|---|---|
| 1 | {{skill_or_equivalent}} | {{why}} | {{inputs}} | {{outputs}} | {{depends_on}} | {{evidence}} |

交接记录：目标 / 来源技能 / 目标技能 / 产物路径与版本 / 约束 ID / 验收 ID / 状态 / 阻塞项。

## 验收与交付

| ID | 场景 | 预期可观察行为/阈值来源 | 验证方法 | 实际证据 | 状态 |
|---|---|---|---|---|---|
| AC-001 | {{scenario}} | {{expected}} | {{method}} | {{artifact_or_run}} | 未运行 |

状态仅用：已通过 / 失败 / 未运行 / 不适用（说明原因）。
已交付：{{deliverables}}  未完成：{{remaining}}  下一步：{{next_action}}
