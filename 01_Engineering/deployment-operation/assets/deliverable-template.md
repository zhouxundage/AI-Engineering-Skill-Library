# 发布与运行手册

系统/制品版本：{{artifact_id}}  目标环境：{{target}}  授权范围：{{authorization}}
配置与密钥来源（只填引用）：{{config_secret_refs}}
资源/网络/存储要求：{{requirements}}
构建/启动步骤：{{build_start}}
迁移与顺序：{{migration_order}}

| 阶段 | 操作 | 成功信号 | 失败处理 | 实际证据 |
|---|---|---|---|---|
| 发布前 | {{preflight}} | {{expected}} | {{fallback}} | {{evidence}} |
| 发布 | {{release}} | {{expected}} | {{fallback}} | {{evidence}} |
| 发布后 | {{business_probe}} | {{expected}} | {{fallback}} | {{evidence}} |

监测指标/阈值来源/责任：{{monitoring}}
日志查找与关联 ID：{{troubleshooting}}
代码回滚：{{rollback}}
数据恢复/兼容性：{{restore}}
恢复验证：已演练 / 未演练 / 不适用；证据：{{restore_evidence}}
实际状态：未部署 / 已部署未验证 / 已部署且验证通过 / 失败
