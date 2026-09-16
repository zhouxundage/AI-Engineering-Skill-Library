# 架构说明与决策记录

系统/版本：{{system_version}}  场景：{{scenario}}  约束 ID：{{constraints}}
上下文图/数据流：{{diagram_or_text_flow}}

| 模块 | 责任/边界 | 输入 | 输出 | 状态所有者 | 依赖 | 失败行为 |
|---|---|---|---|---|---|---|
| {{module}} | {{responsibility}} | {{schema}} | {{schema}} | {{owner}} | {{dependency}} | {{failure}} |

## 接口契约

入口/版本：{{entrypoint_version}}
字段、类型、必需性、单位：{{schema}}
错误码与可重试条件：{{errors}}
超时、幂等性、并发限制：{{runtime_contract}}
鉴权/数据范围（如适用）：{{access_scope}}
目录与责任映射：{{directory_map}}
注册机制：不适用 / {{registry_key_interface_version_duplicate_policy}}

## ADR-001

问题与驱动约束：{{problem}}
备选方案：{{alternatives}}
决定及证据：{{decision_and_evidence}}
代价与后果：{{tradeoffs}}
重审触发条件：{{revisit}}

首个切片：{{entry_to_output}}
成功场景走查：{{success_walkthrough}}
失败场景走查：{{failure_walkthrough}}
待验证假设：{{assumptions}}
