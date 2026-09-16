# 测试与验收报告

被测版本：{{version}}  环境：{{environment}}  数据版本：{{dataset_version}}
范围/风险：{{scope_risk}}  验收责任：{{owner_or_not_applicable}}

| 需求 ID | 风险 | 测试 ID/层级 | 输入/前置条件 | 独立预期依据 | 通过条件 |
|---|---|---|---|---|---|
| REQ-001 | {{risk}} | TEST-001 / {{level}} | {{input}} | {{oracle}} | {{criterion}} |

## E2E 场景

用户入口：{{entrypoint}}
Given：{{initial_state}}
When：{{user_actions}}
Then：{{observable_output_and_content}}
真实依赖/替身：{{real_and_mocked_dependencies}}
异常路径：{{failure_scenario}}

| 测试 ID | 执行命令/操作 | 实际结果 | 证据路径/运行 ID | 状态 | 缺陷 ID |
|---|---|---|---|---|---|
| TEST-001 | {{execution}} | {{observed}} | {{evidence}} | 未运行 | {{defect}} |

覆盖缺口：{{gaps}}
验收结论：通过 / 有条件通过（列条件） / 不通过 / 尚未验收
判断依据：{{criteria_and_evidence}}
真实签署记录（如适用）：{{actual_approval_or_pending}}
