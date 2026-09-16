# AI 任务契约

任务/用户价值：{{task_value}}
输入、允许数据类别：{{inputs}}
期望输出 schema：{{output_schema}}
非 AI 基线：{{baseline}}
AI 必要性：{{reason}}

| 方案 | 约束匹配 | 实测质量/证据 | 延迟/费用依据 | 运维代价 | 决定 |
|---|---|---|---|---|---|
| {{candidate}} | {{fit}} | {{measured_or_unknown}} | {{measurement_or_estimate}} | {{operations}} | {{choice}} |

## 提示契约

角色与任务：{{task_instruction}}
可信规则：{{rules}}
外部数据隔离方式：{{data_boundary}}
输出字段/引用要求：{{format_and_sources}}
缺失或冲突信息：返回 unknown / request_review，并保留原因与来源。
独立校验器：{{validators}}
重试预算/降级/人工接管：{{failure_path}}

版本清单：{{model_parameters_prompt_schema_tools_corpus}}
数据流与外部传输：{{data_flow}}
评估集与发布条件：{{eval_dataset_and_gate}}
