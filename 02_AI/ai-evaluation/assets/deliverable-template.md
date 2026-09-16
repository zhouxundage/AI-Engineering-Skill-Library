# AI 评估计划与报告

任务：{{task}}  基线/候选：{{versions}}  数据版本：{{dataset}}
样本单位/泄漏分组：{{unit_and_group}}
开发/保留集划分依据：{{split}}
真实/合成样本及适用范围：{{data_scope}}

| 指标 | 分子/分母或计算方式 | 聚合/子群 | 阈值及来源 | 关键失败规则 |
|---|---|---|---|---|
| {{metric}} | {{formula}} | {{aggregation}} | {{threshold_source}} | {{critical_failure}} |

标注准则/争议处理：{{rubric_adjudication}}
人工评审/模型裁判及校准：{{raters_calibration}}
随机参数/重复运行方案：{{repeat_plan}}
版本：模型、提示、schema、语料、检索、工具、评分器。

| 样本 ID | 期望依据 | 实际输出引用 | 各项评分 | 失败类别 | 运行 ID |
|---|---|---|---|---|---|
| E-001 | {{gold}} | {{output}} | {{scores}} | {{failure_type}} | {{run}} |

样本数与分层结果：{{results}}
波动/区间及计算依据：{{uncertainty}}
费用/延迟测量方式：{{performance}}
结论：通过 / 不通过 / 证据不足
支持证据、限制与后续：{{decision_evidence_limitations}}
