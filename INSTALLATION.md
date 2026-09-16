# 安装说明

本库包含 15 个独立技能。分类目录用于维护；安装脚本会将每个技能复制为独立目录。

## 使用方法

1. 下载或克隆本仓库。
2. 使用 Python 3，先预览安装，再执行安装。例如在 Windows PowerShell 中：

```powershell
python scripts/install_library.py --target "$HOME/.agents/skills" --dry-run
python scripts/install_library.py --target "$HOME/.agents/skills"
```

已有内容完全相同的技能会跳过；同名内容不同则停止，不覆盖。安装器会逐文件校验复制结果。

若 Python 未加入 PATH，请使用其可执行文件的绝对路径。不同宿主或组织环境应选择其实际支持的技能目录。

首次使用可明确提及 `$ai-project-architect`。若技能列表尚未刷新，重新打开应用后检查。

目录约定参考 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

## 检查与维护

```powershell
python -m pip install PyYAML
python scripts/validate_library.py
```

技能说明与模板本身不依赖 Python；Python 用于辅助安装和验证。更新流程见 MAINTENANCE.md，初版检查记录见 VALIDATION.md。
