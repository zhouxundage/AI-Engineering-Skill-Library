# RAG 规格与评估卡

用途：{{use_case}}  语料快照：{{corpus_version}}
摄取流程：{{ingestion}}

| 字段 | 契约 |
|---|---|
| document_id / version | {{stable_identity_and_version}} |
| source / locator | {{origin_page_section_table}} |
| access_scope | {{authorized_subjects_or_groups}} |
| effective_status | {{validity_rules}} |
| chunk_id / parser_version | {{lineage}} |

解析与切分：{{structure_preservation}}
检索基线/候选方法：{{retrieval_methods}}
权限过滤位置：{{pre_retrieval_or_context_control}}
引用输出：claim → document_id + version + locator + supporting_excerpt
无证据/冲突时行为：{{fallback}}
索引更新/删除/缓存失效：{{lifecycle}}

| 查询 ID | 相关证据标注 | 检索结果 | 答案支持度 | 权限/版本检查 | 实际结果 |
|---|---|---|---|---|---|
| Q-001 | {{gold_evidence}} | {{retrieved}} | {{support}} | {{checks}} | 未运行 |

指标定义与分母：{{metrics}}
失败归因：解析 / 检索 / 权限 / 版本 / 生成 / 引用校验
