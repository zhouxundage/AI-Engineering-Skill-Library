# Agent 执行契约

目标/允许动作：{{goal_scope}}
采用 Agent 的理由：{{dynamic_decision_need}}
状态与转换条件：{{state_machine}}
检查点/恢复依据：{{checkpoint}}

| 工具/版本 | 输入 schema | 输出/错误 | 读/写 | 授权范围 | 幂等/结果查询 | 超时/重试 |
|---|---|---|---|---|---|---|
| {{tool}} | {{input}} | {{output}} | {{effect}} | {{scope}} | {{idempotency}} | {{retry_policy}} |

预算：最大步骤 {{steps}} / 时长 {{duration}} / 费用 {{cost}}
停止条件：{{done_failure_cancel_budget}}
外部内容隔离：{{untrusted_data_handling}}
人工接管条件：{{handoff_conditions}}
轨迹字段：run_id、step_id、tool_version、参数摘要/引用、结果状态、产物引用、耗时、重试次数。

| 场景 | 预期行为 | 实际证据 | 状态 |
|---|---|---|---|
| 工具超时且结果未知 | 先查状态，不盲目重复写入 | {{evidence}} | 未运行 |
| 中断后恢复 | 从检查点继续，已完成动作不重复 | {{evidence}} | 未运行 |
| 不可信工具文本要求越权 | 保持原任务与工具权限 | {{evidence}} | 未运行 |
| 用户取消 | 停止后续动作并报告已发生效果 | {{evidence}} | 未运行 |
